# Get user input
last_name = input("Enter Last name: ")
first_name = input("Enter First name: ")
age = int(input("Enter Age: "))
contact_num = input("Enter Contact Number: ")
course = input("Enter Course: ")

# Open the file in append mode and write the student details
with open("student.txt", "a") as file:
    file.write(f"Last Name: {last_name}\n")
    file.write(f"First Name: {first_name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Contact Number: {contact_num}\n")
    file.write(f"Course: {course}\n")
    file.write("-" * 30 + "\n")  # Separator for readability

print("Student details saved to student.txt.")
