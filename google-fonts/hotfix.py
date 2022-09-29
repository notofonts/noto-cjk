from gftools.util.google_fonts import _KNOWN_WEIGHTS
from gftools.stat import gen_stat_tables
from gftools.fix import fix_unhinted_font
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._f_v_a_r import NamedInstance
import argparse
import re
import os

HOTFIX_NUMBER = 1

parser = argparse.ArgumentParser(description='Hotfix Noto CJK VF TTFs to Google Fonts standard')
parser.add_argument('--output-dir', default=".",
                    help='output directory')
parser.add_argument('fonts', metavar='N', type=str, nargs='+',
                    help='fonts to fix')

args = parser.parse_args()

if not os.path.exists(args.output_dir):
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

def build_fvar(ttfont):
    fvar = ttfont["fvar"]
    psname = ttfont["name"].getName(6,3,1).toUnicode()
    base_psname = re.sub("-.*", "", psname)
    for name, weight in _KNOWN_WEIGHTS.items():
        instance = NamedInstance()
        instance.postscriptNameID = ttfont["name"].addName(base_psname+"-"+name)
        instance.subfamilyNameID = ttfont["name"].addName(name)
        instance.coordinates = { "wght": weight }
        fvar.instances.append(instance)

def fix_copyright(ttfont):
    ttfont["name"].setName(ttfont["name"].getName(0,3,1).toUnicode().replace("©", "(c)"), 0, 3, 1, 0x409)

def fix_version(ttfont):
    ttfont["name"].setName(ttfont["name"].getName(5,3,1).toUnicode().replace(";hotconv", f"-H{HOTFIX_NUMBER};hotconv"), 5, 3, 1, 0x409)


def rename(ttfont):
    for name in ttfont["name"].names:
        if isinstance(name.string, bytes):
            name.string = name.string.decode("utf-16-be")
            name.string = re.sub("CJK\s*", "", name.string)
            name.string = re.sub(r"Noto(?:Sans|Serif)\w\w", lambda x:x[0][0:-2]+x[0][-2:].upper(), name.string).encode("utf-16-be")
        else:
            name.string = re.sub("CJK\s*", "", name.string)
            name.string = re.sub(r"Noto(?:Sans|Serif)\w\w", lambda x:x[0][0:-2]+x[0][-2:].upper(), name.string)

for font in args.fonts:
    ttfont = TTFont(font)
    scratch_font(ttfont)
    build_fvar(ttfont)
    gen_stat_tables([ttfont], ["wght"], {"wght": [400]})
    fix_copyright(ttfont)
    fix_version(ttfont)
    fix_unhinted_font(ttfont)
    rename(ttfont)
    if "DSIG" in ttfont:
        del ttfont["DSIG"]
    axis_tags = sorted([ax.axisTag for ax in ttfont["fvar"].axes])
    axis_tags = ",".join(axis_tags)
    newname = os.path.basename(font).replace("-VF.ttf", "[%s].ttf" % axis_tags)
    newname = re.sub("CJK(..)", lambda x:x[0][-2:].upper(), newname)
    
    ttfont.save(os.path.join(args.output_dir, newname))
