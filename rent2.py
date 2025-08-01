##user input 
#rent 
#food 
#ELECTRICITY SPEND 
#CAHRGE PER UNIT 
# TOTAL ELECTRICITY BILL
#HOW MANY PERSON LIVING IN THE HOUSE

USER_INPUT = input("entre the  your name = ")
rent  = float(input("Enter your total rent = "))
food = float(input("Enter your total food expenses = "))
electricity_spend = float(input("entre the your room electricity spend = "))
charge_per_unit = float(input("entre the your room charge per unit = "))

total_electricity_bill = electricity_spend * charge_per_unit
how_many_person = int(input("How many person living in the house = "))

total_monthly_expenses = (rent + food + total_electricity_bill) / how_many_person
print("Total monthly expenses per person = ", total_monthly_expenses)
print(f"Hello {USER_INPUT}, here is your monthly expenses summary:")