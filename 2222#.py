side1 = int(input("what is the length of your first side "))
side2= int(input("what is the length of your second side "))
side3 = int(input("what is the length of your third side "))
if side1 == side2 == side3:
    print ("your triangle is an equalitaral")
if side1 == side2 or side2 == side3 or side3 == side2:
        print ("your triangle is a isosceles")
else:
     print ("your triangle is a scalene")
     
digit = input("enter any digit ")
if digit[-1] == "4":
    print ("your digit ends in a 4")  
elif digit[-1] == "8":
    print("your digit ends in a 8")
else:
    print ("your digit ends in neither")
    
number = int(input("pick a number less than 20 "))
if number < 20:
    for i in range(11, number + 1):
        if i % 3 == 0:
            print ("tipsy")
        if i % 7 == 0:
            print("topsy")
        if i % 7 == 0 and i % 3 == 0:
            print("tipsy topsy")
        print (i)
        
M = int(input("Pick a number "))
N = int(input("Pick another number "))
for m in range(1, M +1):
    if m % N == 0:
        print ( m )
        if m % 2 == 0:
            print("can be divided by an even number")
        else:
            print("can be divided by an odd number")
            
q = int(input("pick any number "))

for Q in range(1, q, 2):
     sums = Q ** 2
     summ = (1**2) + (3**2) + (5**2) + (sums) + (q ** 2)
     if Q == q-1:
         print(summ)
         
C = float(input("whats your temp in celcius "))
F = (C * 9/5) + 32
if F < -273.15:
    print ("your temp is invaild as it is below absoulte zero")
if F == -273.15:
    print("your temp is absoulte zero")
if 0 > F > -273.15:
    print("your temp is below zero")
if F == 0:
    print("your temp is at freezing point")
if 0 < F < 100:
    print("your temp is in a normal range")
if F == 100:
    print("your temp is at boiling point")
if F > 101:
    print("your temp is above boiling point")

        
    
    
    