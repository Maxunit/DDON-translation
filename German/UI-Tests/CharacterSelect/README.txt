DDON – Charakterauswahl: deutscher Wortlängentest 0.1.1

Dieser eigene Testbranch stellt vollständige gmd.csv-Dateien für den Custom-Import des Launchers bereit.
Jede CSV enthält 131.125 Datensätze. In den drei deutschen Varianten ändern sich ausschließlich die MsgEn-Felder für Create, Confirm und Cancel. Die englische Basis ist bytegleich zur vollständigen Quell-CSV.

Raw-URLs – jeweils eine Variante im Launcher verwenden
00-englische-basis
https://raw.githubusercontent.com/Maxunit/DDON-translation/refs/heads/test/charselect-de-0.1.1/German/UI-Tests/CharacterSelect/00-englische-basis/gmd.csv

01-kurz
https://raw.githubusercontent.com/Maxunit/DDON-translation/refs/heads/test/charselect-de-0.1.1/German/UI-Tests/CharacterSelect/01-kurz/gmd.csv

02-normal
https://raw.githubusercontent.com/Maxunit/DDON-translation/refs/heads/test/charselect-de-0.1.1/German/UI-Tests/CharacterSelect/02-normal/gmd.csv

03-lang
https://raw.githubusercontent.com/Maxunit/DDON-translation/refs/heads/test/charselect-de-0.1.1/German/UI-Tests/CharacterSelect/03-lang/gmd.csv

Beschriftungen (Create / Confirm / Cancel)
00-englische-basis: Create / Confirm / Cancel
01-kurz: Neu / OK / Zurück
02-normal: Erstellen / Bestätigen / Abbrechen
03-lang: Neuen Charakter für dieses Konto erstellen / Auswahl anschließend bestätigen / Vorgang ohne Änderungen abbrechen

Deutsch steht in der englischen Zielspalte MsgEn. Falls der Launcher nach der Zielsprache fragt, Englisch/English wählen.
Die Dateien sind Testformulierungen, keine vollständige deutsche Lokalisierung. Änderungen an DDS, GUI-Layouts oder Titelmenü-Grafiken gehören nicht zu diesem Test.
Bei gleicher Auflösung, UI-Skalierung und Eingabeart kurz/normal/lang vergleichen. Auf Abschneiden, Umbruch, Schriftverkleinerung, Überlagerung und Ä/ä/ü/ß achten. Falls ein Zieltext nicht erscheint, als nicht sichtbar dokumentieren; daraus folgt noch kein Längenlimit.
Die Löschfunktion gehört nicht zum Test. Die tatsächliche Zuordnung der Schlüssel zu sichtbaren GUI-Flächen muss noch im Client bestätigt werden.

Englische Basis und Prüfung
00-englische-basis/gmd.csv setzt die Übersetzungsdaten auf den angegebenen englischen Repository-Stand zurück. Sie ist kein Backup der tatsächlich installierten ARC-Dateien oder individueller anderer Änderungen.
Offline geprüft: vollständiger Vergleich aller Datensätze, exakt drei geänderte Felder je deutscher Variante, bytegenau unveränderter übriger Inhalt, UTF-8 und Prüfsummen. CSV-Dateihashes stehen in SHA256SUMS.txt und manifest.json.
Kein automatischer Launcherimport, kein Renderingtest und keine Installation wurden durch die Veröffentlichung ausgeführt.
Basis: Maxunit/DDON-translation / 6a6b28e6ff55285acc9d2950eb6a9498e9e7bc13
