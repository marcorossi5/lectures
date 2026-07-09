# Ricostruzione Ora 2 — Introduzione a Claude (Hup deck) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the "Ora 2 — Introduzione a Claude" section of `slides/20260710_intro_AI_hup/index.html` from 9 to 28 slides, covering all 18 claude101.com articles across its 4 levels (Beginner/Intermediate/Advanced/Expert) with concept bullets per page and one live hands-on exercise per level.

**Architecture:** Content-only edit to a single contiguous region of one self-contained HTML file (reveal.js deck, no build step). New slides reuse existing CSS component classes already defined in the file (`.card`, `.callout`, `layout-list`, `layout-two-col`) — no new CSS, no new images. The section is rebuilt across 4 sequential tasks (one per claude101.com level) using HTML-comment placeholder markers, the same pattern used when the deck was first scaffolded. "Tests" are grep-based structural checks (tag balance, marker counts, no leftover indigo hex) plus manual visual review in a browser.

**Tech Stack:** reveal.js (already bundled inline in the target file), plain HTML/CSS using the file's existing custom properties. No npm/build tooling.

## Global Constraints

- Target file: `slides/20260710_intro_AI_hup/index.html`. Only the `data-section-title="Ora 2 — Introduzione a Claude"` section (starts line 1911) may be touched. Do not modify Ora 1, Ora 3, Ora 4, Chiusura, or Glossario.
- All copy is in Italian, matching the rest of the deck.
- Pages from claude101.com that are personal-brand-focused in the source (voice capture, "Claude replaced me", "Stop sounding like AI") are reframed for corporate/team use, not personal blogging — per design spec decision.
- No new CSS rules, no new image assets. Reuse existing classes only: `.card`, `.callout`, `layout-list`, `layout-two-col`.
- Every new slide keeps the existing header pattern `<span class="slide-section-label">Ora 2 · Claude</span>` (exercise slides use `Ora 2 · Claude · Esercizio`) and the existing footer pattern (`<img class="footer-logo" alt="Hup.">` + `<span class="footer-page"></span>`).
- Exactly 4 live hands-on exercises total, one per level: Claude For Dummies (L1), Claude Cowork (L2), Stop sounding like AI (L3), Stop using your own Claude at work (L4). No exercises on any other page — per design spec, the remaining pages get concept slides only.
- Git: commit locally only after each task. **Do not push** (standing user instruction for this branch).
- Full content source (bullet content, exercise steps, level structure) is `docs/superpowers/specs/2026-07-09-hup-ora2-claude-intro-design.md` — this plan's HTML blocks are already the final copy derived from it; do not re-fetch claude101.com.

---

## Task 1: Overview slide + Livello 1 (Beginner) — 7 slides

**Files:**
- Modify: `slides/20260710_intro_AI_hup/index.html:1913-2157` (the entire current Ora 2 inner content — divider through the current Riepilogo slide)

**Interfaces:**
- Consumes: the file as it exists on the current branch tip, specifically the exact text block from `<section class="slide-section">` (Ora 2 divider) through the closing `</section>` of the current "Riepilogo Ora 2" slide.
- Produces: the updated divider + overview slide (2.1) + Livello 1 roadmap/concepts/exercise (2.2-2.6), followed by an HTML comment marker `<!-- ORA2_LEVEL2_PLACEHOLDER: Task 2 inserts Livello 2 slides here -->` that Task 2 replaces. Task 2 does not depend on any specific text this task produces beyond that marker string.

- [ ] **Step 1: Replace the entire current Ora 2 inner content**

Find this exact block in `slides/20260710_intro_AI_hup/index.html` (currently lines 1913-2157):

