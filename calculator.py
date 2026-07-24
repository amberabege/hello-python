first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /,): ")
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation =="/":
    print(first_number/second_number)
else:
    print("Invalid operation, cannot perform operation")
