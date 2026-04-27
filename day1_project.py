
user_name = input("What is your name? ")
user_age = input("How old are you? ")
user_favenumber = input ("what is your favourite number? ")

age_int = int(user_age)
favenumber_int = int(user_favenumber)

magic_number = age_int * favenumber_int

years_left = 100 - age_int

print(f"Hello {user_name}! You have {years_left} years until you turn 100. Your magic number is {magic_number}")
