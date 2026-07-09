# Design: Ricostruzione Ora 2 — Introduzione a Claude (Hup deck)

## Contesto

Il deck `slides/20260710_intro_AI_hup/index.html` (branch `feat/intro-ai-hup`) contiene
un'Ora 2 (9 slide) che riassume la guida claude101.com solo a livello di titoli di
pagina, senza entrarne nei contenuti. L'utente ha chiesto di ricostruire la sezione in
modo che, per ogni pagina di ogni livello della guida, vengano estratti i concetti
principali come punti elenco e, dove sensato, venga proposto un esercizio pratico
basato sui passi già descritti dalla guida stessa.

Il contenuto di tutte le 18 pagine (4 livelli: Beginner/Intermediate/Advanced/Expert)
è stato estratto direttamente da claude101.com/ruben.substack.com durante la fase di
design (vedi sezione "Contenuti dettagliati" — è la fonte fattuale per l'implementazione,
non va ri-scaricato).

## Vincoli

- Riusa lo stile visivo esistente (`layout-list`, `layout-two-col`, `layout-three-col`,
  `.card`, `.callout`, `.diagram`) — nessun nuovo pattern CSS, coerente con il vincolo
  già applicato all'espansione di Ora 1.
- Tutti gli esempi restano generalizzati per contesto aziendale — le pagine della guida
  a taglio personal-brand (voce personale, "Claude replaced me", "Stop sounding like AI")
  vanno riformulate per un pubblico aziendale (comunicazioni di team/cliente, non blog o
  newsletter personali).
- Branding Hup (token colore, font, logo) già applicato — nessun colore hardcoded.
- Sostituisce interamente l'attuale sezione Ora 2 (righe ~1911-2159 dell'index.html
  attuale, dal divider `slide-section` alla chiusura `</section>` prima di Ora 3). Non
  toccare Ora 1, Ora 3, Ora 4, Chiusura, Glossario.
- L'utente ha accettato che Ora 2 superi il budget nominale di 60 minuti (stima
  realistica ~90-100 minuti con i 4 esercizi dal vivo) — lo schedule complessivo della
  giornata andrà aggiustato separatamente, fuori scope per questo design.
- 4 esercizi pratici dal vivo, uno per livello, scelti tra le pagine con il setup più
  ricco e realizzabile in aula (niente account aziendali reali connessi in diretta,
  niente setup multi-servizio a pagamento come Claude Code+Netlify+Supabase).

## Struttura risultante (9 → 28 slide)

| # | Slide | Stato |
|---|-------|-------|
| 2.1 | Claude 101: una guida a 4 livelli (overview) | modificata — testo aggiornato per riflettere la nuova profondità |
| 2.2 | Livello 1 — cosa vedremo (roadmap) | nuova |
| 2.3 | Claude For Dummies (concetti) | nuova |
| 2.4 | Esercizio pratico — Riscrivi nel tuo stile | nuova (esercizio flagship L1) |
| 2.5 | Be good at Claude is (stupidly) simple (concetti) | nuova |
| 2.6 | Claude Certified (concetti) | nuova |
| 2.7 | Livello 2 — cosa vedremo (roadmap) | nuova |
| 2.8 | Claude Cowork (concetti) | modificata — sostituisce l'attuale "Zoom Cowork" |
| 2.9 | Esercizio pratico — Configura il tuo Cowork | nuova (esercizio flagship L2) |
| 2.10 | Claude for teams (concetti) | nuova |
| 2.11 | Claude Design (concetti) | nuova |
| 2.12 | Claude Cowork + Projects (concetti) | modificata — sostituisce l'attuale "Zoom Projects" |
| 2.13 | Claude for slides (concetti) | nuova |
| 2.14 | Claude Skills (concetti) | modificata — sostituisce l'attuale "Zoom Skills" |
| 2.15 | Livello 3 — cosa vedremo (roadmap) | nuova |
| 2.16 | Claude to sound like you (concetti) | nuova |
| 2.17 | Stop hitting Claude limits (concetti) | nuova |
| 2.18 | Stop Prompting (concetti) | nuova |
| 2.19 | Claude replaced me (concetti) | nuova |
| 2.20 | Stop sounding like AI (concetti) | nuova |
| 2.21 | Esercizio pratico — Verifica il tuo testo | nuova (esercizio flagship L3) |
| 2.22 | Excel with Claude cowork (concetti) | nuova |
| 2.23 | Livello 4 — cosa vedremo (roadmap) | nuova |
| 2.24 | Claude Connectors (concetti) | nuova |
| 2.25 | Claude Code (concetti) | nuova |
| 2.26 | Stop using your own Claude at work (concetti) | nuova |
| 2.27 | Esercizio pratico — Metti in sicurezza il tuo account | nuova (esercizio flagship L4) |
| 2.28 | Riepilogo Ora 2 | modificata — bullet aggiornati |

