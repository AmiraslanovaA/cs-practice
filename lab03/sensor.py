p = int(input(""))
n = int(input(""))
ce = 0
cp = 0
max = -10000000000
sum = 0
for i in range(n):
    x = input("")
    if x == "error":
        ce +=1
    else:
        x = float(x)
        sum += x
        if x > p:
            cp +=1
        if x > max:
            max = x
print(n)
print(ce)
print(cp)
print(f"{max: .1f}")
print(f"{sum/(n-ce): .1f}")
