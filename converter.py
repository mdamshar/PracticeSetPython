def time_converter():
    print("-----------------------------")
    print("1. Minute to Second")
    print("2. Minute to Hour")
    print("3. Hour to Minute")
    print("4. Hour to Second")
    print("5. Second to Minute")
    print("6. Second to Hour")
    op = int(input("Choose any one option: "))

    match op:
        case 1:
            minute = float(input("Enter minutes: "))
            print(f"{minute} minute = {minute * 60} seconds")

        case 2:
            minute = float(input("Enter minutes: "))
            print(f"{minute} minute = {minute / 60} hours")

        case 3:
            hour = float(input("Enter hours: "))
            print(f"{hour} hour = {hour * 60} minutes")

        case 4:
            hour = float(input("Enter hours: "))
            print(f"{hour} hour = {hour * 3600} seconds")

        case 5:
            second = float(input("Enter seconds: "))
            print(f"{second} second = {second / 60} minutes")

        case 6:
            second = float(input("Enter seconds: "))
            print(f"{second} second = {second / 3600} hours")

        case _:
            print("Invalid option")


def volume_converter():
    print("-----------------------------")
    print("1. Liter to Milliliter")
    print("2. Milliliter to Liter")
    option = int(input("Choose any one option: "))

    match option:
        case 1:
            liter = float(input("Enter liters: "))
            print(f"{liter} L = {liter * 1000} ml")

        case 2:
            ml = float(input("Enter milliliters: "))
            print(f"{ml} ml = {ml / 1000} L")

        case _:
            print("Invalid option")


def length_converter():
    print("-----------------------------")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Meter to Inches")
    print("4. Inches to Meter")
    option = int(input("Choose any one option: "))

    match option:
        case 1:
            meter = float(input("Enter meters: "))
            print(f"{meter} m = {meter / 1000} km")

        case 2:
            km = float(input("Enter kilometers: "))
            print(f"{km} km = {km * 1000} m")

        case 3:
            meter = float(input("Enter meters: "))
            print(f"{meter} m = {meter * 39.3701} inches")

        case 4:
            inches = float(input("Enter inches: "))
            print(f"{inches} inches = {inches * 0.0254} m")

        case _:
            print("Invalid option")


def temperature_converter():
    print("-----------------------------")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    option = int(input("Choose any one option: "))

    match option:
        case 1:
            c = float(input("Enter Celsius: "))
            print(f"{c} °C = {(c * 9/5) + 32} °F")

        case 2:
            c = float(input("Enter Celsius: "))
            print(f"{c} °C = {c + 273.15} K")

        case 3:
            f = float(input("Enter Fahrenheit: "))
            print(f"{f} °F = {(f - 32) * 5/9} °C")

        case 4:
            f = float(input("Enter Fahrenheit: "))
            print(f"{f} °F = {(f - 32) * 5/9 + 273.15} K")

        case 5:
            k = float(input("Enter Kelvin: "))
            print(f"{k} K = {k - 273.15} °C")

        case 6:
            k = float(input("Enter Kelvin: "))
            print(f"{k} K = {(k - 273.15) * 9/5 + 32} °F")

        case _:
            print("Invalid option")


def mass_converter():
    print("-----------------------------")
    print("1. Kilogram to Gram")
    print("2. Gram to Kilogram")
    option = int(input("Choose any one option: "))

    match option:
        case 1:
            kg = float(input("Enter kilograms: "))
            print(f"{kg} kg = {kg * 1000} g")

        case 2:
            g = float(input("Enter grams: "))
            print(f"{g} g = {g / 1000} kg")

        case _:
            print("Invalid option")


def bitbyte_converter():
    print("-----------------------------")
    print("1. Bytes to Bits")
    print("2. Bits to Bytes")
    print("3. MB to KB")
    print("4. KB to MB")
    print("5. MB to GB")
    print("6. GB to MB")
    print("7. GB to TB")
    print("8. TB to GB")
    option = int(input("Choose any one option: "))

    match option:
        case 1:
            b = float(input("Enter bytes: "))
            print(f"{b} Bytes = {b * 8} bits")

        case 2:
            bits = float(input("Enter bits: "))
            print(f"{bits} bits = {bits / 8} Bytes")

        case 3:
            mb = float(input("Enter MB: "))
            print(f"{mb} MB = {mb * 1024} KB")

        case 4:
            kb = float(input("Enter KB: "))
            print(f"{kb} KB = {kb / 1024} MB")

        case 5:
            mb = float(input("Enter MB: "))
            print(f"{mb} MB = {mb / 1024} GB")

        case 6:
            gb = float(input("Enter GB: "))
            print(f"{gb} GB = {gb * 1024} MB")

        case 7:
            gb = float(input("Enter GB: "))
            print(f"{gb} GB = {gb / 1024} TB")

        case 8:
            tb = float(input("Enter TB: "))
            print(f"{tb} TB = {tb * 1024} GB")

        case _:
            print("Invalid option")


print("Welcome to Converter Portal")
print("-----------------------------")
print("1. Time Converter")
print("2. Volume Converter")
print("3. Length Converter")
print("4. Temperature Converter")
print("5. Mass Converter")
print("6. Bit & Byte Converter")

choice = int(input("Choose any one option: "))

match choice:
    case 1:
        time_converter()
    case 2:
        volume_converter()
    case 3:
        length_converter()
    case 4:
        temperature_converter()
    case 5:
        mass_converter()
    case 6:
        bitbyte_converter()
    case _:
        print("Invalid option")