```html
  <section class="slide-section">
    <div class="section-eyebrow">Ora 2</div>
    <h2>Introduzione a Claude</h2>
    <p class="section-desc">I livelli e le pagine della guida Claude 101, da Claude for Dummies a Claude Code</p>
  </section>

  <!-- 2.1 — Overview dei 4 livelli -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude 101: una guida a 4 livelli</h2>
    </div>
    <div class="slide-body layout-list">
      <p class="text-muted text-small">claude101.com raccoglie articoli pratici organizzati per livello di esperienza, dal primo utilizzo fino all'uso avanzato al lavoro.</p>
      <ul>
        <li><strong>Livello 1 — Beginner</strong>: primi passi, letture da 5 minuti</li>
        <li><strong>Livello 2 — Intermediate</strong>: Cowork, team, progetti, skill — letture da 7-18 minuti</li>
        <li><strong>Livello 3 — Advanced</strong>: personalizzazione, tecniche oltre il prompting classico — letture da 10-20 minuti</li>
        <li><strong>Livello 4 — Expert</strong>: connettori, Claude Code, adozione aziendale — letture da 8-14 minuti</li>
      </ul>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.2 — Livello 1 -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Livello 1 — Beginner</h2>
    </div>
    <div class="slide-body layout-three-col">
      <div class="card">
        <h4>Claude For Dummies</h4>
        <p>Introduzione per chi usa Claude per la prima volta.</p>
      </div>
      <div class="card">
        <h4>Be good at Claude is (stupidly) simple</h4>
        <p>Una guida di sopravvivenza essenziale all'uso quotidiano dell'AI.</p>
      </div>
      <div class="card">
        <h4>Claude Certified</h4>
        <p>Come ottenere la certificazione gratuita Claude.</p>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.3 — Livello 2 -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Livello 2 — Intermediate</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <ul>
          <li><strong>Claude Cowork</strong> — setup della collaborazione locale con l'AI</li>
          <li><strong>Claude for teams</strong> — onboarding e configurazione per i team</li>
          <li><strong>Claude Design</strong> — orientarsi nell'interfaccia aggiornata</li>
        </ul>
      </div>
      <div>
        <ul>
          <li><strong>Claude Cowork + Projects</strong> — creare spazi di lavoro dedicati dentro Cowork</li>
          <li><strong>Claude for slides</strong> — metodo per creare presentazioni</li>
          <li><strong>Claude Skills</strong> — costruire la tua prima skill personalizzata</li>
        </ul>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.4 — Livello 3 -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Livello 3 — Advanced</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <ul>
          <li><strong>Claude to sound like you</strong> — personalizzare lo stile di comunicazione</li>
          <li><strong>Stop hitting Claude limits</strong> — gestire i limiti di utilizzo</li>
          <li><strong>Stop Prompting</strong> — tecniche oltre il prompt engineering tradizionale</li>
        </ul>
      </div>
      <div>
        <ul>
          <li><strong>Claude replaced me</strong> — creare skill che insegnano un processo passo-passo</li>
          <li><strong>Stop sounding like AI</strong> — eliminare i pattern linguistici artificiali</li>
          <li><strong>Excel with Claude cowork</strong> — creare fogli di calcolo con l'AI</li>
        </ul>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.5 — Livello 4 -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Livello 4 — Expert</h2>
    </div>
    <div class="slide-body layout-three-col">
      <div class="card">
        <h4>Claude Connectors</h4>
        <p>Integrare Claude con applicazioni esterne.</p>
      </div>
      <div class="card">
        <h4>Claude Code</h4>
        <p>"Per chi non scriverà mai una riga di codice" — usare Claude per compiti da sviluppatore senza saper programmare.</p>
      </div>
      <div class="card">
        <h4>Stop using your own Claude at work</h4>
        <p>Strategia per un'adozione professionale, non personale, dell'AI in azienda.</p>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.6 — Zoom: Claude Cowork -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Zoom — Claude Cowork</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Cos'è</h3>
        <ul>
          <li>Collaborazione locale con Claude nell'app desktop: accede ai file di una cartella sul tuo computer</li>
          <li>Mantiene contesto persistente su chi sei, cosa valuti, come lavori — non riparte da zero ogni volta</li>
        </ul>
      </div>
      <div>
        <h3>Struttura consigliata</h3>
        <ul>
          <li><strong>ABOUT ME</strong>: chi sei, il tuo stile, gli obiettivi aziendali (sotto i 6.000 token totali)</li>
          <li><strong>OUTPUTS</strong>: risultati generati per ogni progetto</li>
          <li><strong>TEMPLATES</strong>: strutture riutilizzabili dai tuoi lavori migliori</li>
        </ul>
      </div>
      <div class="callout">Setup in circa 20 minuti. Usa Opus con Extended Thinking per il lavoro complesso, modelli più leggeri per grammatica e brainstorming.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.7 — Zoom: Claude Projects -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Zoom — Claude Cowork Projects</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Cosa risolvono</h3>
        <ul>
          <li>Ogni sessione Cowork partiva da zero, richiedendo di re-spiegare contesto e ricaricare file</li>
          <li>Un Project è uno spazio persistente: cartella dedicata, istruzioni personalizzate, memoria isolata a quel progetto</li>
        </ul>
      </div>
      <div>
        <h3>Setup in 5 passi</h3>
        <ul>
          <li>Cowork → Projects → "+"</li>
          <li>Scegli: da zero, da un Project esistente, o da una cartella</li>
          <li>Aggiungi istruzioni personalizzate (5-8 righe) e file di riferimento</li>
          <li>Prompt iniziale: "Leggi tutto in questa cartella e riassumi cosa sai"</li>
          <li>Opzionale: automatizza task ricorrenti con task pianificati</li>
        </ul>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.8 — Zoom: Claude Skills -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Zoom — Claude Skills</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Cos'è una Skill</h3>
        <ul>
          <li>Istruzioni persistenti e riutilizzabili, richiamabili automaticamente (es. via <code>/comando</code>) quando Claude riconosce il task giusto</li>
          <li>Non serve invocarla a mano: si attiva da sola in base alla descrizione</li>
          <li>Si costruisce con lo Skill Creator integrato (intervista guidata) e produce un file <strong>SKILL.md</strong></li>
        </ul>
      </div>
      <div>
        <h3>Cosa rende una skill efficace</h3>
        <ul>
          <li>La descrizione "quando usarla" è ciò che ne determina l'attivazione — se è vaga, la skill non parte</li>
          <li>Il "quando NON usarla" conta più del "quando usarla": evita che la skill si attivi a sproposito</li>
          <li>Carica le istruzioni complete solo quando serve: puoi installarne molte senza appesantire il contesto</li>
        </ul>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.9 — Riepilogo -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Riepilogo Ora 2</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li>claude101.com copre 4 livelli, da primo utilizzo ad adozione aziendale avanzata</li>
        <li>Cowork porta Claude a lavorare direttamente sui tuoi file locali, con contesto persistente</li>
        <li>I Project isolano memoria e istruzioni per ogni area di lavoro</li>
        <li>Le Skill automatizzano processi ricorrenti: le vediamo applicate in azienda nell'Ora 3</li>
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
  <section class="slide-section">
    <div class="section-eyebrow">Ora 2</div>
    <h2>Introduzione a Claude</h2>
    <p class="section-desc">Le 18 pagine della guida Claude 101, livello per livello, con 4 esercizi pratici dal vivo</p>
  </section>

  <!-- 2.1 — Overview dei 4 livelli -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude 101: una guida a 4 livelli</h2>
    </div>
    <div class="slide-body layout-list">
      <p class="text-muted text-small">claude101.com raccoglie 18 articoli pratici organizzati per livello di esperienza, dal primo utilizzo fino all'uso avanzato al lavoro. Li ripercorriamo tutti, livello per livello, con 4 esercizi pratici dal vivo.</p>
      <ul>
        <li><strong>Livello 1 — Beginner</strong>: 3 articoli, primi passi, letture da 4-5 minuti</li>
        <li><strong>Livello 2 — Intermediate</strong>: 6 articoli, Cowork, team, progetti, skill — letture da 6-18 minuti</li>
        <li><strong>Livello 3 — Advanced</strong>: 6 articoli, personalizzazione, tecniche oltre il prompting classico — letture da 4-20 minuti</li>
        <li><strong>Livello 4 — Expert</strong>: 3 articoli, connettori, Claude Code, adozione aziendale — letture da 8-14 minuti</li>
      </ul>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.2 — Livello 1: cosa vedremo -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Livello 1 — Beginner: cosa vedremo</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li><strong>Claude For Dummies</strong> (5 min) — primi passi con Claude</li>
        <li><strong>Be good at Claude is (stupidly) simple</strong> (5 min) — guida di sopravvivenza all'uso quotidiano</li>
        <li><strong>Claude Certified</strong> (4 min) — la certificazione gratuita Claude</li>
      </ul>
      <div class="callout">Chiudiamo il livello con un esercizio pratico: riscrivere un tuo testo nel tuo stile.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.3 — Claude For Dummies -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude For Dummies</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>I concetti base</h3>
        <ul>
          <li>Claude è l'assistente AI di Anthropic: completamento automatico su scala sovrumana, tendenza ad assecondarti ("sycophancy"), token che limitano la lunghezza di una conversazione</li>
          <li>Tre modalità: Chat (conversazione), Desktop (accesso ai file locali), Cowork (esecuzione autonoma di task lunghi)</li>
        </ul>
      </div>
      <div>
        <h3>Piani e buone pratiche</h3>
        <ul>
          <li>Piani: Free (limitato), Pro 20$/mese, Max 100-200$/mese per uso intensivo</li>
          <li>Cinque regole per prompt efficaci: sii specifico, fornisci esempi, dì cosa fare (non cosa evitare), parti breve e itera, apri una nuova chat se il modello si confonde</li>
        </ul>
      </div>
      <div class="callout">I tre concetti da conoscere per iniziare — Token, Cowork, Claude Code — li ritroveremo per tutta la sessione.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.4 — Esercizio pratico: Riscrivi nel tuo stile -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude · Esercizio</span>
      <h2>Esercizio pratico — Riscrivi nel tuo stile</h2>
    </div>
    <div class="slide-body layout-list">
      <p class="text-muted text-small">~8 minuti · serve solo un account Claude gratuito</p>
      <ol>
        <li>Accedi a claude.ai con un account gratuito</li>
        <li>Incolla un tuo testo reale (email, comunicazione interna, breve report)</li>
        <li>Chiedi a Claude di riscriverlo mantenendo il tuo stile ma migliorando chiarezza e tono</li>
        <li>Confronta il risultato con l'originale: cosa ha cambiato? Cosa avresti fatto diversamente?</li>
      </ol>
      <div class="callout">Obiettivo: capire come Claude interpreta "il tuo stile" da un solo esempio, prima ancora di configurare nulla.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.5 — Be good at Claude is (stupidly) simple -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Be good at Claude is (stupidly) simple</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li>Usa Opus (a pagamento) invece di Sonnet gratuito quando possibile; attiva "Thinking" su High per task complessi</li>
        <li>Tecnica AskUserQuestion: istruisci Claude a farti domande di chiarimento prima di eseguire, invece di scrivere il prompt perfetto</li>
        <li>Gli strumenti di dettatura vocale permettono di parlare a Claude fino a 4 volte più veloce che scrivere</li>
        <li>Cowork crea file reali (PDF, fogli di calcolo) salvati su disco, senza copia-incolla</li>
        <li>I Connector integrano email, calendario, trascrizioni di riunioni per dare contesto</li>
        <li>Il comando <code>/skill-creator</code> costruisce skill personalizzate passo passo</li>
      </ul>
      <div class="callout">Non serve scrivere prompt perfetti — basta far fare a Claude le domande giuste.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.6 — Claude Certified -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude Certified</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Perché conta</h3>
        <ul>
          <li>Esistono solo tre certificazioni gratuite legittime, erogate da Anthropic; altre "certificazioni" a pagamento online non sono ufficiali</li>
          <li>Nel 2024 il 78% delle organizzazioni ha usato l'AI (era il 55% nel 2023)</li>
          <li>Chi ha competenze AI ottiene in media un premio salariale del 56% (era il 25% l'anno precedente)</li>
        </ul>
      </div>
      <div>
        <h3>Il percorso</h3>
        <ul>
          <li>"Claude 101" (1h): Chat vs Cowork vs Code, Project, Skill, integrazioni</li>
          <li>"AI Fluency" (3h): framework delle 4D — Delegation, Description, Discernment, Diligence</li>
          <li>"Introduction to Claude Cowork" (2h): Project, Plugin, Skill, pianificazione</li>
        </ul>
      </div>
      <div class="callout">Percorso gratuito di ~6 ore, aggiungibile a LinkedIn come certificazione Anthropic — attività consigliata dopo la sessione, non fattibile in aula.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- ORA2_LEVEL2_PLACEHOLDER: Task 2 inserts Livello 2 slides here -->
```

