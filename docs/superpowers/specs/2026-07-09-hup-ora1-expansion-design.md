# Design: Espansione Ora 1 — Concetti Fondamentali AI (Hup deck)

## Contesto

Il deck `slides/20260710_intro_AI_hup/index.html` (branch `feat/intro-ai-hup`) è stato
condensato dal corso full-day `slides/20260302_AI_per_turismo/index.html` in una sessione
di 4 ore per Hup. Dopo revisione, l'Ora 1 (Concetti Fondamentali AI, 8 slide) è risultata
troppo astratta: mancano esempi visivi concreti che nel corso sorgente erano distribuiti
su più sezioni (LLM, Context Window, Agenti AI).

Questo design espande solo l'Ora 1, da 8 a 14 slide, riportando/adattando contenuti ed
elementi visivi dal corso sorgente, generalizzati per un contesto aziendale (non turismo)
per coerenza con il resto del deck Hup.

## Vincoli

- Riusa lo stile visivo esistente (classi `layout-diagram`, `layout-three-col`, `.diagram`,
  `.callout`, `.card`, chat-mockup inline-style) — nessun nuovo pattern CSS.
- Nessuna immagine nuova: tutti gli elementi grafici sono HTML/CSS nativi (coerente con la
  decisione dell'utente di riusare gli snippet HTML del corso turismo invece di generare
  asset immagine).
