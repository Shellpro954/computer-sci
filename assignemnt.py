print("""
    1
        2
            3
""")

text ="Test. \nNext line."
print(text)

print("One", "Two" * 2)
print("One", "Two" * 2)
print(len("0123456789"))

s = "0123456789"
print(s[3],",",s[0:3],"-",s[2:5])
print(s[:3],"-",s[3:],",",s[3:100])
print(s[20:],s[2:1],s[1:1])
s = "987654321"
print(s[-1],s[-3])
print(s[-3:],s[:-3])
print(s[-100:-3], s[-100:3])

y = str(123)
x= "hello" * 3
print(x,y)
x="hello" + "world"
y = len(x)
print(y,x)

x = "hello" + \
"to python" + \
"world"
for char in x :
    y = char
    print(y,":", end = "")
    
x = "hello world"
print(x[:2], x[:-2], x[-2:])
print(x[6], x[2:4])
print(x[2:-3],x[-4:-2])

thestr = "this is a test "
inputstr = input("enter an integer: ")
inputint = int(inputstr)
teststr = thestr
while inputint >=0:
    teststr = teststr[1:-1]
    inputint = inputint - 12
testbool = "t" in teststr
print(thestr)
print(teststr)
print(inputint)
print(testbool)

teststr = "abcdefghi"
inputstr = int(input("enter an int: "))
count = 2
newstr = ""
while count <= inputstr:
    newstr = newstr +teststr[0 : count]
    teststr = teststr[2:-1]
    count = count + 1
print(newstr)
print(teststr)
print(count)
print(inputstr)

inputstr = input("give me a string: ")
bigint = 0
littleint = 0
otherint = 0
for ele in inputstr:
    if ele >= "a" and ele <="m":
        littleint = littleint + 1
    elif ele > "m" and ele <= "z":
        bigint = bigint + 1
    else:
        otherint = otherint + 1
print(bigint)
print(littleint)
print(otherint)
print(inputstr.isdigit())

in1str = input("enter a string of digits")
in2str = input("enter a string of digits")

if len (in1str)>len(in2str):
    small = in2str
    large = in1str
else:
    small = in1str
    large = in2str
newstr = ""
for element in small:
    result = int(element) + int(large[0])
    newstr = newstr + str(result)
    large = large[1:]
print(len(newstr))
print(newstr)
print(large)
print(small)

s = input("enter string :")
rs = ""
for ch in s :
    rs = ch+rs
print(s+rs)

# s = input("enter string :")
# rs = ""
# for ch in s :
#    rs = ch+2+s
# print(s+rs)

# s = "pura vida"
# print(s[9] + s[9:15]