- [ ] **Step 2: Verify structural balance and marker counts**

Run:

```bash
grep -c '<section' slides/20260710_intro_AI_hup/index.html
grep -c '</section>' slides/20260710_intro_AI_hup/index.html
grep -c 'class="slide"' slides/20260710_intro_AI_hup/index.html
grep -c 'ORA2_LEVEL2_PLACEHOLDER' slides/20260710_intro_AI_hup/index.html
grep -n '#6366f1\|#4f46e5\|rgba(99,102,241' slides/20260710_intro_AI_hup/index.html
```

Expected: first two commands print the same number (50), the third prints 35, the
fourth prints 1, the fifth prints nothing (no leftover indigo hex).

- [ ] **Step 3: Visual check**

```bash
open slides/20260710_intro_AI_hup/index.html
```

Navigate to Ora 2: confirm the divider text mentions "18 pagine" / "4 esercizi", the
overview slide (2.1) lists all 4 levels with article counts, and the 5 new Livello 1
slides (roadmap, Claude For Dummies, exercise, Be good at Claude, Claude Certified)
render without overflow. Confirm no broken layout past the last real slide (the
placeholder comment is invisible in the rendered deck).

- [ ] **Step 4: Commit**

```bash
git add slides/20260710_intro_AI_hup/index.html
git commit -m "$(cat <<'EOF'
Rebuild Ora 2 overview and Livello 1 with per-page concepts

Replace the teaser-card overview with a full walkthrough of all 18
claude101.com articles, starting with Livello 1 (Beginner) and its
first live hands-on exercise.
EOF
)"
```

