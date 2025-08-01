##INPUT FROM USER
#USER NAME 
# TOTAL RENT 
#TOTAL  FOOD ORDER BY SANKING 
# TOTAL ELECTRICITY BILL
# TOTAL WATER BILL
# TOTAL INTERNET BILL
# TOTAL GROCERY BILL
# TOTAL OTHER EXPENSES
# TOTAL MONTHLY EXPENSES

#OUTPUT 
# TOTAL MONTHLY EXPENSES
# TOTAL RENT 
#TOTAL  FOOD ORDER BY SANKING 
# TOTAL ELECTRICITY BILL
# TOTAL WATER BILL
# TOTAL INTERNET BILL
# TOTAL GROCERY BILL
# TOTAL OTHER EXPENSES


user_name = input("Enter your name = ")
total_rent = float(input("Enter your total rent = "))
total_food = float(input("Enter your total food expenses = "))
total_electricity = float(input("Enter your total electricity bill = "))
total_water = float(input("Enter your total water bill = "))
total_internet = float(input("Enter your total internet bill = "))
total_grocery = float(input("Enter your total grocery bill = "))
total_other = float(input("Enter your total other expenses = "))

total_monthly_expenses = (total_rent + total_food + total_electricity + total_water + total_internet + total_grocery + total_other)
print("Total monthly expenses = ", total_monthly_expenses)

print(f"Hello {user_name}, here is your monthly expenses summary:")
