from controller import CalendarController
from view import CalendarView

def main():
    view = CalendarView()
    controller = CalendarController(view)
    controller.run()

if __name__ == "__main__":
    main()
