class CalendarView:

    def show_menu(self):
        print("\n=== Calendar Menu ===")
        print("1. Show current information")
        print("2. Create event")
        print("3. Edit event")
        print("4. Delete event")
        print("5. Show events")
        print("6. Exit")
        return input("Choose option: ")

    # --- Submenu for option "Show current information"
    def show_current_info_menu(self):
        print("\n=== Current Information Menu ===")
        print("1. Show current month")
        print("2. Show current day")
        print("3. Enter another month (1-12)")
        print("4. Back to main menu")
        return input("Choose option: ")

    def prompt(self, text):
        return input(text)

    def display_message(self, msg):
        print(msg)

    def display_month(self, month_str):
        print("\n" + month_str)

    def display_day(self, day_str):
        print("\n" + day_str)

    def display_events(self, events):
        print("\n=== Events ===")
        if not events:
            print("No events saved.")
        else:
            for i, event in enumerate(events):
                date = event.get("date", "")
                title = event.get("title", "")
                description = event.get("description", "")
                print(f"[{i}] {date} - {title}: {description}")
