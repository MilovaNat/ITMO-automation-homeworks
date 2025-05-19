num = -1

if num >= 0:
    print('Число больше или равно 0')
else:
    print('Число отрицательное')


str_1 = 'test'
str_2 = 'test1'

if str_2.find(str_1) >= 0:
    print('ДА')
else:
    print('НЕТ')

def yes_or_no(str1: str, str2: str) -> str:
    if str1 in str2:
        return "Yes"
    else:
        return "No"


print(yes_or_no(str1='test', str2='test1'))