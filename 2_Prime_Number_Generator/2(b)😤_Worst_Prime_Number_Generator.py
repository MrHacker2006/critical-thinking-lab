
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


num_to_print = int(input("How many Primes Number you want? : "))

count_found = 0    # Kitne prime numbers mile 
current_num = 2   # Checking yaha se chalu karenge , because 2 is the smallest prime number

while count_found < num_to_print:
    if isPrime(current_num): 
        print(current_num, end=" ")
        count_found += 1
    
    current_num += 1
      