---

## Task 2: Livello 2 (Intermediate) — 8 slides

**Files:**
- Modify: `slides/20260710_intro_AI_hup/index.html` (replace the `<!-- ORA2_LEVEL2_PLACEHOLDER -->` marker left by Task 1)

**Interfaces:**
- Consumes: the file as left by Task 1, specifically the exact marker line
  `  <!-- ORA2_LEVEL2_PLACEHOLDER: Task 2 inserts Livello 2 slides here -->`.
- Produces: Livello 2 roadmap/concepts/exercise (2.7-2.14), followed by a new marker
  `<!-- ORA2_LEVEL3_PLACEHOLDER: Task 3 inserts Livello 3 slides here -->` that Task 3
  replaces.

- [ ] **Step 1: Replace the Level 2 placeholder**

Find this exact line in `slides/20260710_intro_AI_hup/index.html`:

```html
  <!-- ORA2_LEVEL2_PLACEHOLDER: Task 2 inserts Livello 2 slides here -->
```

Replace with:

```html
  <!-- 2.7 — Livello 2: cosa vedremo -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Livello 2 — Intermediate: cosa vedremo</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li><strong>Claude Cowork</strong> (18 min) — collaborazione locale con l'AI</li>
        <li><strong>Claude for teams</strong> (11 min) — onboarding e configurazione per i team</li>
        <li><strong>Claude Design</strong> (9 min) — siti, slide e video con l'AI</li>
        <li><strong>Claude Cowork + Projects</strong> (10 min) — spazi di lavoro persistenti</li>
        <li><strong>Claude for slides</strong> (7 min) — metodo per creare presentazioni</li>
        <li><strong>Claude Skills</strong> (6 min) — automatizzare workflow ricorrenti</li>
      </ul>
      <div class="callout">Chiudiamo il livello con un esercizio pratico: configurare il tuo primo Cowork.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.8 — Claude Cowork -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude Cowork</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Architettura a cartelle</h3>
        <ul>
          <li><strong>ABOUT ME</strong>: chi sei, il tuo stile, gli obiettivi aziendali — letto prima di ogni sessione</li>
          <li><strong>OUTPUTS</strong>: risultati generati per ogni progetto</li>
          <li><strong>TEMPLATES</strong>: strutture riutilizzabili dai tuoi lavori migliori</li>
        </ul>
      </div>
      <div>
        <h3>Economia dei token</h3>
        <ul>
          <li>Il messaggio 30 costa ~31 volte il messaggio 1 — riparti da una nuova chat dopo ~20 messaggi</li>
          <li>Sonnet/Haiku per task semplici, Opus + Extended Thinking per lavoro complesso</li>
        </ul>
      </div>
      <div class="callout">Mantieni ABOUT ME sotto i 6.000 token totali — più contesto non è sempre meglio (lo avevamo già visto in Ora 1).</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.9 — Esercizio pratico: Configura il tuo Cowork -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude · Esercizio</span>
      <h2>Esercizio pratico — Configura il tuo Cowork</h2>
    </div>
    <div class="slide-body layout-list">
      <p class="text-muted text-small">~10 minuti · serve l'app desktop di Claude</p>
      <ol>
        <li>Apri l'app desktop di Claude e crea una cartella "Claude Cowork" con tre sottocartelle: ABOUT ME, OUTPUTS, TEMPLATES</li>
        <li>Scrivi un <code>about-me.md</code> essenziale: 5-6 righe su ruolo, stile di lavoro, priorità</li>
        <li>Imposta le Istruzioni Globali (Impostazioni → Cowork) perché legga sempre quella cartella</li>
        <li>Fai una prima richiesta reale: "Leggi la cartella e riassumi cosa sai di me"</li>
      </ol>
      <div class="callout">Bastano poche righe ben scritte — la qualità del file conta più della lunghezza.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.10 — Claude for teams -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude for teams</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Setup</h3>
        <ul>
          <li>Piano Team: minimo 5 posti (fino a 150), livello Premium consigliato per uso quotidiano</li>
          <li>Architettura a Project: 3-5 Project per tipo di deliverable ricorrente, ognuno con istruzioni e documenti mirati</li>
        </ul>
      </div>
      <div>
        <h3>Adozione</h3>
        <ul>
          <li>Converti prima un collega oberato di lavoro, poi usa il suo entusiasmo per il rollout</li>
          <li>Prompt template a una frase, un solo campo di input, pronti da copiare per i colleghi</li>
          <li>Claude non si addestra sui dati del team, a nessun livello di piano</li>
        </ul>
      </div>
      <div class="callout">Percorso di adozione in 5 giorni: setup Project → template pronti → demo prima/dopo → conversione di un singolo utente → rollout team. Non eseguibile in aula, ma riutilizzabile come piano concreto.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.11 — Claude Design -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude Design</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Cos'è</h3>
        <ul>
          <li>Prodotto separato su claude.ai/design, richiede piano Pro/Max o abilitazione admin per Team/Enterprise</li>
          <li>Tre formati di output: siti ad alta fedeltà, presentazioni (con note del relatore), video animati</li>
        </ul>
      </div>
      <div>
        <h3>Attenzioni</h3>
        <ul>
          <li>Il consumo di token è molto rapido — richiede monitoraggio attento</li>
          <li>Un file DESIGN.md (linee guida di brand estratte) permette a Claude di applicare uno stile coerente senza doverlo rispecificare ogni volta</li>
          <li>Workflow avanzato: post/brief → ricerca → video animato → deck di slide, spesso con risultati migliori della generazione diretta del deck</li>
        </ul>
      </div>
      <div class="callout">La scelta finale tra le varianti generate resta una decisione umana, non automatizzabile.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.12 — Claude Cowork + Projects -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude Cowork + Projects</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Cosa risolve</h3>
        <ul>
          <li>Combina memoria persistente e ambito ristretto con esecuzione agentica, integrato nell'app desktop</li>
          <li>Tre modalità di creazione: da zero, da un Project esistente, o da una cartella locale</li>
        </ul>
      </div>
      <div>
        <h3>Limiti e usi</h3>
        <ul>
          <li>La memoria isolata per Project evita che il contesto di un progetto contamini un altro</li>
          <li>I task pianificati automatizzano attività ricorrenti quando l'app desktop è attiva</li>
          <li>Limite: i Project Cowork sono locali alla macchina — non ancora condivisibili in team</li>
        </ul>
      </div>
      <div class="callout">Quattro casi d'uso tipici: newsletter, deliverable per clienti, proposte commerciali, report operativi ricorrenti.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.13 — Claude for slides -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude for slides</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Tre metodi</h3>
        <ul>
          <li>Claude da solo — rapido ma design piatto</li>
          <li>Uno strumento di design esterno — output rifinito, immagini AI, analytics</li>
          <li>I due combinati — consigliato per deck importanti</li>
        </ul>
      </div>
      <div>
        <h3>Pipeline consigliata</h3>
        <ul>
          <li>Standardizzazione del brand aziendale tramite un tema condiviso + un file brand-deck-rules.md</li>
          <li>Pipeline "ricerca → brief": Claude fa la ricerca web, produce un brief strutturato, poi un outline slide-per-slide</li>
        </ul>
      </div>
      <div class="callout">La generazione diretta di slide senza ricerca/outline preliminare produce quasi sempre risultati generici — vale anche per le slide di questa stessa sessione.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.14 — Claude Skills -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude Skills</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Cos'è una Skill</h3>
        <ul>
          <li>Istruzioni persistenti e riutilizzabili, richiamabili automaticamente (es. via <code>/comando</code>) quando Claude riconosce il task giusto</li>
          <li>Non serve invocarla a mano: si attiva da sola in base alla descrizione</li>
          <li>Si costruisce con lo Skill Creator integrato (intervista guidata) e produce un file <strong>SKILL.md</strong></li>
        </ul>
      </div>
      <div>
        <h3>Cosa rende una skill efficace</h3>
        <ul>
          <li>La descrizione "quando usarla" è ciò che ne determina l'attivazione — se è vaga, la skill non parte</li>
          <li>Il "quando NON usarla" conta più del "quando usarla": evita che la skill si attivi a sproposito</li>
          <li>Un task che richiedeva 12.000 token e 15 scambi è sceso a 6.000 token e 2 scambi grazie a una skill</li>
        </ul>
      </div>
      <div class="callout">Anche con una skill ben scritta, prevedi comunque una revisione umana del ~20% dell'output.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- ORA2_LEVEL3_PLACEHOLDER: Task 3 inserts Livello 3 slides here -->
```

