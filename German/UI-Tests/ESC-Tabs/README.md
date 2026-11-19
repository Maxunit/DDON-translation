# Deutsche ESC-Reiter

Die sieben Reiter lauten „Charakter“, „Quests“, „Welt“, „Gruppe“, „Soziales“, „Optionen“ und „Online-Shop“. Alle sieben wurden im Client geprüft. Der Patch ersetzt RGB und Alpha der Schriftzüge im Atlas `word_ID_jpn`.

Für den Patch wird die englisch beschriftete `ddo_common.arc` aus dem Stand der Menu Translation Mod 1.21 mit der SHA-256-Prüfsumme `e68de748c56dc1698f8cad6804743119175d363e49626254a67051eb6d4b3ec8` benötigt. Mit `apply.py` und `esc-tabs.patch.json` im selben Ordner erzeugt der folgende Befehl die separat geprüfte Datei mit der SHA-256-Prüfsumme `d040952af3d58019d0252a46c9a4d037d90264764a9d025a9d664913df1750d4`.

```sh
python apply.py ddo_common.arc ddo_common-de.arc
```

`ddo_common-de.arc` kann nach der Sicherung der vorhandenen Datei als `nativePC/rom/ddo_common.arc` installiert werden. Die Untermenüs werden über die vollständige deutsche Launcher-CSV aktualisiert.
