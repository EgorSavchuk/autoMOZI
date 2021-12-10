if __name__ == '__main__':
    task2 = str(input("Решить задачу с исследованием абстрактной циклической группы? y/n: "))
    task3 = str(input("Решить задачу 2 y/n: "))
    task4 = str(input("Решить задачу 3 y/n: "))
    all_answer = ''
    if task2 == 'y':
        from task2 import get_answer_task2
        cardinality = int(input("Задача с исследованием абстрактной циклической группы: Введите порядок группы: "))
    if task3 == 'y':
        from task3 import get_result_task3
        substitution1 = input("Задача 2: Первая подстановка, введите только числа второй строки через пробел: ").split()
        substitution1 = list(map(int, substitution1))
        substitution2 = input("Задача 2: Вторая подстановка, введите только числа второй строки через пробел: ").split()
        substitution2 = list(map(int, substitution2))
        pow_substitution1 = int(input("Задача 2: Введите степень первой подстановки: "))
        pow_substitution2 = int(input("Задача 2: Введите степень второй подстановки: "))
        pow_general = int(input("Задача 2: Введите общую степень подстановок, если такой нет в задании введите 1: "))
    if task4 == 'y':
        from task4 import get_answer_for_task4
        p = int(input("Задача 3: Введите Z_: "))
    if task2 == 'y':
        all_answer += get_answer_task2(cardinality)
    if task3 == 'y':
        all_answer += get_result_task3(substitution1, substitution2, pow_substitution1, pow_substitution2, pow_general)
    if task4 == 'y':
        all_answer += get_answer_for_task4(p)
    print(all_answer)

