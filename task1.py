def gettingValues():
    """
    Функция запрашивает от пользователя правило операции\n
    :return: Математическое выражение в строковой форме
    """
    print('Введите, чему равна операция x * y, заменяя степени произведением. \n'
          'Знаки сложения опускаются, умножение пишется слитно. \n'
          'Вычитание ставится перед делителем и вычитаемым соответственно. \n'
          'Например: 3ххх -2хуу 2 будет означать 3х^3 - 2xy^2 + 2')
    line = str(input())
    return line


def parse(expression):
    """
    Преобразует математическое выражение в строковой форме
    в вид для работы программы\n
    :param string expression: Математическое выражение
    :return: Словарь {переменная -> коэффициент}
    """
    split_expression = expression.split(' ')
    values = {}
    for i in split_expression:
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
        if coefficient == '':
            coefficient = '1'
        values[variable] = int(coefficient)
    for i, j in values.items():
        print(i, j)
    return values


def complex_multiplication(x, y):
    """
    Вычисляет результат умножения двух выражений\n
    :param dict[str, int] x: Выражение х
    :param dict[str, int] y: Выражение у
    :return: Результат умножения
    """
    result = {}
    for i, j in x.items():
        for m, n in y.items():
            variable = i + m
            sort_var = ""
            for k in sorted(variable):
                sort_var += k
            coefficient = j * n
            if sort_var not in result:
                result[sort_var] = coefficient
            else:
                result[sort_var] += coefficient
    for i, j in result.items():
        print(i, j)
    return result


def complex_sum(x, y):
    """
    Вычисляет результат сложения двух выражений\n
    :param dict[str, int] x: Выражение х
    :param dict[str, int] y: Выражение н
    :return: Результат сложения
    """
    for i, j in y.items():
        if i in x:
            x[i] += j
        else:
            x[i] = j
    for i, j in x.items():
        print(i, j)
    return x


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


# parse('хxx -2xyy 2')
x = {'a': 3, 'aab': 4}
y = {'a': 5, 'aab': -7}
complex_multiplication(x, y)
complex_sum(x, y)
