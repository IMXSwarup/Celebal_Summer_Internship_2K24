import math as meow

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Undefined."
    else:
        return num1 / num2

def modulus(num1, num2):
    return num1 % num2


def main():
    while True:
        print("Simple Calculator \n" \
              "1. Add\n" \
              "2. Subtract\n" \
              "3. Multiply\n" \
              "4. Divide\n" \
              "5. Modulus\n" \
              "6. To the power of\n" \
              "7. Square Root\n" \
              "8. Factorial\n" \
              "0. Quit\n")

        try:
            select = int(input("Select operation from 1, 2, 3, 4, 5, 6, 7, 8, or 0 to quit: "))

            if select == 0:
                print("Quitting the program. Goodbye!")
                break

            if select in [1, 2, 3, 4, 5, 6]:
                number_1 = float(input("Enter first number: "))
                number_2 = float(input("Enter second number: "))

                if select == 1:
                    print(f"{number_1} + {number_2} = {add(number_1, number_2)}")
                    
                elif select == 2:
                    print(f"{number_1} - {number_2} = {subtract(number_1, number_2)}")
                    
                elif select == 3:
                    print(f"{number_1} * {number_2} = {multiply(number_1, number_2)}")
                    
                elif select == 4:
                    print(f"{number_1} / {number_2} = {divide(number_1, number_2)}")
                    
                elif select == 5:
                    print(f"{number_1} % {number_2} = {modulus(number_1, number_2)}")
                    
                elif select == 6:
                    print(f"{number_1} ** {number_2} =", meow.pow(number_1, number_2))

            elif select == 7:
                number = float(input("Enter a number: "))
                print(f"Square root of {number} = ", meow.sqrt(number))

            elif select == 8:
                number = int(input("Enter a number: "))
                print(f"Factorial of {number} = ", meow.factorial(number))

            else:
                print("Invalid input! Please enter a number between 1 and 4, or 0 to quit.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number...")

        print("\n")

if __name__ == "__main__":
    main()
