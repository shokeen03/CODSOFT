
print("**********Welcome to the Calculator**********")
print("Arithmetic Operations:")
print("Press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")

operator=int(input("Enter your Choice: "))

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

if operator==1:
  print("Result:",x+y)
elif operator==2:
  print("Result:",x-y)
elif operator==3:
 print("Result:",x*y)
elif operator==4:
  print("Result:",x/y)
else:
  print("*****Invalid choice*****")
