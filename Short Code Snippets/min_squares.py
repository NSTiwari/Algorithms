import math

t = int(input())
while t>0:
    l, b = map(int, input().split())
    square_side = math.gcd(l, b)
    result = (l*b)/(square_side*square_side)
    print(int(result))
    t=t-1