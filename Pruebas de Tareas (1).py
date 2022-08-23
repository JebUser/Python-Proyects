cad  = "ab++cd+"
lis = []
for e in range(len(cad)):
    if cad[e] == "+":
        for i in range(e):
            lis.append(cad[i])
        break
print(lis)