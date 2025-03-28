a = int(input())
b = list(map(int, input().split()))

count = 0
result = []

if a == len(b):
    for i in range(0, a, 1):
        for j in range(1, b[i] + 1, 1):
            if b[i] % j == 0:
                result.append(b[i])
        if len(result) == 2:
            count += 1
            result = []
        else:
            result = []
print(count)