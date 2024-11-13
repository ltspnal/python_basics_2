import math

a = int(input())
b = int(input())
x = int(input())

y = 5 * x + (3 * x) ** 2 * math.sqrt(1 + math.sin(x)**2)

print(y)