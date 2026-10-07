import json
import os

FILE_NAME = "student_data.json"


# ---------------- LOAD DATA ----------------

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    assignments = data.get("assignments", [])
    expenses = data.get("expenses", [])
    attendance = data.get("attendance", [])
    notes = data.get("notes", [])

else:
    assignments = []
    expenses = []
    attendance = []
    notes = []


# ---------------- SAVE DATA ----------------

def save_data():
    data = {
        "assignments": assignments,
        "expenses": expenses,
        "attendance": attendance,
        "notes": notes
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# ---------------- MAIN PROGRAM ----------------

while True:

    print("\n================================")
    print("      STUDENT LIFE ORGANIZER")
    print("================================")

    print("1. Add Assignment")
    print("2. View Assignments")
    print("3. Add Expense")
    print("4. View Expenses")
    print("5. Track Attendance")
    print("6. View Attendance")
    print("7. Add Note")
    print("8. View Notes")
    print("9. Exit")

    choice = input("\nEnter your choice: ")


    # ---------------- ASSIGNMENT ----------------

    if choice == "1":

        assignment = input("Enter assignment name: ")
        deadline = input("Enter deadline: ")

        assignments.append({
            "name": assignment,
            "deadline": deadline
        })

        save_data()

        print("\nAssignment added successfully!")


    elif choice == "2":

        print("\n===== YOUR ASSIGNMENTS =====")

        if len(assignments) == 0:
            print("No assignments added yet.")

        else:

            for i, assignment in enumerate(assignments, start=1):

                print(f"{i}. {assignment['name']}")
                print(f"   Deadline: {assignment['deadline']}")
                print("------------------------")


    # ---------------- EXPENSE ----------------

    elif choice == "3":

        expense_name = input("Enter expense name: ")

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if amount < 0:
            print("Amount cannot be negative.")
            continue

        expenses.append({
            "name": expense_name,
            "amount": amount
        })

        save_data()

        print("\nExpense added successfully!")


    elif choice == "4":

        print("\n===== YOUR EXPENSES =====")

        if len(expenses) == 0:
            print("No expenses added yet.")

        else:

            total = 0

            for i, expense in enumerate(expenses, start=1):

                print(f"{i}. {expense['name']} - ₹{expense['amount']}")

                total += expense["amount"]

            print("------------------------")
            print(f"Total Expense: ₹{total}")


    # ---------------- ATTENDANCE ----------------

    elif choice == "5":

        subject = input("Enter subject name: ")

        try:
            total_classes = int(input("Enter total classes: "))
            attended_classes = int(input("Enter classes attended: "))
        except ValueError:
            print("Please enter numbers only.")
            continue

        if total_classes <= 0:
            print("Total classes must be greater than 0.")
            continue

        if attended_classes < 0 or attended_classes > total_classes:
            print("Invalid number of attended classes.")
            continue

        percentage = (attended_classes / total_classes) * 100

        attendance.append({
            "subject": subject,
            "percentage": round(percentage, 2)
        })

        save_data()

        print(f"\nAttendance: {percentage:.2f}%")

        if percentage >= 75:
            print("Attendance is above 75%.")

        else:
            print("Warning: Attendance is below 75%!")


    elif choice == "6":

        print("\n===== ATTENDANCE =====")

        if len(attendance) == 0:
            print("No attendance records yet.")

        else:

            for record in attendance:

                print(
                    f"{record['subject']} : "
                    f"{record['percentage']}%"
                )

                print("------------------------")


    # ---------------- NOTES ----------------

    elif choice == "7":

        note = input("Enter your note: ")

        if note.strip() == "":
            print("Note cannot be empty.")
            continue

        notes.append(note)

        save_data()

        print("\nNote added successfully!")


    elif choice == "8":

        print("\n===== YOUR NOTES =====")

        if len(notes) == 0:
            print("No notes added yet.")

        else:

            for i, note in enumerate(notes, start=1):

                print(f"{i}. {note}")


    # ---------------- EXIT ----------------

    elif choice == "9":

        print("\nThank you for using Student Life Organizer!")
        print("Good luck with your studies! 📚")

        break


    # ---------------- INVALID INPUT ----------------

    else:

        print("\nInvalid choice.")
        print("Please enter a number from 1 to 9.")