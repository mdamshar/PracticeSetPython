while True:
    a = input("Enter 1st variable : ")
    b = input("Enter 2nd variable : ")
    print(f"1st variable is : {a} and 2nd variable is {b}")
    swap = input("type <S> for Swap / <Q> for quit : ")
    if swap.lower() == "s" :
        a , b = b , a
        print(f"1st variable is : {a} and 2nd variable is {b}")
    else:
        break