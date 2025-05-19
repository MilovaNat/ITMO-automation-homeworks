def test_passing() :
    assert (1, 2, 3) == (1, 2, 3)


# def test_failing() :
#     assert 'test' == 'testing'


# функция проверки на несоответствие
def test_not():
     a = 'test'
     b = 'testing'
     assert not a == b


# функция проверки неравенства двух списков
def test_not_equals_lists():
    x = ["a", "b", "c"]
    y = [1, 2, 3]
    assert x != y