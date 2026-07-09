# Espansione Ora 1 (Hup deck) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand the "Ora 1 — Concetti Fondamentali AI" section of `slides/20260710_intro_AI_hup/index.html` from 8 to 14 slides, adding concrete visual examples (model examples, tokenization, generation process, context window conversation example, context rot) that were present in the source tourism deck but were lost during condensation, generalized for a business audience.

**Architecture:** Content-only edit to a single contiguous region of one self-contained HTML file (reveal.js deck, no build step). New slides reuse existing CSS component classes already defined in the file (`.card`, `.callout`, `.diagram`, `layout-three-col`, `layout-diagram`, `layout-list`) plus one inline-styled chat-mockup pattern adapted from the source deck. No new CSS, no new images, no build tooling. "Tests" are grep-based structural checks (tag balance, marker counts, no leftover indigo/tourism hex) plus manual visual review in a browser.

**Tech Stack:** reveal.js (already bundled inline in the target file), plain HTML/CSS using the file's existing custom properties. No npm/build tooling.

## Global Constraints

- Target file: `slides/20260710_intro_AI_hup/index.html`. Only the `data-section-title="Ora 1 — Concetti Fondamentali AI"` section (currently lines ~1435-1671) may be touched. Do not modify Ora 2, Ora 3, Ora 4, Chiusura, or Glossario.
- All new copy is in Italian, matching the rest of the deck.
- All examples must be business-generic — no tourism references (per design spec, `docs/superpowers/specs/2026-07-09-hup-ora1-expansion-design.md`).
- No new CSS rules, no new image assets. Reuse existing classes: `.card`, `.callout`, `.warning`, `.diagram`/`.block-diagram`, `layout-three-col`, `layout-diagram`, `layout-list`, `layout-two-col`, `table-keyed`.
- Any inline color must use the file's existing CSS custom properties (`var(--accent-color)`, `var(--border-color)`, etc.) or neutral grays already used elsewhere in the file (e.g. `#e2e8f0`, `#f8fafc`, `#94a3b8`). **Never** reintroduce indigo/tourism-brand hex values (e.g. `#6366f1`, `#4f46e5`, `rgba(99,102,241,...)`) — a prior task on this branch already had to remove one such leftover.
- Every new/renumbered slide keeps the existing header pattern: `<span class="slide-section-label">Ora 1 · Concetti AI</span>` and the existing footer pattern (`<img class="footer-logo" alt="Hup.">` + `<span class="footer-page"></span>`).
- Git: commit locally only after each task. **Do not push** (standing user instruction for this branch).
- Slide-numbering comments (`<!-- 1.X — Title -->`) are code comments only, not rendered content — update them for maintainability but they have no visual effect.

---

## Task 1: Slides 1.1–1.8 (model examples, tokenization, generation, context window + context rot)

**Files:**
- Modify: `slides/20260710_intro_AI_hup/index.html:1437-1528` (the `slide-section` divider through the end of the current "Context Window" slide)

**Interfaces:**
- Consumes: the file as it exists on the current branch tip (commit `0a7898d`), specifically the exact text block from `<section class="slide-section">` (Ora 1 divider) through the closing `</section>` of the current "Context Window" slide.
- Produces: 8 slides (1.1 unchanged, 1.2 new, 1.3 unchanged content/renumbered comment, 1.4 new, 1.5 new, 1.6 unchanged content/renumbered comment, 1.7 new, 1.8 new), ending immediately before the still-untouched `<!-- 1.4 — Fine-tuning vs Prompting vs RAG -->` comment that Task 2 will modify. Task 2 does not depend on any specific text Task 1 produces (its Find target is untouched by this task) but must run after Task 1 commits, since both tasks edit the same file sequentially.

- [ ] **Step 1: Replace the slide-section divider through the end of the Context Window slide**

Find this exact block in `slides/20260710_intro_AI_hup/index.html` (currently lines 1437-1528):

