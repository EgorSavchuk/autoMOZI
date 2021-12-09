def gettingValues():
    """
    Функция запрашивает от пользователя правило операции
    и преобразует её в вид для работы программы\n
    :return: Словарь {переменная -> коэффициент}"""
    print('Введите, чему равна операция x * y, заменяя степени произведением. \n'
          'Знаки сложения опускаются, умножение пишется слитно. \n'
          'Деление и вычитание ставится перед делителем и вычитаемым соответственно. \n'
          'Например: 3ххх -2хуу 2 будет означать 3х^2 - 2xy^2 + 2')
    line = str(input())
    split_line = line.split(' ')
    values = {}
    for i in split_line:
        coefficient = ''
        variable = ''
        for j in i:
            if j.isdigit():
                coefficient += j
            elif j.isalpha():
                variable += j
            elif j == '-':
                coefficient += '-'
        if variable == '':
            variable = 'С'
        values[variable] = int(coefficient)
    for i, j in values.items():
        print(i, j)
    return values


def calculation(x, y, values):
    """
    Считает, значение операции\n
    :param string x: Первое выражение операции
    :param string y: Второе выражение операции
    :param dict values: Правило операции
    :return Результат проведения операции
    """
    z = ''
    return z


def associativity(values):
    """Проверяет на ассоциативность:\n
    x * (y * z) = (x * y) * z\n
    :param dict values: Правило операции
    :return: Результат проверки
    """
    return True


gettingValues()
