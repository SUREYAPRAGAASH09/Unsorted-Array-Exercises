a = [5,6,9,7,7,9,1]
b = []

for i in a:
    if i in b:
        m = i
    else:
        b.append(i)

print (m)
