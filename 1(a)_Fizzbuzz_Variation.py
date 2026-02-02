num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)

for i in range(1,101):
    if i/3 in num and i/5 not in num :
      print("Fizz")
    elif i/5 in num and i/3 not in num:
       print("Buzz")
    elif (i/3 in num) and (i/5 in num):     # wrong --> elif (i/3 and i/5) in num:
       print("FizzBuzz")
    else:
      print(i)