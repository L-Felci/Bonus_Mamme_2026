# 👩‍👧‍👦 Chatbot & Simulatore "Nuovo Bonus Mamme 2026"

Applicazione web sviluppata in Python con **Streamlit** per la simulazione dell'idoneità, il calcolo dell'importo e la risposta rapida alle domande sul **Nuovo Bonus Mamme 2026** (Art. 1, c. 207, L. 199/2025; Circolare INPS n. 106/2026; Messaggio INPS n. 3343/2026).

---

## 🚀 Caratteristiche dell'Applicazione

1. **🧮 Simulatore & Calcolatore d'Importo**:
   - Verifica automatica dei requisiti (categoria lavorativa, tipo di contratto, numero e età dei figli, limite reddituale di 40.000 €).
   - Calcolo delle mensilità spettanti (60 €/mese, fino a 720 € totali).
   - Gestione delle casistiche speciali (es. cessazione contratto ad agosto, lavoratrici autonome, 3 figli a tempo indeterminato e decontribuzione IVS, lavoro domestico).

2. **💬 Chatbot Risposte Veloci**:
   - Motore di ricerca Q&A istantaneo basato su una **Knowledge Base** chiusa derivata dalle fonti ufficiali INPS ed Eutekne.
   - Pulsanti di richiesta rapida sulle domande più diffuse.

3. **📋 Guida alla Domanda INPS**:
   - Percorso di navigazione dettagliato sul portale INPS.
   - Scadenze (31 dicembre 2026 / 31 gennaio 2027) e modalità di erogazione (unica soluzione a Dicembre 2026).

---

## 💻 Come pubblicare su GitHub e Streamlit Cloud (Gratis)

### Passo 1: Crea un Repository su GitHub
1. Accedi al tuo account GitHub (o registrati gratuitamente).
2. Clicca su **Nuovo Repository** (New Repository).
3. Assegna un nome al repository (es. `bonus-mamme-2026`).
4. Seleziona **Public** e clicca su **Create repository**.

### Passo 2: Carica i File
Carica nel repository GitHub i seguenti file presi da questo pacchetto:
- `app.py`
- `knowledge_base.json`
- `requirements.txt`
- `README.md`

### Passo 3: Deploy su Streamlit Cloud
1. Vai sul portale Streamlit Community Cloud (share.streamlit.io) e fai il login con il tuo account GitHub.
2. Clicca su **New app**.
3. Seleziona il tuo repository `bonus-mamme-2026`, il branch `main` e specifica come file principale: `app.py`.
4. Clicca su **Deploy!**

Nel giro di 1-2 minuti l'applicazione sarà live con un link pubblico condivisibile con chiunque!

---

## 📖 Fonti Normative
- **Legge 30 dicembre 2025, n. 199** (Legge di Bilancio 2026), art. 1 comma 207.
- **Circolare INPS n. 106 del 16/10/2026**.
- **Messaggio INPS n. 3343 del 20/10/2026**.
- **Guide e Schede di Aggiornamento Eutekne 2026**.
