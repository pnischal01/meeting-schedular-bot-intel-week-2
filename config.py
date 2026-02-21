import os
from dotenv import load_dotenv
from pathlib import Path

# 1. Force Python to find the .env file in YOUR specific project folder
# This creates an absolute path: C:\Users\potla\Desktop\chatbot_intel_week2\.env
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

class Config:
    # Use the VARIABLE NAMES exactly as they appear in your .env
    GROQ_API_KEY = os.getenv("AI_BOT_API_KEY") 
    SCALEDOWN_API_KEY = os.getenv("COMPRESSION_API_KEY")
    
    # PostgreSQL Database Settings
    DB_NAME = os.getenv("DB_NAME", "appointment_bot")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")

# 2. Add a terminal debug check
print(f"--- DEBUG: Loading .env from {env_path} ---")
if Config.GROQ_API_KEY:
    print(f"✅ SUCCESS: Key found starting with {Config.GROQ_API_KEY[:5]}")
else:
    print("❌ FAILURE: Key is still None. Check your .env file content!")