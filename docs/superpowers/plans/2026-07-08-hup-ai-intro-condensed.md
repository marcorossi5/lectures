# Deck condensato "Intro AI" per Hup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `slides/20260710_intro_AI_hup/index.html`, a self-contained reveal.js deck for a 4-hour Hup training session, by rebranding the reveal.js engine/CSS from `slides/20260302_AI_per_turismo/index.html` (Digitiamo/indigo theme) to the Hup design system (navy/blue/lime, Helvetica Neue), and by writing new condensed, business-generic content across 4 one-hour blocks (AI fundamentals, Claude via claude101.com, prompting+MCP+skills, use cases placeholder) plus a glossary appendix.

**Architecture:** Single self-contained HTML file (reveal.js bundled inline, as in the source deck) built by copying the source file, remapping its CSS custom-property theme and logo assets, then replacing all section content. No build step, no test framework — this is a static content deliverable; "tests" are grep-based structural checks plus manual visual review in a browser (`open index.html`).

**Tech Stack:** reveal.js (bundled inline in the source file), plain CSS custom properties, vanilla JS. No npm/build tooling involved — this repo has no test framework or bundler for slides (see `README.md`); verification is grep + visual.

## Global Constraints

- Output file: `slides/20260710_intro_AI_hup/index.html` (per design spec, approved 2026-07-08).
- Logo asset: `slides/20260710_intro_AI_hup/public/logo-hup_header-blu.png` (already present, 162×103, RGBA, blue-on-transparent). This is the **only** logo asset — no separate white variant exists; white renderings are produced via CSS `filter: brightness(0) invert(1)`.
- Do not touch `slides/20260710_intro_AI_hup/hup-brand-components.html` (design-system reference, out of scope).
- Do not modify `slides/20260302_AI_per_turismo/` or `slides/20260302_AI_per_turismo_en/` (source material, read-only reference).
- All new slide copy is in Italian, matching the source deck's language.
- Examples must be business-generic (no tourism references) — per design spec decision.
- No quiz/"Challenge" slides, no `Strumenti AI: guida pratica`, `Identificare Opportunità`, `Sicurezza e Privacy`, or `Filo Conduttore` sections — all cut per design spec.
- Skills aziendali content is a placeholder — no invented Hup-specific skills.
- Ora 4 content is a placeholder — use cases to be defined later by the user.
- Git: commit locally only after each task. **Do not push** (explicit user instruction).
- Hup color tokens (from `hup-brand-components.html`): `--hup-blue #2A68D4`, `--hup-blue-mid #4872DA`, `--hup-navy #08205C`, `--hup-navy-900 #041233`, `--hup-lime #C8FF00`, `--hup-ink #1F2937`, `--hup-gray-500 #535353`, `--hup-gray-200 #E5E7EB`, `--hup-gray-100 #F8F8F8`. Font stack: `"Helvetica Neue", Helvetica, Arial, "Liberation Sans", system-ui, sans-serif`.

---

## Task 1: Skeleton, rebranding, and structural chrome

**Files:**
- Create: `slides/20260710_intro_AI_hup/index.html` (copy of `slides/20260302_AI_per_turismo/index.html`, then edited)
- Create: `slides/20260710_intro_AI_hup/public/images/panoramica_ai.png` (copied)
- Create: `slides/20260710_intro_AI_hup/public/images/rag_architecture.png` (copied)
- Existing (untouched): `slides/20260710_intro_AI_hup/public/logo-hup_header-blu.png`

**Interfaces:**
- Produces: the deck skeleton with 5 empty `<section data-section-title="...">` wrappers ready to receive content in Tasks 2-5:
  - `data-section-title="Ora 1 — Concetti Fondamentali AI"` (opens with a `slide-section` divider, closes before Ora 2)
  - `data-section-title="Ora 2 — Introduzione a Claude"`
  - `data-section-title="Ora 3 — Prompting, MCP e Skill Aziendali"`
  - `data-section-title="Ora 4 — Use Case"`
  - `data-section-title="Appendice — Glossario"`
- Produces: rebranded CSS tokens and logo mechanism that all later tasks' slide markup relies on (`.slide`, `.slide-header`, `.slide-body.layout-*`, `.card`, `.callout`, `.slide-footer .footer-logo`, `.slide-section`, `.slide-closing` — unchanged class names/behavior from the source deck, only colors/fonts/logo change).

- [ ] **Step 1: Copy base file and images**

```bash
cp "slides/20260302_AI_per_turismo/index.html" "slides/20260710_intro_AI_hup/index.html"
mkdir -p "slides/20260710_intro_AI_hup/public/images"
cp "slides/20260302_AI_per_turismo/public/images/panoramica_ai.png" "slides/20260302_AI_per_turismo/public/images/rag_architecture.png" "slides/20260710_intro_AI_hup/public/images/"
```

- [ ] **Step 2: Update title and favicon**

In `slides/20260710_intro_AI_hup/index.html`, find the `<title>` tag (near line 5) and the favicon `<link>` (line 7). Replace:

```html
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%236366f1'/%3E%3Ctext x='16' y='22' font-family='system-ui,sans-serif' font-size='14' font-weight='700' fill='white' text-anchor='middle' letter-spacing='-0.5'%3EAI%3C/text%3E%3C/svg%3E">
```

with (same badge, Hup blue instead of indigo):

```html
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232A68D4'/%3E%3Ctext x='16' y='22' font-family='system-ui,sans-serif' font-size='14' font-weight='700' fill='white' text-anchor='middle' letter-spacing='-0.5'%3EAI%3C/text%3E%3C/svg%3E">
```

Replace the `<title>` tag content with `<title>Introduzione all'AI e a Claude — Hup</title>`.

- [ ] **Step 3: Remap reveal.js core color/font variables**

Find this block (near line 31-55, inside the first `:root`):

```css
  --r-background-color: #fff;
  --r-main-font: Source Sans Pro, Helvetica, sans-serif;
  --r-main-font-size: 42px;
  --r-main-color: #222;
```

Replace with:

```css
  --r-background-color: #fff;
  --r-main-font: "Helvetica Neue", Helvetica, Arial, "Liberation Sans", system-ui, sans-serif;
  --r-main-font-size: 42px;
  --r-main-color: #1F2937;
```

Find:

```css
  --r-heading-font: Source Sans Pro, Helvetica, sans-serif;
  --r-heading-color: #222;
```

Replace with:

