# Downloading Noto Serif CJK
 
Noto Serif CJK is available in multiple formats which have different uses. Each of
these font formats used below has the capability to display both horizontal
and vertical forms where appropriate. Any of the fonts that support
Japanese will also be able to support proportional kana.
### Variable OTCs

The Variable OTC file contains all five language specific variable font resources in
either OTF/CFF2 or TTF formats. This format requires a system that supports both OTC 
OpenType Collections and variable fonts. Select this deployment format if you want all five languages and all weights and your system supports both variable fonts and OTCs.

Variable OTC [OTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/OTC/NotoSerifCJK-VF.otf.ttc) | [TTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/OTC/NotoSerifCJK-VF.ttf.ttc)

**Note**: There are no Region-specific Variable OTCs as the file size would be larger than the 
Language-specific OTC, defeating the benefits of file size. 

### Language-specific Variable Fonts

Select this deployment format if your system supports variable fonts and you prefer to use only one language, but also want full character coverage or the ability to language-tag text to use glyphs that are appropriate for the other languages (this requires an app that supports language tagging and the OpenType 'locl' GSUB feature).

- Variable Simplified Chinese (简体中文) 
  - [OTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/OTF/NotoSerifCJKsc-VF.otf) | [TTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/TTF/NotoSerifCJKsc-VF.ttf)

- Variable Traditional Chinese — Taiwan (繁體中文—臺灣)
  - [OTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/OTF/NotoSerifCJKtc-VF.otf) | [TTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/TTF/NotoSerifCJKtc-VF.ttf) 

- Variable Traditional Chinese — Hong Kong (繁體中文—香港)
  - [OTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/OTF/NotoSerifCJKhk-VF.otf) | [TTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/TTF/NotoSerifCJKhk-VF.ttf)

- Variable Japanese (日本語)
  - [OTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/OTF/NotoSerifCJKjp-VF.otf) | [TTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/TTF/NotoSerifCJKjp-VF.ttf)

- Variable Korean (한국어)
  - [OTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/OTF/NotoSerifCJKkr-VF.otf) | [TTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/TTF/NotoSerifCJKkr-VF.ttf)

### Region-specific Subset Variable Fonts

Select this deployment format if your system support variable fonts and you need only the glyphs for characters for a particular region.

- Subset Variable Simplified Chinese (简体中文) 
  - [OTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/OTF/Subset/NotoSerifSC-VF.otf) | [TTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/TTF/Subset/NotoSerifSC-VF.ttf)

- Subset Variable Traditional Chinese — Taiwan (繁體中文—臺灣) 
  - [OTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/OTF/Subset/NotoSerifTC-VF.otf) | [TTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/TTF/Subset/NotoSerifTC-VF.ttf)

- Subset Variable Traditional Chinese — Hong Kong (繁體中文—香港) 
  - [OTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/OTF/Subset/NotoSerifHK-VF.otf) | [TTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/TTF/Subset/NotoSerifHK-VF.ttf)

- Subset Variable Japanese (日本語) 
  - [OTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/OTF/Subset/NotoSerifJP-VF.otf) | [TTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/TTF/Subset/NotoSerifJP-VF.ttf)

- Subset Variable Korean (한국어) 
  - [OTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/OTF/Subset/NotoSerifKR-VF.otf) | [TTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/Variable/TTF/Subset/NotoSerifKR-VF.ttf)



### Super OTC

This packaging form carries the fonts for each of Simplified Chinese,
Traditional Chinese, Traditional Chinese HK, Japanese, and Korean multiplied
by all 7 weights for each in one single font file. Once installed it
will appear in font menus as 35 separate fonts. This format is the easiest to
install of all the formats and takes the least space for static fonts due to 
sharing between the 35 parts.

