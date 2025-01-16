#Question 1

temp = int(input("Temp for water "))
if temp < 32:
    print("ice")
elif temp < 212:
    print("water")
else :
    print("steam")
    
#Question 2

x = 1
if x > 3 :
    if x > 4:
        print("A", end = " ")
    else:
        print("B",end = " ")
elif x < 2:
    if (x !=0):
        print("C", end = " ")
print("D")

#Question 3

weather = "raining"
if weather == "sunny":
    print("wear sunblock")
elif weather == "snow":
    print("going skiing")
else :
    print(weather)
    
#Question 4
zero = 0
if int(zero) == 0:
    print("zero")
elif str(0) == "zero":
    print(0)
elif str(0) == "0 ":
    print(str(0))
else:
    print("none of the above")
    
#Question 5
    
n = 3
if n == 0:
    print("zero")
elif  n == 1:
    print("one")
elif n == 2:
    print("two")
else:
    n == 3
    print("three")
    
# Question 6
n = int(input("Enter an integer: "))
if n < 1:
    print("invaild value")
else :
    for i in range(1, n + 1):
        print(i * i)
        
#Question 7
n = int(input("Enter an int: "))
if n > 0:
    for a in range(1,n+n):
        print(a/(n/2))
    else :
        print("Now qutting")
        
n= int(input("Enter an int: "))
if n > 0:
    for a in range(1,n+n):
        print(a/(n/2))
else :
    print("Now qutting")
    
#Question 8 (A)
i = 100
for t in range(i,0,-3):
    print(t)
    
# Question 8 (B)
num = int(input("pick a number "))
for i in range(num, 0):
    print(num % 10)
    num = num/10
    
    

        