- [ ] **Step 2: Verify structural balance and marker counts**

Run:

```bash
grep -c '<section' slides/20260710_intro_AI_hup/index.html
grep -c '</section>' slides/20260710_intro_AI_hup/index.html
grep -c 'class="slide"' slides/20260710_intro_AI_hup/index.html
grep -c 'ORA2_LEVEL2_PLACEHOLDER' slides/20260710_intro_AI_hup/index.html
grep -c 'ORA2_LEVEL3_PLACEHOLDER' slides/20260710_intro_AI_hup/index.html
grep -n '#6366f1\|#4f46e5\|rgba(99,102,241' slides/20260710_intro_AI_hup/index.html
```

Expected: first two commands print the same number (58), the third prints 43, the
fourth prints 0, the fifth prints 1, the sixth prints nothing.

- [ ] **Step 3: Visual check**

```bash
open slides/20260710_intro_AI_hup/index.html
```

Navigate through the new Livello 2 slides (roadmap, Cowork, exercise, for teams,
Design, Cowork+Projects, for slides, Skills): confirm no overflow, all `layout-two-col`
slides show two balanced columns plus a callout, and the Cowork exercise slide renders
its numbered steps.

- [ ] **Step 4: Commit**

```bash
git add slides/20260710_intro_AI_hup/index.html
git commit -m "$(cat <<'EOF'
Add Ora 2 Livello 2 with per-page concepts and Cowork exercise

Cover all 6 Intermediate-level claude101.com articles with concept
bullets, plus a live Cowork setup exercise.
EOF
)"
```

---

## Task 3: Livello 3 (Advanced) — 8 slides

**Files:**
- Modify: `slides/20260710_intro_AI_hup/index.html` (replace the `<!-- ORA2_LEVEL3_PLACEHOLDER -->` marker left by Task 2)

**Interfaces:**
- Consumes: the file as left by Task 2, specifically the exact marker line
  `  <!-- ORA2_LEVEL3_PLACEHOLDER: Task 3 inserts Livello 3 slides here -->`.
- Produces: Livello 3 roadmap/concepts/exercise (2.15-2.22), followed by a new marker
  `<!-- ORA2_LEVEL4_PLACEHOLDER: Task 4 inserts Livello 4 slides and Riepilogo here -->`
  that Task 4 replaces.

- [ ] **Step 1: Replace the Level 3 placeholder**

Find this exact line in `slides/20260710_intro_AI_hup/index.html`:

