"""
Hotfix a set of 'upstream' Noto CJK fonts to comply with fonts.google.com
requirements. The following hotfixes are made:

* Reconstruct fvar/STAT tables to remove any weights which do not
  comply to the fonts.google.com expectations.
* Rewrite the license description within the fonts to be the standard OFL
  text used in other fonts.
* Replace the copyright sign © in the name table with ASCII '(c)'.
* Rename the variable fonts using the GF Family[axes].ttf format.
* Run various other source fixes using gftools.fix.
* Restore the correct hhea ascent = 1160 and descent = -288.
"""

from gftools.util.google_fonts import _KNOWN_WEIGHTS
from gftools.fix import fix_font
from axisregistry import build_name_table, build_fvar_instances, build_stat
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._f_v_a_r import NamedInstance
from gftools.constants import (
    NAMEID_FONT_SUBFAMILY_NAME,
    NAMEID_TYPOGRAPHIC_SUBFAMILY_NAME,
)
import argparse
import re
import os

HOTFIX_NUMBER = 1

OFL_DESCRIPTION = "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL"

parser = argparse.ArgumentParser(
    description="Hotfix Noto CJK VF TTFs to Google Fonts standard"
)
parser.add_argument("--output-dir", help="output directory")
parser.add_argument("-o", help="output file name")
parser.add_argument("fonts", metavar="N", type=str, nargs="+", help="fonts to fix")

args = parser.parse_args()

if len(args.fonts) > 1 and args.o:
    raise ValueError("Cannot specify -o with multiple input files")

if args.o and args.output_dir:
    raise ValueError("Cannot specify -o with --output-dir")

if not args.output_dir:
    args.output_dir = "."

if args.output_dir and not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

if "" in _KNOWN_WEIGHTS:
    del _KNOWN_WEIGHTS[""]
if "Hairline" in _KNOWN_WEIGHTS:
    del _KNOWN_WEIGHTS["Hairline"]


def scratch_font(ttfont):
    # Trash all the names from STAT/fvar and start again.
    deletable_names = set()
    if "STAT" in ttfont:
        stat = ttfont["STAT"].table
        deletable_names.add(stat.ElidedFallbackNameID)
        for av in stat.AxisValueArray.AxisValue:
            deletable_names.add(av.ValueNameID)
        for axis in stat.DesignAxisRecord.Axis:
            deletable_names.add(axis.AxisNameID)
        del ttfont["STAT"]

    fvar = ttfont["fvar"]
    for axis in fvar.axes:
        deletable_names.remove(axis.axisNameID)
    for instance in fvar.instances:
        deletable_names.add(instance.subfamilyNameID)
        deletable_names.add(instance.postscriptNameID)
    for name_id in deletable_names:
        ttfont["name"].removeNames(name_id)
    fvar.instances = []

    # Drop 0x411 font names
    ttfont["name"].names = [x for x in ttfont["name"].names if x.langID == 0x409]


def fix_copyright(ttfont):
    ttfont["name"].setName(
        ttfont["name"].getName(0, 3, 1).toUnicode().replace("©", "(c)"), 0, 3, 1, 0x409
    )
    ttfont["name"].setName(OFL_DESCRIPTION, 13, 3, 1, 0x409)


def fix_version(ttfont):
    ttfont["name"].setName(
        ttfont["name"]
        .getName(5, 3, 1)
        .toUnicode()
        .replace(";hotconv", f"-H{HOTFIX_NUMBER};hotconv"),
        5,
        3,
        1,
        0x409,
    )


def fix_hhea_ascent(ttfont, sans=True):
    if sans:
        ttfont["hhea"].ascender = 1160
        ttfont["hhea"].descent = -288
    else:
        ttfont["hhea"].ascender = 1151
        ttfont["hhea"].descent = -286


for font in args.fonts:
    ttfont = TTFont(font)
    scratch_font(ttfont)
    fix_copyright(ttfont)
    fix_version(ttfont)
    fix_hhea_ascent(ttfont, "Sans" in font)
    ttfont = fix_font(ttfont, include_source_fixes=True)
    build_name_table(ttfont, siblings=[])
    build_fvar_instances(ttfont)
    build_stat(ttfont, [])
    if "DSIG" in ttfont:
        del ttfont["DSIG"]

    axis_tags = sorted([ax.axisTag for ax in ttfont["fvar"].axes])
    axis_tags = ",".join(axis_tags)
    if args.o:
        newname = args.o
    else:
        newname = os.path.basename(font).replace("-VF.ttf", "[%s].ttf" % axis_tags)
        newname = re.sub("CJK(..)", lambda x: x[0][-2:].upper(), newname)
        newname = os.path.join(args.output_dir, newname)
    ttfont.save(newname)