Ogni slide "concetti" usa l'header `<span class="slide-section-label">Ora 2 · Claude</span>`
esistente. Le slide "roadmap" e "esercizio pratico" seguono lo stesso pattern header/footer.

## Contenuti dettagliati per slide

### 2.1 — Overview (modificata)
`layout-list`, stesso impianto attuale, testo introduttivo aggiornato per menzionare
che copriremo tutte le 18 pagine con 4 esercizi pratici dal vivo, uno per livello.

### 2.2 — Livello 1: cosa vedremo (roadmap)
`layout-list` compatta: elenco delle 3 pagine (Claude For Dummies, Be good at Claude is
(stupidly) simple, Claude Certified) con durata di lettura originale (5, 5, 4 min).

### 2.3 — Claude For Dummies (concetti)
`layout-two-col`:
- Claude è l'assistente AI di Anthropic: tre concetti chiave — completamento automatico
  su scala sovrumana, tendenza ad assecondarti ("sycophancy"), token (unità di testo che
  limitano la lunghezza di una conversazione)
- Tre modalità: Chat (conversazione), Desktop (accesso ai file locali), Cowork
  (esecuzione autonoma di task lunghi)
- Piani: Free (limitato), Pro 20$/mese, Max 100-200$/mese per uso intensivo
- Cinque regole per prompt efficaci: sii specifico, fornisci esempi, dì cosa fare (non
  cosa evitare), parti breve e itera, apri una nuova chat se il modello si confonde

Callout: "I tre concetti da conoscere per iniziare — Token, Cowork, Claude Code — li
ritroveremo per tutta la sessione."

### 2.4 — Esercizio pratico: Riscrivi nel tuo stile (flagship L1)
`layout-list` con box passi numerati (stesso pattern `.callout` step-list):
1. Accedi a claude.ai con un account gratuito
2. Incolla un tuo testo reale (email, comunicazione interna, breve report)
3. Chiedi a Claude di riscriverlo mantenendo il tuo stile ma migliorando chiarezza e tono
4. Confronta il risultato con l'originale: cosa ha cambiato? Cosa avresti fatto diversamente?

Callout: "Obiettivo: capire come Claude interpreta 'il tuo stile' da un solo esempio,
prima ancora di configurare nulla. ~8 minuti."

### 2.5 — Be good at Claude is (stupidly) simple (concetti)
`layout-list`:
- Usa Opus (a pagamento) invece di Sonnet gratuito quando possibile; attiva "Thinking"
  su High per task complessi
- Tecnica AskUserQuestion: istruisci Claude a farti domande di chiarimento prima di
  eseguire, invece di scrivere il prompt perfetto
- Gli strumenti di dettatura vocale permettono di parlare a Claude fino a 4 volte più
  veloce che scrivere
- Cowork crea file reali (PDF, fogli di calcolo) salvati su disco, senza copia-incolla
- I Connector integrano email, calendario, trascrizioni di riunioni per dare contesto
- Il comando `/skill-creator` costruisce skill personalizzate passo passo

Callout: "Non serve scrivere prompt perfetti — basta far fare a Claude le domande giuste."

### 2.6 — Claude Certified (concetti)
`layout-two-col`:
- Esistono solo tre certificazioni gratuite legittime, erogate da Anthropic; altre
  "certificazioni" a pagamento online non sono ufficiali
- Nel 2024 il 78% delle organizzazioni ha usato l'AI (era il 55% nel 2023)
- Chi ha competenze AI ottiene in media un premio salariale del 56% (era il 25% l'anno
  precedente)
