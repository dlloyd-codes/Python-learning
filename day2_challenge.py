hour_wage = float(input("How much do you earn per hour?"))
weekly_hours = float(input("How many hours did you work this week?"))
days_worked = input("how many days did you work?")
pay = hour_wage * weekly_hours
print(f"your wage for this week is £ {pay} ")

print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? £"))
tip_percentage = int(input("what percentage of tip would you like to give? 10, 12, or 15?"))
people = int(input("how may people to split the bill?"))
tip_percentage = tip_percentage / 100
total_tip = tip_percentage * bill
final_bill = bill + total_tip
print(f"Your final bill will be £{final_bill:.2f}. your bill per person is £{final_bill / people:.2f}.")

print("Bill!")
billl = float(input("what is the total bill? £"))
tip = float(input("how much tip would you like to leave? £"))
ppl = int(input("how many people is the bill being split by?"))
ttl = billl + tip
print(f"Total bill is £{billl + tip: .2f} Price per person is £{(billl + tip)/ ppl: .2f}.")



            
      
      







