"""Daily Wellness Tracker for the IY499 programming assignment."""

import csv
import os
from datetime import datetime


PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(PROJECT_FOLDER, "wellness_data.csv")
CHART_FILE = os.path.join(PROJECT_FOLDER, "water_intake_chart.txt")
FIELDNAMES = ["date", "mood", "water", "exercise", "sleep"]


def pause():
    """Wait until the user is ready to return to the menu."""
    input("\nPress Enter to return to the menu...")


def create_file_if_not_exists():
    """Create the CSV data file and its headings when it does not exist."""
    if os.path.exists(DATA_FILE):
        return True

    try:
        with open(DATA_FILE, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(FIELDNAMES)
        return True
    except PermissionError:
        print("Error: Permission was denied while creating the data file.")
    except OSError as error:
        print(f"Error: The data file could not be created ({error}).")

    return False


def get_valid_date(message="Enter date (YYYY-MM-DD): "):
    """Ask for a real, non-future date in YYYY-MM-DD format."""
    while True:
        date_text = input(message).strip()

        try:
            entered_date = datetime.strptime(date_text, "%Y-%m-%d").date()

            if entered_date > datetime.today().date():
                print("Future dates are not allowed.")
            else:
                return date_text
        except ValueError:
            print("Invalid date. Please enter a real date in YYYY-MM-DD format.")


def get_non_empty_text(message, maximum_length=40):
    """Ask for text that is not empty or unnecessarily long."""
    while True:
        text = input(message).strip()

        if text == "":
            print("This field cannot be empty.")
        elif len(text) > maximum_length:
            print(f"Please enter no more than {maximum_length} characters.")
        else:
            return text


def get_number_input(message, minimum, maximum):
    """Ask for a whole number inside an accepted range."""
    while True:
        user_input = input(message).strip()

        try:
            number = int(user_input)

            if number < minimum or number > maximum:
                print(f"Please enter a number between {minimum} and {maximum}.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def row_to_entry(row):
    """Convert one CSV row into a validated wellness dictionary."""
    date_text = (row.get("date") or "").strip()
    mood = (row.get("mood") or "").strip()
    water = int(row["water"])
    exercise = int(row["exercise"])
    sleep = int(row["sleep"])

    entry_date = datetime.strptime(date_text, "%Y-%m-%d").date()

    if mood == "":
        raise ValueError("mood is empty")
    if len(mood) > 40:
        raise ValueError("mood is longer than 40 characters")
    if water < 0 or water > 30:
        raise ValueError("water must be between 0 and 30")
    if exercise < 0 or exercise > 300:
        raise ValueError("exercise must be between 0 and 300")
    if sleep < 0 or sleep > 24:
        raise ValueError("sleep must be between 0 and 24")
    if entry_date > datetime.today().date():
        raise ValueError("future dates are not allowed")

    return {
        "date": date_text,
        "mood": mood,
        "water": water,
        "exercise": exercise,
        "sleep": sleep,
    }


def load_entries():
    """Load valid CSV entries and skip damaged rows safely."""
    if not create_file_if_not_exists():
        return None

    entries = []
    skipped_rows = 0

    try:
        with open(DATA_FILE, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print("Error: The data file has no column headings.")
                return None

            missing_fields = []
            for field in FIELDNAMES:
                if field not in reader.fieldnames:
                    missing_fields.append(field)

            if missing_fields:
                print("Error: Missing CSV columns: " + ", ".join(missing_fields))
                return None

            for line_number, row in enumerate(reader, start=2):
                try:
                    entries.append(row_to_entry(row))
                except (KeyError, TypeError, ValueError) as error:
                    skipped_rows += 1
                    print(f"Warning: Line {line_number} was skipped ({error}).")

    except FileNotFoundError:
        print("Error: The data file was not found.")
        return None
    except PermissionError:
        print("Error: Permission was denied while reading the data file.")
        return None
    except (OSError, csv.Error) as error:
        print(f"Error: The data file could not be read ({error}).")
        return None

    if skipped_rows > 0:
        print(f"Skipped invalid rows: {skipped_rows}")

    return entries


def save_entry(entry):
    """Append one wellness entry to the CSV file safely."""
    if not create_file_if_not_exists():
        return False

    try:
        with open(DATA_FILE, "a", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writerow(entry)
        return True
    except PermissionError:
        print("Error: Permission was denied while saving the entry.")
    except (OSError, csv.Error) as error:
        print(f"Error: The entry could not be saved ({error}).")

    return False


def linear_search_by_date(entries, target_date):
    """Return entries matching a date using a linear search algorithm."""
    matching_entries = []

    for entry in entries:
        if entry["date"] == target_date:
            matching_entries.append(entry)

    return matching_entries


def add_entry():
    """Collect, validate and save one daily wellness entry."""
    print("\nAdd Daily Entry")

    entries = load_entries()
    if entries is None:
        print("The entry cannot be added until the data file is corrected.")
        pause()
        return

    date_text = get_valid_date()

    if linear_search_by_date(entries, date_text):
        print("\nAn entry already exists for this date.")
        print("The duplicate entry was not saved.")
        pause()
        return

    mood = get_non_empty_text("Enter your mood today: ")
    water = get_number_input(
        "How many glasses of water did you drink? ", 0, 30
    )
    exercise = get_number_input(
        "How many minutes did you exercise? ", 0, 300
    )
    sleep = get_number_input("How many hours did you sleep? ", 0, 24)

    entry = {
        "date": date_text,
        "mood": mood,
        "water": water,
        "exercise": exercise,
        "sleep": sleep,
    }

    if save_entry(entry):
        print("\nEntry saved successfully!")

    pause()


def display_entry(entry):
    """Display one wellness entry in a readable format."""
    print("----------------------------")
    print("Date:", entry["date"])
    print("Mood:", entry["mood"])
    print("Water:", entry["water"], "glasses")
    print("Exercise:", entry["exercise"], "minutes")
    print("Sleep:", entry["sleep"], "hours")


def display_entry_list(entries, title):
    """Display a heading followed by a list of entries."""
    if len(entries) == 0:
        print("\nNo entries found.")
        return

    print(f"\n{title}")
    for entry in entries:
        display_entry(entry)

    print("----------------------------")
    print("Total entries:", len(entries))


def view_entries():
    """Display every valid saved entry."""
    entries = load_entries()

    if entries is not None:
        display_entry_list(entries, "All Wellness Entries")

    pause()


def search_entry_by_date():
    """Ask for a date and search entries one by one."""
    entries = load_entries()

    if entries is None:
        pause()
        return
    if len(entries) == 0:
        print("\nNo entries found.")
        pause()
        return

    search_date = get_valid_date("Enter the date to search (YYYY-MM-DD): ")
    matching_entries = linear_search_by_date(entries, search_date)
    display_entry_list(matching_entries, "Search Results")
    pause()


def bubble_sort_by_water(entries, descending=False):
    """Return a copy ordered by water intake using bubble sort."""
    sorted_entries = entries.copy()

    for end_position in range(len(sorted_entries) - 1, 0, -1):
        swapped = False

        for index in range(end_position):
            left_water = sorted_entries[index]["water"]
            right_water = sorted_entries[index + 1]["water"]

            wrong_order = left_water > right_water
            if descending:
                wrong_order = left_water < right_water

            if wrong_order:
                sorted_entries[index], sorted_entries[index + 1] = (
                    sorted_entries[index + 1],
                    sorted_entries[index],
                )
                swapped = True

        if not swapped:
            break

    return sorted_entries


def get_sort_direction():
    """Ask whether water values should be sorted up or down."""
    while True:
        print("\nSort order")
        print("1. Lowest to highest")
        print("2. Highest to lowest")
        choice = input("Choose 1 or 2: ").strip()

        if choice == "1":
            return False
        if choice == "2":
            return True

        print("Invalid choice. Please enter 1 or 2.")


def sort_entries_by_water():
    """Load and display entries ordered by water intake."""
    entries = load_entries()

    if entries is None:
        pause()
        return
    if len(entries) == 0:
        print("\nNo entries found.")
        pause()
        return

    descending = get_sort_direction()
    sorted_entries = bubble_sort_by_water(entries, descending)
    display_entry_list(sorted_entries, "Entries Sorted by Water Intake")
    pause()


def filter_entries_by_date_range(entries, start_date, end_date):
    """Return entries with dates inside the selected range."""
    matching_entries = []

    for entry in entries:
        if start_date <= entry["date"] <= end_date:
            matching_entries.append(entry)

    return matching_entries


def show_entries_in_date_range():
    """Ask for a date range and display all matching entries."""
    entries = load_entries()

    if entries is None:
        pause()
        return
    if len(entries) == 0:
        print("\nNo entries found.")
        pause()
        return

    print("\nFilter Entries by Date Range")
    start_date = get_valid_date("Start date (YYYY-MM-DD): ")

    while True:
        end_date = get_valid_date("End date (YYYY-MM-DD): ")
        if end_date < start_date:
            print("The end date cannot be before the start date.")
        else:
            break

    matching_entries = filter_entries_by_date_range(
        entries, start_date, end_date
    )
    display_entry_list(matching_entries, "Date Range Results")
    pause()


def build_text_chart(entries):
    """Build the water-intake chart as a list of text lines."""
    chart_lines = [
        "WATER INTAKE CHART",
        "Each # symbol represents one glass of water.",
        "",
    ]

    for entry in entries:
        bar = "#" * entry["water"]
        chart_lines.append(
            f"{entry['date']} | {bar} {entry['water']} glasses"
        )

    return chart_lines


def save_text_chart(chart_lines):
    """Save the generated water-intake chart to a text file."""
    try:
        with open(CHART_FILE, "w", encoding="utf-8") as file:
            file.write("\n".join(chart_lines) + "\n")
        return True
    except PermissionError:
        print("Error: Permission was denied while saving the chart.")
    except OSError as error:
        print(f"Error: The chart could not be saved ({error}).")

    return False


def show_text_chart(entries):
    """Display and save a simple water-intake bar chart."""
    chart_lines = build_text_chart(entries)

    print()
    print("\n".join(chart_lines))

    if save_text_chart(chart_lines):
        print("\nChart saved to: water_intake_chart.txt")


def show_summary():
    """Display average wellness values and the water chart."""
    entries = load_entries()

    if entries is None:
        pause()
        return
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
    """Display the main program menu."""
    print("\nDaily Wellness Tracker")
    print("1. Add daily entry")
    print("2. View all entries")
    print("3. Search entry by date")
    print("4. Sort entries by water intake")
    print("5. Filter entries by date range")
    print("6. Show summary")
    print("7. Exit")


def main():
    """Create the data file and run the menu until Exit is selected."""
    if not create_file_if_not_exists():
        print("The program cannot start without a data file.")
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entry_by_date()
        elif choice == "4":
            sort_entries_by_water()
        elif choice == "5":
            show_entries_in_date_range()
        elif choice == "6":
            show_summary()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed safely.")
