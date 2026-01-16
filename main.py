a= int(input("Enter a number:"))
b= int (input("Enter a number:"))

print("""ENTER:
      A:Addition
      S:Substraction
      M:Multiplication
      D:Division""")

choice=input("Enter the operation you want to do:").lower()

match choice:
    case "a":
        print(f"The sum of {a} and {b} is {a+b}")

    case "s":
        print(f"The difference of {a} and {b} is {a-b}")

    case "m":
        print(f"The product of {a} and {b} is {a*b}")

    case "d":
        try:
            print(f"The quoitent of {a} and {b} is {a/b}")
        except ZeroDivisionError as e:
            print(" Cannot be divided by 0.Enter a valid divider")

    case _:
        print("Something went wrong!!!")