Select this deployment format if you want all five languages and all seven weights in a single and easy-to-manage font resource that includes 35 fonts. Changing languages is accomplished by either selecting the font of the desired language or by language-tagging the text. A limited number of apps support language tagging and the corresponding OpenType 'locl' (*Localized Forms*) GSUB feature, such as [Adobe InDesign](https://www.adobe.com/products/indesign.html) and modern browsers.

[Super OTC](https://github.com/googlefonts/noto-cjk/releases/download/Serif2.003/01_NotoSerifCJK.ttc.zip)

**Special Note**: This deployment format requires macOS (OS X) Version 10.8 (aka *Mountain Lion*) or later, iOS 7 or later, Windows 10 Version 1703 (aka *Creators Update*) or later, a flavor of Linux that uses *fontconfig* and FreeType Version 2.5.0.1 or greater, or Adobe CS6 apps or later.

### Static OTCs
This packaging form carries the fonts for each of Simplified Chinese, 
Traditional Chinese, Traditional Chinese HK, Japanese, and Korean in a single font file. Once
installed it will appear in font menus as five separate fonts. 
This format is the easiest to install and compared to installing separate fonts
takes less space. There are 7 of these OTC font files with one for each weight
from ExtraLight to Black.

Select this deployment format if you want all five languages and particular weights, or if your environment does not support the Super OTC. Changing languages is accomplished the same way as the Super OTC. If you need particular weights, download individual font resources from the [OTC](https://github.com/googlefonts/noto-cjk/raw/main/Serif/OTC) folder, otherwise click on the following link:

[Static OTCs](https://github.com/googlefonts/noto-cjk/releases/download/Serif2.003/04_NotoSerifCJKOTC.zip)

**Special Note**: This deployment format requires macOS (OS X) Version 10.8 (aka *Mountain Lion*) or later, iOS 7 or later, Windows 10 Version 1607 (aka *Anniversary Update*) or later, a flavor of Linux that uses *fontconfig* and FreeType Version 2.5.0.1 or greater, or Adobe CS6 apps or later.

### Language-specific OTFs

Select this deployment format if you prefer to use only one language, but also want full character coverage or the ability to language-tag text to use glyphs that are appropriate for the other languages (like the Super OTC and OTCs, this requires an app that supports language tagging and the OpenType 'locl' GSUB feature). If you need only specific weights, download individual font resources from the [OTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/OTF) folder, otherwise click on the appropriate links below:

[Simplified Chinese (简体中文)](https://github.com/googlefonts/noto-cjk/releases/download/Serif2.003/09_NotoSerifCJKsc.zip)

[Traditional Chinese — Taiwan (繁體中文—臺灣)](https://github.com/googlefonts/noto-cjk/releases/download/Serif2.003/10_NotoSerifCJKtc.zip)

[Traditional Chinese — Hong Kong (繁體中文—香港)](https://github.com/googlefonts/noto-cjk/releases/download/Serif2.003/11_NotoSerifCJKhk.zip)

[Japanese (日本語)](https://github.com/googlefonts/noto-cjk/releases/download/Serif2.003/07_NotoSerifCJKjp.zip)

[Korean (한국어)](https://github.com/googlefonts/noto-cjk/releases/download/Serif2.003/08_NotoSerifCJKkr.zip)

### Region-specific Subset OTFs

Select this deployment format if you need only the glyphs for characters for a particular region, **or if you are not sure which deployment format to choose**.

Each ZIP file contains seven font resources, one for each of the seven weights. If you need specific weights, download individual font resources from the [SubsetOTF](https://github.com/googlefonts/noto-cjk/raw/main/Serif/SubsetOTF) folder, otherwise click on the appropriate links below:

[China (中国)](https://github.com/googlefonts/noto-cjk/releases/download/Serif2.003/14_NotoSerifSC.zip)

[Taiwan (臺灣)](https://github.com/googlefonts/noto-cjk/releases/download/Serif2.003/15_NotoSerifTC.zip)

[Hong Kong (香港)](https://github.com/googlefonts/noto-cjk/releases/download/Serif2.003/16_NotoSerifHK.zip)

[Japan (日本)](https://github.com/googlefonts/noto-cjk/releases/download/Serif2.003/12_NotoSerifJP.zip)

[Korea (한국)](https://github.com/googlefonts/noto-cjk/releases/download/Serif2.003/13_NotoSerifKR.zip)

## Getting Involved

[Open or respond to an issue](https://github.com/googlefonts/noto-cjk/issues/).
