import requests
import json
from config import Config

class CompressionService:
    def __init__(self):
        # FIXED: Matches exactly what is in your config.py
        self.api_key = Config.SCALEDOWN_API_KEY
        self.url = "https://api.scaledown.xyz/compress/raw/"

    # FIXED: Renamed to match the exact call in your rag_pipeline.py
    def compress_context(self, context_text):
        """
        Uses ScaleDown API to compress context to save tokens and reduce latency.
        """
        headers = {
            'x-api-key': self.api_key,
            'Content-Type': 'application/json'
        }
        
        payload = {
            "context": context_text,
            "prompt": "Extract relevant availability and scheduling rules.", 
            "scaledown": {
                "rate": "auto" 
            }
        }

        try:
            response = requests.post(self.url, headers=headers, json=payload)
            result = response.json()
            return result.get("compressed_context", "")
        except Exception as e:
            print(f"ScaleDown Error: {e}")
            return str(context_text)[:500] # Fallback to simple truncation