# DDON-Glossar und Stilregeln für Deutsch

Das [Referenzglossar](snapshot/Terms%20and%20references%20directory/glossary.csv) liefert die japanischen und englischen Begriffe. Hier stehen die deutschen Festlegungen und Regeln für die Oberfläche. Bei Abweichungen ist der japanische Originaltext maßgeblich. Die englische Fassung hilft bei der Zuordnung. Bereits festgelegte deutsche Menübegriffe gelten auch in den Anleitungen.

| Referenz | Deutsch |
| --- | --- |
| Pawn | Vasall |
| Main Pawn | Hauptvasall |
| Support Pawn | Hilfsvasall |
| Quick Party | Schnellsuche |
| Lestania News | Lestania-Nachrichten |
| World im Sinn von Channel | Kanal |

## Umbrüche in Questbeschreibungen

Im Questfenster für „Pflege für Waffen und Rüstungen“ ohne den 44er-Wert für die UI-Skalierung passt die Zeile mit „Trockener Knoc“ hinein. Das folgende `h` landet auf der nächsten Zeile. Gemessen mit den Zeichenvorschüben aus `ddo_font_jpn_win.gfd` sind das 860 Einheiten bis zum `c` und 881 mit dem `h`. Das ergibt einen Richtwert von rund 870 Schrifteinheiten bzw. etwa 325–330 Pixeln für dieses Questfenster. Für deutsche Questbeschreibungen in diesem Fenster sind **höchstens 810 Schrifteinheiten je Zeile** der Arbeitswert mit Reserve.

- Zeilenbreiten anhand der Zeichenvorschübe prüfen. Bei `<LQEM>` den Gegnernamen samt Stufenangabe wie `(LV.12~)` einsetzen. Bei `<LQIM>` den Gegenstandsnamen und bei `<LQVA>` die Zahl einsetzen. Die Board-Rotation kann diese Werte ändern.
- Feste GMD-Umbrüche als `\r\n` an Satz- oder Wortgrenzen setzen. Ein dynamisches Ziel möglichst an den Zeilenanfang setzen. Bei langem Zielnamen bekommt es eine eigene Zeile.
- GMD-Platzhalter und Steuercodes vollständig erhalten. Einen Umbruch nur außerhalb eines Platzhalters setzen. Nach einem Umbruch auch die Zeichensetzung und verbleibende Zeilenzahl prüfen.
- Bei einem Sichttest einen möglichst langen Zielnamen wählen und das Fenster mit nativer Skalierung ansehen. Bei einer abweichenden UI-Skalierung zusätzlich die Breite, die Zahl sichtbarer Zeilen und die letzte Zeile kontrollieren.

## Umbrüche in NPC-Dialogen

Für NPC-Dialogboxen gilt die native UI-Größe als Referenz. Der Arbeitswert liegt bei **höchstens 775 Schrifteinheiten pro Zeile**. Bei Alfred war eine so breite Zeile vollständig sichtbar. Die genaue Umbruchgrenze ist noch offen.

| UI-Einstellung | Gemessene Schriftbreite | Beobachtung |
| --- | --- | --- |
| Native UI-Größe | Rund 0,50 Screenshot-Pixel je Schrifteinheit | Die Zeile mit 775 Einheiten belegt rund 385 Pixel. |
| 1080p mit `Enlarge UI = 44` | Rund 0,60 Screenshot-Pixel je Schrifteinheit | Der frühere Arbeitswert von 700 Einheiten entspricht rund 420 Pixeln. |

Die Zeilen anhand der Zeichenvorschübe prüfen und feste GMD-Umbrüche als `\r\n` an Satz- oder Wortgrenzen setzen. Bei Alfred standen die beiden beobachteten Umbrüche bereits in der englischen GMD-Vorlage. Beim Sichttest auch die letzte Zeile und den Abstand zum Fensterrand kontrollieren. Die Originalmessungen für NPC-Dialog und Chat stehen im [Sichttestprotokoll von Goal 3](first-pawn/Goal-3-Bestandsaufnahme.md).
