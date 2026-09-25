# Demo: `/reorient` i Codex och VS Code

Det här är ett körklart manus. Demon visar hur agenten hittar en avsiktlig
regression, väljer minsta värdefulla nästa steg och verifierar resultatet.

## Vad publiken ska få se

`/reorient` ska:

1. pausa implementationen
2. läsa mål, krav och processregler
3. granska kod, tester och Git-diff
4. skilja på processfel och implementationsfel
5. föreslå exakt ett konkret nästa steg
6. välja `CORRECT COURSE` när riktningen är fel
7. välja `STOP` när allt är klart och verifierat

## Förberedelser

1. Öppna repots rotmapp i VS Code.
2. Öppna terminalen med **Terminal > New Terminal**.
3. Kör `git status --short`.
4. Kontrollera att `app.py` är den enda ändrade implementationsfilen.
5. Kontrollera att VIP-raden i `app.py` är `return total * 0.85`.
6. Öppna flikarna `README.md`, `SPEC.md`, `PROCESS.md`, `AGENTS.md`,
   `app.py` och `test_app.py`.
7. Öppna Codex-chatten i VS Code.

Startläget är avsiktligt fel: `SPEC.md` kräver 20 procent VIP-rabatt, medan
`app.py` bara ger 15 procent.

## 1. Introducera projektet

**Klicka:** Öppna `README.md`.

**Säg:**

> Det här är ett träningsprojekt för agentkontrollen `/reorient`. Det är inte
> ett inbyggt VS Code-kommando, utan en triggerfras definierad i `AGENTS.md`.

**Visa:** Peka på de åtta områden som granskas: mål, specifikation, process,
framsteg, fastnat arbete, nästa åtgärd, värde och beslut.

## 2. Visa källorna till sanning

**Klicka:** Öppna `SPEC.md` och peka på `REQ-004`.

**Säg:**

> Premiumkunder får 10 procent rabatt och VIP-kunder ska få 20 procent.
> Alla tester i `test_app.py` ska gå igenom och ingen orelaterad funktionalitet
> får läggas till.

**Klicka:** Öppna `PROCESS.md`.

**Säg:**

> Processen kräver att agenten läser specifikationen, gör minsta nödvändiga
> ändring och kör hela testsviten innan arbetet förklaras färdigt.

**Klicka:** Öppna `AGENTS.md`, tryck `Ctrl+F` och sök efter
`Trigger: /reorient`.

**Säg:**

> Här finns agentinstruktionen. När jag skriver `/reorient` ska agenten pausa
> implementationen och samla konkreta bevis innan den fattar ett beslut.

## 3. Visa det avsiktliga felet

**Klicka:** Öppna `app.py` och markera:

```python
if customer_type == "vip":
    return total * 0.85
```

**Säg:**

> Multiplikatorn 0,85 ger 15 procent rabatt och bryter mot `REQ-004`.

**Klicka:** Öppna `test_app.py` och markera VIP-testets förväntade värde `160`.

**Säg:**

> Två varor för 100 kronor ska kosta 160 kronor efter 20 procents rabatt.
> Den nuvarande koden ger i stället 170 kronor.

**Skriv i terminalen:**

```powershell
python -m unittest discover
```

**Visa och säg:**

> Fyra tester går igenom och VIP-testet fallerar med `170.0 != 160`. Nu har vi
> ett verifierat fel, inte bara en misstanke.

## 4. Kör `/reorient`

**Klicka:** Klicka i Codex-chattens inmatningsfält.

**Skriv och skicka:**

```text
/reorient
```

Agenten ska läsa projektfilerna, bedöma testresultatet och kontrollera
`git status --short`, `git diff --stat` och `git diff`.

### Förväntat svar

- **Goal alignment:** `YES` – ändringen gäller rabattfunktionen.
- **Specification alignment:** `NO` – `0.85` bryter mot `REQ-004`.
- **Process compliance:** kan vara `YES`; fel kod är inte automatiskt fel process.
- **Verifiable progress:** `NO` – diffen introducerar en regression.
- **Stuck detection:** `NO` – ett enstaka fel är ingen upprepad loop.
- **Best next action:** återställ VIP-multiplikatorn till `0.80`.
- **Value test:** `YES` – åtgärden fixar ett verifierat fel.
- **Decision:** `CORRECT COURSE`.

Svaret ska avslutas ungefär så här:

```text
Direction: CORRECT | Next: Restore VIP multiplier to 0.80 | Value: Satisfies REQ-004
```

**Säg:**

> Agenten föreslår ingen stor refaktorering. Den hittar den minsta ändring som
> skapar verifierbart värde.

## 5. Låt agenten rätta felet

**Skriv i Codex-chatten:**

```text
Gör den föreslagna minsta ändringen.
```

**Visa:** Öppna `app.py` och kontrollera att raden är
`return total * 0.80`.

**Säg:**

> Agenten ändrade bara den felaktiga multiplikatorn och lade inte till något
> orelaterat.

## 6. Verifiera rättningen

**Skriv i terminalen:**

```powershell
python -m unittest discover
```

**Visa och säg:**

> Nu går alla fem tester igenom. Testerna verifierar beteendet och `REQ-004`
> visar att implementationen matchar kravet.

Kör därefter dessa kommandon, ett i taget:

```powershell
git status --short
git diff
```

Om regressionen var den enda lokala ändringen ska implementationens diff nu
vara tom.

## 7. Kör `/reorient` igen

**Skriv i Codex-chatten:**

```text
/reorient
```

Den andra granskningen ska se att kraven är uppfyllda och att hela testsviten
går igenom. **Verifiable progress** ska ändå vara `NO`, eftersom en tom aktuell
implementationsdiff inte räknas som nuvarande framsteg enligt `AGENTS.md`.

Beslutet ska vara `STOP`: inget känt krav återstår och mer kod skulle inte ge
nödvändigt värde. En rimlig slutrad är:

```text
Direction: OK | Next: Stop implementation | Value: Avoids unnecessary changes
```

## Avslutning

**Säg:**

> Demon visar skillnaden mellan aktivitet och verkliga framsteg. `/reorient`
> kräver bevis från krav, kod, tester och Git. Agenten kan därför både korrigera
> en felaktig riktning och sluta när arbetet faktiskt är färdigt.

## Snabbversion på cirka två minuter

1. Visa `REQ-004` i `SPEC.md`.
2. Visa `0.85` i `app.py`.
3. Kör testerna och visa VIP-felet.
4. Skriv `/reorient` i Codex-chatten.
5. Visa `CORRECT COURSE` och nästa steg `0.80`.
6. Be agenten göra minsta ändringen.
7. Kör testerna igen och visa att alla fem går igenom.
8. Kör `/reorient` igen och visa beslutet `STOP`.

## Reservplan

- Om inget händer efter `/reorient`, skriv först `Läs AGENTS.md`.
- Om testet inte fallerar, kontrollera att VIP-raden är `0.85`.
- Om flera filer är ändrade, kör `git status --short` och förklara vilka som
  hör till demon.
- Om agenten föreslår flera nästa steg, visa regeln i `AGENTS.md` om exakt en
  konkret åtgärd.
- Om agenten väljer `STOP AND VERIFY` efter komplett verifiering, visa
  beslutsprecedensen i `AGENTS.md`: uppfyllda krav och godkända tester ger `STOP`.
