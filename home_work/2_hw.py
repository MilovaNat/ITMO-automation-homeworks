# типы данных
def task_1() -> None:
    int_value : int = 1
    bool_value : bool = True
    float_value : float = 3.5
    str_value : str = 'hello'
    list_value : list = [1, 2, 3]

    print('Ответ задание 1:')
    print(int_value, "относится к типу", type(int_value))
    print(bool_value, "относится к типу", type(bool_value))
    print(float_value, "относится к типу", type(float_value))
    print(str_value, "относится к типу", type(str_value))
    print(list_value, "относится к типу", type(list_value),'\n')

task_1()

# последовательность Фибоначчи (но мне кажется, для полного совпадения должна начинаться с 0,1,1,....)
def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print('Ответ задание 2:', a[0:3], '\n')

task_2()


# квадрат числа
def task_3(x : int) -> int:
    return x ** 2

print('Ответ задание 3:', task_3(3), '\n')