```css
  --r-heading-font: "Helvetica Neue", Helvetica, Arial, "Liberation Sans", system-ui, sans-serif;
  --r-heading-color: #08205C;
```

Find:

```css
  --r-link-color: #2a76dd;
  --r-link-color-dark: #1a53a1;
  --r-link-color-hover: #6ca0e8;
  --r-selection-background-color: #98bdef;
```

Replace with:

```css
  --r-link-color: #2A68D4;
  --r-link-color-dark: #17429A;
  --r-link-color-hover: #4872DA;
  --r-selection-background-color: #A9C6F5;
```

- [ ] **Step 4: Remap the custom theme token block**

Find the full block (the one under the `CORSO TURISMO — DESIGN SYSTEM` comment):

```css
:root {
  /* Palette — Slate base + Indigo accent */
  --primary-color:     #0f172a;   /* slate-900  */
  --accent-color:      #6366f1;   /* indigo-500 */
  --accent-dark:       #4338ca;   /* indigo-700 */
  --accent-bg:         #eef2ff;   /* indigo-50  */
  --stage-bg:          #cbd5e1;   /* slate-300  */
  --slide-bg:          #ffffff;
  --header-bg:         #ffffff;
  --footer-bg:         #f8fafc;   /* slate-50   */

  /* Text */
  --text-color:        #334155;   /* slate-700  */
  --text-muted:        #94a3b8;   /* slate-400  */
  --heading-color:     #0f172a;   /* slate-900  */
  --heading-weight:    700;

  /* Tipografia */
  --font-main:         -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui,
                       'Helvetica Neue', Arial, sans-serif;
  --font-mono:         'JetBrains Mono', 'Fira Code', ui-monospace,
                       'Cascadia Code', monospace;
  --font-size-base:    20px;
  --line-height:       1.6;

  /* Chrome dimensioni */
  --header-height:     60px;
  --footer-height:     44px;
  --header-accent-w:   3px;
  --slide-padding-h:   40px;
  --slide-padding-v:   18px;

  /* Spaziature */
  --gap-xs:   4px;
  --gap-sm:   8px;
  --gap-md:   16px;
  --gap-lg:   24px;
  --gap-xl:   36px;

  /* Bordi */
  --border-radius:     6px;
  --border-radius-lg:  10px;
  --border-color:      #e2e8f0;   /* slate-200 */
  --card-shadow:       0 1px 3px rgba(0,0,0,0.07), 0 1px 2px rgba(0,0,0,0.05);

  /* Code */
  --code-bg:           #f1f5f9;   /* slate-100 */
  --code-color:        #1e293b;   /* slate-800 */
  --code-border:       #e2e8f0;

  /* Tabelle */
  --table-header-bg:   #4338ca;   /* indigo-700 */
  --table-header-text: #ffffff;
  --table-row-alt:     #eef2ff;   /* indigo-50  */

  /* Callout */
  --callout-bg:        #eff6ff;   /* blue-50   */
  --callout-border:    #3b82f6;   /* blue-500  */
  --callout-text:      #1d4ed8;   /* blue-700  */
  --warning-bg:        #fffbeb;   /* amber-50  */
  --warning-border:    #f59e0b;   /* amber-500 */
  --warning-text:      #92400e;   /* amber-800 */
  --success-bg:        #ecfdf5;   /* emerald-50  */
  --success-border:    #10b981;   /* emerald-500 */
  --success-text:      #065f46;   /* emerald-800 */

  /* Progress */
  --progress-color:    #6366f1;
  --link-color:        #6366f1;
}
```

Replace with:

```css
:root {
  /* Palette — Hup navy base + Hup blue accent */
  --primary-color:     #08205C;   /* hup-navy   */
  --accent-color:      #2A68D4;   /* hup-blue   */
  --accent-dark:       #17429A;   /* hup-blue pressed */
  --accent-bg:         #EAF1FC;   /* hup-blue tint */
  --stage-bg:          #D7DEEA;   /* cool neutral behind the scaled slide */
  --slide-bg:          #ffffff;
  --header-bg:         #ffffff;
  --footer-bg:         #F8F8F8;   /* hup-gray-100 */

  /* Text */
  --text-color:        #1F2937;   /* hup-ink */
  --text-muted:        #535353;   /* hup-gray-500 */
  --heading-color:     #08205C;   /* hup-navy */
  --heading-weight:    700;

  /* Tipografia */
  --font-main:         "Helvetica Neue", Helvetica, Arial, "Liberation Sans",
                       system-ui, sans-serif;
  --font-mono:         'JetBrains Mono', 'Fira Code', ui-monospace,
                       'Cascadia Code', monospace;
  --font-size-base:    20px;
  --line-height:       1.6;

  /* Chrome dimensioni */
  --header-height:     60px;
  --footer-height:     44px;
  --header-accent-w:   3px;
  --slide-padding-h:   40px;
  --slide-padding-v:   18px;

  /* Spaziature */
  --gap-xs:   4px;
  --gap-sm:   8px;
  --gap-md:   16px;
  --gap-lg:   24px;
  --gap-xl:   36px;

  /* Bordi */
  --border-radius:     6px;
  --border-radius-lg:  10px;
  --border-color:      #E5E7EB;   /* hup-gray-200 */
  --card-shadow:       0 1px 3px rgba(8,32,92,0.07), 0 1px 2px rgba(8,32,92,0.05);

  /* Code */
  --code-bg:           #F8F8F8;   /* hup-gray-100 */
  --code-color:        #1F2937;   /* hup-ink */
  --code-border:       #E5E7EB;

  /* Tabelle */
  --table-header-bg:   #2A68D4;   /* hup-blue */
  --table-header-text: #ffffff;
  --table-row-alt:     #EAF1FC;   /* hup-blue tint */

  /* Callout */
  --callout-bg:        #EAF1FC;   /* hup-blue tint */
  --callout-border:    #2A68D4;   /* hup-blue */
  --callout-text:      #08205C;   /* hup-navy */
  --warning-bg:        #fffbeb;   /* amber-50 — semantic, unchanged */
  --warning-border:    #f59e0b;   /* amber-500 */
  --warning-text:      #92400e;   /* amber-800 */
  --success-bg:        #ecfdf5;   /* emerald-50 — semantic, unchanged */
  --success-border:    #10b981;   /* emerald-500 */
  --success-text:      #065f46;   /* emerald-800 */

  /* Progress */
  --progress-color:    #2A68D4;   /* hup-blue */
  --link-color:        #2A68D4;   /* hup-blue */
}
```

- [ ] **Step 5: Retint the slide-header accent line**

