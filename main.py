from datetime import datetime
import csv
import os

DATA_FILE = "wellness_data.csv"


def pause():
    input("\nPress Enter to return to the menu...")


def create_file_if_not_exists():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "mood", "water", "exercise", "sleep"])


def get_valid_date():
    while True:
        date_text = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text
        except ValueError:
            print("Invalid date. Please enter a real date in YYYY-MM-DD format.")


def get_non_empty_text(message):
    while True:
        text = input(message).strip()

        if text == "":
            print("This field cannot be empty.")
        else:
            return text


def get_number_input(message, minimum, maximum):
    while True:
        user_input = input(message)

        try:
            number = int(user_input)

            if number < minimum or number > maximum:
                print(f"Please enter a number between {minimum} and {maximum}.")
            else:
                return number

        except ValueError:
            print("Invalid input. Please enter a number.")


def save_entry(entry):
    create_file_if_not_exists()

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            entry["date"],
            entry["mood"],
            entry["water"],
            entry["exercise"],
            entry["sleep"]
        ])


def load_entries():
    create_file_if_not_exists()

    entries = []

    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            entry = {
                "date": row["date"],
                "mood": row["mood"],
                "water": int(row["water"]),
                "exercise": int(row["exercise"]),
                "sleep": int(row["sleep"])
            }

            entries.append(entry)

    return entries


def add_entry():
    print("\nAdd Daily Entry")

    date = get_valid_date()
    mood = get_non_empty_text("Enter your mood today: ")

    water = get_number_input("How many glasses of water did you drink? ", 0, 30)
    exercise = get_number_input("How many minutes did you exercise? ", 0, 300)
    sleep = get_number_input("How many hours did you sleep? ", 0, 24)

    entry = {
        "date": date,
        "mood": mood,
        "water": water,
        "exercise": exercise,
        "sleep": sleep
    }

    save_entry(entry)

    print("\nEntry saved successfully!")
    pause()


def display_entry(entry):
    print("----------------------------")
    print("Date:", entry["date"])
    print("Mood:", entry["mood"])
    print("Water:", entry["water"], "glasses")
    print("Exercise:", entry["exercise"], "minutes")
    print("Sleep:", entry["sleep"], "hours")


def view_entries():
    entries = load_entries()

    if len(entries) == 0:
        print("\nNo entries found.")
    else:
        print("\nAll Wellness Entries")
        for entry in entries:
            display_entry(entry)

    pause()


def search_entry_by_date():
    entries = load_entries()

    if len(entries) == 0:
        print("\nNo entries found.")
        pause()
        return

    search_date = get_valid_date()
    found = False

    for entry in entries:
        if entry["date"] == search_date:
            display_entry(entry)
            found = True

    if not found:
        print("\nNo entry found for that date.")

    pause()


def sort_entries_by_water():
    entries = load_entries()

    if len(entries) == 0:
        print("\nNo entries found.")
        pause()
        return

    sorted_entries = sorted(entries, key=lambda entry: entry["water"])

    print("\nEntries Sorted by Water Intake")
    for entry in sorted_entries:
        display_entry(entry)

    pause()


def show_text_chart(entries):
    print("\nWater Intake Chart")

    for entry in entries:
        bar = "#" * entry["water"]
        print(entry["date"], "|", bar, entry["water"], "glasses")


def show_summary():
    entries = load_entries()

    if len(entries) == 0:
        print("\nNo entries found.")
        pause()
        return

    total_water = 0
    total_exercise = 0
    total_sleep = 0

    for entry in entries:
        total_water += entry["water"]
        total_exercise += entry["exercise"]
        total_sleep += entry["sleep"]

    count = len(entries)

    average_water = total_water / count
    average_exercise = total_exercise / count
    average_sleep = total_sleep / count

    print("\nWellness Summary")
    print("Total entries:", count)
    print("Average water intake:", round(average_water, 2), "glasses")
    print("Average exercise:", round(average_exercise, 2), "minutes")
    print("Average sleep:", round(average_sleep, 2), "hours")

    show_text_chart(entries)

    pause()


def show_menu():
    print("\nDaily Wellness Tracker")
    print("1. Add daily entry")
    print("2. View all entries")
    print("3. Search entry by date")
    print("4. Sort entries by water intake")
    print("5. Show summary")
    print("6. Exit")


def main():
    create_file_if_not_exists()

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
            show_summary()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


main()