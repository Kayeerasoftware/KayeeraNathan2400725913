import csv
import json
import logging
from datetime import datetime


# CUSTOM EXCEPTIONS

class StudentExistsError(Exception):
    pass

class StudentNotFoundError(Exception):
    pass

class LoginError(Exception):
    pass


# LOGGING SETUP

logging.basicConfig(
    filename="student_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

CSV_FILE = "students.csv"
JSON_FILE = "students.json"


# LOGIN SYSTEM

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username == "kayeera" and password == "kayeera123":
        print("Login successful\n")
        logging.info("System login successful")
    else:
        logging.error("Failed login attempt")
        raise LoginError("Invalid credentials")


# FILE INITIALIZATION

def initialize_files():
    try:
        with open(CSV_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["RegNo", "Name"])
    except FileExistsError:
        pass

    try:
        with open(JSON_FILE, "x") as file:
            json.dump({}, file)
    except FileExistsError:
        pass


# JSON HANDLERS

def load_json():
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(JSON_FILE, "w") as file:
            json.dump({}, file)
        return {}


def save_json(data):
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

# HELPERS

def student_exists(reg_no):
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == reg_no:
                return True
    return False


# ADD STUDENT

def add_student():
    try:
        reg_no = input("RegNo: ")
        name = input("Name: ")
        address = input("Address: ")
        contact = input("Contact: ")
        program = input("Program: ")

        if student_exists(reg_no):
            raise StudentExistsError("Student already exists")

        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([reg_no, name])

        data = load_json()
        data[reg_no] = {
            "address": address,
            "contact": contact,
            "program": program,
            "created": str(datetime.now())
        }
        save_json(data)

        logging.info(f"Added student {reg_no}")
        print("Student added successfully")

    except StudentExistsError as e:
        logging.error(str(e))
        print(e)


# VIEW STUDENTS

def view_students():
    try:
        data = load_json()

        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)

            print("\n" + "=" * 70)
            print("                 STUDENT LIST")
            print("=" * 70)
            print(f"{'RegNo':<15}{'Name':<20}{'Address':<15}{'Contact':<15}{'Program':<10}")
            print("-" * 70)

            for row in reader:
                reg_no, name = row
                extra = data.get(reg_no, {})

                print(
                    f"{reg_no:<15}"
                    f"{name:<20}"
                    f"{extra.get('address', ''):<15}"
                    f"{extra.get('contact', ''):<15}"
                    f"{extra.get('program', ''):<10}"
                )

            print("-" * 70)

        logging.info("Viewed all students")

    except Exception as e:
        logging.error(str(e))
        print("Error viewing students")


# SEARCH STUDENT

def search_student():
    key = input("Enter RegNo or Name: ")

    try:
        found = False
        data = load_json()

        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and (row[0] == key or row[1].lower() == key.lower()):
                    print("\nFOUND STUDENT")
                    print("Basic:", row)
                    print("Extra:", data.get(row[0]))
                    found = True

        if not found:
            raise StudentNotFoundError("Student not found")

        logging.info(f"Searched {key}")

    except StudentNotFoundError as e:
        logging.error(str(e))
        print(e)


# UPDATE STUDENT

def update_student():
    reg_no = input("RegNo to update: ")

    try:
        if not student_exists(reg_no):
            raise StudentNotFoundError("Student not found")

        name = input("New Name: ")
        address = input("New Address: ")
        contact = input("New Contact: ")
        program = input("New Program: ")

        rows = []
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == reg_no:
                    row[1] = name
                rows.append(row)

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        data = load_json()
        data[reg_no] = {
            "address": address,
            "contact": contact,
            "program": program
        }
        save_json(data)

        logging.info(f"Updated {reg_no}")
        print("Updated successfully")

    except StudentNotFoundError as e:
        logging.error(str(e))
        print(e)


# DELETE STUDENT

def delete_student():
    reg_no = input("RegNo to delete: ")

    try:
        if not student_exists(reg_no):
            raise StudentNotFoundError("Student not found")

        rows = []
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] != reg_no:
                    rows.append(row)

        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        data = load_json()
        data.pop(reg_no, None)
        save_json(data)

        logging.info(f"Deleted {reg_no}")
        print("Deleted successfully")

    except StudentNotFoundError as e:
        logging.error(str(e))
        print(e)


# REPORT EXPORT

def export_report():
    data = load_json()

    with open("report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["RegNo", "Address", "Contact", "Program"])

        for reg, info in data.items():
            writer.writerow([
                reg,
                info.get("address"),
                info.get("contact"),
                info.get("program")
            ])

    print("Report exported successfully")


# MENU SYSTEM

def main():
    try:
        login()
    except LoginError as e:
        print(e)
        return

    initialize_files()

    while True:
        print("\n===== STUDENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Export Report")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            export_report()
        elif choice == "7":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


main()