Find (near line 511-517):

```css
.reveal .slide-header::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--accent-color), var(--accent-dark));
}
```

This already references `var(--accent-color)`/`var(--accent-dark)`, which now resolve to Hup blue — **no change needed** here. Skip to Step 6.

- [ ] **Step 6: Retint cover top bar, logo watermark, and eyebrow**

Find:

```css
/* Decorative top gradient bar on cover */
.reveal section.slide-cover::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--accent-color), #8b5cf6);
}

/* Logo watermark + subtle circle on cover */
.reveal section.slide-cover::after {
  content: '';
  position: absolute;
  inset: 0;
  background:
    url('public/logos/Digitiamo%20-%20Logo%20-%20Blue.png') no-repeat calc(100% - 48px) calc(100% - 40px) / 360px auto,
    radial-gradient(ellipse at 110% 115%, var(--accent-bg) 0%, transparent 50%);
  opacity: 0.28;
  pointer-events: none;
}
```

Replace with (top bar now blue→lime, the one deliberate sparing use of the lime accent; logo path updated, no filter needed since the blue logo reads fine on the white cover):

```css
/* Decorative top gradient bar on cover */
.reveal section.slide-cover::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--accent-color), #C8FF00);
}

/* Logo watermark + subtle circle on cover */
.reveal section.slide-cover::after {
  content: '';
  position: absolute;
  inset: 0;
  background:
    url('public/logo-hup_header-blu.png') no-repeat calc(100% - 48px) calc(100% - 40px) / 360px auto,
    radial-gradient(ellipse at 110% 115%, var(--accent-bg) 0%, transparent 50%);
  opacity: 0.28;
  pointer-events: none;
}
```

- [ ] **Step 7: Retint section-divider background, watermark, and glow**

Find:

```css
/* Section divider */
.reveal section.slide-section {
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start;
  justify-content: center;
  height: 100% !important;
  padding: 56px var(--slide-padding-h) !important;
  box-sizing: border-box;
  background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #1e293b 100%) !important;
  position: relative;
  overflow: hidden;
}
```

Replace the `background` line with the Hup hero gradient:

```css
  background: radial-gradient(120% 130% at 70% 20%, #3E86F2 0%, #2A68D4 35%, #10306E 72%, #041233 100%) !important;
```

Find:

```css
/* Logo watermark — bottom-right background */
.reveal section.slide-section::before {
  content: '';
  position: absolute;
  bottom: 44px;
  right: 48px;
  width: 380px;
  height: 120px;
  background: url('public/logos/Digitiamo%20-%20Logo%20-%20White.png') no-repeat right center / contain;
  opacity: 0.28;
  pointer-events: none;
  z-index: 0;
}

/* Radial glow accent — top-right */
.reveal section.slide-section::after {
  content: '';
  position: absolute;
  top: -60px; right: -60px;
  width: 320px; height: 320px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(99,102,241,0.25) 0%, transparent 65%);
  pointer-events: none;
  z-index: 0;
}

.reveal section.slide-section .section-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 0.52em;
  font-weight: 600;
  color: rgba(165,180,252,0.9);   /* indigo-300 */
  background: rgba(99,102,241,0.15);
  padding: 3px 10px;
  border-radius: 9999px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: var(--gap-md);
}
```

Replace with (logo now white via CSS filter since it sits on the dark gradient; glow and eyebrow retinted to Hup blue):

```css
/* Logo watermark — bottom-right background */
.reveal section.slide-section::before {
  content: '';
  position: absolute;
  bottom: 44px;
  right: 48px;
  width: 380px;
  height: 120px;
  background: url('public/logo-hup_header-blu.png') no-repeat right center / contain;
  filter: brightness(0) invert(1);
  opacity: 0.28;
  pointer-events: none;
  z-index: 0;
}

/* Radial glow accent — top-right */
.reveal section.slide-section::after {
  content: '';
  position: absolute;
  top: -60px; right: -60px;
  width: 320px; height: 320px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(72,114,218,0.35) 0%, transparent 65%);
  pointer-events: none;
  z-index: 0;
}

.reveal section.slide-section .section-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 0.52em;
  font-weight: 600;
  color: rgba(200,255,0,0.9);   /* hup-lime */
  background: rgba(72,114,218,0.2);
  padding: 3px 10px;
  border-radius: 9999px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: var(--gap-md);
}
```

- [ ] **Step 8: Retint closing slide background, glow, and watermark**

Find:

```css
/* Closing */
.reveal section.slide-closing {
  display: flex !important;
  flex-direction: column !important;
  align-items: center;
  justify-content: center;
  height: 100% !important;
  padding: 56px !important;
  box-sizing: border-box;
  text-align: center;
  background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #1e293b 100%) !important;
  position: relative;
  overflow: hidden;
}

.reveal section.slide-closing::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 40%, rgba(99,102,241,0.2) 0%, transparent 65%);
  pointer-events: none;
  z-index: 0;
}

/* Logo watermark on closing slide */
.reveal section.slide-closing::after {
  content: '';
  position: absolute;
  bottom: 44px;
  right: 48px;
  width: 380px;
  height: 120px;
  background: url('public/logos/Digitiamo%20-%20Logo%20-%20White.png') no-repeat right center / contain;
  opacity: 0.28;
  pointer-events: none;
  z-index: 0;
}
```

Replace with:

```css
/* Closing */
.reveal section.slide-closing {
  display: flex !important;
  flex-direction: column !important;
  align-items: center;
  justify-content: center;
  height: 100% !important;
  padding: 56px !important;
  box-sizing: border-box;
  text-align: center;
  background: radial-gradient(120% 130% at 70% 20%, #3E86F2 0%, #2A68D4 35%, #10306E 72%, #041233 100%) !important;
  position: relative;
  overflow: hidden;
}

.reveal section.slide-closing::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 40%, rgba(72,114,218,0.25) 0%, transparent 65%);
  pointer-events: none;
  z-index: 0;
}

/* Logo watermark on closing slide */
.reveal section.slide-closing::after {
  content: '';
  position: absolute;
  bottom: 44px;
  right: 48px;
  width: 380px;
  height: 120px;
  background: url('public/logo-hup_header-blu.png') no-repeat right center / contain;
  filter: brightness(0) invert(1);
  opacity: 0.28;
  pointer-events: none;
  z-index: 0;
}
```

- [ ] **Step 9: Replace the JS logo-source constants**

Find (near line 5302-5303):

