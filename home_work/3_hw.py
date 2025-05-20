def max_number(a, b):
    return max(a, b)

print(max_number(5, 88))

def difference_135(a, b) -> str:
    if abs(a - b) == 135:
        return 'Yes'
    return 'No'

print(difference_135(141, 5))
print(difference_135(140, 5))

def get_season_by_month_number(x) -> str:
   if x < 1 or x > 30:
       return 'Введен не номер месяца, необходим номер от 1 до 12'
   if x in range(3, 6):
       return 'Spring'
   elif x in range(6, 9):
       return 'Summer'
   elif x in range(9, 12):
       return 'Autumn'
   else:
       return 'Winter'


print(get_season_by_month_number(0))

def all_gth_10(x, y, z) -> str:
    if x > 10 and y > 10 and z > 10:
        return 'Yes'
    return 'No'

print(all_gth_10(11, 11, 11))
print(all_gth_10(10, 11, 11))

def positive_count(l : list) -> int:
    return len([l for el in l if el >= 0])

print(positive_count([1, 2, 3, 5, -18, 13, 21]))

def days_count(years_count: int, months_count: int) -> int:
    days_count_in_month = 29
    return months_count * days_count_in_month + years_count * 12 * days_count_in_month

print(days_count(2, 6))