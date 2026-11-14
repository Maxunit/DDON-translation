DDON – deutsche Charakterauswahl (Testfassung)

Feste Custom-URL für den Launcher:
https://raw.githubusercontent.com/Maxunit/DDON-translation/refs/heads/test/charselect-de-0.1.1/German/gmd.csv

Diese URL beibehalten. German/gmd.csv ist eine vollständige CSV mit 131.125 Datensätzen. 31 Einträge der CharacterSelect_res.gmd und fünf Profil-Einträge sind erfasst; Status und die absichtlich unterdrückte zweite Überschrift (ein Leerzeichen) bleiben erhalten.

Neu, Bestätigen und Abbrechen wurden vom Benutzer gemeinsam im Client geprüft und korrekt angezeigt. Der Benutzer bestätigt die Darstellung von Charakter löschen, den Löschhinweisen, Drehen / Zoomen, Kamerasteuerung und Clan-Benachrichtigung. Die Profiltexte und Pässe sind neu und im Client noch zu prüfen.

Pflege und automatische Erstellung
Die Texte stehen in German/translations/character-select.json und character-select-profile.json. Für jeden Eintrag sind Schlüssel, ReadIndex, japanischer und englischer Quelltext sowie deutscher Zieltext dokumentiert. Zeilenumbrüche sind als \r\n gespeichert. Das einzelne Leerzeichen bei char_sel_index_jp darf nicht entfernt werden.

Die Action "Build German launcher CSV" läuft bei Änderungen an Übersetzungen, Generator, Tests, Workflow oder der vollständigen englischen gmd.csv im Repository-Stamm auf test/charselect-de-0.1.1. Sie erstellt daraus German/gmd.csv und gmd-manifest.json und committet die Ergebnisse auf denselben Branch. Die Launcher-URL bleibt gleich. Sind die Dateien bereits aktuell, entsteht kein zusätzlicher Commit. Der Workflow verändert keine Dateien auf main.

Der Generator nutzt ausschließlich die eingecheckte vollständige gmd.csv im Repository-Stamm als englische Basis. Er holt keine externen Updates und baut die englischen Split-Dateien nicht selbst neu zusammen. Soll eine neuere englische Basis übernommen werden, muss zuerst diese Stammdatei im Testbranch aktualisiert werden. Geänderte Quelltexte unserer deutschen Einträge stoppen den Build, bis die Übersetzungen geprüft und die Quelltextreferenzen angepasst sind.

Prüfungen: mindestens 131.125 Datensätze; vollständiger CSV-Vergleich; ausschließlich freigegebene MsgEn-Felder geändert; Kontrolltags in identischer Reihenfolge; eindeutige und vorhandene Einträge; übrige Quellbytes bleiben unverändert. Generator und Tests benötigen nur die Python-Standardbibliothek.
Lokal: python German/build_gmd.py
Prüfen ohne Schreiben: python German/build_gmd.py --check
Tests: python -m unittest discover -s German/tests -v

Weitere Hinweise
Deutsch wird weiterhin in MsgEn gespeichert. Weitere Profiltexte, Serverwahl, Charaktererstellung und DDS-Grafiken gehören nicht zu dieser Fassung. Die dortigen Texte bleiben auf dem bisherigen Stand. Die alten kurz/normal/lang-Dateien unter German/UI-Tests/CharacterSelect bleiben Vergleichsstände.

Vorläufige Begriffe: Course wird testweise als Pässe bezeichnet; Golden Gemstones als Goldsteine. Das ist keine verbindliche Terminologiefestlegung für das gesamte Spiel. Die UI-Texte sind neutral formuliert und legen Du/Sie für Dialoge nicht fest. Dynamische Texte aus <OPCS> können aus anderen, noch nicht bearbeiteten Ressourcen stammen.

Keine Installation und keine Änderung von Clientdateien durch den Agenten.
