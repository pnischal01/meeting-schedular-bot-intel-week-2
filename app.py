import streamlit as st
from rag_pipeline import RAGPipeline

# 1. Page Configuration & Dark Theme
st.set_page_config(page_title="Meeting Scheduler Agent", page_icon="", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    section[data-testid="stSidebar"] { background-color: #161B22; border-right: 1px solid #30363D; }
    .stChatInputContainer { background-color: #0E1117 !important; }
    h1, h2, h3, p { color: #E6EDF3 !important; }
    [data-testid="stChatMessage"] { background-color: #1C2128; border: 1px solid #30363D; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Initialize Backend Services 
@st.cache_resource
def load_backend():
    from vector_db import VectorDB
    from compression_service import CompressionService
    from ai_service import AIService
    from database import DatabaseManager

    v_db = VectorDB()
    comp = CompressionService()
    ai = AIService()
    db_manager = DatabaseManager()
    
    # Handing services to the pipeline
    pipe = RAGPipeline(vector_db=v_db, compressor=comp, ai_bot=ai)
    
    return pipe, db_manager

pipeline, db = load_backend()

# 3. Sidebar: System Status & Direct Booking
with st.sidebar:
    st.header("Control Panel")
    st.success("Connected to PostgreSQL")
    st.success("ScaleDown & Groq Active")
    
    st.markdown("---")
    # st.subheader("Confirm & Book Slot")
    
    # with st.form("booking_form"):
    #     name = st.text_input("Attendee Name")
    #     phone = st.text_input("Phone Number")
    #     date_time = st.text_input("Time (YYYY-MM-DD HH:MM:SS)")
        
    #     if st.form_submit_button("Save to Database"):
    #         if name and phone and date_time:
    #             if db.log_appointment(name, phone, date_time):
    #                 st.success("Meeting securely saved!")
    #             else:
    #                 st.error("Database error.")
    #         else:
    #             st.warning("Fill all fields.")

# 4. Main Chat Interface
st.title("AI Meeting Scheduler")
st.markdown("---")

# Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello Nischal! I've checked your PostgreSQL schedule. What meeting would you like to arrange?"}
    ]

# Render existing conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Unified Chat Input (Only one instance)
if prompt := st.chat_input("Ex: Suggest a 30min slot for a code review tomorrow...", key="chat_input_unique"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing schedule..."):
            try:
                # Using the handle_query method defined in your rag_pipeline.py
                response = pipeline.handle_query(prompt) 
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Execution Error: {str(e)}")