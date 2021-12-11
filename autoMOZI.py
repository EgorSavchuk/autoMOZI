import sys
from jinja2 import Environment, FileSystemLoader
from task1 import get_answer_task1, to_html
from task2 import get_answer_task2, get_answer_task2_html
from task3 import get_result_task3, get_result_task3_html
from task4 import get_answer_for_task4, get_answer_for_task4_html

if __name__ == '__main__':
    task1 = str(input("Решить задачу 'Изучение свойств алгебраической структуры?' y/n: "))
    if task1 == 'y' or task1 == 'н':
        condition = str(input("Операция a * b =  "))
    task2 = str(input("Решить задачу с исследованием абстрактной циклической группы? y/n: "))
    if task2 == 'y' or task2 == 'н':
        cardinality = int(input("Задача с исследованием абстрактной циклической группы: Введите порядок группы: "))
    task3 = str(input("Решить задачу с вычислением подстановок? y/n: "))
    if task3 == 'y' or task3 == 'н':
        substitution1 = input("Задача 2: Первая подстановка, введите только числа второй строки через пробел: ").split()
        substitution1 = list(map(int, substitution1))
        substitution2 = input("Задача 2: Вторая подстановка, введите только числа второй строки через пробел: ").split()
        substitution2 = list(map(int, substitution2))
        pow_substitution1 = int(input("Задача 2: Введите степень первой подстановки: "))
        pow_substitution2 = int(input("Задача 2: Введите степень второй подстановки: "))
        pow_general = int(input("Задача 2: Введите общую степень подстановок, если такой нет в задании введите 1: "))
    task4 = str(input("Решить задачу про кольцо классов вычетов? y/n: "))
    if task4 == 'y' or task4 == 'н':
        p = int(input("Задача 3: Введите Z_: "))

    if '-html' in sys.argv:
        file_loader = FileSystemLoader('Templates')
        env = Environment(loader=file_loader)
        tm = env.get_template('index.html')
        visibility_task1 = 'hidden="true"'
        visibility_task2 = 'hidden="true"'
        visibility_task3 = 'hidden="true"'
        visibility_task4 = 'hidden="true"'
        answer_task1 = ''
        answer_task2 = ''
        answer_task3 = ''
        answer_task4 = ''
        if task1 == 'y':
            answer_task1 = to_html(get_answer_task1(condition))
            visibility_task1 = ''
        if task2 == 'y':
            answer_task2 = get_answer_task2_html(cardinality)
            visibility_task2 = ''
        if task3 == 'y':
            answer_task3 = get_result_task3_html(substitution1, substitution2, pow_substitution1, pow_substitution2, pow_general)
            visibility_task3 = ''
        if task4 == 'y':
            answer_task4 = get_answer_for_task4_html(p)
            visibility_task4 = ''

        msg = tm.render(
            visibility_task1=visibility_task1,
            visibility_task2=visibility_task2,
            visibility_task3=visibility_task3,
            visibility_task4=visibility_task4,
            answer_task1=answer_task1,
            answer_task2=answer_task2,
            answer_task3=answer_task3,
            answer_task4=answer_task4
        )

        f = open('solve.html', 'w')
        f.write(msg)
        print("Файл с решением solve.html создан в корневой папке (autoMOZI)")
    else:
        all_answer = ''
        if task1 == 'y':
            all_answer += get_answer_task1(condition)
        if task2 == 'y':
            all_answer += get_answer_task2(cardinality)
        if task3 == 'y':
            all_answer += get_result_task3(substitution1, substitution2, pow_substitution1, pow_substitution2, pow_general)
        if task4 == 'y':
            all_answer += get_answer_for_task4(p)
        print(all_answer)

