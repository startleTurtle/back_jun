a, b = map(int, input().split())

result = 1

for i in range(1, min(a, b) + 1, 1):
    if a % i == 0 and b % i == 0:
        result = i
print(result)

print((a * b) // result)