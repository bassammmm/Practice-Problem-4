print("Muhammad Bassam")
print("18B-077-CS(A)")
print("\n\nPractice Problem 4.4\n\n")

def even(num):
    for x in range(2,num):
        if x%2==0 or x%3==0:
            print(x,end=", ")

user = int(input("Please enter a number :"))
even(user)