- Percorso: "Claude 101" (1h) → "AI Fluency" (3h, framework delle 4D: Delegation,
  Description, Discernment, Diligence) → "Introduction to Claude Cowork" (2h)

Callout: "Percorso gratuito di ~6 ore, aggiungibile a LinkedIn come certificazione
Anthropic — attività consigliata dopo la sessione, non fattibile in aula."

### 2.7 — Livello 2: cosa vedremo (roadmap)
`layout-list` compatta: elenco delle 6 pagine con durata di lettura (Cowork 18min,
for teams 11min, Design 9min, Cowork+Projects 10min, for slides 7min, Skills 6min).

### 2.8 — Claude Cowork (concetti, modificata)
`layout-two-col` (sostituisce l'attuale "Zoom — Claude Cowork" 2.6, contenuto invariato
nella sostanza, spostato qui come slide di concetti pura — l'esercizio si sposta sulla
slide successiva dedicata):
- Architettura a cartelle: ABOUT ME (identità), OUTPUTS (deliverable), TEMPLATES
  (strutture riutilizzabili) — ABOUT ME viene letto prima di ogni sessione
- Tre file in ABOUT ME: `about-me.md` (<2.000 token), `anti-ai-writing-style.md` (80+
  parole "da AI" da evitare), `my-company.md` (<1.000 token)
- Economia dei token: il messaggio 30 costa ~31 volte il messaggio 1 — riparti da una
  nuova chat dopo ~20 messaggi
- Modelli: Sonnet/Haiku per task semplici, Opus + Extended Thinking per lavoro complesso

Callout: "Mantieni ABOUT ME sotto i 6.000 token totali — più contesto non è sempre
meglio (lo avevamo già visto in Ora 1)."

### 2.9 — Esercizio pratico: Configura il tuo Cowork (flagship L2)
`layout-list` con box passi numerati:
1. Apri l'app desktop di Claude e crea una cartella "Claude Cowork" con tre
   sottocartelle: ABOUT ME, OUTPUTS, TEMPLATES
2. Scrivi un `about-me.md` essenziale: 5-6 righe su ruolo, stile di lavoro, priorità
3. Imposta le Istruzioni Globali (Impostazioni → Cowork) perché legga sempre quella
   cartella
4. Fai una prima richiesta reale: "Leggi la cartella e riassumi cosa sai di me"

Callout: "Bastano poche righe ben scritte — la qualità del file conta più della
lunghezza. ~10 minuti."

### 2.10 — Claude for teams (concetti)
`layout-two-col`:
- Piano Team: minimo 5 posti (fino a 150), livello Premium consigliato per uso
  quotidiano
- Architettura a Project: 3-5 Project per tipo di deliverable ricorrente, ognuno con
  istruzioni e documenti mirati — "le proposte commerciali non hanno bisogno delle
  linee guida di brand"
- Strategia di adozione: converti prima un collega oberato di lavoro, poi usa il suo
  entusiasmo per il rollout
- Prompt template a una frase, un solo campo di input, pronti da copiare per i colleghi
- Sicurezza: Claude non si addestra sui dati del team, a nessun livello di piano

Callout: "Percorso di adozione in 5 giorni: setup Project → template pronti → demo
prima/dopo → conversione di un singolo utente → rollout team. Non eseguibile in aula,
ma riutilizzabile come piano concreto."

### 2.11 — Claude Design (concetti)
`layout-two-col`:
- Prodotto separato su claude.ai/design, richiede piano Pro/Max o abilitazione admin
  per Team/Enterprise
- Tre formati di output: siti ad alta fedeltà, presentazioni (con note del relatore),
  video animati
- Il consumo di token è molto rapido — richiede monitoraggio attento
- Un file DESIGN.md (linee guida di brand estratte) permette a Claude di applicare uno
  stile coerente senza doverlo rispecificare ogni volta
- Workflow avanzato: post/brief → ricerca → video animato → deck di slide, spesso con
  risultati migliori della generazione diretta del deck

Callout: "La scelta finale tra le varianti generate resta una decisione umana, non
automatizzabile."