```html
  <!-- ORA2_LEVEL3_PLACEHOLDER: Task 3 inserts Livello 3 slides here -->
```

Replace with:

```html
  <!-- 2.15 — Livello 3: cosa vedremo -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Livello 3 — Advanced: cosa vedremo</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li><strong>Claude to sound like you</strong> (12 min) — catturare lo stile di scrittura di un team</li>
        <li><strong>Stop hitting Claude limits</strong> (12 min) — gestire i limiti di utilizzo</li>
        <li><strong>Stop Prompting</strong> (10 min) — tecniche oltre il prompt engineering tradizionale</li>
        <li><strong>Claude replaced me</strong> (4 min) — trasformare competenza ripetuta in una skill</li>
        <li><strong>Stop sounding like AI</strong> (20 min) — eliminare i pattern linguistici artificiali</li>
        <li><strong>Excel with Claude cowork</strong> (7 min) — creare fogli di calcolo con l'AI</li>
      </ul>
      <div class="callout">Chiudiamo il livello con un esercizio pratico: verificare un tuo testo con il file di stile anti-AI.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.16 — Claude to sound like you -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude to sound like you</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Cosa cattura</h3>
        <ul>
          <li>Lo stile di scrittura di un team (scelte lessicali, tono, struttura) può essere catturato in un file di testo e riutilizzato in ogni conversazione</li>
          <li>Processo di estrazione: intervista guidata (100 domande) su tono, regole di scrittura, esempi da imitare/evitare</li>
        </ul>
      </div>
      <div>
        <h3>Il file risultante</h3>
        <ul>
          <li>Il risultato viene compresso da decine di migliaia di parole a un file di 2.000-5.000 token — solo le istruzioni ad alto segnale restano</li>
          <li>Va salvato nella cartella Cowork per essere caricato automaticamente ad ogni sessione</li>
          <li>È portabile su altri assistenti AI ed è un documento vivo, da aggiornare nel tempo</li>
        </ul>
      </div>
      <div class="callout">Pensala come alla guida di stile del tuo team, applicata automaticamente da Claude a ogni comunicazione.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.17 — Stop hitting Claude limits -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Stop hitting Claude limits</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Da dove vengono i costi</h3>
        <ul>
          <li>Ogni messaggio rilegge l'intera cronologia della conversazione — i messaggi successivi costano esponenzialmente di più</li>
          <li>Un PDF costa 1.500-3.000 token a pagina, uno screenshot ~1.300 — convertire in testo semplice riduce i costi</li>
        </ul>
      </div>
      <div>
        <h3>Come ridurli</h3>
        <ul>
          <li>Abbinamento prodotto-task: Chat+modello leggero per domande rapide, Cowork+Opus per report su file, Code+Sonnet per task sui dati</li>
          <li>Le conversazioni lunghe diventano "fornaci di token" (il 98,5% della spesa va a rileggere la cronologia) — riparti dopo 15-20 messaggi</li>
          <li>"Modifica invece di rispondere": usa Edit su un messaggio precedente e rigenera, invece di accumulare follow-up</li>
        </ul>
      </div>
      <div class="callout">Disattiva ricerca web/connector/extended thinking quando non servono — sono le prime voci di spreco di token.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.18 — Stop Prompting -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Stop Prompting</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Il problema</h3>
        <ul>
          <li>I prompt "usa e getta" producono risultati generici perché mancano di contesto su stile, pubblico, obiettivi</li>
        </ul>
      </div>
      <div>
        <h3>La soluzione</h3>
        <ul>
          <li>Cowork collega Claude a una cartella locale di file di istruzioni in markdown, letti automaticamente ad ogni sessione</li>
          <li>Un editor di note esterno (gratuito) permette di modificare facilmente quella stessa cartella</li>
          <li>Le Skill trasformano workflow ricorrenti in comandi riutilizzabili</li>
        </ul>
      </div>
      <div class="callout">Il salto di qualità non è "un prompt migliore", ma smettere di ripartire da zero ogni volta.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.19 — Claude replaced me -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude replaced me</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li>L'autore ha creato una skill che automatizza una guida che prima scriveva a mano ogni settimana per i suoi lettori</li>
        <li>Il valore umano si sposta su "la parte difficile": risolvere eccezioni, testare iterazioni, accompagnare le persone nel cambiamento</li>
        <li>Modello consigliato per skill complesse: un modello di fascia alta con "effort" alto</li>
      </ul>
      <div class="callout">La stessa logica vale per qualunque processo che spieghi spesso ai colleghi — può diventare una skill condivisa, non solo un documento che nessuno legge.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.20 — Stop sounding like AI -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Stop sounding like AI</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>I segnali</h3>
        <ul>
          <li>Il pattern "non è X, è Y" appare 4 volte più spesso nei documenti aziendali recenti — è un segnale riconoscibile di testo generato da AI</li>
          <li>Lista di 100+ parole da evitare ("sfruttare", "sinergia", "senza soluzione di continuità"...)</li>
          <li>Oltre 15 pattern strutturali da evitare, non solo di vocabolario</li>
        </ul>
      </div>
      <div>
        <h3>Come intervenire</h3>
        <ul>
          <li>La specificità batte la levigatezza: sostituire affermazioni vaghe con dettagli concreti</li>
          <li>Un file di stile "anti-AI" letto da Claude prima di ogni task, invece di ripetere le istruzioni ogni volta</li>
        </ul>
      </div>
      <div class="callout">Rivedi periodicamente le tue ultime bozze e aggiorna la lista di pattern da evitare — i "tell" dell'AI cambiano nel tempo.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.21 — Esercizio pratico: Verifica il tuo testo -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude · Esercizio</span>
      <h2>Esercizio pratico — Verifica il tuo testo</h2>
    </div>
    <div class="slide-body layout-list">
      <p class="text-muted text-small">~8-10 minuti · serve un tuo testo aziendale reale</p>
      <ol>
        <li>Crea un file di stile "anti-AI" con la lista di parole/pattern da evitare (fornito durante la sessione)</li>
        <li>Prendi un tuo testo aziendale reale (email, comunicazione, report breve)</li>
        <li>Chiedi a Claude: "Verifica questo testo usando il file di stile anti-AI: quali pattern trovi?"</li>
        <li>Rivedi insieme le correzioni proposte</li>
      </ol>
      <div class="callout">L'obiettivo non è eliminare ogni traccia di AI, ma riconoscere i pattern che rendono un testo generico e sostituirli con dettagli concreti.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.22 — Excel with Claude cowork -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Excel with Claude cowork</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Perché Cowork</h3>
        <ul>
          <li>Risultato il miglior strumento per costruire fogli di calcolo da zero, testato contro altri 10 strumenti AI</li>
          <li>Workflow a 3 strumenti: Cowork (creazione) → foglio condiviso (condivisione/archiviazione) → editor esterno (modifica avanzata)</li>
        </ul>
      </div>
      <div>
        <h3>Come strutturare il prompt</h3>
        <ul>
          <li>Scopo, fogli necessari, specifiche di formattazione, e "le 10 assunzioni principali da verificare" prima di procedere</li>
          <li>Richiede piano Pro per l'app desktop; un connector cloud storage semplifica il trasferimento</li>
        </ul>
      </div>
      <div class="callout">Chiedi sempre a Claude di elencare le sue assunzioni prima di generare il foglio — evita errori silenziosi su formule e numeri.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- ORA2_LEVEL4_PLACEHOLDER: Task 4 inserts Livello 4 slides and Riepilogo here -->
```

