
def calculator():
    print("**Simple Calculator**")
    print("------------------------")
#definig operations
    print("**Operations:**")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

#getting input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    choice = input("Enter operation choice (1/2/3/4): ")
    
#check cases
    if choice == "1":
        result = num1 + num2
        print(f"Result : {num1} + {num2} = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"Result : {num1} - {num2} = {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"Result : {num1} * {num2} = {result}")
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"Result : {num1} / {num2} = {result}")
        else:
            print("**Error:** Division by zero is not allowed.")
    else:
        print("**Invalid Choice:** Please try again.")

def main():
    calculator()
    while True:
     response = input("Do you want to calculate again? (yes/no): ")
     if response.lower() == "yes":
        calculator()
     elif  response.lower()=="no":
         print("Goodbye!")
         return
     else :
        print("invalid option") 
       # return  
    #  else:
    #     print("**Invalid option**")       

if __name__ == "__main__":
    main()


