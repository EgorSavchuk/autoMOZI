from math import lcm


def get_default_substitution(substitution):
    result_substitution = [1] * len(substitution)
    for i in range(0, len(substitution)):
        result_substitution[i] = i + 1
    return result_substitution


def get_cycle(substitution):
    """
    :param substitution: Нижнюю строчку табличной подстановки
    :return: Цикл этой подстановки
    """
    cycles = [[]]
    in_result = []
    for i in range(1, len(substitution)):
        if i not in in_result:
            num1 = i - 1
            num2 = substitution[num1]
            cycle = [i]
            while num2 != i:
                in_result.append(substitution[num1])
                cycle.append(substitution[num1])
                num1 = num2 - 1
                num2 = substitution[num1]
            cycles.append(cycle)
    cycles.remove([])
    return cycles


def get_lcm(full_cycle) -> int:
    """
    :param full_cycle: Цикл подстановки
    :return: НОК порядков циклов цикла подстановки
    """

    cycles_len = []
    for one_cycle in full_cycle:
        cycles_len.append(len(one_cycle))
    cycle_lcm = lcm(*cycles_len)
    return cycle_lcm


def get_modulo(cycle_pow, cycle_lcm):
    """
    :param cycle_pow: Степень в которую нужно возвести подстановку по заданию
    :param cycle_lcm: НОК цикла
    :return: Остаток от деления, наименьшая степень в которую можно возвести подстановку
    """
    return cycle_pow % cycle_lcm


def get_cycle_in_pow(single_cycle, cycle_pow):
    """
    :param single_cycle: Одиночный цикл, который нужно возвести в степень
    :param cycle_pow: Степень в которую нужно возвести цикл
    :return: Одиночный цикл, возведенный в степень
    """
    mod = cycle_pow % lcm(len(single_cycle), cycle_pow)
    result_cycle = [single_cycle[0]] * len(single_cycle)
    if mod == 1:
        return single_cycle
    if mod == 0:
        return ['e']
    else:
        for i in range(1, len(single_cycle)):
            multiplier = cycle_pow * i
            if multiplier >= len(single_cycle):
                multiplier %= len(single_cycle)
            result_cycle[i] = single_cycle[multiplier]
    return result_cycle


def get_raised_full_cycle(cycle, cycle_pow):
    """
    :param cycle: Полный цикл подставновки
    :param cycle_pow: Степень цикла
    :return: Полный цикл, возведенный в нужную степень
    """
    result_cycle = [[]]
    for single_cycle in cycle:
        result_cycle.append(get_cycle_in_pow(single_cycle, cycle_pow))
    result_cycle.remove([])
    return result_cycle


def to_substitution(full_cycle, substitution):
    """
    :param full_cycle: Полный цикл подстановки
    :param substitution: Любую подстановку из задания
    :return: Подстановку из цикла
    """
    result_substitution = [1] * len(substitution)
    for i in range(0, len(substitution)):
        result_substitution[i] = i + 1
    for single_cycle in full_cycle:
        if single_cycle == ['e']:
            continue
        for i in single_cycle:
            index = int(single_cycle.index(i) + 1)
            if index == len(single_cycle):
                index = 0
            result_substitution[i - 1] = single_cycle[index]
    return result_substitution


def calculate_substitutions(substitution1, substitution2):
    """
    :param substitution1: Подстановка 1
    :param substitution2: Подстановка 2
    :return: Результат двух подстановок
    """
    result_substitution = [1] * len(substitution1)
    for i in range(0, len(substitution1)):
        result_substitution[i] = substitution1[substitution2[i] - 1]
    return result_substitution


def print_lcm(full_cycle):
    """
    :param full_cycle: Цикл подстановки
    :return: список цифр из которых вычисляется НОК
    """
    cycles_len = []
    for one_cycle in full_cycle:
        cycles_len.append(len(one_cycle))
    result = ''
    for i in str(cycles_len):
        if i == '[':
            result += ''
        elif i == ']':
            result += ''
        else:
            result += i
    return result


def print_simplification(task_pow, s_pow, s_lcm):
    """
    :param task_pow: Изначальная степень, которую нужно упростить
    :param s_pow: Остаток от деления, степнь в которую нужно будет возвести
    :param s_lcm: Нок цикла
    :return:
    """
    result = f'{task_pow} = '
    multiplier = int(task_pow / s_lcm)
    result += f'{multiplier} * {s_lcm} + {s_pow}'
    return result


