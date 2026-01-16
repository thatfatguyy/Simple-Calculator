decision=""

while (decision != "n"):
    try:
        a= int(input("Enter a number:"))
        b= int (input("Enter a number:"))
        print("""\nPress:
        A:Addition
        S:Substraction
        M:Multiplication
        D:Division\n""")

        choice=input("Enter the operation you want to do:").lower()
        match choice:
            case "a":
                print(f"\nThe sum of {a} and {b} is {a+b}\n")

            case "s":
                print(f"\nThe difference of {a} and {b} is {a-b}\n")

            case "m":
                print(f"\nThe product of {a} and {b} is {a*b}\n")

            case "d":
                try:
                    print(f"\nThe quoitent of {a} and {b} is {a/b}\n")
                except ZeroDivisionError as e:
                    print("\nCannot be divided by 0.Enter a valid divider\n")

            case _:
                print("\nSomething went wrong!!!\n")
    except ValueError :
        print("\nEnter a valid number.")

 
        
    print("""\nDo you want to continue for more operations:
                    Press \"Y\" for Yes
                    Press \"N\" for No\n""")
    decision=input("Enter your decision:").lower()