### 2.12 — Claude Cowork + Projects (concetti, modificata)
`layout-two-col` (sostituisce l'attuale "Zoom — Claude Cowork Projects" 2.7, contenuto
sostanzialmente invariato):
- Combina memoria persistente e ambito ristretto con esecuzione agentica, integrato
  nell'app desktop
- Tre modalità di creazione: da zero, da un Project esistente, o da una cartella locale
- La memoria isolata per Project evita che il contesto di un progetto contamini un altro
- I task pianificati automatizzano attività ricorrenti quando l'app desktop è attiva
- Limite: i Project Cowork sono locali alla macchina — non ancora condivisibili in team

Callout: "Quattro casi d'uso tipici: newsletter, deliverable per clienti, proposte
commerciali, report operativi ricorrenti."

### 2.13 — Claude for slides (concetti)
`layout-two-col`:
- Tre metodi di generazione slide a confronto: Claude da solo (design piatto), uno
  strumento di design esterno (output rifinito, immagini AI, analytics), i due
  combinati (consigliato per deck importanti)
- Standardizzazione del brand aziendale tramite un tema condiviso + un file
  `brand-deck-rules.md`
- Pipeline "ricerca → brief": Claude fa la ricerca web, produce un brief strutturato,
  poi un outline slide-per-slide

Callout: "La generazione diretta di slide senza ricerca/outline preliminare produce
quasi sempre risultati generici — vale anche per le slide di questa stessa sessione."

### 2.14 — Claude Skills (concetti, modificata)
`layout-two-col` (sostituisce l'attuale "Zoom — Claude Skills" 2.8, contenuto
sostanzialmente invariato):
- Le Skill sono istruzioni persistenti attivate da comandi slash, si attivano da sole
  quando Claude riconosce il task giusto
- Si costruiscono con lo Skill Creator integrato (intervista guidata) oppure con
  strumenti esterni di generazione rapida
- Esempio di efficienza: un task che richiedeva 12.000 token e 15 scambi è sceso a
  6.000 token e 2 scambi grazie a una skill
- Formato aperto e portabile (file .md): funziona anche su altri assistenti AI
- Il "quando NON usarla" conta più del "quando usarla" — evita attivazioni indesiderate

Callout: "Anche con una skill ben scritta, prevedi comunque una revisione umana del
~20% dell'output."

### 2.15 — Livello 3: cosa vedremo (roadmap)
`layout-list` compatta: elenco delle 6 pagine con durata (to sound like you 12min, Stop
hitting limits 12min, Stop Prompting 10min, replaced me 4min, Stop sounding like AI
20min, Excel 7min).

### 2.16 — Claude to sound like you (concetti)
`layout-two-col`, riformulata per voce di team/azienda invece che personal-brand:
- Lo stile di scrittura di un team (scelte lessicali, tono, struttura) può essere
  catturato in un file di testo e riutilizzato in ogni conversazione
- Processo di estrazione: intervista guidata (100 domande) su tono, regole di
  scrittura, esempi da imitare/evitare
- Il risultato viene compresso da decine di migliaia di parole a un file di
  2.000-5.000 token — solo le istruzioni ad alto segnale restano
- Il file va salvato nella cartella Cowork per essere caricato automaticamente ad ogni
  sessione, ed è un documento vivo da aggiornare nel tempo

Callout: "Pensala come alla guida di stile del tuo team, applicata automaticamente da
Claude a ogni comunicazione."

### 2.17 — Stop hitting Claude limits (concetti)
`layout-two-col`:
- Ogni messaggio rilegge l'intera cronologia della conversazione — i messaggi
  successivi costano esponenzialmente di più
- Conversione dei file: un PDF costa 1.500-3.000 token a pagina, uno screenshot
  ~1.300 — convertire in testo semplice riduce i costi
- Abbinamento prodotto-task: Chat+modello leggero per domande rapide, Cowork+Opus per
  report su file, Code+Sonnet per task sui dati
- Le conversazioni lunghe diventano "fornaci di token" (il 98,5% della spesa va a
  rileggere la cronologia) — riparti dopo 15-20 messaggi
- "Modifica invece di rispondere": usa Edit su un messaggio precedente e rigenera,
  invece di accumulare follow-up

Callout: "Disattiva ricerca web/connector/extended thinking quando non servono — sono
le prime voci di spreco di token."

