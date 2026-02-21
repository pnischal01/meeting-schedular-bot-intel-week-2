import os
from langchain_groq import ChatGroq
from config import Config

class AIService:
    def __init__(self):
        # 1. Direct validation from your Config class
        api_key = Config.GROQ_API_KEY
        
        if not api_key or not api_key.startswith("gsk_"):
            raise ValueError("❌ Invalid Groq API Key. Ensure it starts with 'gsk_' in your .env file.")

        # 2. Initialize the model with the validated key
        # We use llama-3.3-70b-versatile for high performance in your Intel project
        self.llm = ChatGroq(
            groq_api_key=api_key, 
            model_name="llama-3.3-70b-versatile",
            temperature=0.1
        )

    def generate_response(self, user_query, compressed_context):
        # We must tell the LLM exactly what today is so it can resolve "Tuesday"
        today_date = "Saturday, Feb 21, 2026"
        
        prompt = f"""
        Today's Date: {today_date}
        Role: Meeting Scheduler for Nischal.
        
        GOAL: You must collect 4 pieces of info: Meeting Name, Day, Time, and Phone.
        
        STRICT RULES:
        1. If a detail is missing (like Phone or Meeting Name), ask for it immediately.
        2. DO NOT suggest alternative times unless there is a conflict in the context.
        3. Once you have all 4 details, DO NOT ask "would you like to book?". 
           Instead, say "I am booking that for you now" and provide the tag.
        4. TRIGGER TAG (Must be at the very end):
           TRIGGER_BOOKING: [Attendee Name] | [Phone] | [YYYY-MM-DD HH:MM:SS] | [Meeting Name]
        
        Context: {compressed_context}
        User says: {user_query}
        """
        response = self.llm.invoke(prompt)
        return response.content