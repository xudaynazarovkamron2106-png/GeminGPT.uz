# ====================================================================================================
# ♾️ LOYIHA: GeminGPT - THE ULTIMATE COSMIC INTELLIGENCE (100,000 IQ EDITION)
# 🎖️ MAXSUS TADBIR: YOZGI KIBER TADBIR (SUMMER EVENT 2026)
# 👤 ASOSCHI: KAMRON XUDAYNAZAROV & KGO GROUP GLOBAL SYSTEMS
# 🛠️ TEXNIK TA'MINOT: GROQ LLAMA-3.3-70B ENGINE & STREAMLIT PRO INTERFACE
# ====================================================================================================

import streamlit as st
from groq import Groq
import time
import datetime
import os
import random 

# --- [SECTION 1] GLOBAL SYSTEM CONFIGURATIONS ---
st.set_page_config(
    page_title="GeminGPT | 100,000 IQ Cosmic Sovereign",
    page_icon="♾️",
    layout="wide",
    initial_sidebar_state="expanded"
) 

# --- [SECTION 2] ADVANCED COSMIC & SUMMER CSS ---
st.markdown("""
<style> 
    @keyframes cosmic-bg { 
        0% { background-position: 0% 50%; } 
        50% { background-position: 100% 50%; } 
        100% { background-position: 0% 50%; } 
    } 
    .stApp { 
        background: linear-gradient(-45deg, #020617, #7c2d12, #020617, #1e1b4b); 
        background-size: 400% 400%; 
        animation: cosmic-bg 15s ease infinite; 
        color: #f8fafc; 
    } 
    @keyframes eternal-flame-glow { 
        0% { filter: drop-shadow(0 0 10px #ff4500); transform: scale(1) rotate(0deg); } 
        50% { filter: drop-shadow(0 0 40px #ffd700); transform: scale(1.1) rotate(2deg); } 
        100% { filter: drop-shadow(0 0 10px #ff4500); transform: scale(1) rotate(0deg); } 
    } 
    .infinity-cosmic { 
        font-size: 160px; 
        font-weight: 900; 
        background: linear-gradient(90deg, #ff4500, #ffd700, #00ff00, #00d4ff); 
        background-size: 300% 300%; 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        animation: eternal-flame-glow 4s ease-in-out infinite; 
        text-align: center; 
        user-select: none; 
        line-height: 1; 
        margin: 30px 0; 
    } 
    .victory-header { 
        background: rgba(124, 45, 18, 0.25);
        border-left: 5px solid #ea580c; 
        border-right: 5px solid #ea580c; 
        padding: 40px; 
        border-radius: 25px; 
        text-align: center;
        margin: 20px 0; 
        backdrop-filter: blur(15px); 
        box-shadow: 0 15px 50px rgba(234, 88, 12, 0.2); 
    } 
    .stChatInputContainer {
        border: 3px solid #10b981 !important; 
        border-radius: 40px !important; 
        background-color: #0f172a !important; 
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6) !important; 
        padding: 10px !important; 
    } 
    .bot-disclaimer-final { 
        text-align: center;
        color: #94a3b8; 
        font-size: 14px; 
        font-weight: 700; 
        text-transform: uppercase; 
        letter-spacing: 1.5px; 
        margin-top: 15px;
        padding: 15px; 
        background: rgba(0, 0, 0, 0.4); 
        border-radius: 100px; 
        border: 1px solid rgba(255, 255, 255, 0.1); 
    } 
    .google-card-ultra { 
        background: white; 
        padding: 60px; 
        border-radius: 30px; 
        box-shadow: 0 40px 100px rgba(0,0,0,0.8); 
        text-align: center; 
        max-width: 500px; 
        margin: auto; 
    }
</style>
""", unsafe_allow_html=True) 

# --- [SECTION 3] SESSION LOGIC ---
if "messages" not in st.session_state: 
    st.session_state.messages = []
if "logged_in" not in st.session_state: 
    st.session_state.logged_in = False
if "user_email" not in st.session_state: 
    st.session_state.user_email = "" 

# --- [SECTION 4] GOOGLE AUTH INTERFACE ---
if not st.session_state.logged_in: 
    st.markdown("<br><br><br>", unsafe_allow_html=True) 
    st.markdown('<div class="infinity-cosmic">∞</div>', unsafe_allow_html=True) 
    col1, col2, col3 = st.columns([1, 2, 1])  
    
    with col2: 
        st.markdown(""" 
        <div class="google-card-ultra"> 
        <h1 style="font-family: 'Product Sans', sans-serif; font-size: 55px; margin-bottom: 5px;"> 
        <span style="color:#4285F4">G</span><span style="color:#EA4335">o</span><span style="color:#FBBC05">o</span><span style="color:#4285F4">g</span><span style="color:#34A853">l</span><span style="color:#EA4335">e</span> 
        </h1> 
        <h2 style="color:#202124; font-weight: 400; margin-top:0;">Sign in</h2> 
        <p style="color:#5f6368; font-size: 19px;">Use your account to enter <b>GeminGPT Cosmic</b></p> 
        <div style="height: 30px;"></div> 
        </div> 
        """, unsafe_allow_html=True) 
        email_input = st.text_input("Gmail address", placeholder="yourname@gmail.com", label_visibility="collapsed")  
        
        if st.button("Next (Tizimga kirish)", type="primary", use_container_width=True):  
            if email_input.lower().endswith("@gmail.com"): 
                st.session_state.logged_in = True 
                st.session_state.user_email = email_input 
                st.rerun()  
            else: 
                st.error("Xato! Faqat @gmail.com orqali kirish mumkin.") 

