num1 = float(input("Enter 1st value : "))
num2 = float(input("Enter 2nd value : "))
num3 = float(input("Enter 3rd value : "))
if num1 > num2 and num1 > num3:
    print(f"largest number is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"largest number is {num2}")
else:
    print(f"largest number is {num3}")
    