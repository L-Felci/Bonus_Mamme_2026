# 👩‍👧‍👦 Chatbot & Simulatore "Nuovo Bonus Mamme 2026" (v2.0)

Applicazione web sviluppata in **Python** con **Streamlit** per la divulgazione e l'assistenza sui requisiti, sul calcolo dell'importo e sulle modalità di presentazione della domanda per il **Nuovo Bonus Mamme 2026** (Circolare INPS n. 106/2026 e Messaggio INPS n. 3343/2026).

---

## 📁 Struttura del Repository

* `app.py`: Codice principale dell'applicazione Streamlit (versione 2.0 con motore di ricerca e simulatore esteso).
* `knowledge_base.json`: Banca dati JSON con 20 categorie di FAQ ufficiali INPS e normativa aggiornata.
* `requirements.txt`: Dipendenze Python necessarie (`streamlit`, `pandas`).
* `README.md`: Guida alla configurazione e alla pubblicazione online.

---

## 🚀 Guida alla Pubblicazione su Streamlit Cloud

1. **Crea un repository su GitHub**:
   * Vai su [GitHub.com](https://github.com) e crea un nuovo repository pubblico (es. `bonus-mamme-2026`).
   * Carica i file `app.py`, `knowledge_base.json`, `requirements.txt` e `README.md`.

2. **Connetti a Streamlit Cloud**:
   * Accedi a [share.streamlit.io](https://share.streamlit.io) con il tuo account GitHub.
   * Clicca su **"Create app"** > **"Yep, I have an app"**.
   * Seleziona il repository `bonus-mamme-2026`, ramo `main` e `Main file path` impostato su `app.py`.
   * Clicca su **"Deploy!"**.

3. **Verifica e Condivisione**:
   * L'applicazione sarà online entro 1-2 minuti all'URL dedicato `https://<tuo-nome-repo>.streamlit.app`.