```javascript
  var LOGO_BLUE  = 'public/logos/Digitiamo%20-%20Logo%20-%20Blue.png';
  var LOGO_WHITE = 'public/logos/Digitiamo%20-%20Logo%20-%20White.png';
```

Replace with (footer logo only ever appears on the light `--footer-bg`, in regular `.slide` sections — both constants can point at the one blue asset; see `updateSlide()` a few lines below, unchanged):

```javascript
  var LOGO_BLUE  = 'public/logo-hup_header-blu.png';
  var LOGO_WHITE = 'public/logo-hup_header-blu.png';
```

- [ ] **Step 10: Replace all remaining `alt="Digitiamo"` attributes**

Run a global replace across the file:

```bash
sed -i '' 's/alt="Digitiamo"/alt="Hup."/g' "slides/20260710_intro_AI_hup/index.html"
```

- [ ] **Step 11: Verify no Digitiamo references remain**

```bash
grep -n "Digitiamo" "slides/20260710_intro_AI_hup/index.html"
```

Expected: no output (empty).

- [ ] **Step 12: Replace the "Apertura" section (cover + objectives)**

Find the full `<section data-section-title="Apertura">...</section>` block (from `<section data-section-title="Apertura">` down to its closing `</section>`, currently containing the cover slide, "Obiettivi di apprendimento", and "Contesto del corso"). Replace the entire block with:

```html
<section data-section-title="Apertura">

  <!-- 0.1 — Titolo principale -->
  <section class="slide-cover">
    <div class="cover-eyebrow">Hup · Formazione AI</div>
    <h1>Introduzione all'AI e a Claude</h1>
    <p class="cover-subtitle">Concetti fondamentali di intelligenza artificiale, Claude e prompt engineering per il lavoro quotidiano</p>
    <p class="cover-meta">Sessione da 4 ore · 10 luglio 2026</p>
    <img class="cover-logo" alt="Hup.">
  </section>

  <!-- 0.2 — Obiettivi di apprendimento -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Apertura</span>
      <h2>Obiettivi della sessione</h2>
    </div>
    <div class="slide-body layout-list">
      <p class="text-muted text-small">Al termine della sessione sarai in grado di:</p>
      <ul>
        <li>Spiegare cos'è un LLM e come genera testo (token, contesto, addestramento)</li>
        <li>Distinguere fine-tuning, RAG e prompting e scegliere l'approccio corretto</li>
        <li>Orientarti tra i livelli e le risorse della guida Claude 101</li>
        <li>Scrivere prompt strutturati ed efficaci per il lavoro quotidiano</li>
        <li>Capire cosa sono MCP, tool calling e le skill Claude riutilizzabili in azienda</li>
      </ul>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

</section>
```

- [ ] **Step 13: Replace the "Programma della Giornata" section with the new 4-block agenda**

Find the full `<section data-section-title="Programma della Giornata">...</section>` block (including its inline `<style>` for `.schedule-tbl`). Replace with:

```html
<section data-section-title="Programma della Sessione">

<style>
  .reveal .slide-body table.schedule-tbl { flex: none !important; }

  .schedule-tbl {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;
    font-size: 0.7em;
  }

  .schedule-tbl thead th {
    background: var(--table-header-bg);
    color: var(--table-header-text);
    padding: 8px 12px;
    text-align: left;
    font-weight: 600;
    font-size: 0.88em;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-bottom: 2px solid rgba(255,255,255,0.15);
  }

  .schedule-tbl td {
    padding: 8px 12px;
    vertical-align: middle;
    border-bottom: 1px solid var(--border-color);
  }
  .schedule-tbl tr:last-child td { border-bottom: none; }

  .schedule-tbl .col-time    { width: 110px; }
  .schedule-tbl .col-part    { width: 220px; border-right: 1px solid var(--border-color); }

  .schedule-tbl .col-time {
    font-family: var(--font-mono);
    font-size: 0.88em;
    font-weight: 700;
    color: var(--accent-dark);
    white-space: nowrap;
    border-right: 2px solid var(--border-color);
  }
  .schedule-tbl .col-part {
    font-weight: 700;
    white-space: nowrap;
    padding-left: 14px;
  }
  .schedule-tbl .col-topics { padding-left: 14px; font-size: 0.9em; }

  .schedule-tbl ul {
    margin: 0;
    padding: 0 0 0 1.1em;
    list-style: disc;
    color: var(--text-color);
  }
  .schedule-tbl ul li { margin: 0; padding: 0; line-height: 1.6; }

  .sched-row td { background: #EAF1FC; }
</style>

  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Apertura</span>
      <h2>Programma della Sessione</h2>
    </div>
    <div class="slide-body layout-table" style="justify-content:center;">
      <table class="schedule-tbl">
        <thead>
          <tr>
            <th class="col-time">Durata</th>
            <th class="col-part">Blocco</th>
            <th class="col-topics">Argomenti</th>
          </tr>
        </thead>
        <tbody>
          <tr class="sched-row">
            <td class="col-time">60 min</td>
            <td class="col-part">Ora 1 · Concetti AI</td>
            <td class="col-topics">
              <ul>
                <li>LLM, context window, fine-tuning</li>
                <li>RAG, agenti AI, tool calling</li>
              </ul>
            </td>
          </tr>
          <tr class="sched-row">
            <td class="col-time">60 min</td>
            <td class="col-part">Ora 2 · Claude</td>
            <td class="col-topics">
              <ul>
                <li>I 4 livelli della guida Claude 101</li>
                <li>Cowork, Projects, Skills</li>
              </ul>
            </td>
          </tr>
          <tr class="sched-row">
            <td class="col-time">60 min</td>
            <td class="col-part">Ora 3 · Prompting &amp; Skill</td>
            <td class="col-topics">
              <ul>
                <li>Prompt engineering efficace</li>
                <li>MCP, tool calling, skill aziendali</li>
              </ul>
            </td>
          </tr>
          <tr class="sched-row">
            <td class="col-time">60 min</td>
            <td class="col-part">Ora 4 · Use Case</td>
            <td class="col-topics">
              <ul>
                <li>Esempi applicati al nostro contesto</li>
              </ul>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

</section>
```

- [ ] **Step 14: Delete the "Filo Conduttore" section**

