#Creating a Calculator

while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to mutiply two numbers")
    print("Enter 'divid' to divid two numbers")
    print("Enter 'quit' to end program")
    user_input=input(":")
    if user_input=="quit":
        break

    elif user_input=="add":
      num1=float(input("Enter a number:"))
      num2=float(input("Enter another number:"))
      result=str(num1 + num2)
      print("The answer is "  + result)

    elif user_input=="subtract":
      num1=float(input("Enter a number:"))
      num2=float(input("Enter another number:"))
      result=str(num1 - num2)
      print("The answer is " + result)

    elif user_input=="multiply":
      num1=float(input("Enter a number:"))
      num2=float(input("Enter another number:"))
      result=str(num1 * num2)
      print("The answer is " + result)

    elif user_input=="divid":
      num1=float(input("Enter a number:"))
      num2=float(input("Enter another number:"))
      result=str(num1 / num2)
      print("The answer is " + result)

    else:
      print("Unknown input")
