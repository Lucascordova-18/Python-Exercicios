print("Calculator with functions")

def calculator(x, y):
    def calculation(operator):
        operator = operator.lower()
        if operator == "sum":
            return f"{x} + {y} is the same {x + y}"
        elif operator == "subtraction":
            return f"{x} - {y} is the same {x - y}"
        elif operator == "muiltiplication":
            return f"{x} * {y} is the same {x * y}"
        elif operator == "division":
            if y == 0:
                return "it is not possible to divide by zero"
            return f"{x} / {y} is the same {x / y}"
        else:
            return "You did not type an operation correctly."
    return calculation


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
operator = input("Which operation do you want to use? (sum, subtraction, multiplication, division): ")
calc = calculator(n1, n2)

print(calc(operator))