### 2.18 — Stop Prompting (concetti)
`layout-two-col`:
- I prompt "usa e getta" producono risultati generici perché mancano di contesto su
  stile, pubblico, obiettivi
- Cowork collega Claude a una cartella locale di file di istruzioni in markdown, letti
  automaticamente ad ogni sessione
- Un editor di note esterno (gratuito) permette di modificare facilmente quella stessa
  cartella
- Le Skill trasformano workflow ricorrenti in comandi riutilizzabili

Callout: "Il salto di qualità non è 'un prompt migliore', ma smettere di ripartire da
zero ogni volta."

### 2.19 — Claude replaced me (concetti)
`layout-list`, riformulata da "sostituire un autore di newsletter" a "trasformare
competenza ripetuta in una skill di team":
- L'autore ha creato una skill che automatizza una guida che prima scriveva a mano ogni
  settimana per i suoi lettori
- Il valore umano si sposta su "la parte difficile": risolvere eccezioni, testare
  iterazioni, accompagnare le persone nel cambiamento
- Modello consigliato per skill complesse: un modello di fascia alta con "effort" alto

Callout (riformulata, business-generica): "La stessa logica vale per qualunque processo
che spieghi spesso ai colleghi — può diventare una skill condivisa, non solo un
documento che nessuno legge."

### 2.20 — Stop sounding like AI (concetti)
`layout-two-col`, riformulata su comunicazioni aziendali invece che contenuti social:
- Il pattern "non è X, è Y" appare 4 volte più spesso nei documenti aziendali recenti —
  è un segnale riconoscibile di testo generato da AI