- Tutti gli esempi devono essere generalizzati per contesto aziendale, non turistico
  (vincolo già stabilito per l'intero deck Hup).
- Il branding Hup (token colore, font, logo) è già applicato all'intero file — le nuove
  slide devono usare gli stessi componenti/var CSS già definiti, senza hardcode di colori.
- Non toccare Ora 2, Ora 3, Ora 4, Chiusura, Glossario — modifica isolata alla sezione
  `data-section-title="Ora 1 — Concetti Fondamentali AI"` (righe ~1435-1671 dell'index.html
  attuale).
- L'utente ha accettato che Ora 1 diventi più densa (14 slide) senza sottrarre tempo alle
  altre ore.

## Struttura risultante (8 → 14 slide)

| # | Slide | Stato |
|---|-------|-------|
| 1.1 | AI, ML, Deep Learning, AI Generativa (panoramica) | invariata |
| 1.2 | Esempi concreti di modelli (ML, DL, GenAI esistenti) | **nuova** |
| 1.3 | Cos'è un LLM | invariata |
| 1.4 | Tokenizzazione: il testo diventa numeri | **nuova** — adattata da corso turismo §2.2 |
| 1.5 | Come un LLM genera testo | **nuova** — adattata da corso turismo §2.1/§2.3, semplificata |
| 1.6 | Context Window (definizione) | invariata |
| 1.7 | Context Window — esempio di conversazione | **nuova** — chat-mockup adattato da corso turismo §3.3, business-generico |
| 1.8 | Context rot — quando iniziare una nuova conversazione | **nuova**, contenuto originale (nessun equivalente nel corso sorgente) |
| 1.9 | Fine-tuning, Prompting, RAG: quando usare cosa | invariata, callout rinforzato |
| 1.10 | RAG — Retrieval Augmented Generation | invariata |
| 1.11 | Agenti AI: LLM, Assistente, Agente | invariata nei contenuti, upgrade visivo (icon-card da corso turismo §6.1) |
| 1.12 | Agenti con accesso a strumenti reali (bash, python, file) | **nuova** — diagramma ReAct adattato da corso turismo §6.2, esempio business/coding |
| 1.13 | Tools, Function Calling e MCP | invariata |
| 1.14 | Riepilogo Ora 1 | invariata nella struttura, bullet aggiornati |

## Contenuti dettagliati per slide nuove/modificate

### 1.2 — Esempi concreti di modelli
`layout-three-col`, tre card:
- **ML** — regressione, alberi decisionali, random forest → *previsione vendite, scoring
  crediti, rilevamento frodi*
- **Deep Learning** — reti neurali profonde, CNN → *riconoscimento immagini, trascrizione
  vocale*
- **AI Generativa** — LLM (GPT-4, Claude, Gemini, Llama) → testo, codice; modelli immagine
  (Midjourney, DALL-E, Stable Diffusion) → immagini

Callout: "Stesso principio — apprendere pattern dai dati — output molto diversi."

### 1.4 — Tokenizzazione
`layout-diagram`, blocco `.diagram` in stile ASCII (adattato da corso turismo §2.2, parole
sostituite con esempi business-generici):

```
"Fatturazione" → ["Fatt", "ura", "zione"] → [4921, 1203, 3847]
"dashboard"    → ["dash", "board"]        → [10314, 2898]
"€"            → ["€"]                     → [27975]
```

- ~1 token ≈ 0.75 parole in inglese / 0.6 parole in italiano
- Il costo delle chiamate API si misura in token (input + output)
- Link allo strumento interattivo: platform.openai.com/tokenizer

### 1.5 — Come un LLM genera testo
`layout-diagram`, fusione semplificata di corso turismo §2.1 (predizione) e §2.3
(transformer, senza il dettaglio architetturale):

```
Input: "Il report di vendita mostra un calo del"
   ↓
[LLM: predice probabilità per ogni token possibile]
   ↓
"15" (68%) → "10" (12%) → "20" (9%) → ...
   ↓
Sceglie "15", lo aggiunge al testo, e ripete da capo
```

Callout: genera un token alla volta; ogni nuovo token tiene conto di tutto il testo
precedente, incluso quello appena generato dal modello stesso.

### 1.7 — Context Window, esempio di conversazione
Chat-mockup adattato da corso turismo §3.3 (stessa struttura inline-style: header,
messaggi sbiaditi fuori dalla context window, box evidenziato "↕ context window", input
bar). Scenario sostituito da hotel a business-generico: un "Assistente Operations" che
gestisce una richiesta interna aziendale su più turni, con i messaggi più vecchi
visivamente sbiaditi (fuori dalla finestra di contesto) e gli ultimi scambi dentro il box
evidenziato.

### 1.8 — Context rot
`layout-list` + callout, contenuto originale (non presente nel corso sorgente):
- Man mano che il contesto cresce — specialmente se pieno di informazioni irrilevanti o
  contraddittorie — la qualità delle risposte peggiora, non solo quando il contesto è
  "pieno" ma già prima
- Regola pratica per iniziare una nuova conversazione:
  - cambio di argomento netto rispetto a quanto discusso finora
  - il modello inizia a ignorare istruzioni date in precedenza
  - la conversazione ha accumulato molti tentativi/correzioni falliti
  - si sta per iniziare un task grande e indipendente dal precedente

### 1.9 — Fine-tuning, Prompting, RAG (callout rinforzato)
Aggiunta di un callout più esplicito sul messaggio chiave: "Il modello non impara nulla di
nuovo in prompting e RAG: i suoi pesi restano identici. Cambia solo cosa gli mettiamo nel
contesto. Il fine-tuning è l'eccezione — lì i pesi cambiano davvero — ma resta un caso raro."

### 1.11 — Agenti AI (upgrade visivo)
Stessa struttura concettuale a 3 card (LLM / Assistente / Agente), ma con lo stile
icon-card del corso turismo §6.1 (icona + badge colorato + lista puntata compatta + tag
monospace del flusso input→output) al posto delle card testuali semplici attuali.

### 1.12 — Agenti con accesso a strumenti reali
Diagramma in stile ReAct (`layout-diagram`, adattato da corso turismo §6.2), esempio
business/coding invece di prenotazione voli:

```
Goal: "Analizza vendite_2026.csv e riassumi i trend per reparto"

[Reason] → Devo leggere il file e capire la struttura dati
[Act]     → leggi_file("vendite_2026.csv")
[Observe] → {colonne: [data, reparto, importo], righe: 4200}

[Reason] → Serve uno script per aggregare per reparto
[Act]     → esegui_python("pandas.groupby('reparto').sum()")
[Observe] → {Vendite: 120k, Marketing: 45k, IT: 30k, ...}

[Reason] → Ho i dati aggregati, task completato
[Output]  → "Riepilogo pronto: Vendite +12%, Marketing stabile..."
```

Callout: questi sono gli stessi strumenti che useremo con Claude nell'Ora 2 (lettura file,
esecuzione codice, bash) — collegamento esplicito in avanti.

### 1.14 — Riepilogo Ora 1 (bullet aggiornati)
I bullet esistenti restano, integrati con almeno un riferimento a tokenizzazione/context
rot/agenti-con-strumenti per riflettere il contenuto ampliato.

## Fuori scope

- Nessuna modifica a Ora 2, Ora 3, Ora 4, Chiusura, Glossario.
- Nessuna nuova immagine PNG/asset grafico.
- Nessun contenuto tourism-specifico riportato as-is (tutto generalizzato per business).