```html
  <section class="slide-section">
    <div class="section-eyebrow">Ora 1</div>
    <h2>Concetti Fondamentali di AI</h2>
    <p class="section-desc">Cos'è un LLM · Context window · Fine-tuning, RAG e prompting · Agenti e tool calling</p>
  </section>

  <!-- 1.1 — AI, ML, DL, GenAI -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>AI, ML, Deep Learning, AI Generativa</h2>
    </div>
    <div class="slide-body layout-diagram">
      <img src="public/images/panoramica_ai.png" alt="AI, ML, Deep Learning, AI Generativa" style="width:50%; height:auto; border-radius:var(--border-radius);">
      <ul style="font-size:0.8em; margin-top:2em;">
        <li><strong>AI</strong> — sistemi che eseguono compiti tipicamente umani</li>
        <li><strong>ML</strong> — apprende da dati, senza regole scritte a mano</li>
        <li><strong>Deep Learning</strong> — ML con reti neurali profonde</li>
        <li><strong>AI Generativa</strong> — produce testo, immagini, audio, codice</li>
      </ul>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.2 — Cos'è un LLM -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Cos'è un Large Language Model</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Come funziona</h3>
        <ul>
          <li>Il testo viene spezzato in <strong>token</strong> (pezzi di parola) e convertito in numeri</li>
          <li>Il modello predice, un token alla volta, quale sia il più probabile successivo</li>
          <li>Ha imparato questa capacità leggendo enormi quantità di testo</li>
        </ul>
      </div>
      <div>
        <h3>Cosa NON fa</h3>
        <ul>
          <li>Non "ragiona" come un umano: non ha una comprensione, ma un modello statistico del linguaggio</li>
          <li>Può generare testo fluente e sbagliato allo stesso tempo (allucinazioni)</li>
          <li>Non accede a dati nuovi se non glieli fornisci tu (vedi RAG)</li>
        </ul>
      </div>
      <div class="callout">
        Un LLM è un motore di previsione del testo addestrato su scala enorme — non un database di fatti, non un ragionatore logico puro.
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.3 — Context window -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Context Window</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Cos'è</h3>
        <ul>
          <li>La quantità di testo che il modello può "vedere" in un colpo solo (prompt + conversazione + documenti allegati)</li>
          <li>Misurata in token, non in parole o pagine</li>
          <li>I modelli attuali vanno da ~128k a oltre 1M di token di contesto</li>
        </ul>
      </div>
      <div>
        <h3>Perché conta</h3>
        <ul>
          <li>Contesto pieno → il modello "dimentica" le parti più vecchie della conversazione</li>
          <li>Più contesto non è sempre meglio: informazioni irrilevanti diluiscono l'attenzione del modello</li>
          <li>Documenti lunghi vanno riassunti o recuperati selettivamente (vedi RAG), non sempre incollati per intero</li>
        </ul>
      </div>
      <div class="callout">
        Regola pratica: dai al modello solo il contesto rilevante per il task, non tutto quello che hai a disposizione.
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>
```

Replace with:

