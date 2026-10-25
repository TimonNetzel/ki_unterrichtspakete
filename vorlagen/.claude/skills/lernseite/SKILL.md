---
name: "lernseite"
description: "Macht aus einer Lerneinheit lernen.md eine interaktive Lernseite als eine HTML-Datei (offline, Handy und Tablet) plus Lernblatt-PDF und Lösungs-PDF."
---

# lernseite

**Sprache und Stil: verbindlich nach `CLAUDE.md`, Abschnitt „Sprache“.**

Einstiegsfassung. Ziel ist eine schlichte, verlässliche Seite. Ausbauen könnt ihr sie später Schritt für Schritt (Level, Punkte, Partnerarbeit, Quiz).

## Grundsatz: feste Vorlage, nur Inhalt neu
Beim ersten Mal baust du mit der Lehrkraft eine feste Vorlage `_werkzeuge/lernseite/vorlage.html` (Design, Navigation, Aufgabentypen, Druckansicht). Danach schreibst du pro Woche **nur** die Inhaltsdatei `content.js`. Das Bauskript setzt beides zusammen. So sieht jede Woche gleich aus und Fehler im Design entstehen nicht neu.

## Aufbau der Seite
1. Lernziele mit Selbsteinschätzung (unsicher, teilweise, sicher)
2. Aufwärmen (3 Fragen aus den Vorwochen)
3. Einstieg mit Leitfrage
4. Je Lernabschnitt: kurze Erklärung, 2–4 Aufgaben mit „Prüfen“-Knopf, Hilfen in Stufen, Lösung erst auf Wunsch
5. Abschlussprodukt mit Checkliste
6. Quiz zu den Fachbegriffen

Aufgabentypen in `content.js`: `mcq` (Auswahl), `cloze` (Lücken), `calc` (Zahl mit Toleranz), `order` (Reihenfolge), `write` (freier Text mit Musterantwort).

## Ausgabe
- `lernen.html`: eine Datei, alles eingebettet, ohne Internet nutzbar
- `lernen.pdf`: Lernblatt zum Ausfüllen (höchstens 2 Seiten)
- `lernen_loesungen.pdf`: gleiches Blatt mit Lösungen

## Test (im Bauskript)
- Die Seite mit Playwright auf 390 px (Handy) und 820 px (Tablet) öffnen, jede Aufgabe einmal richtig lösen, Screenshots ablegen.
- Keine JavaScript-Fehler, kein horizontales Scrollen, jede Aufgabe lösbar.
- Zeitschätzung: 1,5 min je Aufgabe, 0,5 min je Quizfrage. Liegt sie über der Dauer, kürzen (zuerst Wiederholungen, dann Bonusaufgaben) und jede Kürzung melden.
