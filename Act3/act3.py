# Define first name and last name
first_name = str(input("Enter First name: "))
last_name =str(input("Enter Last name: "))

# Concatenate to form full name
full_name = first_name + " " + last_name

# Slice the first three characters of the first name
sliced_first_name = first_name[:3]

# Create a greeting message using string formatting
greeting_message = f"Hello, {sliced_first_name}! Welcome to the program."

# Display the results
print("Full Name:", full_name)
print("Sliced First Name:", sliced_first_name)
print("Greeting Message:", greeting_message)
