print("Welcome to the tip calculator.")
print("")
# Get the input from the user
bill = float(input("What was the total bill?:\n"))
perc = float(input("What percentage tip would you like to give?:\n"))
people = int(input("How many people to split the bill?:\n"))
print("")

# Calculations
total_bill = bill * (1 + perc/100)
split = "{:.2f}".format(total_bill/people)

# Output the  
print(f"Each person should pay: ${split}") 