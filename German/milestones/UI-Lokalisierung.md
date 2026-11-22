# Deutsche Spieloberfläche

Die deutsche Spieloberfläche deckt die spielerseitigen Texte in
`ui\00_message\ui\` außerhalb der Credits ab. In der Übersetzungsrunde mit
lokalen Modellentwürfen wurden 3.705 Einträge übernommen. Dazu zählen auch
Glossareinträge, sprachneutrale Bezeichnungen und mehrere im Spiel verwendete
Kopien desselben Textes.

Die sprachliche Einzelprüfung dieser 3.705 Einträge ist abgeschlossen.
Maßgeblich waren der japanische Originaltext, die englische Vorlage, der
Menükontext und die bisherige deutsche Terminologie. Die Texte verwenden für
die direkte Spieleransprache die Du-Form.

Der Vergleich mit `8c24348` ergibt 2.283 Änderungen an Anzeigetextfeldern.
Die übrigen CSV-Felder sind bytegleich. Die Launcher-CSV und ihr Manifest
wurden neu erzeugt und geprüft. Die CSV enthält 131.126 Datensätze.
Platzhalter, Formatargumente, Steuerzeichen und Spielsymbole wurden
abgeglichen. Alle neun Repository-Tests sind bestanden.

Ein Sichttest im Client steht aus. Dazu gehört die zusammengesetzte
Anzeige mit `common_msg_jp_of` aus `systemFlow.arc` und `gui_cmn.arc`.
Die deutsche Fassung verwendet dort einen Gedankenstrich als Trennzeichen.

## Technische Fundstellen

- 211 Datensätze enthalten in beiden Quellfeldern ausschließlich Steuerzeichen,
  Leerraum oder leere Werte. Sie haben keinen statischen Text.
- Im Optionsmenü liegt der Eintrag `OPTION_MSG_TITLE_M_TITLE01` mit
  ReadIndex `38` in `option_res_win.gmd` und ARC `\ui\uGUIOption.arc`
  dreimal mit identischer Identität und identischem Quelltext vor. Die japanische
  Bedeutung ist „Geräteeinstellungen“. Der Generator kann die drei identischen
  Datensätze nicht eindeutig adressieren und weist ein Overlay dafür zurück.
- Die folgenden Einträge sind Befehlsliterale. Schlüssel und ReadIndex
  bezeichnen jeden Datensatz einzeln. Eine Übersetzung der Befehlswörter
  würde die Syntax ändern.

| GMD | ARC | Schlüssel | ReadIndex |
| --- | --- | --- | --- |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2388` | `0` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2389` | `1` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2390` | `2` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2391` | `3` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2392` | `4` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2393` | `5` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2394` | `6` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2395` | `7` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2396` | `8` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2397` | `9` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2398` | `10` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2399` | `11` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2400` | `12` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2401` | `13` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2402` | `14` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2403` | `15` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2404` | `16` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2405` | `17` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2406` | `18` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2407` | `19` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2408` | `20` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2409` | `21` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2411` | `22` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2412` | `23` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2413` | `24` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2414` | `25` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2415` | `26` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2416` | `27` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2417` | `28` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2419` | `29` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2420` | `30` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2421` | `31` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2422` | `32` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2424` | `33` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2425` | `34` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2426` | `35` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2427` | `36` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2428` | `37` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2429` | `38` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2430` | `39` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2433` | `40` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2434` | `41` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2435` | `42` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2436` | `43` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2437` | `44` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2438` | `45` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2439` | `46` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2441` | `47` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2442` | `48` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2443` | `49` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2444` | `50` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2445` | `51` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2447` | `52` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2448` | `53` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2449` | `54` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2450` | `55` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2451` | `56` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2454` | `57` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2455` | `58` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2456` | `59` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2457` | `60` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2463` | `61` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2464` | `62` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2466` | `63` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2467` | `64` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2470` | `65` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2471` | `66` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2472` | `67` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2473` | `68` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2477` | `69` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2478` | `70` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2479` | `71` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2482` | `72` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2483` | `73` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2484` | `74` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2486` | `75` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2488` | `76` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2489` | `77` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2490` | `78` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2491` | `79` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2492` | `80` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2493` | `81` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2495` | `82` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2496` | `83` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2497` | `84` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2498` | `85` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2499` | `86` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2501` | `87` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2502` | `88` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2504` | `89` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2505` | `90` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2507` | `91` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2509` | `92` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2510` | `93` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2512` | `94` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2513` | `95` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2515` | `96` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2516` | `97` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2518` | `98` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2522` | `99` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2523` | `100` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2527` | `101` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2529` | `102` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2530` | `103` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2533` | `104` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2534` | `105` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2537` | `106` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2538` | `107` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2539` | `108` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_2540` | `109` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9069` | `110` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9070` | `111` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9071` | `112` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9072` | `113` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9073` | `114` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9074` | `115` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9075` | `116` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9076` | `117` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9077` | `118` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9078` | `119` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9079` | `120` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9080` | `121` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9081` | `122` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9082` | `123` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9083` | `124` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9084` | `125` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9085` | `126` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9086` | `127` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9087` | `128` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9088` | `129` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9089` | `130` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9090` | `131` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9091` | `132` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9092` | `133` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9093` | `134` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9094` | `135` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9095` | `136` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9096` | `137` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9097` | `138` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9098` | `139` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9099` | `140` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9100` | `141` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9101` | `142` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9102` | `143` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9103` | `144` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9104` | `145` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9105` | `146` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9106` | `147` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9107` | `148` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9108` | `149` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9109` | `150` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9110` | `151` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9111` | `152` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9112` | `153` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9113` | `154` |
| `ui\00_message\ui\simple_text.gmd` | `\ui\gui_cmn.arc` | `simple_text_9114` | `155` |
