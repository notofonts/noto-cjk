# SPDX-License-Identifier: Apache-2.0
import glob
import hashlib
import json
import os
import re
import subprocess

from fontTools.ttLib import TTFont
from lib4sbom.data.file import SBOMFile
from lib4sbom.data.package import SBOMPackage
from lib4sbom.generator import SBOMGenerator
from lib4sbom.sbom import SBOM
from lib4sbom.output import SBOMOutput
from sbom4python.scanner import SBOMScanner

__version__ = "0.0.1"
DRAFT = True
# Most of this is written in as general a way as possible, so it can be reused
# as a basis for other font projects. The noto-cjk specific stuff is at the end.


def file_id(s):
    return re.sub(r"[^a-zA-Z0-9\.]", "-", s)


def add_checksums(file):
    filename = file.get_name()
    file.set_checksum(
        "SHA1", hashlib.file_digest(open(filename, "rb"), "sha1").hexdigest()
    )
    file.set_checksum(
        "SHA256", hashlib.file_digest(open(filename, "rb"), "sha256").hexdigest()
    )


def font_to_file(filename, upstream_binary=False):
    file = SBOMFile()
    file.initialise()
    file.set_id(file_id(filename))
    file.set_name(filename)
    file.set_filetype("OTHER")
    add_checksums(file)

    name = TTFont(filename, fontNumber=0)["name"]
    license = name.getDebugName(13)
    copyright = name.getDebugName(0)
    rfn = (
        "-RFN"
        if (
            "reserved font name" in license.lower()
            or "reserved font name" in copyright.lower()
        )
        else ""
    )
    if "Open Font License, Version 1.0" in license:
        file.set_licenseinfoinfile("OFL-1.0" + rfn)
        file.set_licenseconcluded("OFL-1.0" + rfn)
    if "Open Font License, Version 1.1" in license:
        file.set_licenseinfoinfile("OFL-1.1" + rfn)
        file.set_licenseconcluded("OFL-1.1" + rfn)

    file.set_copyrighttext(copyright)

    if upstream_binary:
        manufacturer = name.getDebugName(8)
        file.set_contributor(manufacturer)
        designer = name.getDebugName(9)
        file.set_contributor(designer)

        file.set_comment("Binary file contributed by " + manufacturer)
    return file.get_file()


def homebrew_package(package_name):
    package = SBOMPackage()
    package.initialise()
    package.set_name(package_name)
    info = subprocess.run(
        f"brew info --json=v1 {package_name}", shell=True, capture_output=True
    ).stdout
    info = json.loads(info)[0]
    package.set_version(info["linked_keg"])
    package.set_homepage(info["homepage"])
    package.set_licenseinfoinfiles(info["license"])
    # Extend this to handle more licenses if needed
    if "MIT" in info["license"]:
        package.set_licenseconcluded("MIT")
    return package.get_package()


def source_to_file(filename):
    file = SBOMFile()
    file.initialise()
    file.set_id(file_id(filename))
    file.set_name(filename)
    file.set_filetype("SOURCE")
    add_checksums(file)
    file.set_licenseinfoinfile("Apache-2.0")
    file.set_licenseconcluded("Apache-2.0")
    file.set_comment(
        "Taken from "
        + subprocess.run(
            "git config --get remote.origin.url", shell=True, capture_output=True
        ).stdout.decode("utf8")
        + " git rev "
        + subprocess.run(
            "git rev-parse main:" + filename, shell=True, capture_output=True
        )
        .stdout.decode("utf8")
        .strip()
    )
    return file.get_file()


sbom_scan = SBOMScanner(False, False, False, False)
sbom_gen = SBOMGenerator(
    sbom_type="spdx", format="json", application=__file__, version=__version__
)

sbom = SBOM()
document = sbom_scan.get_document()
sbom.add_document(document)

files = {}
# Input files from Adobe
adobe = {
    font: font_to_file(font, upstream_binary=True)
    for font in glob.glob("S*/**/*.[o,t]t[f,c]", recursive=True)
}
files.update(adobe)

# Files we generated
ours = {
    font: font_to_file(font)
    for font in glob.glob("google-fonts/*.[o,t]t[f,c]", recursive=True)
}
for our in ours.values():
    our["comment"] = "Generated as described in relationships section"
files.update(ours)

sbom.add_files(files)

sbom_gen.generate(
    project_name="noto-cjk" + ("-DRAFT" if DRAFT else " "),
    sbom_data=sbom.get_sbom(),
    send_to_output=False,
)

# lib4sbom does not support file->file relationships, so we have to
# add them manually
sbom_gen.sbom_complete = False


def relates(sbom, source, target, relationship):
    if os.path.isfile(source):
        source_ident = sbom.bom.file_ident(sbom._get_element(source, file_id(source)))
    elif source == "-":  # This document
        source_ident = sbom.bom.SPDX_PROJECT_ID
    else:
        source_ident = sbom.bom.package_ident(
            sbom._get_element(source, file_id(source))
        )
    if os.path.isfile(target):
        target_ident = sbom.bom.file_ident(sbom._get_element(target, file_id(target)))
    else:
        target_ident = sbom.bom.package_ident(
            sbom._get_element(target, file_id(target))
        )
    sbom_gen.bom.generateRelationship(
        source_ident,
        target_ident,
        " " + relationship + " ",
    )


for original in adobe.keys():
    relates(sbom_gen, "-", original, "DESCRIBES")

for original in glob.glob("S*/Variable/*/Subset/*.ttf"):
    modified = os.path.basename(original).replace("-VF.ttf", "[wght].ttf")
    modified = "google-fonts/" + re.sub(
        "CJK(..)", lambda x: x[0][-2:].upper(), modified
    )
    relates(sbom_gen, modified, original, "FILE_MODIFIED")
    relates(sbom_gen, "-", modified, "DESCRIBES")

sbom_gen.bom.showRelationship()
sbom_out = SBOMOutput("manifest.spdx.json", output_format="json")
sbom_out.generate_output(sbom_gen.sbom)
