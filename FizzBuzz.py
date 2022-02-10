#Amogh T.
#Mr. Sedlar
#3rd February 2022
#FizzBuzz Lab

for x in range(1, 101): #sets range to not include 0
    if x % 15 == 0:
        print ("FizzBuzz") #when divisible by 15 (so both 3 and 5) replace value with "FizzBuzz"
    elif x % 3 == 0:
        print ("Fizz") #when divisible by 3 replace value with "Fizz"
    elif x % 5 == 0:
        print ("Buzz") #when divisible by 5 replace value with "Buzz"
    else:
        print(x) #if not divisble by 3, 5, or 15 print regular number