---
name: "lerneinheit-vorbereiten"
description: "Nur als Hilfsschritt von /wochenpaket: macht aus schnitt_woche.md eine ausführliche Lerneinheit lernen.md für den Skill lernseite."
---

# lerneinheit-vorbereiten

**Sprache und Stil: verbindlich nach `CLAUDE.md`, Abschnitt „Sprache“.**

Eingabe: `<Klasse> <Woche>`. `_werkzeuge/arbeit/<Klasse>-wNN/schnitt_woche.md` und `schnitt_bis.md` existieren. Lies außerdem `<Klasse>/kurs.json`. Keine Rückfragen.

Aufgabe: Erzeuge `_werkzeuge/arbeit/<Klasse>-wNN/lernen/lernen.md` mit diesen Abschnitten:

1. `# Titel der Woche` (aus dem Skript)
2. `## Auftrag`: Zielgruppe aus den Kursdaten, Anrede (Du, wenn das Skript nichts anderes sagt), Dauer in Minuten.
3. `## Lernziele`: 2–3 Ziele „Am Ende kannst du …“ in Alltagssprache.
4. `## Aufwärmen`: 3 kurze Fragen aus den **Vorwochen** laut `schnitt_bis.md`, je 4 Antworten, alle ähnlich lang, die richtige nicht die längste.
5. `## Einstieg`: kurze Situation aus dem Berufsfeld der Klasse mit Leitfrage. Namen und Daten konstruiert.
6. `## Lernabschnitt 1`, `## Lernabschnitt 2`: Ziel, Kernaussagen, Aufträge, je 2–3 Sätze „Ich kann …“.
7. `## Fachbegriffe`: Tabelle Begriff | Erklärung in einfacher Sprache | Beispiel.
8. `## Abschlussprodukt`: aus dem Lernauftrag der Woche.
9. `## Referenzergebnisse`: vollständige Lösungen. Rechne jede Zahl mit Python nach.
10. `**Stoffgrenze:**` Was NICHT eingeführt werden darf (Stoff späterer Wochen).

## Regeln
- Nur Stoff der Woche und der Vorwochen, nichts aus späteren Wochen.
- Angaben zu Personen, Jahren und Studien nur, wenn sie sicher sind. Im Zweifel weglassen.
- Umfang knapp halten, damit die Weiterverarbeitung wenig Token kostet.
- Gib am Ende nur den Pfad der Datei und eine Zeile Zusammenfassung zurück.
