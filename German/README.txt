DDON – deutsche Launcher-Testfassung

Feste Custom-URL für den Launcher:
https://raw.githubusercontent.com/Maxunit/DDON-translation/refs/heads/test/charselect-de-0.1.1/German/gmd.csv

Diese URL beibehalten. German/gmd.csv ist eine vollständige CSV mit 131.125 Datensätzen.

Neu, Bestätigen und Abbrechen wurden vom Benutzer gemeinsam im Client geprüft und korrekt angezeigt. Der Benutzer bestätigt die Darstellung von Charakter löschen, den Löschhinweisen, Drehen / Zoomen, Kamerasteuerung und Clan-Benachrichtigung. Der Test im Client bestätigte auch die Profiltexte, Pässe und die untere Tastenleiste mit dem Standard-Font.

Kämpfer-Durchlauf
Bei „Neu“ beginnen, einen gültigen Namen und eine Vorlage wählen, dann als Kämpfer starten. Die GMD-Texte decken die Kernmenüs des Editors, die Klassenwahl, die erste Szene mit Leo und Iris sowie die Tutorialfenster „Was sind Erweckte?“, „Grundsteuerung“ und „Grundtaktik: Kämpfer“ ab. Der Test endet vor dem Betreten der Festung Gritten. Im Client sind die Darstellung der längeren Hilfetexte, die Tastensymbole und weitere Dialoge im Kampf zu prüfen.

Pflege und automatische Erstellung
Die Texte stehen in German/translations/. Die neuen Einträge für den Kämpfer-Durchlauf stehen in fighter-opening-*.json. Für jeden Eintrag sind Schlüssel, ReadIndex, japanischer und englischer Quelltext sowie deutscher Zieltext dokumentiert. Zeilenumbrüche sind als \r\n gespeichert. Das einzelne Leerzeichen bei char_sel_index_jp darf nicht entfernt werden.

Die Action "Build German launcher CSV" läuft bei Änderungen an Übersetzungen, Generator, Tests, Workflow oder der vollständigen englischen gmd.csv im Repository-Stamm auf test/charselect-de-0.1.1. Sie erstellt daraus German/gmd.csv und gmd-manifest.json und committet die Ergebnisse auf denselben Branch. Die Launcher-URL bleibt gleich. Sind die Dateien bereits aktuell, entsteht kein zusätzlicher Commit. Der Workflow verändert keine Dateien auf main.

Der Generator nutzt ausschließlich die eingecheckte vollständige gmd.csv im Repository-Stamm als englische Basis. Er holt keine externen Updates und baut die englischen Split-Dateien nicht selbst neu zusammen. Soll eine neuere englische Basis übernommen werden, muss zuerst diese Stammdatei im Testbranch aktualisiert werden. Geänderte Quelltexte unserer deutschen Einträge stoppen den Build, bis die Übersetzungen geprüft und die Quelltextreferenzen angepasst sind.

Prüfungen: mindestens 131.125 Datensätze; vollständiger CSV-Vergleich; ausschließlich freigegebene MsgEn-Felder geändert; Kontrolltags in identischer Reihenfolge; eindeutige und vorhandene Einträge; übrige Quellbytes bleiben unverändert. Generator und Tests benötigen nur die Python-Standardbibliothek.
Lokal: python German/build_gmd.py
Prüfen ohne Schreiben: python German/build_gmd.py --check
Tests: python -m unittest discover -s German/tests -v

Weitere Hinweise
Deutsch wird weiterhin in MsgEn gespeichert. Die alten kurz/normal/lang-Dateien unter German/UI-Tests/CharacterSelect dienen als Vergleichsstände.

Vorläufige Begriffe: Course wird testweise als Pässe bezeichnet; Golden Gemstones als Goldsteine. Das ist keine verbindliche Terminologiefestlegung für das gesamte Spiel. Die UI-Texte sind neutral formuliert und legen Du/Sie für Dialoge nicht fest. Dynamische Texte aus <OPCS> können aus anderen, noch nicht bearbeiteten Ressourcen stammen.