Find the full `<section data-section-title="Filo Conduttore">...</section>` block and delete it entirely (it's day-narrative content not needed for the condensed session).

- [ ] **Step 15: Replace every remaining original content section (from "AI nel Turismo: Panoramica" through "Glossario") with 5 empty divider shells**

Find everything from `<section data-section-title="AI nel Turismo: Panoramica">` down to the end of the file's `<section data-section-title="Glossario">...</section>` block (i.e. all remaining original section wrappers). Replace that entire span with:

```html
<section data-section-title="Ora 1 — Concetti Fondamentali AI">

  <section class="slide-section">
    <div class="section-eyebrow">Ora 1</div>
    <h2>Concetti Fondamentali di AI</h2>
    <p class="section-desc">Cos'è un LLM · Context window · Fine-tuning, RAG e prompting · Agenti e tool calling</p>
  </section>

  <!-- ORA1_CONTENT_PLACEHOLDER: Task 2 inserts slides here -->

</section>

<section data-section-title="Ora 2 — Introduzione a Claude">

  <section class="slide-section">
    <div class="section-eyebrow">Ora 2</div>
    <h2>Introduzione a Claude</h2>
    <p class="section-desc">I livelli e le pagine della guida Claude 101, da Claude for Dummies a Claude Code</p>
  </section>

  <!-- ORA2_CONTENT_PLACEHOLDER: Task 3 inserts slides here -->

</section>

<section data-section-title="Ora 3 — Prompting, MCP e Skill Aziendali">

  <section class="slide-section">
    <div class="section-eyebrow">Ora 3</div>
    <h2>Prompting, MCP e Skill Aziendali</h2>
    <p class="section-desc">Prompt engineering efficace · Model Context Protocol · Skill Claude riutilizzabili in azienda</p>
  </section>

  <!-- ORA3_CONTENT_PLACEHOLDER: Task 4 inserts slides here -->

</section>

<section data-section-title="Ora 4 — Use Case">

  <section class="slide-section">
    <div class="section-eyebrow">Ora 4</div>
    <h2>Use Case</h2>
    <p class="section-desc">Esempi pratici applicati al nostro contesto di lavoro</p>
  </section>

  <!-- ORA4_CONTENT_PLACEHOLDER: Task 5 inserts slides here -->

</section>

<section data-section-title="Chiusura">

  <!-- CHIUSURA_CONTENT_PLACEHOLDER: Task 5 inserts slides here -->

</section>

<section data-section-title="Appendice — Glossario">

  <section class="slide-section">
    <div class="section-eyebrow">Appendice</div>
    <h2>Glossario</h2>
    <p class="section-desc">Termini chiave usati durante la sessione</p>
  </section>

  <!-- GLOSSARIO_CONTENT_PLACEHOLDER: Task 5 inserts slides here -->

</section>
```

- [ ] **Step 16: Verify structure**

```bash
grep -c 'data-section-title' "slides/20260710_intro_AI_hup/index.html"
```

Expected: `8` (Apertura, Programma della Sessione, Ora 1, Ora 2, Ora 3, Ora 4, Chiusura, Appendice — Glossario).

```bash
grep -c 'PLACEHOLDER' "slides/20260710_intro_AI_hup/index.html"
```

Expected: `6` (ORA1, ORA2, ORA3, ORA4, CHIUSURA, GLOSSARIO — these HTML comments are removed as each task fills its section; they are not visible in the rendered deck).

- [ ] **Step 17: Visual check**

```bash
open "slides/20260710_intro_AI_hup/index.html"
```

Confirm in the browser: cover slide shows Hup branding (navy heading, blue/lime top bar, blue Hup logo watermark bottom-right, no Digitiamo text anywhere), agenda table renders with 4 rows, section-divider slides show white Hup logo watermark on the navy/blue gradient background. Navigate with arrow keys through all slides to confirm no broken layout.

- [ ] **Step 18: Commit**

```bash
git add slides/20260710_intro_AI_hup/index.html slides/20260710_intro_AI_hup/public/images/
git commit -m "$(cat <<'EOF'
Scaffold Hup-branded condensed AI intro deck

Rebrand the reveal.js deck engine/CSS from the source tourism deck to
Hup's navy/blue/lime palette and logo, and lay out the 4-hour agenda
as empty section shells ready for content.
EOF
)"
```

---

## Task 2: Ora 1 content — Concetti Fondamentali di AI

**Files:**
- Modify: `slides/20260710_intro_AI_hup/index.html` (insert content at the `<!-- ORA1_CONTENT_PLACEHOLDER -->` marker left by Task 1, then remove the marker comment)

**Interfaces:**
- Consumes: `.slide`, `.slide-header`, `.slide-body.layout-list/.layout-two-col/.layout-three-col/.layout-diagram/.layout-table`, `.card`, `.callout`, `.slide-footer .footer-logo/.footer-page` classes established in Task 1 (unchanged from source deck).
- Consumes: `public/images/panoramica_ai.png` (copied in Task 1).

- [ ] **Step 1: Write the Ora 1 content slides**

Replace the line `<!-- ORA1_CONTENT_PLACEHOLDER: Task 2 inserts slides here -->` with:

```html
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

- [ ] **Step 2: Verify slide count and no leftover placeholder**

```bash
grep -c 'ORA1_CONTENT_PLACEHOLDER' "slides/20260710_intro_AI_hup/index.html"
```

Expected: `0`.

```bash
awk '/data-section-title="Ora 1/,/data-section-title="Ora 2/' "slides/20260710_intro_AI_hup/index.html" | grep -c 'class="slide"'
```

Expected: `8` (8 content slides between the Ora 1 divider and the Ora 2 divider).

- [ ] **Step 3: Visual check**

```bash
open "slides/20260710_intro_AI_hup/index.html"
```

Navigate to the Ora 1 section: confirm all 8 slides render without overflow, the RAG diagram image displays, the fine-tuning/RAG/prompting table is readable, no tourism-specific wording appears anywhere.

- [ ] **Step 4: Commit**

```bash
git add slides/20260710_intro_AI_hup/index.html
git commit -m "$(cat <<'EOF'
Add Ora 1 content: Concetti Fondamentali di AI

Condense LLM, context window, fine-tuning/RAG/prompting, agents, and
tool calling/MCP into 8 slides with business-generic examples.
EOF
)"
```

---

## Task 3: Ora 2 content — Introduzione a Claude (claude101.com)

**Files:**
- Modify: `slides/20260710_intro_AI_hup/index.html` (insert content at the `<!-- ORA2_CONTENT_PLACEHOLDER -->` marker, then remove the marker comment)

**Interfaces:**
- Consumes: same layout classes as Task 2.
- Content basis (already fetched during design, reuse verbatim as source facts — do not re-fetch):
  - Site structure: 4 levels (Beginner/Intermediate/Advanced/Expert), each with 3-6 named pages (listed in Step 1 below).
  - Claude Cowork: local desktop AI collaboration; ABOUT ME / OUTPUTS / TEMPLATES folder structure; about-me.md, anti-ai-writing-style, my-company files; global instructions; restart-conversation-from-here over follow-ups; model selection by task complexity (Opus+Extended Thinking for deep work, Sonnet/Haiku for lighter tasks); ~20-minute setup.
  - Claude Cowork Projects: persistent workspace = folder + custom instructions + scoped memory + scheduled tasks + task history; solves "cold start" of re-explaining context each session; setup via Cowork → Projects → "+"; ~15-minute setup; local to one machine (no team sharing yet); higher resource usage (Pro/Max plan).
  - Claude Skills: persistent, reusable instructions triggered automatically (e.g. via `/slash-command`) when Claude recognizes a matching task; built via Skill Creator inside Cowork (interview-based) or makemyskill.com; core file is `SKILL.md` with trigger name, "when to use", explicit "when NOT to use" (negative boundaries matter more than positive ones), and step-by-step instructions; only loads full instructions when triggered (token-efficient); portable as an open standard.

- [ ] **Step 1: Write the Ora 2 content slides**

Replace the line `<!-- ORA2_CONTENT_PLACEHOLDER: Task 3 inserts slides here -->` with:

```html
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

