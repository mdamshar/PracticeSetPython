def simple():
    b = float(input("Enter base value (in cm) : "))
    h = float(input("Enter perpendicular height value (in cm) : "))
    area = 0.5 * b * h 
    print("-----------------------")
    print(f"Area of rectangle is : {area} cm square.")

def rightAngle():
    b = float(input("Enter base value (in cm) : "))
    h = float(input("Enter Perpendicular distance value (in cm) : "))
    area = 0.5 * b * h 
    print("-----------------------")
    print(f"Area of rightAngle is : {area} cm square.")
    print("-----------------------")

def Equilateral():
    side = float(input("Enter Side value : "))
    area = (1.732/4) * side**2
    print("-----------------------")
    print(f"Are of Equilateral traingle is : {area} cm square.")
    print("-----------------------")

def Isosceles():
    a = float(input("Enter value of 1st side : "))
    b = float(input("Enter value of 2nd side : "))
    print("-----------------------")
    area = (1/4 * b)* ((4 * a**2 - b**2)*0.5)
    print("-----------------------")

def herons():
    a = float(input("Enter value of 1st side : "))
    b = float(input("Enter value of 2nd side : "))
    c = float(input("Enter value of 3rd side : "))
    s = ( a + b + c ) / 2
    area = 0.5 * (s*(s-a)*(s-b)*(s-c))
    print("-----------------------")
    print(f"Area pf rectangle is : {area} cm square.")
    print("-----------------------")


while True:
    print("Are of Traingle")
    print("---------------")
    print("1. Area of traingle (if b and h given)")
    print("2. Area of a Right Angled Triangle")
    print("3. Area of an Equilateral Triangle")
    print("4. Area of an Isosceles Triangle")
    print("5. Area of Triangle with Three Sides (Heron’s Formula)")
    print("For exit enter blank")
    op = input("Choice any one : ")
    match op:
        case "1" :
            simple()
        case "2":
            rightAngle()
        case "3":
            Equilateral()
        case "4":
            Isosceles()
        case "5":
            herons()
        case "":
            print("--------")
            print("Exited")
            print("--------")
            break
        
