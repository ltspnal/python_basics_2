import math

a = int(input())
b = int(input())
x = int(input())

y = (math.cos(x**2)**2 + math.sin(2 * x - 1)**2)**(1/3)

print(y)