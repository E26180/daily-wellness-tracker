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
            print("Add daily entry selected")
        elif choice == "2":
            print("View all entries selected")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()