```html
  <section class="slide-section">
    <div class="section-eyebrow">Ora 1</div>
    <h2>Concetti Fondamentali di AI</h2>
    <p class="section-desc">Modelli e tokenizzazione · Context window e context rot · Fine-tuning, RAG e prompting · Agenti e tool reali</p>
  </section>

  <!-- 1.1 — AI, ML, DL, GenAI -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>AI, ML, Deep Learning, AI Generativa</h2>
    </div>
    <div class="slide-body layout-diagram">
      <img src="public/images/panoramica_ai.png" alt="AI, ML, Deep Learning, AI Generativa" style="width:50%; height:auto; border-radius:var(--border-radius);">
      <ul style="font-size:0.8em; margin-top:2em;">
        <li><strong>AI</strong> — sistemi che eseguono compiti tipicamente umani</li>
        <li><strong>ML</strong> — apprende da dati, senza regole scritte a mano</li>
        <li><strong>Deep Learning</strong> — ML con reti neurali profonde</li>
        <li><strong>AI Generativa</strong> — produce testo, immagini, audio, codice</li>
      </ul>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.2 — Esempi concreti di modelli -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Esempi concreti: modelli in uso oggi</h2>
    </div>
    <div class="slide-body layout-three-col">
      <div class="card">
        <h4>Machine Learning</h4>
        <p>Regressione, alberi decisionali, random forest.</p>
        <p class="text-muted text-small">Previsione vendite, scoring crediti, rilevamento frodi.</p>
      </div>
      <div class="card">
        <h4>Deep Learning</h4>
        <p>Reti neurali profonde, reti convoluzionali (CNN).</p>
        <p class="text-muted text-small">Riconoscimento immagini, trascrizione vocale.</p>
      </div>
      <div class="card">
        <h4>AI Generativa</h4>
        <p>LLM (GPT-4, Claude, Gemini, Llama); modelli immagine (Midjourney, DALL-E, Stable Diffusion).</p>
        <p class="text-muted text-small">Genera testo, codice, immagini.</p>
      </div>
      <div class="callout">Stesso principio — apprendere pattern dai dati — output molto diversi.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.3 — Cos'è un LLM -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Cos'è un Large Language Model</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Come funziona</h3>
        <ul>
          <li>Il testo viene spezzato in <strong>token</strong> (pezzi di parola) e convertito in numeri</li>
          <li>Il modello predice, un token alla volta, quale sia il più probabile successivo</li>
          <li>Ha imparato questa capacità leggendo enormi quantità di testo</li>
        </ul>
      </div>
      <div>
        <h3>Cosa NON fa</h3>
        <ul>
          <li>Non "ragiona" come un umano: non ha una comprensione, ma un modello statistico del linguaggio</li>
          <li>Può generare testo fluente e sbagliato allo stesso tempo (allucinazioni)</li>
          <li>Non accede a dati nuovi se non glieli fornisci tu (vedi RAG)</li>
        </ul>
      </div>
      <div class="callout">
        Un LLM è un motore di previsione del testo addestrato su scala enorme — non un database di fatti, non un ragionatore logico puro.
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.4 — Tokenizzazione -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Tokenizzazione: il testo diventa numeri</h2>
    </div>
    <div class="slide-body layout-diagram">
      <p>Prima di elaborare il testo, l'LLM lo converte in <strong>token</strong> (frammenti di parole).</p>
      <div class="diagram">
"Fatturazione" → ["Fatt", "ura", "zione"] → [4921, 1203, 3847]

"dashboard"    → ["dash", "board"]        → [10314, 2898]

"€"            → ["€"]                     → [27975]
      </div>
      <ul style="margin-top:0.8em">
        <li>~1 token ≈ 0.75 parole in inglese / ~0.6 parole in italiano</li>
        <li>Il costo delle chiamate API si misura in token (input + output)</li>
        <li>Parole rare o tecniche → più token → più costose</li>
      </ul>
      <p class="text-small text-muted">Strumento interattivo: <a href="https://platform.openai.com/tokenizer" target="_blank" rel="noopener">platform.openai.com/tokenizer</a></p>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.5 — Come un LLM genera testo -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Come un LLM genera testo</h2>
    </div>
    <div class="slide-body layout-diagram">
      <div class="diagram">
Input: "Il report di vendita mostra un calo del"
   ↓
[LLM: predice una probabilità per ogni token possibile]
   ↓
"15" (68%)  →  "10" (12%)  →  "20" (9%)  →  ...
   ↓
Sceglie "15", lo aggiunge al testo, e ripete da capo
      </div>
      <div class="callout" style="margin-top:1em">
        Il modello genera un token alla volta: ogni nuovo token tiene conto di tutto il testo precedente, incluso quello che ha appena generato lui stesso.
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.6 — Context window -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Context Window</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Cos'è</h3>
        <ul>
          <li>La quantità di testo che il modello può "vedere" in un colpo solo (prompt + conversazione + documenti allegati)</li>
          <li>Misurata in token, non in parole o pagine</li>
          <li>I modelli attuali vanno da ~128k a oltre 1M di token di contesto</li>
        </ul>
      </div>
      <div>
        <h3>Perché conta</h3>
        <ul>
          <li>Contesto pieno → il modello "dimentica" le parti più vecchie della conversazione</li>
          <li>Più contesto non è sempre meglio: informazioni irrilevanti diluiscono l'attenzione del modello</li>
          <li>Documenti lunghi vanno riassunti o recuperati selettivamente (vedi RAG), non sempre incollati per intero</li>
        </ul>
      </div>
      <div class="callout">
        Regola pratica: dai al modello solo il contesto rilevante per il task, non tutto quello che hai a disposizione.
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.7 — Context window: esempio di conversazione -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Context window: un esempio di conversazione</h2>
    </div>
    <div class="slide-body" style="display:grid; grid-template-columns:1.4fr 1fr; gap:var(--gap-lg); align-content:center;">
      <div>
        <h3>Cosa succede in pratica</h3>
        <ul>
          <li>Ogni nuovo messaggio si aggiunge alla conversazione, ma la finestra di contesto ha una dimensione massima</li>
          <li>I messaggi più vecchi, se il contesto è pieno, escono dalla finestra: il modello smette di "vederli"</li>
          <li>Il modello risponde solo in base a ciò che rientra ancora nella finestra</li>
        </ul>
        <div class="callout" style="margin-top:0.8em">
          Nell'esempio a destra, i primi scambi (sbiaditi) sono ormai fuori dalla context window: se chiedessi di nuovo "che laptop ha richiesto Marco", il modello non lo saprebbe più.
        </div>
      </div>

      <!-- Chat mock -->
      <div style="display:flex; flex-direction:column; font-size:0.56em; background:#f8f9fb; border-radius:12px; overflow:hidden; border:1px solid var(--border-color); box-shadow:0 4px 16px rgba(0,0,0,0.08);">
        <div style="display:flex; align-items:center; gap:0.5em; background:var(--accent-color); color:#fff; padding:0.55em 0.9em; flex-shrink:0;">
          <div style="width:1.8em; height:1.8em; background:rgba(255,255,255,0.25); border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.1em; flex-shrink:0;">💬</div>
          <div>
            <div style="font-weight:700; line-height:1.2;">Assistente Operations</div>
            <div style="font-size:0.75em; color:#4ade80;">● online</div>
          </div>
        </div>

        <div style="display:flex; flex-direction:column; gap:0.14em; padding:0.6em 0.65em; flex:1; overflow:hidden;">

          <!-- Out-of-context messages — faded -->
          <div style="opacity:0.35; display:flex; flex-direction:column; gap:0.14em;">
            <div style="align-self:flex-end; background:var(--accent-color); color:#fff; padding:0.28em 0.6em; border-radius:10px 10px 2px 10px; max-width:82%; line-height:1.35;">
              Ho aperto il ticket IT-4021 per il laptop di Marco.
            </div>
            <div style="align-self:flex-start; background:#fff; border:1px solid #e2e8f0; padding:0.28em 0.6em; border-radius:10px 10px 10px 2px; max-width:88%; box-shadow:0 1px 3px rgba(0,0,0,0.06); line-height:1.35;">
              Registrato. Modello richiesto: 14", 16GB RAM.
            </div>
            <div style="align-self:flex-end; background:var(--accent-color); color:#fff; padding:0.28em 0.6em; border-radius:10px 10px 2px 10px; max-width:82%; line-height:1.35;">
              Puoi anche ordinare un secondo monitor?
            </div>
            <div style="align-self:flex-start; background:#fff; border:1px solid #e2e8f0; padding:0.28em 0.6em; border-radius:10px 10px 10px 2px; max-width:88%; box-shadow:0 1px 3px rgba(0,0,0,0.06); line-height:1.35;">
              Aggiunto alla richiesta.
            </div>
            <div style="align-self:flex-end; background:var(--accent-color); color:#fff; padding:0.28em 0.6em; border-radius:10px 10px 2px 10px; max-width:82%; line-height:1.35;">
              Quando arriva di solito il materiale?
            </div>
            <div style="align-self:flex-start; background:#fff; border:1px solid #e2e8f0; padding:0.28em 0.6em; border-radius:10px 10px 10px 2px; max-width:88%; box-shadow:0 1px 3px rgba(0,0,0,0.06); line-height:1.35;">
              In genere 5-7 giorni lavorativi dall'ordine.
            </div>
          </div>

          <!-- Context window box -->
          <div style="position:relative; border:2px solid #f59e0b; border-radius:8px; padding:0.45em 0.5em 0.45em 0.5em; margin-top:0.3em; background:rgba(245,158,11,0.07); display:flex; flex-direction:column; gap:0.14em;">
            <div style="position:absolute; top:-0.75em; left:50%; transform:translateX(-50%); background:#f59e0b; color:#fff; font-size:0.75em; font-weight:700; padding:0.1em 0.5em; border-radius:6px; white-space:nowrap; letter-spacing:0.03em;">
              ↕ context window
            </div>

            <div style="align-self:flex-end; background:var(--accent-color); color:#fff; padding:0.28em 0.6em; border-radius:10px 10px 2px 10px; max-width:82%; line-height:1.35;">
              E per l'accesso al VPN aziendale?
            </div>
            <div style="align-self:flex-start; background:#fff; border:1px solid #e2e8f0; padding:0.28em 0.6em; border-radius:10px 10px 10px 2px; max-width:88%; box-shadow:0 1px 3px rgba(0,0,0,0.06); line-height:1.35;">
              Serve un ticket separato all'IT Security: te lo apro ora?
            </div>
            <div style="align-self:flex-end; background:var(--accent-color); color:#fff; padding:0.28em 0.6em; border-radius:10px 10px 2px 10px; max-width:82%; line-height:1.35;">
              Sì grazie. Aggiungimi anche il badge per il parcheggio.
            </div>
            <div style="align-self:flex-start; background:#fff; border:1px solid #e2e8f0; padding:0.28em 0.6em; border-radius:10px 10px 10px 2px; max-width:88%; box-shadow:0 1px 3px rgba(0,0,0,0.06); line-height:1.35;">
              Fatto: ticket Security aperto, richiesta badge inoltrata a reception.
            </div>
          </div>
        </div>

        <div style="display:flex; align-items:center; gap:0.4em; padding:0.45em 0.65em; background:#fff; border-top:1px solid #e2e8f0; flex-shrink:0;">
          <div style="flex:1; background:#f1f5f9; border:1px solid #e2e8f0; border-radius:20px; padding:0.32em 0.8em; color:#94a3b8; font-size:0.95em;">
            Scrivi un messaggio…
          </div>
          <div style="width:1.7em; height:1.7em; background:var(--accent-color); border-radius:50%; display:flex; align-items:center; justify-content:center; color:#fff; font-size:0.85em; flex-shrink:0; box-shadow:0 2px 6px rgba(42,104,212,0.4);">➤</div>
        </div>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.8 — Context rot -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Context rot: quando iniziare una nuova conversazione</h2>
    </div>
    <div class="slide-body layout-list">
      <p>Man mano che il contesto cresce — specialmente se pieno di informazioni irrilevanti o contraddittorie — la qualità delle risposte peggiora. Non solo quando il contesto è "pieno": già prima.</p>
      <h3 style="margin-top:0.8em">Regola pratica: apri una nuova conversazione quando</h3>
      <ul>
        <li>Cambi argomento in modo netto rispetto a quanto discusso finora</li>
        <li>Il modello inizia a ignorare istruzioni date in precedenza</li>
        <li>La conversazione ha accumulato molti tentativi e correzioni falliti</li>
        <li>Stai per iniziare un task grande, indipendente dal precedente</li>
      </ul>
      <div class="callout" style="margin-top:0.8em">Una conversazione pulita e mirata batte quasi sempre una conversazione lunga e affollata.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>
```

