def CheckPrime(x):
    limit=int(x/2)+1
    for i in range(2,limit):
        rem=x%i
        if rem==0:
            print(x,"is a coprime number")
            break
        else:
            print(x,"is a prime number")
num=int(input("enter number to check whether it's (prime/coprime):"))
CheckPrime(num)