- [ ] **Step 2: Verify structural balance and marker counts**

Run:

```bash
grep -c '<section' slides/20260710_intro_AI_hup/index.html
grep -c '</section>' slides/20260710_intro_AI_hup/index.html
grep -c 'class="slide"' slides/20260710_intro_AI_hup/index.html
grep -c 'ORA2_LEVEL3_PLACEHOLDER' slides/20260710_intro_AI_hup/index.html
grep -c 'ORA2_LEVEL4_PLACEHOLDER' slides/20260710_intro_AI_hup/index.html
grep -n '#6366f1\|#4f46e5\|rgba(99,102,241' slides/20260710_intro_AI_hup/index.html
```

Expected: first two commands print the same number (66), the third prints 51, the
fourth prints 0, the fifth prints 1, the sixth prints nothing.

- [ ] **Step 3: Visual check**

```bash
open slides/20260710_intro_AI_hup/index.html
```

Navigate through the new Livello 3 slides (roadmap, to sound like you, Stop hitting
limits, Stop Prompting, replaced me, Stop sounding like AI, exercise, Excel): confirm
no overflow and the exercise slide's numbered list renders correctly.

- [ ] **Step 4: Commit**

```bash
git add slides/20260710_intro_AI_hup/index.html
git commit -m "$(cat <<'EOF'
Add Ora 2 Livello 3 with per-page concepts and writing-audit exercise

Cover all 6 Advanced-level claude101.com articles, reframed for
corporate use, plus a live anti-AI writing style audit exercise.
EOF
)"
```

---

## Task 4: Livello 4 (Expert) + Riepilogo — 6 slides

**Files:**
- Modify: `slides/20260710_intro_AI_hup/index.html` (replace the `<!-- ORA2_LEVEL4_PLACEHOLDER -->` marker left by Task 3)

**Interfaces:**
- Consumes: the file as left by Task 3, specifically the exact marker line
  `  <!-- ORA2_LEVEL4_PLACEHOLDER: Task 4 inserts Livello 4 slides and Riepilogo here -->`.
- Produces: the completed 28-slide Ora 2 section, ending immediately before the
  untouched `<section data-section-title="Ora 3 — Prompting, MCP e Skill Aziendali">`.

- [ ] **Step 1: Replace the Level 4 placeholder**

Find this exact line in `slides/20260710_intro_AI_hup/index.html`:

```html
  <!-- ORA2_LEVEL4_PLACEHOLDER: Task 4 inserts Livello 4 slides and Riepilogo here -->
```

Replace with:

