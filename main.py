
n, m = tuple(map(int, input().split()))

f = list(map(int, input().split()))
f.sort()

s = f[:n]
diff = s[-1] - s[0]
for i in range(1, m - n + 1):
    s = f[i:i+n]
    a = s[-1] - s[0]

    if a < diff: diff = a

print(diff)
