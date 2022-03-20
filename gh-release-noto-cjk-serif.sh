#!/bin/bash

# Until Sans and Serif are split into two repos on https://github.com/notofonts 
# we have everything in this single repo https://github.com/googlefonts/noto-cjk
# This script will make a new release for Serif. To do a Sans release use gh-release-noto-cjk-sans.sh
# Requires GitHub CLI (https://github.com/cli/cli/releases)

VERSION=2.001

echo "Download individual assets from below or through the download [guide](https://github.com/googlefonts/noto-cjk/tree/main/Serif#downloading-noto-serif-cjk)." > Serif/git-release-notes.md

cd Serif
zip -r -v 02_NotoSerifCJK-OTF-VF.zip Variable/OTF Variable/OTC/NotoSerifCJK-VF.otf.ttc LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 03_NotoSerifCJK-TTF-VF.zip Variable/TTF Variable/OTC/NotoSerifCJK-VF.ttf.ttc LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 04_NotoSerifCJKOTC.zip OTC LICENSE --exclude "*.zip" "*.DS_Store" "OTC/NotoSerifCJK.ttc"
zip -r -v 05_NotoSerifCJKOTF.zip OTF LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 06_NotoSerifCJKSubsetOTF.zip SubsetOTF LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 07_NotoSerifCJKjp.zip OTF/Japanese LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 08_NotoSerifCJKkr.zip OTF/Korean LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 09_NotoSerifCJKsc.zip OTF/SimplifiedChinese LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 10_NotoSerifCJKtc.zip OTF/TraditionalChinese LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 11_NotoSerifCJKhk.zip OTF/TraditionalChineseHK LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 12_NotoSerifJP.zip SubsetOTF/JP LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 13_NotoSerifKR.zip SubsetOTF/KR LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 14_NotoSerifSC.zip SubsetOTF/SC LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 15_NotoSerifTC.zip SubsetOTF/TC LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 16_NotoSerifHK.zip SubsetOTF/HK LICENSE --exclude "*.zip" "*.DS_Store"

# The Serif SuperOTC is too large to store on GitHub without LFS so we expect it to 
# be created locally first and then we can attach it as a release asset
cp SuperOTC/NotoSerifCJK.ttc.zip 01_NotoSerifCJK.ttc.zip

gh release create Serif${VERSION} --title "Noto Serif CJK Version ${VERSION} (OTF, OTC, Super OTC, Subset OTF, Variable OTF/TTF)" -F git-release-notes.md --target main \
        '01_NotoSerifCJK.ttc.zip#Static Super OTC' \
        '02_NotoSerifCJK-OTF-VF.zip#All Variable OTF/OTC' \
        '03_NotoSerifCJK-TTF-VF.zip#All Variable TTF/OTC' \
        '04_NotoSerifCJKOTC.zip#All Static Language Specific OTCs' \
        '05_NotoSerifCJKOTF.zip#All Static Language Specific OTFs' \
        '06_NotoSerifCJKSubsetOTF.zip#All Static Region Specific Subset OTFs' \
        '07_NotoSerifCJKjp.zip#Language Specific OTFs Japanese (日本語)' \
        '08_NotoSerifCJKkr.zip#Language Specific OTFs Korean (한국어)' \
        '09_NotoSerifCJKsc.zip#Language Specific OTFs Simplified Chinese (简体中文)' \
        '10_NotoSerifCJKtc.zip#Language Specific OTFs Traditional Chinese — Taiwan (繁體中文—臺灣)' \
        '11_NotoSerifCJKhk.zip#Language Specific OTFs Traditional Chinese — Hong Kong (繁體中文—香港)' \
        '12_NotoSerifJP.zip#Region Specific Subset OTFs Japanese (日本語)' \
        '13_NotoSerifKR.zip#Region Specific Subset OTFs Korean (한국어)' \
        '14_NotoSerifSC.zip#Region Specific Subset OTFs Simplified Chinese (简体中文)' \
        '15_NotoSerifTC.zip#Region Specific Subset OTFs Traditional Chinese — Taiwan (繁體中文—臺灣)' \
        '16_NotoSerifHK.zip#Region Specific Subset OTFs Traditional Chinese — Hong Kong (繁體中文—香港)'

rm *.zip
rm git-release-notes.md
cd ..
