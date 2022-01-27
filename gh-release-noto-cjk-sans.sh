#!/bin/bash

# Until Sans and Serif are split into two repos on https://github.com/notofonts 
# we have everything in this single repo https://github.com/googlefonts/noto-cjk
# This script will make a new release for Sans. To do a Serif release use gh-release-noto-cjk-serif.sh
# Requires GitHub CLI (https://github.com/cli/cli/releases)

VERSION=2.004

echo "Download individual assets from below or through the download [guide](https://github.com/googlefonts/noto-cjk/tree/main/Sans#downloading-noto-sans-cjk)." > Sans/git-release-notes.md

cd Sans
zip -r -v 01_NotoSansCJK-OTF-VF.zip Variable/OTF Variable/OTC/NotoSansCJK-VF.otf.ttc ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 02_NotoSansCJK-TTF-VF.zip Variable/TTF Variable/OTC/NotoSansCJK-VF.ttf.ttc ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 03_NotoSansCJK-OTC.zip OTC ../LICENSE --exclude "*.zip" "*.DS_Store" "OTC/NotoSansCJK.ttc"
zip -r -v 04_NotoSansCJK-OTF.zip OTF ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 05_NotoSansCJK-SubsetOTF.zip SubsetOTF ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 06_NotoSansCJKjp.zip OTF/Japanese ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 07_NotoSansCJKkr.zip OTF/Korean ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 08_NotoSansCJKsc.zip OTF/SimplifiedChinese ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 09_NotoSansCJKtc.zip OTF/TraditionalChinese ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 10_NotoSansCJKhk.zip OTF/TraditionalChineseHK ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 11_NotoSansMonoCJKjp.zip Mono/NotoSansMonoCJKjp* ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 12_NotoSansMonoCJKkr.zip Mono/NotoSansMonoCJKkr* ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 13_NotoSansMonoCJKsc.zip Mono/NotoSansMonoCJKsc* ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 14_NotoSansMonoCJKtc.zip Mono/NotoSansMonoCJKtc* ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 15_NotoSansMonoCJKhk.zip Mono/NotoSansMonoCJKhk* ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 16_NotoSansJP.zip SubsetOTF/JP ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 17_NotoSansKR.zip SubsetOTF/KR ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 18_NotoSansSC.zip SubsetOTF/SC ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 19_NotoSansTC.zip SubsetOTF/TC ../LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 20_NotoSansHK.zip SubsetOTF/HK ../LICENSE --exclude "*.zip" "*.DS_Store"

gh release create Sans${VERSION} --title "Noto Sans CJK Version ${VERSION} (OTF, OTC, Super OTC, Subset OTF, Variable OTF/TTF)" -F git-release-notes.md --target main \
        '01_NotoSansCJK-OTF-VF.zip#All Variable OTF/OTC' \
        '02_NotoSansCJK-TTF-VF.zip#All Variable TTF/OTC' \
        '03_NotoSansCJK-OTC.zip#All Static Language Specific OTCs' \
        '04_NotoSansCJK-OTF.zip#All Static Language Specific OTFs' \
        '05_NotoSansCJK-SubsetOTF.zip#All Static Region Specific Subset OTFs' \
        '06_NotoSansCJKjp.zip#Language Specific OTFs Japanese (日本語)' \
        '07_NotoSansCJKkr.zip#Language Specific OTFs Korean (한국어)' \
        '08_NotoSansCJKsc.zip#Language Specific OTFs Simplified Chinese (简体中文)' \
        '09_NotoSansCJKtc.zip#Language Specific OTFs Traditional Chinese — Taiwan (繁體中文—臺灣)' \
        '10_NotoSansCJKhk.zip#Language Specific OTFs Traditional Chinese — Hong Kong (繁體中文—香港)' \
        '11_NotoSansMonoCJKjp.zip#Language Specific Monospace OTFs Japanese (日本語)' \
        '12_NotoSansMonoCJKkr.zip#Language Specific Monospace OTFs Korean (한국어)' \
        '13_NotoSansMonoCJKsc.zip#Language Specific Monospace OTFs Simplified Chinese (简体中文)' \
        '14_NotoSansMonoCJKtc.zip#Language Specific Monospace OTFs Traditional Chinese — Taiwan (繁體中文—臺灣)' \
        '15_NotoSansMonoCJKhk.zip#Language Specific Monospace OTFs Traditional Chinese — Hong Kong (繁體中文—香港)' \
        '16_NotoSansJP.zip#Region Specific Subset OTFs Japanese (日本語)' \
        '17_NotoSansKR.zip#Region Specific Subset OTFs Korean (한국어)' \
        '18_NotoSansSC.zip#Region Specific Subset OTFs Simplified Chinese (简体中文)' \
        '19_NotoSansTC.zip#Region Specific Subset OTFs Traditional Chinese — Taiwan (繁體中文—臺灣)' \
        '20_NotoSansHK.zip#Region Specific Subset OTFs Traditional Chinese — Hong Kong (繁體中文—香港)'

rm *.zip
rm git-release-notes.md
cd ..