```html
  <!-- 2.23 — Livello 4: cosa vedremo -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Livello 4 — Expert: cosa vedremo</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li><strong>Claude Connectors</strong> (8 min) — integrare Claude con applicazioni esterne</li>
        <li><strong>Claude Code</strong> (14 min) — costruire app/siti senza saper programmare</li>
        <li><strong>Stop using your own Claude at work</strong> (9 min) — governance e sicurezza dell'AI personale in azienda</li>
      </ul>
      <div class="callout">Chiudiamo il livello, e l'Ora 2, con un esercizio pratico: mettere in sicurezza il tuo account.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.24 — Claude Connectors -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude Connectors</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Cosa sono</h3>
        <ul>
          <li>Oltre 200 connector disponibili (email, messaggistica, CRM, note riunioni, cloud storage)</li>
          <li>Tre connector fondamentali consigliati per iniziare: note riunioni, email, messaggistica di team</li>
        </ul>
      </div>
      <div>
        <h3>Buone pratiche</h3>
        <ul>
          <li>Per efficienza di token, tieni i connector disattivati di default — attivali solo per la chat che ne ha bisogno</li>
          <li>Prima settimana in sola lettura, poi eventualmente accesso in scrittura</li>
          <li>Disattiva i connector durante il lavoro creativo/di bozza per evitare rumore di contesto</li>
        </ul>
      </div>
      <div class="callout">I connector personalizzati permettono di collegare sistemi interni via standard aperti — accenno, sviluppo completo fuori scope per questa sessione.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.25 — Claude Code -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Claude Code</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Cos'è il vibecoding</h3>
        <ul>
          <li>Costruire app/siti descrivendo i requisiti in linguaggio naturale, senza saper programmare</li>
          <li>Due casi d'uso principali: mockup cliccabili per briefare sviluppatori/designer, strumenti interni su misura dove piccole imperfezioni sono accettabili</li>
        </ul>
      </div>
      <div>
        <h3>Come si usa</h3>
        <ul>
          <li>Non è una scorciatoia imprenditoriale: il valore è l'efficienza, non sostituire un team di sviluppo</li>
          <li>Richiede piano Pro, una cartella dedicata, modalità permessi avanzata, un modello di fascia alta</li>
          <li>Il passaggio a sviluppatori professionisti avviene tramite un documento di consegna (stack usato, funzionalità pronte, punti da rifinire)</li>
        </ul>
      </div>
      <div class="callout">Sapere quando NON usare Claude Code è importante quanto sapere come usarlo — per un singolo componente, un documento o un foglio di calcolo, gli strumenti visti in questa Ora 2 sono più adatti.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.26 — Stop using your own Claude at work -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Stop using your own Claude at work</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>I rischi</h3>
        <ul>
          <li>Gli account AI personali si addestrano di default sulle conversazioni — va disattivato manualmente</li>
          <li>Rischi legali concreti: violazioni di NDA, segreti industriali, normativa privacy (GDPR in Europa)</li>
          <li>Caso reale noto: ingegneri disciplinati dopo aver condiviso codice sorgente sensibile con un assistente AI personale nel giro di pochi giorni</li>
        </ul>
      </div>
      <div>
        <h3>Come proteggersi</h3>
        <ul>
          <li>La ricerca mostra che la maggioranza dei lavoratori usa chatbot personali per il lavoro senza approvazione IT, e molti hanno incollato informazioni sensibili almeno una volta</li>
          <li>Rischio "combinazione letale": account AI personale collegato via connector a email/drive/messaggistica aziendali</li>
          <li>Contenuti da non condividere mai: codice sorgente, dati clienti, roadmap non pubbliche, dati finanziari non pubblici, materiale coperto da NDA, credenziali</li>
        </ul>
      </div>
      <div class="callout">La soluzione non è smettere di usare l'AI, ma separare nettamente uso personale e uso aziendale, con governance esplicita.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.27 — Esercizio pratico: Metti in sicurezza il tuo account -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude · Esercizio</span>
      <h2>Esercizio pratico — Metti in sicurezza il tuo account</h2>
    </div>
    <div class="slide-body layout-list">
      <p class="text-muted text-small">~5 minuti · funziona su qualsiasi piano</p>
      <ol>
        <li>Vai su Impostazioni → Privacy e disattiva "Aiuta a migliorare i nostri modelli AI"</li>
        <li>Verifica la stessa impostazione su qualsiasi altro assistente AI personale che usi</li>
        <li>Prova una chat "Incognito/Temporanea" per un'informazione che non vuoi salvata</li>
        <li>Rivedi quali connector hai collegato e disconnetti quelli che non usi più</li>
      </ol>
      <div class="callout">Due minuti di impostazioni possono evitare un incidente di sicurezza — è il primo passo di adozione responsabile dell'AI in azienda.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 2.28 — Riepilogo -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 2 · Claude</span>
      <h2>Riepilogo Ora 2</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li>claude101.com copre 4 livelli e 18 articoli, da primo utilizzo ad adozione aziendale avanzata</li>
        <li>Cowork porta Claude a lavorare direttamente sui tuoi file locali, con contesto persistente; i Project isolano memoria e istruzioni per ogni area di lavoro</li>
        <li>Le Skill automatizzano processi ricorrenti: le vediamo applicate in azienda nell'Ora 3</li>
        <li>Abbiamo messo in pratica 4 esercizi dal vivo: riscrittura nel tuo stile, setup Cowork, verifica anti-AI di un testo, messa in sicurezza dell'account</li>
      </ul>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>
```

- [ ] **Step 2: Verify structural balance, marker counts, and final totals**

Run:

```bash
grep -c '<section' slides/20260710_intro_AI_hup/index.html
grep -c '</section>' slides/20260710_intro_AI_hup/index.html
grep -c 'class="slide"' slides/20260710_intro_AI_hup/index.html
grep -c 'PLACEHOLDER' slides/20260710_intro_AI_hup/index.html
grep -c 'Ora 2 · Claude' slides/20260710_intro_AI_hup/index.html
grep -n '#6366f1\|#4f46e5\|rgba(99,102,241' slides/20260710_intro_AI_hup/index.html
awk '/data-section-title="Ora 2/,/data-section-title="Ora 3/' slides/20260710_intro_AI_hup/index.html | grep -c 'class="slide"'
```

Expected: first two commands print the same number (72), the third prints 57, the
fourth prints 0 (no leftover placeholder comments anywhere in the file), the fifth
prints 29 (28 new slide-header labels + 1 unrelated occurrence in the "Programma della
Sessione" schedule table from Task 1 of the original scaffolding plan), the sixth
prints nothing, the seventh prints 28 (28 content slides between the Ora 2 divider and
the Ora 3 divider).

- [ ] **Step 3: Visual check**

```bash
open slides/20260710_intro_AI_hup/index.html
```

Navigate through the full Ora 2 section end to end (all 28 slides): confirm the
Livello 4 slides (roadmap, Connectors, Claude Code, Stop using your own Claude, final
exercise) render without overflow, the closing Riepilogo slide immediately precedes
the Ora 3 section divider, and there is no visible trace of any `PLACEHOLDER` comment
text or broken layout anywhere in Ora 2.

- [ ] **Step 4: Commit**

```bash
git add slides/20260710_intro_AI_hup/index.html
git commit -m "$(cat <<'EOF'
Add Ora 2 Livello 4 and updated Riepilogo, completing the rebuild

Cover all 3 Expert-level claude101.com articles plus a live account
privacy/security exercise, and refresh the closing summary to reflect
the full 28-slide, 4-exercise Ora 2.
EOF
)"
```
