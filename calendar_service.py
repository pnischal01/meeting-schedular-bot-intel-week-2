import json
import os
from config import Config

class CalendarService:
    def __init__(self):
        self.file_path = Config.CALENDAR_PATH

    def get_all_meetings(self):
        """
        Loads the full calendar data from the JSON file.
        """
        if not os.path.exists(self.file_path):
            return {"meetings": []}
        
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading calendar: {e}")
            return {"meetings": []}

    def add_meeting(self, title, date, time, priority="medium"):
        """
        Appends a new meeting to the JSON file. 
        This is called after the AI Agent confirms a slot.
        """
        data = self.get_all_meetings()
        
        new_meeting = {
            "id": len(data.get("meetings", [])) + 1,
            "title": title,
            "date": date,
            "time": time,
            "status": "busy",
            "priority": priority
        }
        
        data.setdefault("meetings", []).append(new_meeting)
        
        try:
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving meeting: {e}")
            return False

    def get_available_slots(self, target_date):
        """
        Filters the calendar for a specific date to help the Agent 
        narrow down the context before compression.
        """
        data = self.get_all_meetings()
        day_schedule = [m for m in data.get("meetings", []) if m['date'] == target_date]
        return day_schedule