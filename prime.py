n = 20

for i in range(2, n+1):
    b = []

    for j in range(2, i+1):
        if i % j == 0:
            b.append(j)

    if len(b) == 1:
        print(i)