- [ ] **Step 2: Verify slide count and no leftover placeholder**

```bash
grep -c 'ORA2_CONTENT_PLACEHOLDER' "slides/20260710_intro_AI_hup/index.html"
```

Expected: `0`.

```bash
awk '/data-section-title="Ora 2/,/data-section-title="Ora 3/' "slides/20260710_intro_AI_hup/index.html" | grep -c 'class="slide"'
```

Expected: `9`.

- [ ] **Step 3: Visual check**

```bash
open "slides/20260710_intro_AI_hup/index.html"
```

Navigate to the Ora 2 section: confirm all 9 slides render, the 3-column level cards wrap correctly, no broken `<code>` inline styling.

- [ ] **Step 4: Commit**

```bash
git add slides/20260710_intro_AI_hup/index.html
git commit -m "$(cat <<'EOF'
Add Ora 2 content: Introduzione a Claude (claude101.com)

Cover all 4 claude101.com levels plus a deep-dive on Cowork, Projects,
and Skills, sourced from the live site during design.
EOF
)"
```

---

## Task 4: Ora 3 content — Prompting, MCP e Skill Aziendali

**Files:**
- Modify: `slides/20260710_intro_AI_hup/index.html` (insert content at the `<!-- ORA3_CONTENT_PLACEHOLDER -->` marker, then remove the marker comment)

**Interfaces:**
- Consumes: same layout classes as Task 2. Also uses `.slide-body.layout-code` with a `<pre><code>` block for the prompt before/after example — same pattern as the source deck's "Esempio pratico" slides (a `<pre>` inside `layout-code`, no external library, plain text formatting).

- [ ] **Step 1: Write the Ora 3 content slides**

Replace the line `<!-- ORA3_CONTENT_PLACEHOLDER: Task 4 inserts slides here -->` with:

```html
  <!-- 3.1 — Anatomia di un prompt -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 3 · Prompting</span>
      <h2>Anatomia di un prompt efficace</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li><strong>Ruolo</strong> — chi deve "essere" il modello (es. "Sei un analista finanziario")</li>
        <li><strong>Contesto</strong> — informazioni di sfondo rilevanti per il task</li>
        <li><strong>Istruzione</strong> — cosa deve fare, in modo specifico e verificabile</li>
        <li><strong>Formato di output</strong> — come vuoi la risposta (elenco, tabella, lunghezza, tono)</li>
        <li><strong>Esempi</strong> — 1-2 esempi di input/output atteso, quando il formato è particolare</li>
      </ul>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 3.2 — Tecniche -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 3 · Prompting</span>
      <h2>Zero-shot, Few-shot, Chain-of-Thought</h2>
    </div>
    <div class="slide-body layout-three-col">
      <div class="card">
        <h4>Zero-shot</h4>
        <p>Chiedi direttamente, senza esempi. Funziona bene per task comuni e ben definiti.</p>
      </div>
      <div class="card">
        <h4>Few-shot</h4>
        <p>Fornisci 2-3 esempi di input/output prima della richiesta reale. Utile per formati specifici o stile particolare.</p>
      </div>
      <div class="card">
        <h4>Chain-of-Thought</h4>
        <p>Chiedi al modello di ragionare passo passo prima della risposta finale. Migliora l'accuratezza su task complessi.</p>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 3.3 — Esempio pratico -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 3 · Prompting</span>
      <h2>Esempio: da prompt vago a prompt efficace</h2>
    </div>
    <div class="slide-body layout-code">
      <div class="warning" style="margin-bottom:0.6em;">
        <strong>Vago:</strong> "Scrivi una risposta a questo cliente."
      </div>
      <div class="success">
        <strong>Efficace:</strong> "Sei l'assistente customer care di [azienda]. Il cliente ha scritto lamentando un ritardo nella consegna. Scrivi una risposta in italiano, tono professionale ed empatico, massimo 100 parole, che: 1) riconosca il disagio, 2) spieghi la causa in una frase, 3) offra un'azione concreta di rimedio. Non promettere sconti non autorizzati."
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 3.4 — Errori comuni -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 3 · Prompting</span>
      <h2>Errori comuni nel prompting</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li>Istruzioni ambigue o troppo generiche ("migliora questo testo")</li>
        <li>Nessun formato di output richiesto: il modello sceglie per te, spesso in modo incoerente</li>
        <li>Troppo contesto irrilevante, che diluisce l'attenzione del modello</li>
        <li>Nessuna verifica dell'output: il modello può essere sicuro e sbagliato allo stesso tempo</li>
        <li>Un unico prompt enorme invece di scomporre il task in passi più piccoli</li>
      </ul>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 3.5 — MCP concetto -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 3 · MCP</span>
      <h2>MCP — Model Context Protocol</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Il problema</h3>
        <ul>
          <li>Ogni applicazione AI che vuole usare strumenti esterni (calendario, CRM, file, database) dovrebbe integrarli uno per uno</li>
          <li>Duplicazione di lavoro tra team e strumenti diversi</li>
        </ul>
      </div>
      <div>
        <h3>La soluzione</h3>
        <ul>
          <li>MCP è uno standard aperto: un "server" espone un set di strumenti in un formato comune</li>
          <li>Qualsiasi client compatibile (Claude incluso) può collegarsi e usarli, senza integrazione custom</li>
          <li>Un server MCP per il CRM aziendale, ad esempio, funziona sia con Claude che con altri strumenti compatibili</li>
        </ul>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 3.6 — MCP esempio -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 3 · MCP</span>
      <h2>Esempio pratico: assistente collegato a un tool</h2>
    </div>
    <div class="slide-body layout-list">
      <p class="text-muted text-small">Scenario: "Controlla se ci sono riunioni libere domani pomeriggio e proponi 3 orari."</p>
      <ul>
        <li>Il modello riconosce che serve leggere un calendario e richiama lo strumento <code>get_calendar_events</code> esposto da un server MCP collegato al calendario aziendale</li>
        <li>Riceve la lista di eventi come risultato strutturato (JSON)</li>
        <li>Genera la risposta finale in linguaggio naturale, basata sui dati reali ricevuti — non inventati</li>
      </ul>
      <div class="callout">Senza il tool, il modello potrebbe "inventare" orari plausibili ma falsi. Con il tool, la risposta è ancorata a dati reali.</div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 3.7 — Cos'è una Skill (ripresa) -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 3 · Skill Aziendali</span>
      <h2>Dalla Skill personale alla Skill aziendale</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Cosa abbiamo visto nell'Ora 2</h3>
        <ul>
          <li>Una Skill è un file <strong>SKILL.md</strong>: trigger, descrizione "quando usarla" / "quando NON usarla", istruzioni passo-passo</li>
          <li>Si attiva automaticamente quando Claude riconosce il task</li>
        </ul>
      </div>
      <div>
        <h3>Perché renderla "aziendale"</h3>
        <ul>
          <li>Una skill codifica un processo che normalmente vive solo nella testa di una persona (o in un documento che nessuno legge)</li>
          <li>Condivisa nel team, garantisce lo stesso standard di qualità/formato a chiunque la usi</li>
          <li>È un asset riutilizzabile: si aggiorna una volta, migliora ogni utilizzo futuro</li>
        </ul>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 3.8 — Skill aziendali Hup (placeholder) -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 3 · Skill Aziendali</span>
      <h2>Skill aziendali Hup — da completare</h2>
    </div>
    <div class="slide-body layout-list">
      <div class="callout">
        Questa slide è un segnaposto: verrà completata con esempi reali di skill Claude usate internamente in Hup (nome, scopo, quando si attivano, cosa producono).
      </div>
      <p class="text-muted text-small">Struttura suggerita per ogni skill da presentare: nome del trigger · problema che risolve · input tipico · output prodotto · impatto misurato.</p>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 3.9 — Riepilogo -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 3 · Prompting</span>
      <h2>Riepilogo Ora 3</h2>
    </div>
    <div class="slide-body layout-list">
      <ul>
        <li>Un buon prompt definisce ruolo, contesto, istruzione, formato e — quando serve — esempi</li>
        <li>MCP standardizza come un modello si collega a strumenti e dati esterni</li>
        <li>Le skill aziendali trasformano un processo individuale in uno standard condiviso dal team</li>
      </ul>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>
```

