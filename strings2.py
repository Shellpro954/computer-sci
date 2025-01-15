userinp = input("Put in a string of characters : ")
for x in userinp:
    print(x)

userinp2 = input("Put in a string of characters : ")
length = len(userinp2)
for i in range(0,length):
    print(userinp2[i])

userinp3 = input("Put in a string of characters : ")
length2 = len(userinp3)
if userinp3 == "":
    userinp3 = input("Put in a string of characters : ")
else:
    while userinp3 != "":
        for o in range(0,length2):
             print(userinp3[o])
        break
    
userinp4 = input("Put in a string : ")
length3 = len(userinp4)
for p in range(0,length3):
    if userinp4[p].isupper():
        print(userinp4[p].lower())
    else:
        userinp4[p].upper()
        print(userinp4[p].upper())
        
        
userinp5 = input("Put in a string : ")
length3 = len(userinp4)
for p in userinp4:
    if p.isupper():
        print(p.lower())
    else:
        p.upper()
        print(p.upper())
        
userinp6 = input("Put in a string : ")
length4 = len(userinp5)
num = 0
while num < length4:
    if userinp5[num].isupper():
        print (userinp5[num].lower())
        num += 1
    else:
        print (userinp5[num].upper())
        num += 1
        
userinp7 = input("Put in a string : ")
length5 = len(userinp7)
string = ""
for t in range(0,length5):
    string += userinp7[t] * 2
print(string)
    
