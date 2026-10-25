---
name: "wochenpaket"
description: "Nur bei ausdrücklichem Aufruf (/wochenpaket Klasse Woche MinutenLernen MinutenÜben): erstellt für eine Klasse und Woche die Lernseite lernen.html mit Lernblatt-PDF und Lösung sowie das Aufgabenblatt ueben.html mit PDF im Ordner woche-NN des Klassen-Repos."
---

# wochenpaket

**Sprache und Stil: verbindlich nach `CLAUDE.md`, Abschnitt „Sprache“.** Dort stehen auch Struktur, Klassen-Repos und die Upload-Regeln.

Aufruf: `/wochenpaket <Klasse> <Woche> [MinutenLernen] [MinutenÜben]`, z. B. `/wochenpaket 11A 6 90 20`. Fehlt MinutenLernen, gilt 90. Fehlt MinutenÜben, gilt 20. Keine Rückfragen außer: Fehlt Klasse oder Woche, frage genau einmal in einem Satz.

## Pfade
- `NN` = Woche zweistellig. `<A>` = `_werkzeuge/arbeit/<Klasse>-wNN` (alle Zwischendateien). `<G>` = `<Klasse>/github` (Klon des Klassen-Repos). Ziel: `<G>/woche-NN/`.
- Lernen: Quellen in `<A>/lernen/`. Bauen und kopieren nur mit `bash _werkzeuge/lernen_bauen.sh <Klasse> <Woche> [--test]`.
- Üben: Quellen in `<A>/ueben/`. Bauen und kopieren nur mit `bash _werkzeuge/ueben_bauen.sh <Klasse> <Woche>`.

## Regeln
- Nie ohne ausdrückliches Ok der Lehrkraft committen oder pushen (Schritt 7).
- Ändern darfst du nur `<G>/woche-NN/`, `<G>/index.html` (nur über `index_bauen.py`) und `<A>`.
- Das Halbjahresskript nie vollständig lesen, immer erst schneiden.

## Schritte
0. **Klon.** Klassen-Repo laut `CLAUDE.md` anhängen und klonen oder aktualisieren. Scheitert der Zugriff, den Grund melden und abbrechen.
1. **Prüfen.** Halbjahresskript in `<Klasse>/quellen/*.md` suchen. Fehlt es, Pfad melden und abbrechen. Liegen in `<G>/woche-NN/` schon Dateien, genau einmal fragen: alles ersetzen, nur Lernen, nur Üben oder abbrechen.
2. **Schneiden.** `python3 _werkzeuge/schnitt.py <skript.md> <Woche> <A>`. Ergebnis: `schnitt_woche.md` (nur diese Woche) und `schnitt_bis.md` (Wochen 1 bis Woche).
3. **Agenten.** Starte beide gleichzeitig mit `subagent_type autor`. Jeder bekommt nur Pfade, Parameter und seinen Auftrag, nicht diese Konversation.
   - **Agent A (Lernen):** Führe `.claude/skills/lerneinheit-vorbereiten/SKILL.md` mit `<Klasse> <Woche>` aus. Baue dann nach `.claude/skills/lernseite/SKILL.md` aus `<A>/lernen/lernen.md` die Lernseite für MinutenLernen. Bauen und testen mit `lernen_bauen.sh --test`. Rückmeldung: Abschnitte der Seite, Zeitschätzung, Warnungen des Tests.
   - **Agent B (Üben):** Baue nach `.claude/skills/aufgabenblatt/SKILL.md` aus `<A>/schnitt_bis.md` ein Aufgabenblatt für MinutenÜben, Stoff nur Woche <Woche> mit Anschluss an die Vorwochen. Jede Zahl und jede Musterlösung mit Python nachrechnen (`<A>/ueben/nachrechnen.py`). Zum Schluss `ueben_bauen.sh`. Rückmeldung: „Nachgerechnet: n Aufgaben, Abweichungen: …“ und Liste der Teilaufgaben.
4. **Prüfen und Lektorat.**
   1. In `<G>/woche-NN/` liegen lernen.html, lernen.pdf, lernen_loesungen.pdf, ueben.html, ueben.pdf. Stichprobe mit `pdftotext`: Die Lösungs-PDF enthält Lösungen, `lernen.pdf` keine. Nichts aus späteren Wochen.
   2. `python3 _werkzeuge/stilcheck.py <Quelldateien> > <A>/treffer.txt`
   3. Starte einen frischen Subagenten `lektor`. Er bekommt nur die Quelldateien und `<A>/treffer.txt` und korrigiert direkt in den Quellen.
   4. Neu bauen (beide Bauskripte), Stilprüfung erneut.
5. **Übersichtsseite:** `python3 _werkzeuge/index_bauen.py <Klasse>`.
6. **Abschlussmeldung** in höchstens 15 Zeilen: erstellte Dateien, Standardannahmen, Zeitschätzung, Auffälligkeiten.
7. **Upload, nie ohne Ok:** `git -C <G> add -A`, `git -C <G> status --short`, Änderungsliste zeigen, auf ein klares Ok warten. Erst dann committen und `git -C <G> push origin main`.

Scheitert ein Agent, melde genau, was fehlt, und liefere den erfolgreichen Teil trotzdem.
