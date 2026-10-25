#!/usr/bin/env python3
"""schnitt.py: schneidet ein Halbjahresskript (.md) für einen Wochenlauf zu.

Aufruf:
    python3 schnitt.py <skript.md> <woche> <ausgabeordner>

Erzeugt im Ausgabeordner:
    schnitt_woche.md  Kopf + Abschnitt der Woche (Eingabe für lernen.md)
    schnitt_bis.md    Kopf + Wochen 1 bis <woche> (Eingabe für das Aufgabenblatt)

Erwartetes Format: Wochen als Überschrift "### Woche <n> ...", Kapitel als "## ...".
Der Kopf ist alles vor dem ersten Kapitel. Ein Abschnitt "## Arbeitsauftrag an Claude"
wird verworfen, damit eine Anweisung im Skript nicht versehentlich ausgeführt wird.
"""
import os
import re
import sys


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    pfad, woche, ziel = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    with open(pfad, encoding="utf-8") as f:
        zeilen = f.read().replace("\r\n", "\n").split("\n")

    kopf, wochen, kapitel = [], {}, ""
    aktuell = None   # Nummer der laufenden Woche
    im_kopf = True
    verwerfen = False
    for z in zeilen:
        if z.startswith("## "):
            name = z[3:].strip().lower()
            verwerfen = name.startswith("arbeitsauftrag")
            if name.startswith("kursdaten"):
                kopf.append(z)
            elif not verwerfen:
                im_kopf, kapitel, aktuell = False, z, None
            continue
        if verwerfen:
            continue
        m = re.match(r"###\s+Woche\s+(\d+)", z)
        if m:
            aktuell = int(m.group(1))
            wochen[aktuell] = [kapitel, ""]
        if im_kopf:
            kopf.append(z)
        elif aktuell is not None:
            wochen[aktuell].append(z)

    if woche not in wochen:
        sys.exit(f"Woche {woche} nicht gefunden. Vorhanden: {sorted(wochen)}")

    os.makedirs(ziel, exist_ok=True)
    k = "\n".join(kopf).strip() + "\n\n"
    with open(os.path.join(ziel, "schnitt_woche.md"), "w", encoding="utf-8") as f:
        f.write(k + "\n".join(wochen[woche]).strip() + "\n")
    bis = [w for w in sorted(wochen) if w <= woche]
    with open(os.path.join(ziel, "schnitt_bis.md"), "w", encoding="utf-8") as f:
        f.write(k + "\n\n".join("\n".join(wochen[w]).strip() for w in bis) + "\n")
    print(f"schnitt_woche.md: Woche {woche}, schnitt_bis.md: Wochen {bis[0]} bis {woche}")


if __name__ == "__main__":
    main()
