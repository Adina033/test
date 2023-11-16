n = int(input())
delitel = 0
for i in range (1, n):
    if n % i == 0:
        delitel +=i

if delitel == n:
    print("True")
else:
    print("False")

