import sys

a = int(input())
b = 0

for i in range(0, a, 1):
    c = int(sys.stdin.readline())
    b += c
b = b - (a - 1)

print(b)