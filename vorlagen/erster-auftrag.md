# Erster Auftrag an Claude

Diesen Text kopiert ihr in die erste Cloud-Sitzung von Claude Code, die auf eurem eigenen privaten Repo läuft. Die Teile in spitzen Klammern ersetzt ihr vorher.

---

Ich bin Lehrkraft für <Fach> am <Schulform> und möchte jede Woche Lernmaterial aus meinem Halbjahresskript bauen lassen.

1. Klone das öffentliche Repo `TimonNetzel/ki_unterrichtspakete` nach `/tmp/vorlage` und kopiere den Inhalt von `vorlagen/` in die Wurzel meines Repos. Benenne den Ordner `KLASSE` in `<Klasse>` um.
2. Passe `CLAUDE.md` an: Fach, Klassen, Namen der Klassen-Repos (`<github-name>/<Klasse>_<Fach>`).
3. Lege `.gitignore` an mit `*/github/`, `_werkzeuge/arbeit/`, `node_modules/` und `__pycache__/`.
4. Baue die fehlenden Werkzeuge in `_werkzeuge/` (Beschreibung in `CLAUDE.md` und in den Skills):
   - `stilcheck.py`: meldet Gedankenstriche, Semikolons und Floskeln in HTML, JS und MD, mit Zeilennummer.
   - `lernen_bauen.sh` und `ueben_bauen.sh`: bauen aus den Quellen in `_werkzeuge/arbeit/<Klasse>-wNN/` die fertigen Dateien, testen sie im Browser (Playwright), drucken die PDFs mit Chromium und kopieren **erst nach bestandenem Test** nach `<Klasse>/github/woche-NN/`.
   - `index_bauen.py`: baut aus den Ordnern `woche-NN` die Übersichtsseite `index.html` des Klassen-Repos.
5. Baue mit mir zusammen die feste Vorlage für die Lernseite (Skill `lernseite`). Zeig mir zuerst einen Entwurf mit Beispielinhalt.
6. Zeig mir alle Änderungen und warte auf mein Ok, bevor du committest oder pushst.

Stelle Rückfragen, bevor du loslegst, wenn etwas unklar ist.
