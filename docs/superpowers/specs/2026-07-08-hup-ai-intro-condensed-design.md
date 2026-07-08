# Design: Deck condensato "Intro AI" per Hup (20260710_intro_AI_hup)

## Obiettivo

Condensare i contenuti di `slides/20260302_AI_per_turismo/index.html` (deck full-day, 115 slide, brand Digitiamo, taglio turismo) in un nuovo deck da **4 ore**, brandizzato Hup, pubblico aziendale generico, per la sessione del 2026-07-10.

Output: `slides/20260710_intro_AI_hup/index.html`.

## Agenda (4 ore)

1. **Ora 1 — Introduzione generale ai concetti AI**
2. **Ora 2 — Introduzione a Claude** (basata su tutti i livelli/pagine di https://claude101.com)
3. **Ora 3 — Revisione con esempi**: prompt engineering, MCP tools, skills aziendali
4. **Ora 4 — Use case** (contenuto da definire in seguito dall'utente)

## Rebranding

- Riuso il motore reveal.js e l'architettura CSS del deck originale (già collaudata: layout, responsive, header/footer).
- Rimappo le CSS custom properties del tema (righe ~385-451 e override mobile ~1172-1177 nel file originale) dai valori indigo/slate ai token Hup:
  - `--primary-color`, `--heading-color` → `--hup-navy` (#08205C)
  - `--accent-color`, `--accent-dark`, `--table-header-bg`, `--progress-color`, `--link-color` → `--hup-blue` (#2A68D4) / variante scura per hover
  - `--font-main` → stack Helvetica Neue (`"Helvetica Neue", Helvetica, Arial, "Liberation Sans", system-ui, sans-serif`)
  - `--hup-lime` (#C8FF00) usato con parsimonia per evidenziare 1-2 elementi chiave (es. accento su cover, bullet di enfasi), non come colore diffuso
  - Callout/warning/success mantenuti semanticamente (verde/ambra/blu) ma con tinte coerenti alla palette Hup dove serve armonia
- Logo: unico asset disponibile è `slides/20260710_intro_AI_hup/public/logo-hup_header-blu.png` (blu, trasparente). Copiato/riusato in `slides/20260710_intro_AI_hup/public/`.
  - Sfondi chiari (footer, header): logo blu diretto.
  - Sfondi scuri (cover, slide-section divisori): stesso file con filtro CSS `filter: brightness(0) invert(1)` per ottenere la resa bianca, senza bisogno di un secondo asset.
- Tutti i riferimenti `Digitiamo - Logo - *.png` e `alt="Digitiamo"` sostituiti; title/favicon aggiornati al brand Hup.
- Contenuto: titolo cover, agenda e conclusione riscritti per riflettere la nuova sessione (non più "AI per il Turismo" giornata intera, ma "Intro AI" 4 ore Hup).

## Struttura contenuti per blocco

### Ora 1 — Introduzione generale ai concetti AI (~13 slide)
- Cover + agenda della sessione (nuova, 4 blocchi)
- AI, ML, Deep Learning, AI Generativa: panoramica (1 slide, riuso immagine `panoramica_ai.png`)
- LLM: cos'è, tokenizzazione, training (2-3 slide, condensate dalle 9 originali della sezione "Large Language Models")
- Context window: cos'è, gestione, trend (1 slide, condensata da 6)
- Fine-tuning vs Prompting vs RAG: confronto e quando usare cosa (1 slide comparativa, sostituisce le sezioni "Fine-tuning" e parte di "RAG" originali, 8+11 slide → 1)
- RAG: concetto e architettura (1 slide, riuso immagine `rag_architecture.png` se coerente col nuovo layout)
- Agenti AI: concetto, differenza LLM/assistente/agente (1 slide, condensata da 8)
- Tools/Function calling + MCP: concetto (1 slide, condensata da 10)
- Esempi in tutta l'ora 1: generalizzati per contesto aziendale (non turismo) — es. email clienti, documenti interni, reportistica al posto di recensioni hotel/itinerari.

### Ora 2 — Introduzione a Claude (~10-11 slide)
Contenuto nuovo, non presente nel deck originale. Basato sulla struttura reale di claude101.com:
- 1 slide overview dei 4 livelli
- 1 slide per livello, con elenco pagine e descrizione breve:
  - **Beginner**: Claude For Dummies, Be good at Claude is (stupidly) simple, Claude Certified
  - **Intermediate**: Claude Cowork, Claude for teams, Claude Design, Claude Cowork + Projects, Claude for slides, Claude Skills
  - **Advanced**: Claude to sound like you, Stop hitting Claude limits, Stop Prompting, Claude replaced me, Stop sounding like AI, Excel with Claude cowork
  - **Expert**: Claude Connectors, Claude Code, Stop using your own Claude at work
- 1-2 slide di approfondimento sulle pagine più rilevanti per l'ora 3 (Claude Cowork, Claude Skills, Claude Projects) — contenuto reale recuperato da claude101.com in fase di stesura (via WebFetch pagina per pagina), non solo titoli.

### Ora 3 — Prompt engineering, MCP tools, skills aziendali con esempi (~10-11 slide)
- Prompting efficace: condensato da 10 a ~5 slide (anatomia prompt, zero/few-shot/CoT, templating, errori comuni, debugging), esempi generalizzati per contesto aziendale
- MCP e tool calling: concetto + esempio pratico (2-3 slide, condensate dalla sezione "Tools e Function Calling" originale)
- Skills aziendali: 1 slide di concetto ("cos'è una Skill Claude", come si costruisce) + 1 slide placeholder esplicitamente segnata **"Skill aziendali Hup — da completare"**, pronta per essere riempita con esempi reali forniti in seguito dall'utente.

### Ora 4 — Use case (placeholder)
- Slide divisore "Use Case"
- 1 slide placeholder "da definire" — contenuto reale da concordare con l'utente in un secondo momento.

### Appendice (fuori dal conteggio 4 ore)
- Glossario: mantenuto in fondo come reference post-corso, condensato se necessario ma senza vincoli di tempo stringenti.

## Rimosso rispetto al deck originale
- Tutte le slide "Challenge" (quiz con QR code)
- Sezione "Strumenti AI: guida pratica" (confronto ChatGPT/Copilot/Gemini) — sostituita dal focus specifico su Claude nell'ora 2
- Sezione "Identificare Opportunità" (framework processi ripetitivi, matrice impatto/sforzo)
- Sezione "Sicurezza e Privacy" (GDPR, regole prompt) — tagliata per intero, non compressa

## Stima dimensione finale
~40-45 slide totali (incl. cover, divisori di sezione, appendice glossario) per 4 ore di sessione (~5-6 min/slide con discussione), contro le 115 slide del deck originale.

## Note di implementazione
- Riuso struttura HTML `<section data-section-title="...">` con `<section class="slide-section">` (divisore) e `<section class="slide">` (contenuto), coerente col deck originale.
- Immagini riusate dal deck originale dove il diagramma resta valido dopo la condensazione (`panoramica_ai.png`, `rag_architecture.png`); copiate in `slides/20260710_intro_AI_hup/public/images/`.
- Il file `hup-brand-components.html` resta come riferimento del design system, non viene toccato.
