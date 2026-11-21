# DDON Chunk Manager

Der lokale Chunk Manager verwendet Python 3.10 oder neuer und läuft in diesem
Linux-Workspace. Die Ausgangsbasis ist die englische `gmd.csv` im
Repository-Stamm. Der Split lässt sämtliche Einträge aus
`German/translations/` aus. Ein Chunk gehört jeweils zu einer GMD in einer
ARC, damit zusammenhängende Texte gemeinsam vorliegen.

Der vorbereitete Plan liegt neben dem Checkout unter
`../chunks-goal-5.2/`. Für gezielte neue Pläne gibt es beispielsweise
folgenden Aufruf ab dem Repository-Stamm.

```bash
python German/chunk_manager.py split ../chunks-auswahl --match '*quest*' --rows 60 --chars 10000
```

`--match` akzeptiert einen Glob für Schlüssel, GMD- oder ARC-Pfad. Pfade
lassen sich mit Schrägstrichen schreiben. `--chars` zählt die Zeichen der
japanischen und englischen Quellen einschließlich der Varianten. Einzeltexte
oberhalb des Richtwerts erhalten einen eigenen Chunk. Im Manifest stehen
die Pfade, die Anzahl der Einträge je Chunk und Fälle für eine manuelle
Prüfung, etwa doppelte Quelldatensätze.

Im gewünschten JSON unter `chunks/` nur `target_de` ausfüllen. `null`
steht für offene Einträge. `tag_source` gibt an, aus welcher Referenz die
Platzhalter für den Zieltext stammen. Alle Platzhalter dieser Referenz
müssen in ihrer Reihenfolge erhalten bleiben. Sie stehen für GMD-Tags
und Zeilenumbrüche. Das [deutsche Glossar](Glossar-Deutsch.md) gilt wie
bisher. `sources/` und das Manifest gehören zum vorbereiteten Plan.

```bash
python German/chunk_manager.py merge ../chunks-goal-5.2/chunks/chunk-00001.json
```

Der Merge importiert die ausgefüllten Felder eines Chunks als Overlay nach
`German/translations/`. Er liest die vollständige CSV nicht erneut. Der
Vorgang kann für denselben Chunk wiederholt werden, um weitere Einträge
hinzuzufügen. Bereits importierte Texte lassen sich in der erzeugten
Overlay-Datei korrigieren, sobald der Chunk abgeschlossen ist.
Bei einem Wechsel oder einer Änderung der Basis-CSV einen frischen Plan
anlegen. Die vollständige Launcher-CSV bei Bedarf mit dem vorhandenen
Generator erstellen.

```bash
python -m unittest discover -s German/tests -v
python German/build_gmd.py
python German/build_gmd.py --check
```
