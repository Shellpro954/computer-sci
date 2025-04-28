sports = ["randombb","randomsock"]
sportimp = input("what is your fav sport!!?")
sports.append(sportimp)
sports.sort()
print(sports)

subjects = ["english","maths","irish","pe","history","geography"]
print(subjects)
subimp = input("out of these subjects which do you not enjoy? ")
subimp.lower()
if subimp in subjects:
    subjects.remove(subimp)
    print(subjects)
else:
    print("cuh yo subjc aint in tha list broski")

colors = ["red","yellow","orange","green","cyan","blue","purple","indigo","pink","lime"]
start = int(input("pick a starting number "))
end = int(input("pick an ending number "))
print(colors[start-1:end+1])

digits = [123,321,999,777]
for i in range(0,4):
    print(digits[i])
digitinp = int(input("pick a digit "))
if digitinp in digits:
    digits.index(digitinp)
    print(digits.index(digitinp))
else:
    print("your number is not in the list")
    num = 0
    print(list[num])
    num += 1
