import json
import os

def load_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    print("File not found.")
    return []

def save_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print("File saved successfully.")

def show_data(data):
    if not data:
        print("No student records found.")
    else:
        for r in data:
            print(r)

def sort_data(data, key_index, reverse=False):
    return sorted(data, key=lambda x: x[key_index], reverse=reverse)

def calculate_average(record):
    return record[2] * 0.6 + record[3] * 0.4

def menu():
    data = []
    filename = ""

    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Show all Records")
        print("4. Sort by Last Name")
        print("5. Sort by Grade")
        print("6. Show Student Record")
        print("7. Add Record")
        print("8. Edit Record")
        print("9. Delete Record")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the filename: ")
            data = load_file(filename)
        elif choice == "2":
            if filename:
                save_file(filename, data)
            else:
                print("Enter filename first.")
        elif choice == "3":
            show_data(data)
        elif choice == "4":
            data = sort_data(data, 2)
            show_data(data)
        elif choice == "5":
            data = sorted(data, key=calculate_average, reverse=True)
            show_data(data)
        elif choice == "6":
            student_id = input("Enter the student ID: ")
            found = next((r for r in data if r[0] == student_id), None)
            print(found if found else "Student not found.")
        elif choice == "7":
            data.append((input("ID: "), input("First Name: "), input("Last Name: "), float(input("Class Standing: ")), float(input("Exam Grade: "))))
        elif choice == "8":
            student_id = input("ID to edit: ")
            for i, r in enumerate(data):
                if r[0] == student_id:
                    data[i] = (student_id, input("First Name: "), input("Last Name: "), float(input("Class Standing: ")), float(input("Exam Grade: ")))
                    break
            else:
                print("Student not found.")
        elif choice == "9":
            student_id = input("ID to delete: ")
            data = [r for r in data if r[0] != student_id]
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
