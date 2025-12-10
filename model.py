import calendar
import datetime
import json
import os


class CalendarModel:

    def __init__(self):
        self.filename = "events.json"
        self.events = self.load_events()   # events = list of dict

    # --- Load events (list of dicts) ---
    def load_events(self):
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)

                # file must contain list
                if isinstance(data, list):
                    return data
                else:
                    print("Incorrect JSON format. Resetting to empty list.")
                    return []
        except:
            return []

    # --- Save events ---
    def save_events(self):
        if not isinstance(self.events, list):
            self.events = []

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.events, f, indent=4, ensure_ascii=False)

    # --- Create event ---
    def create_event(self, date, text):
        new_event = {
            "date": date,
            "title": text,
            "description": ""
        }
        self.events.append(new_event)
        self.save_events()

    # --- Edit event by date ---
    def edit_event(self, date, new_text):
        for event in self.events:
            if event["date"] == date:
                event["title"] = new_text
                self.save_events()
                return True
        return False

    # --- Delete event by date ---
    def delete_event(self, date):
        before = len(self.events)
        self.events = [e for e in self.events if e["date"] != date]
        after = len(self.events)

        self.save_events()
        return before != after

    # --- Get all events ---
    def get_all_events(self):
        return self.events

    # --- Calendar outputs ---
    def get_current_month(self):
        now = datetime.date.today()
        return calendar.month(now.year, now.month)

    def get_specific_month(self, month):
        year = datetime.date.today().year
        return calendar.month(year, month)