- [ ] **Step 2: Verify slide count and no leftover placeholder**

```bash
grep -c 'ORA3_CONTENT_PLACEHOLDER' "slides/20260710_intro_AI_hup/index.html"
```

Expected: `0`.

```bash
awk '/data-section-title="Ora 3/,/data-section-title="Ora 4/' "slides/20260710_intro_AI_hup/index.html" | grep -c 'class="slide"'
```

Expected: `9`.

- [ ] **Step 3: Visual check**

```bash
open "slides/20260710_intro_AI_hup/index.html"
```

Navigate to the Ora 3 section: confirm the before/after prompt example (`.warning`/`.success` blocks) is readable, the placeholder "Skill aziendali Hup" slide is clearly marked as such, no tourism examples remain.

- [ ] **Step 4: Commit**

```bash
git add slides/20260710_intro_AI_hup/index.html
git commit -m "$(cat <<'EOF'
Add Ora 3 content: Prompting, MCP e Skill Aziendali

Condense prompt engineering technique/example/pitfalls, MCP concept
and example, and skill-aziendali framing with an explicit placeholder
slide for real Hup skill examples.
EOF
)"
```

---

## Task 5: Ora 4 placeholder, Chiusura, Glossario appendix, and final QA

**Files:**
- Modify: `slides/20260710_intro_AI_hup/index.html` (insert content at the `<!-- ORA4_CONTENT_PLACEHOLDER -->`, `<!-- CHIUSURA_CONTENT_PLACEHOLDER -->`, and `<!-- GLOSSARIO_CONTENT_PLACEHOLDER -->` markers, then remove all three marker comments)

**Interfaces:**
- Consumes: same layout classes as Task 2, plus `.slide-closing` established in Task 1.

- [ ] **Step 1: Write the Ora 4 placeholder slide**

Replace the line `<!-- ORA4_CONTENT_PLACEHOLDER: Task 5 inserts slides here -->` with:

```html
  <!-- 4.1 — Use case (placeholder) -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Ora 4 · Use Case</span>
      <h2>Use case — da definire</h2>
    </div>
    <div class="slide-body layout-list">
      <div class="callout">
        Questa sezione è un segnaposto: verrà completata con i casi d'uso pratici scelti per il nostro contesto di lavoro.
      </div>
      <p class="text-muted text-small">Per ogni use case: scenario di partenza · strumento/approccio usato (prompting, RAG, agente, skill) · risultato ottenuto.</p>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>
```

- [ ] **Step 2: Write the Chiusura slides**

Replace the line `<!-- CHIUSURA_CONTENT_PLACEHOLDER: Task 5 inserts slides here -->` with:

```html
  <!-- 5.1 — Riepilogo finale -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Chiusura</span>
      <h2>Riepilogo della sessione</h2>
    </div>
    <div class="slide-body layout-two-col">
      <div>
        <h3>Concetti e Claude</h3>
        <ul>
          <li>Come funziona un LLM e quando usare prompting, RAG o fine-tuning</li>
          <li>Agenti, tool calling e MCP</li>
          <li>I 4 livelli della guida Claude 101</li>
        </ul>
      </div>
      <div>
        <h3>Prompting e pratica</h3>
        <ul>
          <li>Anatomia di un prompt efficace e tecniche few-shot/CoT</li>
          <li>Come MCP e le skill aziendali automatizzano processi ricorrenti</li>
          <li>I nostri use case (Ora 4)</li>
        </ul>
      </div>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>

  <!-- 5.2 — Domande -->
  <section class="slide-closing">
    <h2>Domande?</h2>
    <p>Grazie per l'attenzione.</p>
  </section>
```

