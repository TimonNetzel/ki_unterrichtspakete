---
name: "aufgabenblatt"
description: "Erstellt aus einem Skriptausschnitt ein Aufgabenblatt im Stil der Abiturvorgaben des Fachs als HTML mit Schülerteil, Lehrkraftteil und Lösung plus PDF des Schülerteils."
---

# aufgabenblatt

**Sprache und Stil: verbindlich nach `CLAUDE.md`, Abschnitt „Sprache“.** Anrede „Sie“, Operatoren laut den Vorgaben des Fachs.

## Standard
- Ein Kopf (Name, Klasse, Datum, Zeit, Hilfsmittel, Punkte).
- **Eine** Ausgangssituation mit **einem** Materialblock (M1, M2, …), danach 6–9 Teilaufgaben.
- Jede Teilaufgabe beginnt mit einem **fett gesetzten Operator** und trägt Anforderungsbereich (I, II, III) und Punkte.
- Umfang: etwa 0,6 Punkte je Minute. Verteilung: I 30–40 %, II 45–55 %, III 15–20 %.
- Baut eine Teilaufgabe auf einer anderen auf, gib Ersatzwerte an. Ersatzwerte verraten nie die richtige Lösung.
- Daten sind konstruiert, Firmennamen fiktiv.

## Ansichten in der HTML-Datei
Gesamt, Schülerteil, Lehrkraftteil (Stoffgrenze, Erwartungshorizont, typische Fehler), Schülerlösung. Ein Drucken-Knopf druckt die gewählte Ansicht auf A4.

## Operatoren
Hier die Operatorenliste eures Fachs eintragen, mit typischem Anforderungsbereich, z. B.:
- nennen (I), beschreiben (I–II), erklären (II), auswerten (II), beurteilen (III)

## Prüfen vor der Abgabe
- Jede Zahl und jede Musterlösung mit Python nachrechnen (`nachrechnen.py`), Abweichungen sofort korrigieren.
- Nichts aus späteren Wochen.
- Stilprüfung über `content.html`.
