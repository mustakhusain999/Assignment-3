# Task 1: Calculate Factorial Using a Function

ui = input("Enter a number: ")

if "." in ui:
    print("Factorial does not exist for float numbers.")
else:
    a = int(ui)

    def factorial(n):
        if n < 0:
            return "Factorial does not exist for negative numbers."
        elif n == 0 or n == 1:
            return 1
        else:
            return n * (factorial(n - 1))

    result = factorial(a)
    print(f"Factorial of {a} is:",result)