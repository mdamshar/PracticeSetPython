def time():
    print("1. minute to second")
    print("2. minute to hour")
    print("3. hour to minute")
    print("4. hour to second")
    print("5. second to minute")
    print("6.second to hour")
    op = int(input("choose any one option : "))
    match op:
        case 1:
            minute = int(input("Enter minute : "))
            second = minute * 60
            print("-----------------------------")
            print(f"{minute} minute = {second} second")
            print("-----------------------------")
        case 2:
            minute = int(input("Enter minute : "))
            hour = minute / 60
            print("-----------------------------")
            print(f"{minute} minute = {hour} hour")
            print("-----------------------------")
        case 3:
            hour = int(input("Enter Hour : "))
            minute = hour * 60
            print("-----------------------------")
            print(f"{hour} hour = {minute} minute")
            print("-----------------------------")
        case 4:
            hour = int(input("Enter Hour : "))
            second = hour * 3600
            print("-----------------------------")
            print(f"{hour} hour = {second} second")
            print("-----------------------------")
        case 5:
            second = int(input("Enter second : "))
            minute = second/60
            print("-----------------------------")
            print(f"{second} second = {minute} minute") 
            print("-----------------------------")
        case 6:
            second = int(input("Enter second : "))
            hour = second/3600
            print("-----------------------------")
            print(f"{second} second = {hour} hour")
            print("-----------------------------")
            
def volume():
    pass

def length():
    pass

def temprature():
    pass

def mass():
    pass

def bitbytes():
    pass

while True:
    print("Welcome to converter portal")
    print("-----------------------------")
    print("1. Time converter")
    print("2. Volume converter")
    print("3. Length converter")
    print("4. Temprature converter")
    print("5. Mass converter")
    print("6. bitBytes converter")
    option = int(input("type any one option : "))
    match option:
        case 1:
            time()
        case 2:
            volume()
        case 3:
            length()
        case 4:
            temprature()
        case 5:
            mass()
        case 6:
            bitbytes()