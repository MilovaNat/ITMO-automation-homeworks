num = 0
boolean = True

if num > 0 and boolean:
    print('Положительное число')
elif not boolean and num == 0:
    print('Ноль')
else:
    print('Отрицательное число')


def get_degree_by_course_year(year : int) -> str:
    if 1 <= year <= 4:
        return 'Бакалавр'
    elif year in range(5,7):
        return 'Магистр'
    elif 7 <= year <= 9:
        return 'Аспирант'
    else:
        return 'Введите корректный год обучения'

print(get_degree_by_course_year(7))


def interval(number : int) -> str:
    if number < -100 or number > 100:
        return '-'
    else:
        return '+'

print(interval(-101))