- [ ] **Step 2: Verify structural balance**

Run:

```bash
grep -c '<section' slides/20260710_intro_AI_hup/index.html
grep -c '</section>' slides/20260710_intro_AI_hup/index.html
grep -c 'class="slide"' slides/20260710_intro_AI_hup/index.html
grep -n '#6366f1\|#4f46e5\|rgba(99,102,241' slides/20260710_intro_AI_hup/index.html
```

Expected: first two commands print the same number (51), the third prints 36, the fourth prints nothing (no output, no leftover indigo hex).

- [ ] **Step 3: Visual check**

Run `open slides/20260710_intro_AI_hup/index.html` (or the project's preview flow) and step through slides 1.1–1.8: confirm the two new `.card` rows (1.2), the two new `.diagram` blocks (1.4, 1.5) render as monospace boxes, the chat mockup (1.7) shows faded messages outside an amber "context window" box, and slide 1.8 renders as a plain bulleted list with a closing callout. Confirm no layout overflow or broken tags.

- [ ] **Step 4: Commit**

```bash
git add slides/20260710_intro_AI_hup/index.html
git commit -m "$(cat <<'EOF'
Add model examples, tokenization, generation process, context window
example, and context rot to Ora 1

EOF
)"
```

---

## Task 2: Slides 1.9–1.14 (frozen-knowledge callout, agent visual upgrade, agents-with-tools, riepilogo)

**Files:**
- Modify: `slides/20260710_intro_AI_hup/index.html` (the block starting at the `<!-- 1.4 — Fine-tuning vs Prompting vs RAG -->` comment through the end of the current "Riepilogo Ora 1" slide, immediately before the Ora 1 section's closing `</section>` and the `<section data-section-title="Ora 2 — Introduzione a Claude">` that follows it)

**Interfaces:**
- Consumes: the file as left by Task 1 (this task's Find target is untouched by Task 1, so it matches the original committed text unchanged).
- Produces: the completed 14-slide Ora 1 section.

- [ ] **Step 1: Replace the Fine-tuning/RAG table through Riepilogo block**

Find this exact block in `slides/20260710_intro_AI_hup/index.html`:

```html
  <!-- 1.4 — Fine-tuning vs Prompting vs RAG -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Fine-tuning, Prompting, RAG: quando usare cosa</h2>
    </div>
    <div class="slide-body layout-table">
      <table class="table-keyed table-compact">
        <tr>
          <th>Approccio</th>
          <th>Cosa fa</th>
          <th>Quando ha senso</th>
        </tr>
        <tr>
          <td><strong>Prompting</strong></td>
          <td>Istruisci il modello con testo, nella conversazione</td>
          <td>Quasi sempre il primo passo: veloce, economico, nessun dato da preparare</td>
        </tr>
        <tr>
          <td><strong>RAG</strong></td>
          <td>Recupera documenti rilevanti e li inserisce nel contesto prima di rispondere</td>
          <td>Serve conoscenza aggiornata o specifica (documenti interni, policy, cataloghi)</td>
        </tr>
        <tr>
          <td><strong>Fine-tuning</strong></td>
          <td>Riaddestra il modello su esempi specifici, cambiandone i pesi</td>
          <td>Serve uno stile/formato molto specifico e ripetuto su grandi volumi — raro per le PMI</td>
        </tr>
      </table>
      <div class="callout" style="margin-top:0.8em">In pratica: si parte sempre dal prompting, si aggiunge RAG quando serve conoscenza esterna, si arriva al fine-tuning solo per casi molto specifici e ad alto volume.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.5 — RAG -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>RAG — Retrieval Augmented Generation</h2>
    </div>
    <div class="slide-body layout-image-text">
      <div class="slide-image">
        <img src="public/images/rag_architecture.png" alt="Architettura RAG">
      </div>
      <div>
        <h3>Il problema che risolve</h3>
        <p style="font-size:0.85em; margin-bottom:0.6em;">Un LLM non conosce i tuoi documenti interni, le tue policy, i tuoi dati aggiornati. RAG glieli fornisce al momento giusto.</p>
        <h3>Come funziona, in 3 passi</h3>
        <ul>
          <li>I documenti vengono trasformati in vettori numerici (embedding) e indicizzati</li>
          <li>Alla domanda dell'utente, si recuperano i passaggi più simili semanticamente</li>
          <li>Questi passaggi vengono inseriti nel prompt: il modello risponde basandosi su di essi</li>
        </ul>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.6 — Agenti AI -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Agenti AI: LLM, Assistente, Agente</h2>
    </div>
    <div class="slide-body layout-three-col">
      <div class="card">
        <h4>LLM</h4>
        <p>Risponde a una domanda con una singola generazione di testo. Nessuna azione sul mondo esterno.</p>
      </div>
      <div class="card">
        <h4>Assistente</h4>
        <p>Conversazione con memoria del contesto. Può richiamare uno strumento se glielo chiedi esplicitamente.</p>
      </div>
      <div class="card">
        <h4>Agente</h4>
        <p>Pianifica autonomamente una sequenza di passi: <strong>Reason → Act → Observe</strong>, ripetuta finché il task è completo.</p>
      </div>
      <p class="text-muted text-small" style="margin-top:0.8em">Gli agenti sono potenti ma meno prevedibili: vanno supervisionati, specialmente su azioni con conseguenze reali (invio email, modifiche a dati).</p>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.7 — Tools, Function Calling, MCP -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Tools, Function Calling e MCP</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Dall'LLM al mondo reale</h3>
        <ul>
          <li>Un modello, da solo, può solo generare testo — non può cercare sul web, leggere un file o interrogare un sistema</li>
          <li><strong>Function calling</strong>: definisci strumenti (funzioni) che il modello può decidere di invocare, con parametri strutturati</li>
          <li>Il modello non esegue lo strumento: chiede all'applicazione di eseguirlo e gli passa il risultato</li>
        </ul>
      </div>
      <div>
        <h3>MCP — Model Context Protocol</h3>
        <ul>
          <li>Uno standard aperto per collegare un modello a strumenti e sorgenti dati esterne</li>
          <li>Invece di integrare ogni tool a mano per ogni applicazione, un server MCP espone gli stessi strumenti a qualsiasi client compatibile</li>
          <li>Ne riparliamo con esempi pratici nell'Ora 3</li>
        </ul>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.8 — Riepilogo -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Riepilogo Ora 1</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li>Un LLM predice testo token per token, non "ragiona" come un umano</li>
        <li>La context window è la memoria di lavoro del modello: va gestita con cura</li>
        <li>Prompting → RAG → fine-tuning, in ordine di complessità crescente</li>
        <li>Un agente pianifica ed esegue passi in autonomia; tool calling e MCP lo collegano al mondo reale</li>
      </ul>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>
```

Replace with:

```html
  <!-- 1.9 — Fine-tuning vs Prompting vs RAG -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Fine-tuning, Prompting, RAG: quando usare cosa</h2>
    </div>
    <div class="slide-body layout-table">
      <table class="table-keyed table-compact">
        <tr>
          <th>Approccio</th>
          <th>Cosa fa</th>
          <th>Quando ha senso</th>
        </tr>
        <tr>
          <td><strong>Prompting</strong></td>
          <td>Istruisci il modello con testo, nella conversazione</td>
          <td>Quasi sempre il primo passo: veloce, economico, nessun dato da preparare</td>
        </tr>
        <tr>
          <td><strong>RAG</strong></td>
          <td>Recupera documenti rilevanti e li inserisce nel contesto prima di rispondere</td>
          <td>Serve conoscenza aggiornata o specifica (documenti interni, policy, cataloghi)</td>
        </tr>
        <tr>
          <td><strong>Fine-tuning</strong></td>
          <td>Riaddestra il modello su esempi specifici, cambiandone i pesi</td>
          <td>Serve uno stile/formato molto specifico e ripetuto su grandi volumi — raro per le PMI</td>
        </tr>
      </table>
      <div class="callout" style="margin-top:0.8em">In pratica: si parte sempre dal prompting, si aggiunge RAG quando serve conoscenza esterna, si arriva al fine-tuning solo per casi molto specifici e ad alto volume.</div>
      <div class="callout" style="margin-top:0.8em">Il modello non impara nulla di nuovo in prompting e RAG: i suoi pesi restano identici, cambia solo cosa gli mettiamo nel contesto. Il fine-tuning è l'eccezione — lì i pesi cambiano davvero — ma resta un caso raro.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.10 — RAG -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>RAG — Retrieval Augmented Generation</h2>
    </div>
    <div class="slide-body layout-image-text">
      <div class="slide-image">
        <img src="public/images/rag_architecture.png" alt="Architettura RAG">
      </div>
      <div>
        <h3>Il problema che risolve</h3>
        <p style="font-size:0.85em; margin-bottom:0.6em;">Un LLM non conosce i tuoi documenti interni, le tue policy, i tuoi dati aggiornati. RAG glieli fornisce al momento giusto.</p>
        <h3>Come funziona, in 3 passi</h3>
        <ul>
          <li>I documenti vengono trasformati in vettori numerici (embedding) e indicizzati</li>
          <li>Alla domanda dell'utente, si recuperano i passaggi più simili semanticamente</li>
          <li>Questi passaggi vengono inseriti nel prompt: il modello risponde basandosi su di essi</li>
        </ul>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.11 — Agenti AI -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Agenti AI: LLM, Assistente, Agente</h2>
    </div>
    <div class="slide-body layout-three-col">
      <div class="card" style="text-align:center;">
        <div style="width:2.6em; height:2.6em; margin:0 auto 0.5em; border-radius:50%; background:#e2e8f0; display:flex; align-items:center; justify-content:center; font-size:1.4em;">🧠</div>
        <h4>LLM</h4>
        <p>Risponde a una domanda con una singola generazione di testo. Nessuna azione sul mondo esterno.</p>
      </div>
      <div class="card" style="text-align:center;">
        <div style="width:2.6em; height:2.6em; margin:0 auto 0.5em; border-radius:50%; background:#dbeafe; display:flex; align-items:center; justify-content:center; font-size:1.4em;">💬</div>
        <h4>Assistente</h4>
        <p>Conversazione con memoria del contesto. Può richiamare uno strumento se glielo chiedi esplicitamente.</p>
      </div>
      <div class="card" style="text-align:center;">
        <div style="width:2.6em; height:2.6em; margin:0 auto 0.5em; border-radius:50%; background:rgba(42,104,212,0.15); display:flex; align-items:center; justify-content:center; font-size:1.4em;">🤖</div>
        <h4>Agente</h4>
        <p>Pianifica autonomamente una sequenza di passi: <strong>Reason → Act → Observe</strong>, ripetuta finché il task è completo.</p>
      </div>
      <p class="text-muted text-small" style="margin-top:0.8em">Gli agenti sono potenti ma meno prevedibili: vanno supervisionati, specialmente su azioni con conseguenze reali (invio email, modifiche a dati).</p>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.12 — Agenti con accesso a strumenti reali -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Agenti con accesso a strumenti reali</h2>
    </div>
    <div class="slide-body layout-diagram">
      <p>Un agente può avere accesso diretto a strumenti come lettura file, esecuzione di script o comandi da terminale — non solo API esterne.</p>
      <div class="diagram">
Goal: "Analizza vendite_2026.csv e riassumi i trend per reparto"

  [Reason] → Devo leggere il file e capire la struttura dati
  [Act]     → leggi_file("vendite_2026.csv")
  [Observe] → {colonne: [data, reparto, importo], righe: 4200}

  [Reason] → Serve uno script per aggregare per reparto
  [Act]     → esegui_python("pandas.groupby('reparto').sum()")
  [Observe] → {Vendite: 120k, Marketing: 45k, IT: 30k, ...}

  [Reason] → Ho i dati aggregati, task completato
  [Output]  → "Riepilogo pronto: Vendite +12%, Marketing stabile..."
      </div>
      <div class="callout" style="margin-top:0.8em">Questi sono gli stessi strumenti che useremo con Claude nell'Ora 2: lettura file, esecuzione di codice, comandi da terminale.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.13 — Tools, Function Calling, MCP -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Tools, Function Calling e MCP</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Dall'LLM al mondo reale</h3>
        <ul>
          <li>Un modello, da solo, può solo generare testo — non può cercare sul web, leggere un file o interrogare un sistema</li>
          <li><strong>Function calling</strong>: definisci strumenti (funzioni) che il modello può decidere di invocare, con parametri strutturati</li>
          <li>Il modello non esegue lo strumento: chiede all'applicazione di eseguirlo e gli passa il risultato</li>
        </ul>
      </div>
      <div>
        <h3>MCP — Model Context Protocol</h3>
        <ul>
          <li>Uno standard aperto per collegare un modello a strumenti e sorgenti dati esterne</li>
          <li>Invece di integrare ogni tool a mano per ogni applicazione, un server MCP espone gli stessi strumenti a qualsiasi client compatibile</li>
          <li>Ne riparliamo con esempi pratici nell'Ora 3</li>
        </ul>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 1.14 — Riepilogo -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 1 · Concetti AI</span>
      <h2>Riepilogo Ora 1</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li>Un LLM tokenizza il testo e predice un token alla volta, non "ragiona" come un umano</li>
        <li>La context window è la memoria di lavoro del modello: va gestita con cura, e "context rot" ci dice quando ripartire da zero</li>
        <li>Prompting → RAG → fine-tuning, in ordine di complessità crescente — ma solo il fine-tuning cambia davvero il modello</li>
        <li>Un agente pianifica ed esegue passi in autonomia, con accesso a strumenti reali (file, codice, terminale); tool calling e MCP lo collegano al mondo esterno</li>
      </ul>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>
```

- [ ] **Step 2: Verify structural balance and marker counts**

Run:

```bash
grep -c '<section' slides/20260710_intro_AI_hup/index.html
grep -c '</section>' slides/20260710_intro_AI_hup/index.html
grep -c 'class="slide"' slides/20260710_intro_AI_hup/index.html
grep -n '#6366f1\|#4f46e5\|rgba(99,102,241' slides/20260710_intro_AI_hup/index.html
grep -c 'Ora 1 · Concetti AI' slides/20260710_intro_AI_hup/index.html
```

Expected: first two commands print the same number (52), the third prints 37, the fourth prints nothing, the fifth prints 14 (one per Ora 1 slide).

- [ ] **Step 3: Visual check**

Run `open slides/20260710_intro_AI_hup/index.html` and step through slides 1.9–1.14: confirm the two stacked callouts on the fine-tuning/RAG table slide, the three agent cards now show colored icon circles, the new ReAct-style diagram (1.12) renders as a monospace box, and Ora 2 still starts correctly right after the updated Riepilogo slide.

- [ ] **Step 4: Commit**

```bash
git add slides/20260710_intro_AI_hup/index.html
git commit -m "$(cat <<'EOF'
Reinforce frozen-knowledge messaging, upgrade agent card visuals, and
add agents-with-real-tools slide to Ora 1

EOF
)"
```
