import csv  

# Dictionary to store exchange rates
currency_rates = {}

# Read the CSV file and store exchange rates
with open("currency.csv", mode="r", encoding="utf-8", errors="replace") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    for row in reader:
        if len(row) >= 3:  # Ensure row has at least 3 columns (code, name, rate)
            currency_code = row[0].strip()
            exchange_value = row[2].strip()

            if exchange_value.replace(".", "").isdigit():  # Check if rate is a valid number
                currency_rates[currency_code] = float(exchange_value)

# Get user input
usd_balance = input("\nHow much dollar do you have? ")

while not usd_balance.replace(".", "").isdigit() or float(usd_balance) <= 0:
    print("Invalid input! Please enter a valid positive number.")
    usd_balance = input("\nHow much dollar do you have? ")

usd_balance = float(usd_balance)  # Convert to float after validation
desired_currency = input("What currency do you want to have? ").strip().upper()

while desired_currency not in currency_rates:
    print("Invalid currency code. Please try again.")
    desired_currency = input("What currency do you want to have? ").strip().upper()

# Perform conversion
final_amount = usd_balance * currency_rates[desired_currency]

# Display results
print(f"\nDollar: {usd_balance:.2f} USD")
print(f"{desired_currency}: {final_amount:.9f}")  # 9 decimal places