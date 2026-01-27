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
    print("1. Liters to milileter")
    print("2. Milileters to Leter")
    option = int(input("Choose any one option : "))
    match option:
        case 1:
            liter = float(input("Enter leter value : "))
            ml = liter*1000
            print(f"{liter} L = {ml} ml")
        case 2:
            ml = float(input("Enter ml value : "))
            l = ml/1000
            print(f"{ml} ml = {l} L" )

def length():
    print("1. meter to Km")
    print("2. Km to meter")
    print("3. meter to inches")
    print("4. inches to meter")
    option = int(input("Choose any one option : "))
    match option:
        case 1:
            meter = float(input("Enter meter value : "))
            km = meter * 0.001000
            print(f"{meter} m = {km} km")
        case 2:
            km = float(input("Enter km value : "))
            meter = km * 1000
            print(f"{km} Km = {meter} m")
        case 3:
            meter = float(input("Enter meter value : "))
            inches = meter * 39.370079
            print(f"{meter} m = {inches} inch")
        case 4:
            inches = float(input("Enter inch value : "))
            meter = inches * 0.025400
            print(f"{inches} inch = {meter} m")            
            
def temprature():
    print("1. Celcius to Fohrenhite")
    print("2. Celcius to Kelvin")
    print("3. Fohrenhite to celcius")
    print("4. Fohrenhite to kelvin")
    print("5. Kelvin to celcius")
    print("6. Kelvin to Fohrenhite")
    option = int(input("Choose any one option : "))
    match option:
        case 1:
            c = float(input("Enter celcius value : "))
            f = c * 33.800000
            print(f"{c} celcius = {f} Fohrenhite")
        case 2:
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