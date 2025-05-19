def add(x, y):
    return x + y


print(add(1, 2))


def add2(x, y, z = 3):
    return x + y + z

print(add2(1, 2))
print(add2(1, 2, 7))
# print(add2(1, 2, 3.5))

print(add2(1, z=2, y=3.5))

def first_tuple_element(a = (1, 2, 3, 4)):
    return a[0]

print(first_tuple_element())
print(first_tuple_element((4, 6, 8)))

def square(radius, pi = 3.14159):
    return pi * radius ** 2

print(square(2))