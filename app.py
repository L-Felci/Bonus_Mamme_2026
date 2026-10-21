import streamlit as st
import json
import os
import re
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Chatbot & Simulatore Nuovo Bonus Mamme 2026",
    page_icon="👩‍👧‍👦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #00529B 0%, #0073E6 100%);
        color: white;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .main-header h1 {
        color: white !important;
        margin: 0 0 8px 0;
        font-size: 2.2rem;
    }
    .main-header p {
        color: #E6F0FA !important;
        margin: 0;
        font-size: 1.05rem;
    }
    .badge-inps {
        background-color: #E1F0FF;
        color: #00529B;
        padding: 4px 12px;
        border-radius: 16px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
        margin-right: 8px;
    }
    .card-result {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 5px solid #00529B;
        padding: 20px;
        border-radius: 8px;
        margin-top: 16px;
    }
    .card-success {
        background-color: #F0FDF4;
        border: 1px solid #BBF7D0;
        border-left: 5px solid #16A34A;
        padding: 20px;
        border-radius: 8px;
        margin-top: 16px;
    }
    .card-warning {
        background-color: #FFFBEB;
        border: 1px solid #FDE68A;
        border-left: 5px solid #D97706;
        padding: 20px;
        border-radius: 8px;
        margin-top: 16px;
    }
    .card-danger {
        background-color: #FEF2F2;
        border: 1px solid #FECACA;
        border-left: 5px solid #DC2626;
        padding: 20px;
        border-radius: 8px;
        margin-top: 16px;
    }
    .faq-question {
        font-weight: bold;
        color: #00529B;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# Load Knowledge Base
@st.cache_data
def load_kb():
    possible_paths = [
        os.path.join(os.path.dirname(__file__), "knowledge_base-v2.json"),
        os.path.join(os.path.dirname(__file__), "knowledge_base.json"),
        "knowledge_base.json"
    ]
    for kb_path in possible_paths:
        if os.path.exists(kb_path):
            try:
                with open(kb_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
    return {}

kb_data = load_kb()

# Header Section
st.markdown("""
<div class="main-header">
    <h1>👩‍👧‍👦 Assistant & Simulatore "Nuovo Bonus Mamme 2026" v2.0</h1>
    <p>Strumento informativo e simulatore di calcolo basato su <strong>Circolare INPS n. 106/2026</strong>, <strong>Messaggio INPS n. 3343/2026</strong> e <strong>Legge n. 199/2025</strong>.</p>
    <div style="margin-top: 12px;">
        <span class="badge-inps">INPS Circ. 106/2026</span>
        <span class="badge-inps">INPS Mess. 3343/2026</span>
        <span class="badge-inps">Art. 1 c. 207 L. 199/2025</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Guida Rapida 2026")
    st.info("""
    **Punti chiave del beneficio:**
    - **Importo**: 60 € / mese per ogni mese di lavoro nel 2026 (Max 720 €).
    - **Erogazione**: Unica soluzione a **Dicembre 2026** dall'INPS.
    - **Reddito max**: 40.000 € lordi da lavoro.
    - **Apertura domande**: **20 Ottobre 2026**.
    - **Scadenza domanda**: **31 Dicembre 2026** (31 Gennaio 2027 se i requisiti spettano a Dicembre).
    - **Esente IRPEF e non rileva ai fini ISEE**.
    """)
    st.markdown("---")
    st.caption("Fonti Ufficiali INPS 2026 | Sviluppato per divulgazione e assistenza ai cittadini.")

# Navigation Tabs
tab_sim, tab_chat, tab_guide = st.tabs([
    "🧮 Simulatore & Calcolatore", 
    "💬 Chatbot & Ricerca Fonti", 
    "📋 Scheda Informativa & Domanda INPS"
])

# ==========================================
# TAB 1: SIMULATORE
# ==========================================
with tab_sim:
    st.subheader("Simula la tua idoneità e calcola l'importo spettante")
    st.write("Inserisci i dati della tua posizione lavorativa e familiare nel 2026 per verificare se ti spetta il bonus e calcolare l'importo totale.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### 1. Tipologia Lavorativa e Contratto")
        categoria_lavoro = st.selectbox(
            "Categoria lavorativa",
            [
                "Lavoratrice Dipendente (Pubblica o Privata)",
                "Lavoratrice Autonoma (Artigiana, Commerciante, Agricola)",
                "Iscritta a Cassa di Previdenza Professionale (Forense, CNDP, ENPACL, ecc.)",
                "Iscritta alla Gestione Separata INPS (Co.Co.Co, Libera Prof.)",
                "Lavoratrice Domestica (Colf, Badante, Babysitter)"
            ]
        )

        tipo_contratto = "N/A"
        if "Dipendente" in categoria_lavoro:
            tipo_contratto = st.radio(
                "Tipologia di contratto nel 2026",
                ["Tempo Determinato (o somministrazione / intermittente / apprendistato)", "Tempo Indeterminato"]
            )

        reddito_2026 = st.number_input(
            "Stima Reddito da Lavoro Lordo 2026 (€)",
            min_value=0,
            max_value=150000,
            value=25000,
            step=1000,
            help="Somma dei redditi da lavoro 2026 al netto dei contributi previdenziali obbligatori trattenuti. Non contano NASpI, pensioni e Assegno Unico."
        )

    with col2:
        st.markdown("##### 2. Requisiti Familiari e Mesi Lavorati")
        num_figli = st.radio(
            "Numero di figli nel nucleo familiare nel 2026",
            ["Meno di 2 figli", "2 figli", "3 o più figli"]
        )

        eta_minore = 0
        if num_figli == "2 figli":
            eta_minore = st.number_input("Età del 2° figlio (più piccolo) nel 2026", min_value=0, max_value=25, value=5)
        elif num_figli == "3 o più figli":
            eta_minore = st.number_input("Età del figlio più piccolo nel 2026", min_value=0, max_value=25, value=12)

        mesi_lavorati = st.slider(
            "Mesi o frazioni di mese di lavoro effettivo/vigente nel 2026",
            min_value=1,
            max_value=12,
            value=12,
            help="Conteggia ogni mese o frazione di mese in cui il contratto di lavoro è stato attivo o l'attività autonoma esercitata."
        )

    st.markdown("---")

    if st.button("🚀 Calcola Idoneità e Importo", type="primary", use_container_width=True):
        esito = True
        motivi_esclusione = []
        note_speciali = []

        if "Domestica" in categoria_lavoro:
            esito = False
            motivi_esclusione.append("I rapporti di lavoro domestico sono attualmente esclusi dalla legge (art. 1 c. 207 L. 199/2025).")
            note_speciali.append("Nota legale: Il Tribunale di Milano ha sollevato questione di costituzionalità alla Consulta per presunta discriminazione, ma la normativa vigente non consente l'accoglimento della domanda.")

        if reddito_2026 > 40000:
            esito = False
            motivi_esclusione.append(f"Il reddito stimato ({reddito_2026:,.2f} €) supera il limite massimo di 40.000,00 € annui fissato dalla legge.")

        if num_figli == "Meno di 2 figli":
            esito = False
            motivi_esclusione.append("Il bonus richiede un minimo di 2 figli compresi nel nucleo familiare.")
        elif num_figli == "2 figli":
            if eta_minore >= 10:
                esito = False
                motivi_esclusione.append("Per le madri di 2 figli, il beneficio spetta fino al compimento del 10° anno del figlio più piccolo.")
        elif num_figli == "3 o più figli":
            if eta_minore >= 18:
                esito = False
                motivi_esclusione.append("Per le madri di 3 o più figli, il beneficio spetta fino al compimento del 18° anno del figlio più piccolo.")
            
            if "Dipendente" in categoria_lavoro and "Tempo Indeterminato" in tipo_contratto:
                esito = False
                motivi_esclusione.append("Per le lavoratrici con 3 o più figli e contratto a tempo indeterminato, il Nuovo Bonus Mamme NON spetta poiché si applica già l'esonero contributivo IVS al 100% (art. 1 c. 180 L. 213/2023).")

        if esito:
            importo_totale = mesi_lavorati * 60
            st.markdown(f"""
            <div class="card-success">
                <h3>✅ ESITO POSITIVO: Hai diritto al Nuovo Bonus Mamme 2026!</h3>
                <p style="font-size: 1.3rem; font-weight: bold; color: #15803D;">
                    Importo Totale Spettante: {importo_totale:,.2f} €
                </p>
                <ul>
                    <li><strong>Mensilità riconosciute</strong>: {mesi_lavorati} mesi nel 2026</li>
                    <li><strong>Quota mensile</strong>: 60,00 € / mese</li>
                    <li><strong>Modalità di pagamento</strong>: In un'unica soluzione erogata dall'INPS a <strong>Dicembre 2026</strong></li>
                    <li><strong>Regime fiscale</strong>: Totale esenzione IRPEF e contributi, non rileva ai fini ISEE.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            if "Tempo Determinato" in tipo_contratto:
                st.info("💡 **Nota per contratti a termine / cessati nel 2026**: Se il contratto è cessato durante l'anno (es. il 31/08/2026), potrai comunque presentare la domanda entro il 31/12/2026 per ottenere le mensilità maturate (es. 8 mesi = 480 €).")
        else:
            st.markdown("""
            <div class="card-danger">
                <h3>❌ ESITO NON IDONEO</h3>
                <p>In base ai dati inseriti, la posizione non rispetta i requisiti del Nuovo Bonus Mamme 2026 per i seguenti motivi:</p>
            </div>
            """, unsafe_allow_html=True)
            for m in motivi_esclusione:
                st.error(f"• {m}")

        if note_speciali:
            for n in note_speciali:
                st.warning(f"⚠️ {n}")

# ==========================================
# TAB 2: CHATBOT & KNOWLEDGE SEARCH
# ==========================================
with tab_chat:
    st.subheader("💬 Fai una domanda all'Assistente Risposte Veloci")
    st.write("Inserisci qualsiasi domanda o seleziona uno dei quesiti più frequenti estratti dalle Circolari INPS.")

    st.markdown("**Domande Frequenti Popolari:**")
    quick_cols = st.columns(3)
    
    selected_query = None
    with quick_cols[0]:
        if st.button("❓ Se il contratto scade a metà anno?", use_container_width=True):
            selected_query = "contratto scade ad agosto o durante l'anno"
    with quick_cols[1]:
        if st.button("💰 Quali redditi contano per i 40.000€?", use_container_width=True):
            selected_query = "come si calcola il reddito dei 40000 euro"
    with quick_cols[2]:
        if st.button("👶 Tre figli e tempo indeterminato?", use_container_width=True):
            selected_query = "3 figli tempo indeterminato esonero IVS"

    user_input = st.text_input("Inserisci la tua domanda sul Bonus Mamme 2026:", value="" if not selected_query else selected_query)

    if user_input:
        user_lower = user_input.lower()
        faq_list = kb_data.get("faq", [])
        
        matches = []
        words = [w for w in re.split(r'\W+', user_lower) if len(w) > 2]
        
        for faq in faq_list:
            score = 0
            q_text = faq["domanda"].lower() + " " + faq["risposta"].lower()
            kw_list = faq.get("keywords", [])
            
            for w in words:
                if w in faq["domanda"].lower():
                    score += 3
                elif any(w in kw.lower() for kw in kw_list):
                    score += 3
                elif w in faq["risposta"].lower():
                    score += 1
            if score > 0:
                matches.append((score, faq))
        
        matches.sort(key=lambda x: x[0], reverse=True)

        if matches:
            st.markdown("### 🔍 Risposte individuate nelle fonti ufficiali INPS:")
            for score, match in matches[:3]:
                st.markdown(f"""
                <div class="card-result">
                    <p class="faq-question">❓ {match['domanda']}</p>
                    <p>{match['risposta']}</p>
                    <p style="font-size: 0.85rem; color: #64748B;">📌 <em>Fonte: {match['fonte']}</em></p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="card-result">
                <p class="faq-question">💡 Risposta Sintetica dell'Assistente INPS:</p>
                <p>In merito al quesito posto ("<em>{user_input}</em>"), sulla base della <strong>Circolare INPS n. 106/2026</strong> e del <strong>Messaggio INPS n. 3343/2026</strong>:</p>
                <ul>
                    <li><strong>Principio generale</strong>: Il Nuovo Bonus Mamme 2026 riconosce <strong>60 €/mese</strong> per ogni mese o frazione di mese di vigenza del rapporto di lavoro dipendente o autonomo svolto nel 2026 (fino a un max di 720 € annui).</li>
                    <li><strong>Requisito reddituale</strong>: Reddito annuo da lavoro per il 2026 non superiore a <strong>40.000 € lordi</strong> (esclusi NASpI, pensioni e Assegno Unico).</li>
                    <li><strong>Requisito figli</strong>: Madri di 2 figli (figlio minore <10 anni) oppure madri di 3+ figli (figlio minore <18 anni).</li>
                    <li><strong>Domanda e Pagamento</strong>: La domanda si presenta sul sito inps.it entro il <strong>31 dicembre 2026</strong> e il pagamento viene erogato in un'unica soluzione a <strong>dicembre 2026</strong>.</li>
                </ul>
                <p style="font-size: 0.85rem; color: #64748B;">📌 <em>Fonte: Circolare INPS 106/2026 e Messaggio INPS 3343/2026</em></p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📚 Banca Dati Domande & Risposte Ufficiali INPS 2026")
    for faq in kb_data.get("faq", []):
        with st.expander(f"❓ {faq['domanda']}"):
            st.write(faq["risposta"])
            st.caption(f"Fonte: {faq['fonte']}")

# ==========================================
# TAB 3: GUIDA INPS
# ==========================================
with tab_guide:
    st.subheader("📋 Scheda Sintetica & Procedura di Domanda INPS")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        ### 📌 Sintesi Normativa
        - **Legge di Riferimento**: Art. 1, comma 207, Legge 30/12/2025 n. 199 (Legge di Bilancio 2026).
        - **Circolare Operativa**: Circolare INPS n. 106 del 16/10/2026.
        - **Apertura Servizio**: Messaggio INPS n. 3343 del 20/10/2026.
        - **Importo**: 60,00 € mensili pro-quota per mese/frazione di mese lavorato (max 720,00 € annui).
        - **Scadenza Presentazione**: **31 dicembre 2026** (31 gennaio 2027 per requisiti spettanti a dicembre 2026).
        - **Data Erogazione**: **Mese di dicembre 2026** in unica soluzione.
        """)

    with col_b:
        st.markdown("""
        ### 💻 Come Presentare Domanda Online
        1. Accedi al portale ufficiale INPS (inps.it) con credenziali **SPID (livello 2)**, **CIE 3.0**, **CNS** o **eIDAS**.
        2. Cerca nel portale o segui il percorso:
           `Sostegni, Sussidi e Indennità` ➔ `Per genitori` ➔ `Nuovo Bonus mamme`.
        3. Dichiara i dati anagrafici dei figli (codice fiscale e data di nascita).
        4. Indica il metodo di accredito (IBAN bancario/postale o bonifico domiciliato).
        5. Invia la domanda e scarica la ricevuta con protocollo.
        """)

    st.markdown("---")
    st.info("ℹ️ **Altre modalità di presentazione**: La domanda può essere inoltrata anche tramite **Contact Center Multicanale INPS** (803.164 da rete fissa o 06 164.164 da rete mobile) o tramite gli **Istituti di Patronato**.")
