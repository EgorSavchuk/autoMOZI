import sympy


def to_html(line):
    line += " "
    r = ""
    c = 0
    p = ""
    for i in line:
        if i == "^":
            r += "<sup>"
            c = 1
        elif c == 1:
            if i.isalpha() and p != "^" or i == " " or i == "\n":
                r += "</sup>"
                c = 0
            r += i
        else:
            r += i
        p = i
    return r[:-1]


def print_primer(s, a, b):
    # Название не оч удачное.
    """
    На примере будет понятен смысл функции
    Пример работы:
    На входные данные (2a + 3b, 'b', 'c')
    Она вернёт: 2b + 3c
    Более сложный пример:
    На входные данные (ab + a, 'b^3 + b^2 + b', 'c')
    Она вернёт: (b^3 + b^2 + b)c + (b^3 + b^2 + b)
"""
    result = ""
    for i in s:
        if (i == "a"):
            if a.count(' ') > 0:
                result += f"({a})"
            else:
                result += a
        elif (i == "b"):
            if b.count(' ') > 0:
                result += f"({b})"
            else:
                result += b
        else:
            result += i
    return result


def add_zv(s):
    # Добавляет где нужно звёздочки, в катчетве умножения, чтою sympy понял что к чему
    r = ""
    pred = ""
    for i in s:
        if pred.isalpha() and (i.isalpha() or i == "(") or pred.isdigit() and (i.isalpha() or i == "(") or pred == ")" and (i.isalpha() or i.isdigit() or i == "("):
            r += "*"
        pred = i
        r += i
    return r


def associativity(values):
    result = "Ассоциативность:\na * (b * c) = (a * b) * c\n"
    a = print_primer(values, 'a', 'b')
    b = print_primer(values, 'b', 'c')
    result += f"a * ({b}) ? ({a}) * c\n"
    left = print_primer(values, 'a', b)
    right = print_primer(values, a, 'c')
    result += f"{left} ? {right}\n"
    left = str(sympy.simplify(add_zv(left))).replace("**", "^").replace("*", "")
    right = str(sympy.simplify(add_zv(right))).replace("**", "^").replace("*", "")
    result += f"{left} ? {right}\n"
    left = str(sympy.simplify(add_zv(left) + '-' + '(' + add_zv(right) + ')')).replace("**", "^").replace("*", "")
    result += f"{left} ? 0\n"
    if sympy.simplify(add_zv(left) + '==' + '0'):
        result += "0 = 0\nАссоциативность выполняется\n\n\n"
    else:
        result += f"{left} ≠ 0\nАссоциативность не выполняется\n(P.S. Придумайте сами пример, при котором равенство не выполняется)\n\n\n"
    return result
    

def commutativity(values):
    result = "Комутативность:\na * b = b * a\n"
    right = print_primer(values, 'b', 'a')
    result += f"{values} ? {right}\n"
    left = str(sympy.simplify(add_zv(values) + '-' + '(' + add_zv(right) + ')')).replace("**", "^").replace("*", "")
    result += f"{left} ? 0\n"
    if sympy.simplify(add_zv(left) + '==' + '0'):
        result += "0 = 0\nКомутативность выполняется\n\n\n"
    else:
        result += f"{left} ≠ 0\nКомутативность не выполняется\n(P.S. Придумайте сами пример, при котором равенство не выполняется)\n\n\n"
    return result


def neutral_element(values):
    result = "Существование нейтрального элемента:\na * e = e * a = a\n\n"
    left = print_primer(values, 'a', 'e')
    right = print_primer(values, 'e', 'a')
    result += f"{left} = a\n{right} = a\n"
    left = str(sympy.simplify(add_zv(left) + '-' + 'a')).replace("**", "^").replace("*", "")
    right = str(sympy.simplify(add_zv(right) + '-' + 'a')).replace("**", "^").replace("*", "")
    result += f"{left} = 0\n{right} = 0\n"
    left = str(sympy.solvers.solve(add_zv(left), "e"))[1:-1].replace("**", "^").replace("*", "")
    right = str(sympy.solvers.solve(add_zv(right), "e"))[1:-1].replace("**", "^").replace("*", "")
    result += f"e = {left}\ne = {right}\n"
    if left != right:
        result += "Нейтрального элемента не существует\n\n\n"
    elif left.isdigit() == False:
        result += "Нейтрального элемента не существует\n\n\n"
    else:
        result += f"Нейтральный элемент: e = {left}\n\n\n"

    return result, left


def reversible_element(values, e):
    result = "Существование обратимых элементов элементов:\nx * y = y * x = e\n\n"
    left = print_primer(values, 'x', 'y')
    right = print_primer(values, 'y', 'x')
    result += f"{left} = e\n{right} = e\n\n"
    result += f"{left} = {e}\n{right} = {e}\n\n"
    left = str(sympy.solvers.solve(add_zv(left + f"- {e}"), "x"))[1:-1].replace("**", "^").replace("*", "")
    right = str(sympy.solvers.solve(add_zv(right + f"- {e}"), "y"))[1:-1].replace("**", "^").replace("*", "")
    result += f"x = {left}\ny = {right}\n\n\n"
    return result


def quasigroup(values):
    result = "Свойство квазигруппы:\nx * a = a * y = b\n"
    left = print_primer(values, 'x', 'a')
    right = print_primer(values, 'a', 'y')
    result += f"{left} = b\n{right} = b\n"
    left = str(sympy.solvers.solve(add_zv(left + "- b"), "x"))[1:-1].replace("**", "^").replace("*", "")
    right = str(sympy.solvers.solve(add_zv(right + "- b"), "y"))[1:-1].replace("**", "^").replace("*", "")
    result += f"x = {left}\ny = {right}\n\n\n"
    return result


def get_answer_task1(s):
    result = "Задача 1: \n\n"
    # for i in s:
    #     if i != "a" and i != "b" and i != " " and i != "+" and i != "-" and i != "^" and not i.isdigit():
    #         print("Задача 1: Ошибка ввода")
    #         return ""
    try:
        s = str(sympy.simplify(add_zv(s))).replace("**", "^").replace("*", "")  # Оптимизация строки
    except:
        print("Задача 1: Ошибка ввода")
        return ""
    result = "\n"
    try:
        result += associativity(s) # Проверка на ассоциативность
    except:
        print("Задача 1: Ошибка во время проверки на ассоциативность")
    try:
        result += commutativity(s)
    except:
        print("Задача 1: Ошибка во время проверки на комутативность")
    try:
        tmp, e = neutral_element(s)
        result += tmp
    except:
        print("Задача 1: Ошибка во время проверки на существование нейтрального элемента")
    try:
        if result[-16:-3] == "не существует":
            result += "Существование обратимых элементов:\nx * y = y * x = e\nЕсли нейтрального элемента не существует,\nто обратимых элементов тоже не существует\n\n\n"
        else:
            result += reversible_element(s, e)
    except:
        print("Задача 1: Ошибка во время проверки на существование обратимых элементов")
    try:
        result += quasigroup(s)
    except:
        print("Задача 1: Ошибка во время проверки на свойство квазигруппы")

    return result
    
