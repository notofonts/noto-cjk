#!/bin/sh
STYLE=ttf

echo "Building for Google Fonts"
# This is the GF deliverables; these are subset
SERIF_SOURCES=Serif/Variable/*/Subset/*$STYLE
SANS_SOURCES=Sans/Variable/*/Subset/*$STYLE

python3 google-fonts/hotfix.py --output-dir=google-fonts $SERIF_SOURCES $SANS_SOURCES
add-chws -o google-fonts google-fonts/*$STYLE

echo "Building for Android"
# Instance for Android
# We don't use the subset versions here because we want to
# use the shared glyf/gvar table in the eventual TTC
SERIF_SOURCES=Serif/Variable/*/*$STYLE
SANS_SOURCES=Sans/Variable/*/*$STYLE

mkdir -p android/instances

VARIATION="wght=400:900"
VARIATION_FILENAME=`echo $VARIATION | sed "s/:/-/" | sed "s/=/-/"`

for i in $SANS_SOURCES $SERIF_SOURCES
do
   OUTFILE=android/instances/`basename $i | sed "s/.$STYLE/-$VARIATION_FILENAME.$STYLE/"`
   echo "$i => " $OUTFILE
   if [[ $VARIATION == "full" ]]
   then
      cp $i $OUTFILE
   else
      fonttools varLib.instancer -o $OUTFILE $i $VARIATION
   fi
   # Hotfix in place
   python3 google-fonts/hotfix.py -o $OUTFILE $OUTFILE
done
add-chws -o android/instances/ android/instances/*ttf

# Build TTCs for Android
fonttools ttLib -o android/'NotoSansCJK'-$VARIATION_FILENAME.$STYLE.ttc android/instances/NotoSans*.$STYLE
woff2_compress android/'NotoSansCJK'-$VARIATION_FILENAME.$STYLE.ttc
fonttools ttLib -o android/'NotoSerifCJK'-$VARIATION_FILENAME.$STYLE.ttc android/instances/NotoSerif*.$STYLE
woff2_compress android/'NotoSerifCJK'-$VARIATION_FILENAME.$STYLE.ttc
