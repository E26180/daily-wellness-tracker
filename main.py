def add_entry():
    date = input("Enter date (YYYY-MM-DD): ")
    mood = input("Enter your mood today: ")
    water = input("How many glasses of water did you drink? ")
    exercise = input("How many minutes did you exercise? ")
    sleep = input("How many hours did you sleep? ")

    entry = {
        "date": date,
        "mood": mood,
        "water": water,
        "exercise": exercise,
        "sleep": sleep
    }

    print("\nEntry added:")
    print(entry)


def show_menu():
    print("\nDaily Wellness Tracker")
    print("1. Add daily entry")
    print("2. View all entries")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            print("View all entries selected")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()