# Unterrichtsmaterial mit Claude Code

Dieses Repo enthält die Skills, Werkzeuge und Halbjahresskripte, aus denen `/wochenpaket` jede Woche Lernmaterial baut. Die Sitzung läuft in der Cloud unter Linux.

## Sprache
- Generisches Maskulinum (Schüler, Lehrkraft). Keine Doppelformen. (Eure Schule entscheidet das selbst. Wichtig ist nur, dass es hier einmal festgelegt ist.)
- Keine Gedankenstriche, keine Semikolons. Stattdessen ein neuer Satz oder ein Komma.
- Kurze, konkrete Sätze mit Beispiel statt allgemeiner Aussagen. Keine Floskeln wie „In der heutigen Zeit“.
- Prüfung: `python3 _werkzeuge/stilcheck.py <Dateien>`. Fehler beheben, Hinweise kritisch ansehen.

## Struktur
- `.claude/skills/`: wochenpaket, lerneinheit-vorbereiten, lernseite, aufgabenblatt
- `.claude/agents/`: `autor` (erstellt Material), `lektor` (prüft Sprache in den Quelldateien)
- `_werkzeuge/`: `schnitt.py` (Skript zuschneiden), `lernen_bauen.sh` und `ueben_bauen.sh` (bauen, testen, erst bei Erfolg ins Klassen-Repo kopieren), `index_bauen.py` (Übersichtsseite), `stilcheck.py`
- `<KLASSE>/quellen/*.md`: Halbjahresskript der Klasse. `<KLASSE>/kurs.json`: Kursdaten (Fach, Schuljahr, Titel, optional Lehrkraft-Code und Stil).
- `<KLASSE>/github/`: Klon des öffentlichen Klassen-Repos, nur in der Sitzung angelegt, steht in `.gitignore`.
- `_werkzeuge/arbeit/`: Zwischendateien, steht in `.gitignore`.

## Klassen-Repos (öffentlich, mit GitHub Pages)
- 11A: `<github-name>/11A_Biologie`
- (je Klasse eine Zeile)

Ablauf: Repo mit `add_repo` (access `push`) an die Sitzung hängen, dann genau einmal `git clone --depth 1` nach `<KLASSE>/github`, sonst `git pull`. Branch ist `main`.

## Arbeitsweise
- Alle relativen Pfade beziehen sich auf die Repo-Wurzel.
- Python heißt `python3`. Node ist vorhanden. Chromium für PDFs liegt unter `/opt/pw-browsers`.
- Halbjahresskripte nie vollständig lesen, immer erst mit `schnitt.py` schneiden.
- Korrekturen nur in den Quelldateien unter `_werkzeuge/arbeit/`, nie in den fertigen Dateien im Klassen-Repo.

## GitHub-Upload
- Nie ohne klares Ok der Lehrkraft im Chat committen oder pushen. Vorher `git add -A`, `git status --short`, Änderungsliste zeigen (neu, geändert, gelöscht), Ok abwarten.
- Nie hochladen: `kurs.json`, Halbjahresskripte, Klausuren, alles mit dem Lehrkraft-Code.
- Commit-Identität: `-c user.name="Claude" -c user.email="noreply@anthropic.com"`.
