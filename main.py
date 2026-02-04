FILE_NAME = "contacts.txt"


def add_contact():
    name = input("Enter name: ")
    email = input("Enter email: ")

    phone_entries = []
    count = int(input("How many phone numbers to add? "))

    for i in range(count):
        label = input(f"Enter type (Mobile/Home/Office) for number {i+1}: ")
        number = input("Enter number: ")
        phone_entries.append(f"{label}:{number}")

    phones = ",".join(phone_entries)

    with open(FILE_NAME, "a") as file:
        file.write(f"{name}|{phones}|{email}\n")

    print("✅ Contact added successfully!")


def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        if not contacts:
            print("📭 No contacts found.")
            return

        print("\n--- Contact List ---")
        for index, contact in enumerate(contacts, start=1):
            name, phones, email = contact.strip().split("|")
            print(f"\n{index}. Name: {name}")
            print("   Phone Numbers:")
            for phone in phones.split(","):
                print(f"   - {phone}")
            print(f"   Email: {email}")

    except FileNotFoundError:
        print("📭 No contacts file found.")


def search_contact():
    keyword = input("Enter name or number to search: ").lower()
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for contact in file:
                if keyword in contact.lower():
                    name, phones, email = contact.strip().split("|")
                    print("\n🔍 Contact Found")
                    print(f"Name: {name}")
                    print("Phone Numbers:")
                    for phone in phones.split(","):
                        print(f"- {phone}")
                    print(f"Email: {email}")
                    found = True

        if not found:
            print("❌ No matching contact found.")

    except FileNotFoundError:
        print("📭 No contacts file found.")


def edit_contact():
    view_contacts()

    try:
        index = int(input("\nEnter contact number to edit: ")) - 1

        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        name = input("Enter new name: ")
        email = input("Enter new email: ")

        phone_entries = []
        count = int(input("How many phone numbers? "))

        for i in range(count):
            label = input("Enter type (Mobile/Home/Office): ")
            number = input("Enter number: ")
            phone_entries.append(f"{label}:{number}")

        phones = ",".join(phone_entries)
        contacts[index] = f"{name}|{phones}|{email}\n"

        with open(FILE_NAME, "w") as file:
            file.writelines(contacts)

        print("✏️ Contact updated successfully!")

    except (ValueError, IndexError):
        print("❌ Invalid selection.")


def delete_contact():
    view_contacts()

    try:
        index = int(input("\nEnter contact number to delete: ")) - 1

        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        deleted = contacts.pop(index)

        with open(FILE_NAME, "w") as file:
            file.writelines(contacts)

        print(f"🗑️ Contact '{deleted.split('|')[0]}' deleted successfully!")

    except (ValueError, IndexError):
        print("❌ Invalid selection.")


def menu():
    while True:
        print("\n📒 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Exiting Contact Book")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    menu()
