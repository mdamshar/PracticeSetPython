num = int(input("Enter Number to check prime or not : "))
if num <= 1 :
    print("give only +ve integer or greater  than 1")
else:
    prime = True
    for i in range(2,num):
        if ((num%i) == 0):
            prime = False
            break
if prime == True:
    print(f"{num} is a prime number ")
else: 
    print(f"{num} is not a prime number")