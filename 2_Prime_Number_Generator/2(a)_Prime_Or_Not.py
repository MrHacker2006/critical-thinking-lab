def isPrime(N):
    counter = 0
    if N<1:
        print("Please Enter a Positive Number.")
        return False
    elif N>1:
        for i in range(1, N//2 + 1):   # int((N+2)/2)
            if N%i==0:
                counter +=1
        if(counter == 1):
            return True
        else:
            return False

N = int(input("Enter a Number, to check if it is a Prime or Not: "))
if isPrime(N):
    print("The Give number is Prime Number")
else:
    print("Not a Prime.")