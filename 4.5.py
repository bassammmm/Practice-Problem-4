print("Muhammad Bassam")
print("18B-077-CS(A)")
print("\n\nPractice Problem 4.5\n\n")


first  = input("Please enter your First name   : ")
last   = input("Please enter your Last name    : ")
street = input("Please enter your Street name  : ")
number = input("Please enter your Street number: ")
city   = input("Please enter your City         : ")
state  = input("Please enter your State        : ")
zcode  = input("Please enter your Zip Code     : ")

print('\nYour Mailing address is :-\n\n{0} {1}\n{3} {2}\n{4},{5} {6}'.format(first.title(),last.title(),street.title(),number,city.title(),state.title(),zcode))
