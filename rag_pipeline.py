import re

class RAGPipeline:
    def __init__(self, vector_db, compressor, ai_bot):
        self.vdb = vector_db
        self.compressor = compressor
        self.ai = ai_bot
        # Ensure the pipeline has access to the database manager logic
        from database import DatabaseManager
        self.db = DatabaseManager()

    def handle_query(self, user_query):
        """Processes query and checks for the booking trigger."""
        context = self.vdb.search(user_query)
        compressed = self.compressor.compress(context)
        
        # Get response from AI Service
        ai_response = self.ai.generate_response(user_query, compressed)
        
        # DEBUG: See exactly what the AI sent back in your terminal
        print(f"DEBUG: AI Response received: {ai_response}")
        
        # Check if the trigger tag is present
        if "TRIGGER_BOOKING:" in ai_response:
            return self._process_automated_booking(ai_response)
            
        return ai_response

    def _process_automated_booking(self, ai_response):
        """Extracts data and performs the actual SQL insert."""
        # Matches: TRIGGER_BOOKING: [Name] | [Phone] | [Time] | [Meeting Name]
        pattern = r"TRIGGER_BOOKING: \[(.*?)\] \| \[(.*?)\] \| \[(.*?)\] \| \[(.*?)\]"
        match = re.search(pattern, ai_response)
        
        if match:
            u_name, u_phone, u_time, m_name = match.groups()
            
            # Perform the insert using the 4-variable method in database.py
            success = self.db.log_appointment(
                u_name.strip(), 
                u_phone.strip(), 
                u_time.strip(), 
                m_name.strip()
            )
            
            print(f"DEBUG: Database Insert Success? {success}")
            
            if success:
                # Clean the response for the user
                clean_msg = re.sub(r"TRIGGER_BOOKING:.*", "", ai_response, flags=re.DOTALL).strip()
                return f"{clean_msg}\n\n✅ **System:** '{m_name}' scheduled in PostgreSQL."
            else:
                return "AI extracted details, but the database failed to save. Check your DB connection."
        
        print("DEBUG: Trigger found but Regex pattern did not match.")
        return ai_response