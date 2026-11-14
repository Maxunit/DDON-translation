DDON – laufende deutsche UI-Testfassung

Feste Custom-URL für den Launcher:
https://raw.githubusercontent.com/Maxunit/DDON-translation/refs/heads/test/charselect-de-0.1.1/German/gmd.csv

Diese URL ab jetzt für die laufenden Tests beibehalten. Künftige Änderungen werden in derselben Datei unter demselben Branch veröffentlicht; dafür keine neue Varianten-URL wählen.
Die CSV enthält alle 131.125 Einträge des englischen Ausgangsstands. Aktuell sind genau drei Beschriftungen der Charakterauswahl geändert:
Create / char_sel_add_newchar: Neu
Confirm / char_sel_decide: Bestätigen
Cancel / char_sel_cancel: Abbrechen

Neu wurde nach dem Vergleich mit Erstellen vom Benutzer gewählt. Confirm und Cancel gehören laut Benutzer zum Löschablauf der Charakterauswahl; Bestätigen und Abbrechen wurden für diesen Kontext ausdrücklich angenommen.
Deutsch steht weiterhin in MsgEn, also der englischen Zielspalte. Alle übrigen Inhalte bleiben auf dem englischen Ausgangsstand.

Die alten kurz/normal/lang-Dateien unter UI-Tests/CharacterSelect sind Vergleichsstände. Sie sind nicht mehr die laufende Update-URL.
Die vollständige englische Basis bleibt für einen gezielten Rückwechsel verfügbar. Ein URL-Wechsel dorthin kann laut Benutzer wieder den vollständigen Patchablauf auslösen:
https://raw.githubusercontent.com/Maxunit/DDON-translation/refs/heads/test/charselect-de-0.1.1/German/UI-Tests/CharacterSelect/00-englische-basis/gmd.csv

Das Launcher-Symbol und seine Update-Erkennung wurden vom Benutzer beschrieben. Ob das neue Angebot unter dieser festen URL automatisch erkannt wird und schneller patcht, ist beim nächsten Test noch zu bestätigen. Es werden keine Aussagen über Delta-Patches oder die interne Prüfmethodik gemacht.
Die Veröffentlichung installiert nichts und verändert keine Clientdateien. GUI-, DDS- und Archivlayoutänderungen sind nicht enthalten.
gmd-manifest.json dokumentiert Quelle, gewählte Texte, Datensatzanzahl und SHA-256.
