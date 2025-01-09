A = int(input("pick a value for A : "))
B = int(input("pick a value for B : "))
C = int(input("pick a value for C : "))
sum1 = (-B - ((B**2-4*A*C)**0.5))/2*A
sum2 = (-B + ((B**2-4*A*C)**0.5))/2*A
print (sum1)
print (sum2)

A1 = int(input("pick a value for A : "))
B1 = int(input("pick a value for B : "))
C1 = int(input("pick a value for C : "))
if A1 > B1 and  A1 > C1:
    print(A1)
elif B1 > A1 and  B1 > C1:
    print(B1)
elif C1 > A1 and  C1 > B1:
    print(C1)

for i in range (1,51):
    if i% 2 == 0:
        print(i)

n = int(input("pick a value : "))
total = 0
total1 = 1
for i in range (1,n+1,1):
    total += total1
    total1 +=1
    print(total)
    

    

    