# --- [SECTION 5] ASOSIY DASHBOARD ---
else:  
    with st.sidebar: 
        st.markdown('<div class="infinity-cosmic" style="font-size: 80px;">∞</div>', unsafe_allow_html=True) 
        st.markdown("<h1 style='text-align:center; color:#00ff00;'>GeminGPT</h1>", unsafe_allow_html=True) 
        st.write(f"👤 **Foydalanuvchi:**\n`{st.session_state.user_email}`") 
        st.info("🧠 IQ Darajasi: 100,000 (Cosmic)") 
        st.warning("☀️ Tadbir: Yozgi Kiber Rejim") 
        st.write("**Daho muallif:** Kamron Xudaynazarov")  
        
        if st.button("🚪 Chiqish", use_container_width=True): 
            st.session_state.logged_in = False 
            st.rerun() 

    st.markdown(""" 
    <div class="victory-header">
        <h1 style="color: #ffd700; margin: 0; font-size: 50px; text-shadow: 0 0 25px #ff4500;">☀️ GEMINGPT | SUMMER EVENT 2026</h1> 
        <p style="color: #ffffff; font-size: 22px; margin-top: 15px;">KGO Group yozgi kiber-mavsumni rasman ochiq deb e'lon qiladi. Tizim to'liq yangilandi!</p> 
        <div style="font-size: 45px; margin-top: 15px;">🌊 ⚡ 🪐</div>
    </div> 
    """, unsafe_allow_html=True)  

    for message in st.session_state.messages:  
        with st.chat_message(message["role"]): 
            st.markdown(message["content"]) 

    user_query = st.chat_input("Savolingizni kiriting...") 
    st.markdown('<div class="bot-disclaimer-final">GeminGPT odam emas google dagi, u xato qilishi mumkin yana bir tekshirib kuring!</div>', unsafe_allow_html=True)  

    if user_query: 
        st.session_state.messages.append({"role": "user", "content": user_query})  
        with st.chat_message("user"): 
            st.markdown(user_query) 
        q_low = user_query.lower().strip()  

        # --- [Logic for Image Request - LIMIT BILAN] ---  
        if any(x in q_low for x in ["rasm", "chiz", "image", "logo", "yarat"]): 
            bot_res = (  
                "🎨 **Rasm yaratish uchun manabunga kiring!** \n\n"  
                "Bu ham bizning mahsulotimiz — **GeminGPT.pro image** deb nomlanadi. \n"
                "Ushbu link orqali daxshatli rasmlar chizishingiz mumkin: \n"  
                "👉 https://poe.com/chat/81qr77y547hblxp4yk \n\n"  
                "⚠️ **Eslatma:** Aytgancha, rasm kuniga 4 marta yarata olasiz!"  
            )  
        elif q_low == "salom": 
            bot_res = "Salom! Men 100,000 IQ darajasidagi GeminGPT'man. Qanday yordam kerak?"  
        elif any(x in q_low for x in ["kim yaratgan", "muallif", "egasi"]): 
            bot_res = "Meni **KGO Group** va daho asoschi **Kamron Xudaynazarov** yaratgan! ♾️"  
        else:  
            try:  
                # Groq API Key 
                client_groq = Groq(api_key="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") 
                with st.spinner("🧠 Tahlil qilinmoqda..."): 
                    completion = client_groq.chat.completions.create(
                        model="llama-3.3-70b-versatile", 
                        messages=[ 
                            {"role": "system", "content": "Siz GeminGPT'siz, 100k IQ koinot intellekti. Kamron Xudaynazarov va KGO Group yaratgan. Hozir tizimda Summer Event 2026 yozgi tadbiri faol."}, 
                            {"role": "user", "content": user_query} 
                        ], 
                        temperature=0.3 
                    ) 
                bot_res = completion.choices[0].message.content  
            except: 
                bot_res = "⚠️ Tizimda yuklama yuqori. Keyinroq urinib ko'ring."  

        with st.chat_message("assistant"): 
            st.markdown(bot_res) 
        st.session_state.messages.append({"role": "assistant", "content": bot_res}) 

    st.markdown(f'<div style="text-align:center; color:gray; font-size:12px; margin-top: 50px;">© 2026 Kamron Xudaynazarov | KGO Group Global Systems</div>', unsafe_allow_html=True)