- [ ] **Step 3: Write the Glossario slide**

Replace the line `<!-- GLOSSARIO_CONTENT_PLACEHOLDER: Task 5 inserts slides here -->` with:

```html
  <!-- 6.1 — Glossario -->
  <section class="slide">
    <div class="slide-header">
      <span class="slide-section-label">Appendice</span>
      <h2>Abbreviazioni e termini chiave</h2>
    </div>
    <div class="slide-body layout-table">
      <table class="table-keyed table-compact">
        <tr><th>Termine</th><th>Significato</th></tr>
        <tr><td><strong>LLM</strong></td><td>Large Language Model — modello addestrato a predire testo</td></tr>
        <tr><td><strong>Token</strong></td><td>Unità minima di testo elaborata dal modello (parola o frammento)</td></tr>
        <tr><td><strong>Context window</strong></td><td>Quantità massima di token che il modello può considerare in una richiesta</td></tr>
        <tr><td><strong>Fine-tuning</strong></td><td>Riaddestramento del modello su esempi specifici</td></tr>
        <tr><td><strong>RAG</strong></td><td>Retrieval Augmented Generation — recupero di documenti rilevanti inseriti nel prompt</td></tr>
        <tr><td><strong>Embedding</strong></td><td>Rappresentazione numerica del significato di un testo</td></tr>
        <tr><td><strong>Agente</strong></td><td>Sistema che pianifica ed esegue autonomamente una sequenza di azioni</td></tr>
        <tr><td><strong>MCP</strong></td><td>Model Context Protocol — standard aperto per collegare modelli a strumenti esterni</td></tr>
        <tr><td><strong>Function calling</strong></td><td>Meccanismo con cui un modello richiede l'esecuzione di una funzione esterna</td></tr>
        <tr><td><strong>Prompt engineering</strong></td><td>Disciplina di scrittura di istruzioni efficaci per un modello</td></tr>
        <tr><td><strong>Skill</strong></td><td>Istruzioni Claude riutilizzabili, attivate automaticamente in base al task</td></tr>
      </table>
    </div>
    <div class="slide-footer">
      <img class="footer-logo" alt="Hup.">
      <span class="footer-page"></span>
    </div>
  </section>
```

- [ ] **Step 4: Verify no placeholders remain anywhere in the file**

```bash
grep -n 'PLACEHOLDER\|TBD\|da completare con esempi' "slides/20260710_intro_AI_hup/index.html"
```

Expected: only the two intentional, user-approved content placeholders remain as visible slide copy — `Skill aziendali Hup — da completare` (Ora 3) and `Use case — da definire` (Ora 4). No `<!-- ..._PLACEHOLDER -->` HTML comments should remain.

- [ ] **Step 5: Full-file structural check**

```bash
grep -c 'class="slide"' "slides/20260710_intro_AI_hup/index.html"
grep -c 'class="slide-section"' "slides/20260710_intro_AI_hup/index.html"
grep -c 'class="slide-cover"' "slides/20260710_intro_AI_hup/index.html"
grep -c 'class="slide-closing"' "slides/20260710_intro_AI_hup/index.html"
grep -n "Digitiamo\|indigo" "slides/20260710_intro_AI_hup/index.html"
```

Expected: `class="slide"` count = 1 (Apertura obiettivi) + 1 (agenda) + 8 (Ora1) + 9 (Ora2) + 9 (Ora3) + 1 (Ora4) + 1 (Chiusura riepilogo) + 1 (Glossario) = 31; `class="slide-section"` = 4 (Ora1-4 dividers); `class="slide-cover"` = 1; `class="slide-closing"` = 1; the Digitiamo/indigo grep returns no output (comments mentioning "indigo" as a color name may remain in unrelated CSS comments — if so, confirm they're harmless leftover comments, not actual applied colors, and remove the stale comment text for cleanliness).

- [ ] **Step 6: Full visual walkthrough**

```bash
open "slides/20260710_intro_AI_hup/index.html"
```

Page through the entire deck start to finish (arrow keys or the overview mode) and confirm: consistent Hup branding throughout (no indigo/purple remnants), no overflowing text or broken layouts, both placeholder slides read clearly as intentional placeholders, the Glossario appendix is reachable after Chiusura, footer page numbers count correctly across all ~32 slides.

- [ ] **Step 7: Commit**

```bash
git add slides/20260710_intro_AI_hup/index.html
git commit -m "$(cat <<'EOF'
Add Ora 4 placeholder, Chiusura, and Glossario appendix

Complete the deck skeleton with a clearly marked use-case placeholder,
closing/recap slides, and a condensed glossary appendix.
EOF
)"
```

---

## Self-Review Notes

- **Spec coverage:** Rebranding (Task 1) ✓, Ora 1 (Task 2) ✓, Ora 2 claude101 content incl. deep-dives (Task 3) ✓, Ora 3 prompting/MCP/skill placeholder (Task 4) ✓, Ora 4 placeholder + appendix glossario (Task 5) ✓. Quiz slides, `Strumenti AI: guida pratica`, `Identificare Opportunità`, `Sicurezza e Privacy`, `Filo Conduttore` are all omitted by construction (Task 1 Step 14-15 replace/delete their source ranges instead of copying them forward).
- **Placeholder scan:** The only "placeholder"-flavored content left in the rendered deck is the two intentional, user-approved segnaposto slides (Skill aziendali Hup, Use case). All `<!-- ..._PLACEHOLDER -->` HTML comments are removed by Tasks 2-5 as each is filled, and Task 5 Step 4 verifies this.
- **Type/interface consistency:** All tasks reuse the exact same CSS class vocabulary confirmed present in the source deck (`slide`, `slide-header`, `slide-section-label`, `slide-body layout-list/two-col/three-col/table/diagram/image-text/code`, `card`, `callout`, `warning`, `success`, `table-keyed`, `slide-footer`, `footer-logo`, `footer-page`, `slide-section`, `slide-closing`, `section-eyebrow`, `section-desc`) — no new classes are invented, so no new CSS is needed beyond Task 1's token remap and the one `.schedule-tbl`/`.sched-row` block already scoped inside the agenda section.
