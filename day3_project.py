print("Welcome to the cinema!")
age = int(input("Please enter your age:"))

if age <12:
    price = 5
    print("Child ticket: £5")
elif age <18:
    price = 8
    print("Youth ticket: £8")
else:
    price = 12
    print("Adult Ticket: £12")

#popcorn input
pop = input("Would you like to add popcorn to your order? Y/N")
if pop == "Y" or pop == "y":
    price = price + 4
    print("Popcorn added at £4 extra, price to pay below")

#drink input
drink = input("Would you like to add a drink for £2 extra? Y/N")
if drink in ["Y", "y"]:
    price = price + 2
    print("Your drink has been added to your order!")

print(f"Total to pay £{price: .2f}.")






