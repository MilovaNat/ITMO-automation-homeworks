def square(x : int) -> int:
    return x * x

print(square(2.2))

def length(x : str = '') -> int:
    return len(x)

print(length())
print(length('ffffff'))

def longest_list(x : list, y : list) -> int:
    return max(len(x), len(y))

print(longest_list(['a', 'b', 'c'], ['a', 'b', 'c', 'd']))

def add_random(x : list, y) -> list:
    x.append(y)
    return x

print(add_random([1, 2, 3], '4'))

def sum_numbers_list_elements(x : list[int]) -> int:
    return sum(x)

print(sum_numbers_list_elements([1, 2, 3]))