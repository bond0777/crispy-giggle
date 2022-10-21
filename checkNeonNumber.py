import math

Number = int(input("Enter the Number to Check Neon Number = "))
Sum = 0

squr = math.pow(Number, 2)
print("Square of a Given Digit = %d" %squr)

while squr > 0:
    rem = squr % 10
    Sum = Sum + rem
    squr = squr // 10

print("The Sum of the Digits   = %d" %Sum)

if Sum == Number:
    print("\n%d is a Neon Number." %Number)
else:
    print("%d is Not a Neon Number." %Number)
