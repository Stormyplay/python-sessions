calculator_function= int(input("calculator"))

num1 = int(input("number1:"))
num2 = int(input("number 2:"))

print("Welcome to the smart calcultor")
print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
print("Press 5 for modulus")
print("Press 6 for power")

choice = int(input("Enter your choice: "))
if choice == 1:
    print("result is equal to:", num1 + num2)
elif choice == 2:
    print("result is equal to:", num1 - num2)
elif choice == 3:
    print("result is equal to:", num1*num2)
elif choice == 4:
    print("result is equal to:", num1/num2)
elif choice == 5:
    print("result is equal to:", num1%num2)
elif choice == 6:
    print("result is equal to:", num1**num2)