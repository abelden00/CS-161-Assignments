# CS 161 Combined Assignment
# This program demonstrates:
# 1) Using variables and f-strings
# 2) Using input statements and f-strings
# 3) Calculating the number of seconds in the current month
# 4) Using integer division (//) and remainder (%) operators

# -------------------------------------------------
# PART 1: Pet type and name using an f-string
# -------------------------------------------------

pet_type = "dog"
pet_name = "Millie"

print(f"I have a {pet_type} and her name is {pet_name}.")

# -------------------------------------------------
# PART 2: User input and formatted output
# -------------------------------------------------

# Ask the user for basic information
first_name = input("Ashley")
current_age = int(input("25 "))
yearly_savings = float(input("1200 "))

# Display results using f-strings
print(f"Hello {first_name}! You are currently {current_age} years old.")
print(f"In 10 years, you will be {current_age + 10} years old.")
print(f"If you save ${yearly_savings:.0f} each year, in 5 years you will have saved ${yearly_savings * 5:.0f}.")
print(f"Your average monthly savings is ${yearly_savings / 12:.2f}.")

# -------------------------------------------------
# PART 3: Seconds in the current month (using libraries)
# -------------------------------------------------

# Import libraries for date and calendar calculations
import datetime
import calendar

# Get today's date
today = datetime.date.today()

# Get the current year and month
year = today.year
month = today.month

# Determine the number of days in the current month
days_in_month = calendar.monthrange(year, month)[1]

# Calculate seconds in the month
seconds_in_day = 24 * 60 * 60
seconds_in_month = days_in_month * seconds_in_day

# Print result using an f-string
print(f"The number of seconds in the current month is {seconds_in_month}.")

# -------------------------------------------------
# PART 4: Dozen eggs calculation using // and %
# -------------------------------------------------

# Ask the user for the number of eggs
eggs = int(input("Enter the number of eggs: "))

# Calculate full dozens and remaining eggs
dozens = eggs // 12
remaining_eggs = eggs % 12

# Print result using an f-string
print(f"This makes {dozens} dozen eggs with {remaining_eggs} left over.")