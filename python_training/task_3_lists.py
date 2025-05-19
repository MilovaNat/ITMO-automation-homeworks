l = [1, 2, 3, 4, "6"]

print("l[2]=", l[2])

print("l[1:3]=", l[1:3])

l[4] = 2

print(l)

for element in l:
    print(element)

print(len(l))

l.append(5)
print(l)