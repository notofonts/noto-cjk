### Prior Release Notes


### Noto Serif CJK 1.001 Release Notes

May 8, 2017

This is an update to Noto Serif CJK 1.000. It was built by Dr. Ken Lunde (小林劍󠄁)
on May 1, 2017 and released on May 8, 2017.


####General Notes

* The OS/2.usWeightClass value for ExtraLight was changed from 250 to 200.
See Issue [#86](https://github.com/googlei18n/noto-cjk/issues/86).

* Mappings for U+3164 and U+2D544 (Extension F) were added to all CMap resources,
and the Adobe-Japan1 IVS <U+2D544,U+E0100> was added to the Japanese IVS definition
file, SourceHanSerif_JP_sequences.txt.
See Issue [#37](https://github.com/adobe-fonts/source-han-serif/issues/37).

* The glyphs for U+2EC1 ⻁, U+2EEA ⻪, U+2F2C 屮, and U+4EBD 亽 now map to
uni864EuE0101-JP, uni9EFE-CN, uni5C6E-CN, and uni4EBD-CN, respectively, in
all CMap resources.
See Issue [#37](https://github.com/adobe-fonts/source-han-serif/issues/37).

* The glyphs for the 52 half-width jamo—U+FFA0 through U+FFBE, U+FFC2 through U+FFC7,
U+FFCA through U+FFCF, U+FFD2 through U+FFD7, and U+FFDA through U+FFDC—now map to
the glyphs for compatibility jamo (U+3131 through U+3164).

* The alternate proportional digits and punctuation, along with the alternate
half-width punctuation, were added to the scope of the ‘fwid’, ‘hwid’, and ‘pwid’ GSUB features.

####Simplified Chinese

* CN glyphs for U+35EB 㗫, U+385C 㡜, U+5015 倕, U+57F5 埵, U+618F 憏, U+63EF 揯, U+6456 摖, U+6660 晠,
U+66A9 暩, U+68B1 梱, U+6F08 漈, U+76E4 盤, U+7808 砈, U+78DC 磜, U+7A07 稇, U+7A44 穄, U+7BA0 箠,
U+83D9 菙, U+92EE 鋮, U+9318 錘, U+969B 際, U+9BCE 鯎, and U+9C36 鰶 were added.
See Issue [#40](https://github.com/adobe-fonts/source-han-serif/issues/40).

* The glyphs for U+2F22 夊, U+2F58 爻, U+4F8D 侍, U+62FF 拿, U+6301 持, U+6641 晁, U+6C35 氵, U+6DE6 淦,
U+6DFC 淼, U+6EB4 溴, and U+81EC 臬 now map to uni590A-CN, uni723B-CN, uni4F8D-JP, uni62FF-JP,
uni6301-JP, uni6641-JP, uni6C35-JP, uni6DE6-JP, uni6DFC-JP, uni6EB4-JP, and uni81EC-JP, respectively.
See [#37](https://github.com/adobe-fonts/source-han-serif/issues/37).

* The CN glyphs uni3E76-CN, uni414D-CN, uni4A60-CN, uni4BD5-CN, uni4C53-CN, uni4F5B-CN, uni4FB9-CN,
uni596E-CN, uni5957-CN, uni5A17-CN, uni5EAD-CN, uni5EF7-CN, uni5F73-CN, uni602B-CN, uni62C2-CN,
uni633A-CN, uni6883-CN, uni6C11-CN, uni6C1F-CN, uni6CB8-CN, uni6D8F-CN, uni6E88-CN, uni70F6-CN,
uni73FD-CN, uni7829-CN, uni7D8E-CN, uni7ECB-CN, uni8121-CN, uni8247-CN, uni8713-CN, uni8A94-CN,
uni8B04-CN, uni92CC-CN, uni94E4-CN, uni95AE-CN, uni9F2E-CN, uniFF1B-CN, uniFE14-CN, and u2CD9F-CN
were tweaked or corrected.
See Issue [#36](https://github.com/adobe-fonts/source-han-serif/issues/36) and
[#39](https://github.com/adobe-fonts/source-han-serif/issues/39).

####Traditional Chinese—TW

* TW glyphs for U+4FB9 侹, U+5EAD 庭, U+5EF7 廷, U+633A 挺, U+6883 梃, U+6D8F 涏, U+6DEB 淫, U+73FD 珽,
U+7D8E 綎, U+7F54 罔, U+8713 蜓, U+8DA3 趣, U+92CC 鋌, U+95AE 閮, and U+9832 頲 were added.
See [#40](https://github.com/adobe-fonts/source-han-serif/issues/40).

* The glyphs for U+2F61 瓦, U+2FCC 黽, U+504F 偏, U+5553 啓, U+555F 啟, U+58F3 壳, U+58FE 壾, U+591A 多,
U+61DC 懜, U+627F 承, U+6902 椂, U+6903 椃, U+6947 楇, U+7171 煱, U+76EC 盬, U+77A2 瞢, U+77D2 矒,
U+8019 耙, U+803B 耻, U+8B04 謄, and U+9BF1 鯱 now map to uni74E6-JP, uni9EFD-JP, uni504FuE0101-JP,
uni5553uE0101-JP, uni555F-JP, uni58F3-JP, uni58FE-JP, uni591A-JP, uni61DC-JP, uni627F-JP, uni6902-JP,
uni6903-JP, uni6947-JP, uni7171-JP, uni76EC-CN, uni77A2uE0101-JP, uni77D2-JP, uni8019-JP, uni803B-JP,
uni8B04-CN, and uni9BF1-JP, respectively.
See [#37](https://github.com/adobe-fonts/source-han-serif/issues/37).

* The glyphs uni511A-TW, uni5922-TW, uni5A6C-TW, uni5FB5-TW, uni61F5-TW, uni750B-TW, uni750D-TW,
uni7AC5-TW, uni7D73-TW, uni83E1-TW, uni858E-TW, uni85A8-TW, uni8609-TW, uni9138-TW, uni91C5-TW, and
uniFF0C-TW were tweaked or corrected.
See [#36](https://github.com/adobe-fonts/source-han-serif/issues/36) and
[#39](https://github.com/adobe-fonts/source-han-serif/issues/39).

####Japanese

* The JP glyphs uni3CDA-JP, uni3D93-JP, uni507D-JP, uni5316uE0101-JP, uni595C-JP, uni6C2B-JP, uni70BA-JP,
uni7669-JP, uni81F7-JP, uni8285-JP, uni82B1uE0101-JP, and uni9B58-JP were tweaked or corrected.
See [#36](https://github.com/adobe-fonts/source-han-serif/issues/36) and
[#39](https://github.com/adobe-fonts/source-han-serif/issues/39).

* The glyphs for a small number of kana, to include annotated versions thereof, were tweaked in very minor
ways.

####Korean

* The glyphs for U+5173 关 and U+5BE7 寧 now map to uni5173-CN and uni5BE7uE0100-JP, respectively.
See [#37](https://github.com/adobe-fonts/source-han-serif/issues/37).

* The glyphs uniC625, uniC73D, uni1178, uni118C.vjmo01, uni1190.vjmo01, uni1192.vjmo01, uni11ED,
uni11ED.tjmo01, uni11ED.tjmo02, uni11ED.tjmo03, uni11ED.tjmo04, uniD7B5, uniD7B5.vjmo01,
uniD7F5, uniD7F5.tjmo01, uniD7F5.tjmo02, uniD7F5.tjmo03, uniD7F5.tjmo04, uniD7F6, uniD7F6.tjmo01,
uniD7F6.tjmo02, uniD7F6.tjmo03, uniD7F6.tjmo04, uni1112uni119Euni11D9, uni1140uni1175uni11D9, and
uni114Cuni116Funi11D9 were corrected.
See [#39](https://github.com/adobe-fonts/source-han-serif/issues/39).

* The no-op uni115F to uni115F substitutions were removed from the six “ljmo_0n” lookups, referenc-
es to uni115F were removed from the six “ljmo_xxxxxx” lookups, and glyph classes are now used for the
“ljmo_xxxxxx,” “vjmo_xxxxxx,” and “tjmo_xxxxxx” lookups.


###Noto Serif CJK 1.000 Release Notes

April 4, 2017 (addendum)

Please note that due to GitHub restrictions the all-in-one Serif .ttc is not
available via this repo as it exceeds the 100MB GitHub limit.  Please use the
links under "Super OpenType/CFF Collection (Super OTC)" on this page instead:
http://www.google.com/get/noto/help/cjk


April 3, 2017

Introducing Noto Serif CJK 1.000

This introduces a serif-style companion to Noto Sans CJK.  These fonts are again
offered in seven weights, though they are slightly different - ExtraLight,
Light, Regular, Medium, SemiBold, Bold, and Black.  Unlike the Sans there are no
monospace (ASCII-only) versions of these fonts.

The packaging options are the same as for the Sans: you can choose from an
all-in-one CJK TTC, seven weight-specific CJK TTCs, twenty-eight CJK OTF files
(four languages x seven weights) that default to one of the four supported
languages, and twenty-eight region-specific OTF files (four regions x seven
weights) that support a region-specific subset of the full character repertoire.

The character repertoire is shared among all the Serif CJK fonts but there are
slight differences between them and the Sans CJK.  About 50 characters, mostly
new in Unicode 8.0 and 9.0, have been added, and about 1700 Plane 2 characters
(mostly CJK Unified Ideographs Extension B) have been temporarily removed (Hong
Kong support will be added in Version 2.000). The Serif CJK fonts support
approximately 43,000 characters with 65535 glyphs, the maximum number of glyphs
possible in a single font.  Most of the additional glyphs are regional variants,
there are also specific japanese variants, ideographic variation sequences,
vertical variants, precomposed Korean Jamo, and others.

As with Sans CJK, Noto Serif CJK was developed under an open source license by
Adobe Systems, Inc. and is almost identical to their Source Han Serif.  Please
see the detailed Adobe release notes for more information.

Noto Serif CJK is licensed under the SIL Open Font License, Version 1.1.


