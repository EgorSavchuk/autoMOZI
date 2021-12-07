from math import gcd

SETTINGS = {
    'var': 'x',
    'pow': '^',
}


def get_answer(cardinality):
    print(get_g(cardinality))
    print(get_generating_set(cardinality, get_all_elements(cardinality)))
    print(get_other_sets(cardinality, get_all_elements(cardinality)))
    print(get_filled_groups(cardinality, get_groups(cardinality, get_all_elements(cardinality)),
          get_all_elements(cardinality)))


def get_g(cardinality):
    """
    :param cardinality: Порядок циклической группы, которую нужно исследовать
    :return: Строку формата : G = {1g,x^2,x^2,...,x^n-1}
    """
    result_g = 'G = { 1g'
    for i in range(1, cardinality):
        result_g += f', {SETTINGS.get("var")}{SETTINGS.get("pow")}{i}'
    result_g += ' } \n'
    return result_g


def get_all_elements(cardinality):
    """
    :param cardinality: Порядок циклической группы, которую нужно исследовать
    :return: Словарь формата { 'степень элемента' : ' порядок элемента' }
    """
    elements_cardinality = {}
    for i in range(1, cardinality):
        elements_cardinality[i] = int(cardinality / gcd(i, cardinality))
    return elements_cardinality


def get_generating_set(cardinality, elements_cardinality):
    """
    :param cardinality: Порядок циклической группы, которую нужно исследовать
    :param elements_cardinality: Словарь формата { 'степень элемента' : ' порядок элемента' }
    :return: Возвращает строку формата G = <x> = <x2>, где x,x2 - образующие
    """
    result_generating_sets = 'G '
    for i in range(1, len(elements_cardinality) + 1):
        if elements_cardinality.get(i) == cardinality:
            result_generating_sets += f'= <{SETTINGS.get("var")}{SETTINGS.get("pow")}{i}> '
    return result_generating_sets


def get_other_sets(cardinality, elements_cardinality):
    """
    :param cardinality: Порядок циклической группы, которую нужно исследовать
    :param elements_cardinality: Словарь формата { 'степень элемента' : ' порядок элемента' }
    :return: Возвращает все остальные элементы и их порядок
    """
    result_other_sets = ''
    for i in range(1, len(elements_cardinality) + 1):
        if elements_cardinality.get(i) != cardinality:
            result_other_sets += f'O({SETTINGS.get("var")}{SETTINGS.get("pow")}{i}) = {elements_cardinality.get(i)}\n'
    return result_other_sets


def get_groups(cardinality, elements_cardinality):
    """
    :param cardinality: Порядок циклической группы, которую нужно исследовать
    :param elements_cardinality: Словарь формата { 'степень элемента' : ' порядок элемента' }
    :return: Возвращает набор всех существующих порядков элементов
    """
    groups = set()
    for i in range(1, len(elements_cardinality) + 1):
        if elements_cardinality.get(i) != cardinality:
            groups.add(elements_cardinality.get(i))
    return list(groups)


def get_filled_groups(cardinality, groups, elements_cardinality):
    """
    :param cardinality: Порядок циклической группы, которую нужно исследовать
    :param groups: Набор всех существующих порядков элементов
    :param elements_cardinality: Словарь формата { 'степень элемента' : ' порядок элемента' }
    :return: Подгруппу, образующие подгруппы, полный список элементов подгруппы, порядок подгруппы
    """
    filled_groups = f'H1 = {get_generating_set(cardinality, get_all_elements(cardinality))} |H1| = {cardinality}\n'
    i = 1
    for group_order in reversed(groups):
        i += 1
        filled_groups += f'H{i}'
        element_for_fill = 0
        for element, order in elements_cardinality.items():
            if order == group_order:
                if element_for_fill == 0:
                    element_for_fill = element
                filled_groups += f' = <{SETTINGS.get("var")}{SETTINGS.get("pow")}{element}>'
        filled_groups += ' = {1g'
        for j in range(1, group_order):
            filled_groups += f', {SETTINGS.get("var")}{SETTINGS.get("pow")}{element_for_fill * j}'
        filled_groups += f'}} |H{i}| = {group_order}\n'
    filled_groups += f'H{i + 1} = <1g> = {{ 1g }} |H{i + 1}| = 1'
    return filled_groups

