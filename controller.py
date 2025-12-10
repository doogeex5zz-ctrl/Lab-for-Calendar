import datetime
from model import CalendarModel

class CalendarController:

    def __init__(self, view):
        self.view = view
        self.model = CalendarModel()
        self.running = True

    def run(self):
        while self.running:
            choice = self.view.show_menu()

            if choice == "1":
                self.current_info_flow()

            elif choice == "2":
                date = self.view.prompt("Enter date (YYYY-MM-DD): ")
                text = self.view.prompt("Enter event text: ")
                self.model.create_event(date, text)
                self.view.display_message("Event created.")

            elif choice == "3":  # edit event
                events = self.model.get_all_events()
                self.view.display_events(events)
                index = int(self.view.prompt("Select event index to edit: "))
                new_text = self.view.prompt("Enter new event text: ")
                if 0 <= index < len(events):
                    self.model.events[index]["title"] = new_text
                    self.model.save_events()
                    self.view.display_message("Event updated.")
                else:
                    self.view.display_message("Invalid index.")

            elif choice == "4":  # delete event
                events = self.model.get_all_events()
                self.view.display_events(events)
                index = int(self.view.prompt("Select event index to delete: "))
                if 0 <= index < len(events):
                    self.model.events.pop(index)
                    self.model.save_events()
                    self.view.display_message("Event deleted.")
                else:
                    self.view.display_message("Invalid index.")

            elif choice == "5":
                self.view.display_events(self.model.events)

            elif choice == "6":
                self.running = False

            else:
                self.view.display_message("Invalid option.")

    # --- submenu logic ---
    def current_info_flow(self):
        while True:
            sub = self.view.show_current_info_menu()

            if sub == "1":  # show current month
                month_str = self.model.get_current_month()
                self.view.display_month(month_str)

            elif sub == "2":  # show current day
                today = datetime.date.today()
                day_str = f"Today is {today}"
                self.view.display_day(day_str)

            elif sub == "3":  # enter another month
                month = self.view.prompt("Enter a number 1-12 to display a month: ")

                if month.isdigit() and 1 <= int(month) <= 12:
                    month_str = self.model.get_specific_month(int(month))
                    self.view.display_month(month_str)
                else:
                    self.view.display_message("Invalid month number.")

            elif sub == "4":
                return

            else:
                self.view.display_message("Invalid option.")