def print_cycle(substitution_cycle):
    """
    :param substitution_cycle: Цикл
    :return: Цикл, пригодный для вывода
    """
    result = f' '
    for cycle in substitution_cycle:
        prepare = ''
        for i in str(cycle):
            if i == '[':
                prepare += '('
            elif i == ']':
                prepare += ') '
            elif i == ',':
                prepare += ' '
            else:
                prepare += i
        result += prepare
    return result


def print_substitution(substitution):
    """
    :param substitution: Подстановка
    :return: Подстановка, пригодная для вывода
    """
    result = f' '
    for i in str(substitution):
        if i == '[':
            result += '|'
        elif i == ']':
            result += '| '
        elif i == ',':
            result += ' '
        else:
            result += i
    return result


def get_result():
    substitution1 = input("Первая подстановка, введите только числа второй строки через пробел: ").split()
    substitution1 = list(map(int, substitution1))
    substitution2 = input("Вторая подстановка, введите только числа второй строки через пробел: ").split()
    substitution2 = list(map(int, substitution2))
    pow_substitution1 = int(input("Ввееди степень первой подстановки: "))
    pow_substitution2 = int(input("Ввееди степень второй подстановки: "))
    pow_general = int(input("Ввееди общую степень подстановок, если такой нет в задании введите 1: "))
    substitution1_cycle = get_cycle(substitution1)
    substitution2_cycle = get_cycle(substitution2)
    a_lcm = get_lcm(substitution1_cycle)
    b_lcm = get_lcm(substitution2_cycle)
    a_pow = get_modulo(pow_substitution1, a_lcm)
    b_pow = get_modulo(pow_substitution2, b_lcm)
    substitution1_in_pow = get_raised_full_cycle(substitution1_cycle, a_pow)
    substitution2_in_pow = get_raised_full_cycle(substitution2_cycle, b_pow)
    result_substitution = calculate_substitutions(to_substitution(substitution1_in_pow, substitution1),
                                                  to_substitution(substitution2_in_pow, substitution2))
    answer = f'\na = {print_substitution(get_default_substitution(substitution1))}\n' \
             f'    {print_substitution(substitution1)}\n\n' \
             f'b = {print_substitution(get_default_substitution(substitution2))}\n' \
             f'    {print_substitution(substitution2)}\n\n' \
             f'Циклы подстановки a = {print_cycle(substitution1_cycle)}\n' \
             f'Циклы подстановки b = {print_cycle(substitution2_cycle)}\n\n' \
             f'O(a) = НОК({print_lcm(substitution1_cycle)}) = {a_lcm}\n' \
             f'O(b) = НОК({print_lcm(substitution2_cycle)}) = {b_lcm}\n' \
             f'{print_simplification(pow_substitution1, a_pow, a_lcm)}\n' \
             f'{print_simplification(pow_substitution2, b_pow, b_lcm)}\n\n' \
             f'a^{pow_substitution1} = a^{a_pow} = {print_cycle(substitution1_in_pow)}\n' \
             f'b^{pow_substitution2} = b^{b_pow} = {print_cycle(substitution2_in_pow)}\n\n' \
             f'a^{a_pow} =  {print_substitution(get_default_substitution(substitution2))}\n' \
             f'       {print_substitution(to_substitution(substitution1_in_pow, substitution1))}\n\n' \
             f'b^{b_pow} =  {print_substitution(get_default_substitution(substitution2))}\n' \
             f'       {print_substitution(to_substitution(substitution2_in_pow, substitution2))}\n\n' \
             f'a^{a_pow} * b{b_pow} =  {print_substitution(get_default_substitution(result_substitution))}\n' \
             f'             {print_substitution(result_substitution)}\n\n' \
             f'a^{a_pow} * b{b_pow} = {print_cycle(get_cycle(result_substitution))}\n\n'
    if pow_general != 1:
        s_pow = get_modulo(pow_general, get_lcm(get_cycle(result_substitution)))
        answer += f'c = ( a^{a_pow} * b^{b_pow} )^{pow_general}\n\n' \
                  f'O(a^{a_pow} * b^{b_pow}) = ' \
                  f'НОК({print_lcm(get_cycle(result_substitution))})' \
                  f' = {get_lcm(get_cycle(result_substitution))}\n' \
                  f'{print_simplification(pow_general, s_pow, get_lcm(get_cycle(result_substitution)))}\n\n' \
                  f'(a^{a_pow} * b^{b_pow} )^{pow_general} = (a^{a_pow} * b^{b_pow})^{s_pow} = c\n' \
                  f'c = {print_cycle(get_raised_full_cycle(get_cycle(result_substitution), s_pow))}'
    return answer