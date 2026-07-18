DATA_FILE = "wellness_data.txt"


def save_entry(entry):
    with open(DATA_FILE, "a") as file:
        file.write(str(entry) + "\n")


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

    save_entry(entry)
    print("\nEntry saved successfully!")


def view_entries():
    try:
        with open(DATA_FILE, "r") as file:
            entries = file.readlines()

            if len(entries) == 0:
                print("\nNo entries found.")
            else:
                print("\nAll Wellness Entries:")
                for entry in entries:
                    print(entry.strip())

    except FileNotFoundError:
        print("\nNo data file found. Please add an entry first.")


def search_entry_by_date():
    search_date = input("Enter the date to search (YYYY-MM-DD): ")
    found = False

    try:
        with open(DATA_FILE, "r") as file:
            entries = file.readlines()

            for entry in entries:
                if search_date in entry:
                    print("\nEntry found:")
                    print(entry.strip())
                    found = True

            if not found:
                print("\nNo entry found for that date.")

    except FileNotFoundError:
        print("\nNo data file found. Please add an entry first.")


def get_water_amount(entry):
    try:
        water_text = entry.split("'water': '")[1].split("'")[0]
        return int(water_text)
    except:
        return 0


def sort_entries_by_water():
    try:
        with open(DATA_FILE, "r") as file:
            entries = file.readlines()

            if len(entries) == 0:
                print("\nNo entries found.")
            else:
                sorted_entries = sorted(entries, key=get_water_amount)

                print("\nEntries sorted by water intake:")
                for entry in sorted_entries:
                    print(entry.strip())

    except FileNotFoundError:
        print("\nNo data file found. Please add an entry first.")


def show_menu():
    print("\nDaily Wellness Tracker")
    print("1. Add daily entry")
    print("2. View all entries")
    print("3. Search entry by date")
    print("4. Sort entries by water intake")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entry_by_date()
        elif choice == "4":
            sort_entries_by_water()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


main()