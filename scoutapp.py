# 🏒 Hammarby ScoutApp v2.0
# Byggd i Streamlit + Supabase
# Av: Lumerixgruppen / Lars Brandin

import streamlit as st
from dotenv import load_dotenv
import os

# Läs in miljövariabler från .env
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

from datetime import date
from supabase import create_client, Client

# --- 🔐 SUPABASE ANSLUTNING ---
# Gå till Supabase → Settings → API och kopiera:
# Project URL  (börjar med https://...)
# anon public key (börjar med eyJhb...)
# Klistra in nedan:
#url = "https://vqudyvqwiuinusskrsvq.supabase.co"
#key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZxdWR5dnF3aXVpbnVzc2tyc3ZxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjIxODU2MzAsImV4cCI6MjA3Nzc2MTYzMH0.vy8jZDm_V-iM5V-_8yIxIF0onyqmVOFHNsPmA-KyuXQ"

supabase: Client = create_client(url, key)

# --- 🧭 APPENS TITEL ---
st.title("🏒 Hammarby ScoutApp v2.0")
st.caption("Formulär för matchscouting. Spara direkt till Supabase-databasen.")

# --- 📆 MATCHINFORMATION ---
st.header("Matchinformation")
datum = st.date_input("Datum", value=date.today())
match = st.text_input("Match (t.ex. Hammarby J18 – AIK J18)")
nivå = st.selectbox("Nivå", ["J16", "J18", "J20", "A-lag"])
arena = st.text_input("Arena")

# --- 👤 SPELARPROFIL ---
st.header("Spelarprofil")
spelare = st.text_input("Spelarnamn")
född = st.number_input("Födelseår", 1980, 2015, 2008)
klubb = st.text_input("Klubb")
position = st.selectbox("Position", ["LW", "C", "RW", "D", "G"])
tröjnummer = st.number_input("Tröjnummer", 1, 99)

# --- 🧠 BEDÖMNING ---
st.header("Bedömning (1–5)")
skridsko = st.slider("Skridskoåkning", 1, 5, 3)
teknik = st.slider("Teknik", 1, 5, 3)
spelförståelse = st.slider("Spelförståelse", 1, 5, 3)
fysik = st.slider("Fysik", 1, 5, 3)
arbetsmoral = st.slider("Arbetsmoral", 1, 5, 3)
karaktär = st.slider("Karaktär", 1, 5, 3)
tävlingsinstinkt = st.slider("Tävlingsinstinkt", 1, 5, 3)

# --- 🗒️ KOMMENTARER OCH REK ---
st.header("Kommentar & Rekommendation")
kommentar = st.text_area("Sammanfattning / Observationer")
media = st.text_input("Länk till video / foto (valfritt)")
rekommendation = st.selectbox("Rekommendation", ["Följ upp", "Provträning", "Ej aktuell"])
scout = st.text_input("Scout-ID / Namn", "MrB")

# --- 💾 SPARA TILL SUPABASE ---
if st.button("💾 Spara rapport"):
    # Sätt ihop datan till en dictionary
    data = {
        "scout_id": scout,
        "match": match,
        "nivå": nivå,
        "arena": arena,
        "spelare": spelare,
        "född": född,
        "klubb": klubb,
        "position": position,
        "tröjnummer": tröjnummer,
        "skridsko": skridsko,
        "teknik": teknik,
        "spelförståelse": spelförståelse,
        "fysik": fysik,
        "arbetsmoral": arbetsmoral,
        "karaktär": karaktär,
        "tävlingsinstinkt": tävlingsinstinkt,
        "kommentar": kommentar,
        "media": media,
        "rekommendation": rekommendation
    }

    try:
        supabase.table("reports").insert(data).execute()
        st.success("✅ Rapport sparad i databasen!")
    except Exception as e:
        st.error(f"❌ Något gick fel: {e}")
