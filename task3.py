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


def paste_lcm(full_cycle) -> int:
    """
    :param full_cycle: Цикл подстановки
    :return: Массив из НОК каждого цикла
    """
    cycles_len = []
    for one_cycle in full_cycle:
        cycles_len.append(len(one_cycle))
    return cycles_len


def print_simplification(task_pow, s_pow, s_lcm):
    result = f'{task_pow} = '
    multiplier = int(task_pow / s_lcm)
    result += f'{multiplier} * {s_lcm} + {s_pow}'
    return result


def print_cycle(substitution_cycle):
    result = f''
    for cycle in substitution_cycle:
        result += f'{cycle} '
    return result


def get_result():
    substitution1 = [7, 5, 1, 3, 6, 2, 8, 4, 10, 9]
    substitution2 = [5, 9, 1, 2, 3, 7, 4, 10, 6, 8]
    pow_substitution1 = 348
    pow_substitution2 = 423
    pow_general = 80
    # substitution1 = input("Первая подстановка, введите только числа второй строки через пробел: ").split()
    # substitution1 = list(map(int, substitution1))
    # substitution2 = input("Вторая подстановка, введите только числа второй строки через пробел: ").split()
    # substitution2 = list(map(int, substitution2))
    # pow_substitution1 = int(input("Ввееди степень первой подстановки: "))
    # pow_substitution2 = int(input("Ввееди степень второй подстановки: "))
    # pow_general = int(input("Ввееди общую степень подстановок, если такой нет в задании введите 1: "))
    print_pow_general = ''
    if pow_general != 1:
        print_pow_general = f'^{pow_general}'
    substitution1_cycle = get_cycle(substitution1)
    substitution2_cycle = get_cycle(substitution2)
    for_print_substitution1_cycle = f''
    for cycle in substitution1_cycle:
        for_print_substitution1_cycle += f'{cycle} '
    for_print_substitution2_cycle = f''
    for cycle in substitution2_cycle:
        for_print_substitution2_cycle += f'{cycle} '
    a_lcm = get_lcm(substitution1_cycle)
    b_lcm = get_lcm(substitution2_cycle)
    a_pow = get_modulo(pow_substitution1, a_lcm)
    b_pow = get_modulo(pow_substitution2, b_lcm)
    substitution1_in_pow = get_raised_full_cycle(substitution1_cycle, a_pow)
    substitution2_in_pow = get_raised_full_cycle(substitution2_cycle, b_pow)
    result_substitution = calculate_substitutions(to_substitution(substitution1_in_pow, substitution1),
                                                  to_substitution(substitution2_in_pow, substitution2))
    lcm_to_a = paste_lcm(substitution1_cycle)
    lcm_to_b = paste_lcm(substitution2_cycle)
    answer = f'\na = {get_default_substitution(substitution1)}\n' \
             f'    {substitution1}\n\n' \
             f'b = {get_default_substitution(substitution2)}\n' \
             f'    {substitution2}\n\n' \
             f'c = ( a^{pow_substitution1} * b^{pow_substitution2} ){print_pow_general}\n\n' \
             f'Циклы подстановки a = {print_cycle(substitution1_cycle)}\n' \
             f'Циклы подстановки b = {print_cycle(substitution2_cycle)}\n\n' \
             f'O(a) = НОК({print_cycle(lcm_to_a)}) = {a_lcm}\n' \
             f'O(b) = НОК({print_cycle(lcm_to_b)}) = {b_lcm}\n' \
             f'{print_simplification(pow_substitution1, a_pow, a_lcm)}\n' \
             f'{print_simplification(pow_substitution2, b_pow, b_lcm)}\n\n' \
             f'a^{a_pow} = {print_cycle(substitution1_in_pow)}\n' \
             f'b^{b_pow} = {print_cycle(substitution2_in_pow)}\n' \
             f'a^{a_pow} o b{b_pow} = {get_cycle(result_substitution)}'
    return answer


print(get_result())