- Lista di 100+ parole da evitare ("sfruttare", "sinergia", "senza soluzione di
  continuità", ...)
- Oltre 15 pattern strutturali da evitare, non solo di vocabolario
- La specificità batte la levigatezza: sostituire affermazioni vaghe con dettagli
  concreti
- Un file di stile "anti-AI" letto da Claude prima di ogni task, invece di ripetere le
  istruzioni ogni volta

Callout: "Rivedi periodicamente le tue ultime bozze e aggiorna la lista di pattern da
evitare — i 'tell' dell'AI cambiano nel tempo."

### 2.21 — Esercizio pratico: Verifica il tuo testo (flagship L3)
`layout-list` con box passi numerati:
1. Crea un file di stile "anti-AI" con la lista di parole/pattern da evitare (fornito
   durante la sessione)
2. Prendi un tuo testo aziendale reale (email, comunicazione, report breve)
3. Chiedi a Claude: "Verifica questo testo usando il file di stile anti-AI: quali
   pattern trovi?"
4. Rivedi insieme le correzioni proposte

Callout: "L'obiettivo non è eliminare ogni traccia di AI, ma riconoscere i pattern che
rendono un testo generico e sostituirli con dettagli concreti. ~8-10 minuti."

### 2.22 — Excel with Claude cowork (concetti)
`layout-two-col`:
- Cowork è risultato il miglior strumento per costruire fogli di calcolo da zero,
  testato contro altri 10 strumenti AI
- Workflow a 3 strumenti: Cowork (creazione) → foglio condiviso (condivisione/
  archiviazione) → editor esterno (modifica avanzata)
- Struttura del prompt: scopo, fogli necessari, specifiche di formattazione, e "le
  10 assunzioni principali da verificare" prima di procedere
- Richiede piano Pro per l'app desktop; un connector cloud storage semplifica il
  trasferimento

Callout: "Chiedi sempre a Claude di elencare le sue assunzioni prima di generare il
foglio — evita errori silenziosi su formule e numeri."

### 2.23 — Livello 4: cosa vedremo (roadmap)
`layout-list` compatta: elenco delle 3 pagine con durata (Connectors 8min, Claude Code
14min, Stop using your own Claude at work 9min).

### 2.24 — Claude Connectors (concetti)
`layout-two-col`:
- Oltre 200 connector disponibili (email, messaggistica, CRM, note riunioni, cloud
  storage)
- Per efficienza di token, tieni i connector disattivati di default — attivali solo per
  la chat che ne ha bisogno
- Tre connector fondamentali consigliati per iniziare: note riunioni, email,
  messaggistica di team
- Approccio consigliato: prima settimana in sola lettura, poi eventualmente accesso in
  scrittura
- Disattiva i connector durante il lavoro creativo/di bozza per evitare rumore di
  contesto

Callout: "I connector personalizzati permettono di collegare sistemi interni via
standard aperti — accenno, sviluppo completo fuori scope per questa sessione."

### 2.25 — Claude Code (concetti)
`layout-two-col`, riformulata per audience non tecnica:
- "Vibecoding": costruire app/siti descrivendo i requisiti in linguaggio naturale,
  senza saper programmare
- Due casi d'uso principali: mockup cliccabili per briefare sviluppatori/designer,
  strumenti interni su misura dove piccole imperfezioni sono accettabili
- Non è una scorciatoia imprenditoriale: il valore è l'efficienza, non sostituire un
  team di sviluppo
- Richiede piano Pro, una cartella dedicata, modalità permessi avanzata, un modello di
  fascia alta
- Il passaggio a sviluppatori professionisti avviene tramite un documento di consegna
  (stack usato, funzionalità pronte, punti da rifinire)

Callout: "Sapere quando NON usare Claude Code è importante quanto sapere come usarlo —
per un singolo componente, un documento o un foglio di calcolo, gli strumenti visti in
questa Ora 2 sono più adatti."

### 2.26 — Stop using your own Claude at work (concetti)
`layout-two-col`:
- Gli account AI personali si addestrano di default sulle conversazioni — va
  disattivato manualmente
- Rischi legali concreti: violazioni di NDA, segreti industriali, normativa privacy
  (GDPR in Europa)
- Caso reale noto: ingegneri disciplinati dopo aver condiviso codice sorgente sensibile
  con un assistente AI personale nel giro di pochi giorni
- La ricerca mostra che la maggioranza dei lavoratori usa chatbot personali per il
  lavoro senza approvazione IT, e molti hanno incollato informazioni sensibili almeno
  una volta
- Rischio "combinazione letale": account AI personale collegato via connector a email/
  drive/messaggistica aziendali
- Contenuti da non condividere mai: codice sorgente, dati clienti, roadmap non
  pubbliche, dati finanziari non pubblici, materiale coperto da NDA, credenziali

Callout: "La soluzione non è smettere di usare l'AI, ma separare nettamente uso
personale e uso aziendale, con governance esplicita."

### 2.27 — Esercizio pratico: Metti in sicurezza il tuo account (flagship L4)
`layout-list` con box passi numerati:
1. Vai su Impostazioni → Privacy e disattiva "Aiuta a migliorare i nostri modelli AI"
2. Verifica la stessa impostazione su qualsiasi altro assistente AI personale che usi
3. Prova una chat "Incognito/Temporanea" per un'informazione che non vuoi salvata
4. Rivedi quali connector hai collegato e disconnetti quelli che non usi più

Callout: "Due minuti di impostazioni possono evitare un incidente di sicurezza — è il
primo passo di adozione responsabile dell'AI in azienda. ~5 minuti."

### 2.28 — Riepilogo Ora 2 (modificata)
`layout-list`, bullet aggiornati:
- claude101.com copre 4 livelli e 18 articoli, da primo utilizzo ad adozione aziendale
  avanzata
- Cowork porta Claude a lavorare direttamente sui tuoi file locali, con contesto
  persistente; i Project isolano memoria e istruzioni per ogni area di lavoro
- Le Skill automatizzano processi ricorrenti — le vediamo applicate in azienda nell'Ora 3
- Abbiamo messo in pratica 4 esercizi dal vivo: riscrittura nel tuo stile, setup
  Cowork, verifica anti-AI di un testo, messa in sicurezza dell'account

## Fuori scope

- Nessuna modifica a Ora 1, Ora 3, Ora 4, Chiusura, Glossario.
- Nessun aggiustamento dello schedule complessivo della sessione (la Ora 2 più lunga
  richiederà una revisione dei tempi altrove, ma è un'attività separata).
- Nessun esercizio dal vivo su Claude Code, Connectors o Excel/Cowork — richiedono
  piani a pagamento, servizi esterni multipli o connessione di account aziendali reali,
  non adatti a un esercizio in aula in tempi brevi.
- Nessun nuovo asset immagine o pattern CSS.
