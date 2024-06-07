def lower(rows): 
    for i in range(rows): 
        for j in range(i + 1): 
            print("*", end=" ")
        print()

def upper(rows): 
    for i in range(rows): 
        for j in range(i):
            print(" ", end="")
        for j in range(rows - i): 
            print("*", end="")
        print()

def pyramid(rows):
    k = 0
    for i in range(1, rows + 1):
        for space in range(rows - i):
            print(end="  ")
        while k != (2 * i - 1):
            print("* ", end="")
            k += 1
        k = 0
        print()

def main():
    while True:
        print("Select the pattern to display:")
        print("1. Lower Triangular")
        print("2. Upper Triangular")
        print("3. Simple Pyramid")
        print("0. Quit")
        
        choice = int(input("Enter your choice (1/2/3/0): "))
        
        if choice == 0:
            print("Quitting the program. Goodbye!")
            break
        
        if choice not in [1, 2, 3]:
            print("Invalid choice! Please enter 1, 2, 3, or 0.")
            continue
        
        rows = int(input("Enter the number of rows: "))
        
        if choice == 1:
            print("\nLower Triangular:\n")
            lower(rows)
        elif choice == 2:
            print("\nUpper Triangular:\n")
            upper(rows)
        elif choice == 3:
            print("\nPyramid:\n")
            pyramid(rows)
        
        print("\n")

if __name__ == "__main__":
    main()
