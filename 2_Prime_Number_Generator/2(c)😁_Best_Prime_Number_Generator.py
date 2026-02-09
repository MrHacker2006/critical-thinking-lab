import math 

def isPrime(N):
    if N<=1:
        return False
    if N==2: 
        return True
    if N % 2 == 0:
        return False  # Even numbers ko pehle hi hata do (Speed up)
    
    # Loop sirf Square Root tak chalega (step=2, odd numbers only)
    limit = int(math.sqrt(N)) + 1

    for i in range(3, limit, 2):
      if N%i == 0:
          return False
      
    return True

num_to_print = int(input("How many Primes Number you want? : "))

count_found = 0

current_num = 2

while count_found< num_to_print:
   if isPrime(current_num):
       print(current_num, end=" ")
       count_found += 1

   current_num += 1