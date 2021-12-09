from math import gcd


def get_z(power):
    z = [0]
    for i in range(1, power):
        z.append(i)
    return z


def print_z(z):
    printable_z = f'Z_{len(z)} = {{ '
    for i in range(1, 5):
        printable_z += f'{z[i]}, '
    printable_z += f'... '
    for j in range(len(z) - 3, len(z)):
        printable_z += f'{z[j]}, '
    return printable_z[:-2] + ' }'


def get_z_with_star(z):
    z_with_star = []
    for i in z:
        if gcd(i, z[len(z) - 1] + 1) == 1:
            z_with_star.append(i)
    return z_with_star


def print_array(array):
    printable_z_with_star = '{ '
    for i in range(0, len(array)):
        printable_z_with_star += f'{array[i]}, '
    return printable_z_with_star[:-2] + ' }'


def get_order(element, z_with_star, p):
    for i in range(1, len(z_with_star) + 1):
        if pow(element, i) % p == 1:
            order = i
            return order
    return 'error'


def get_orders_for_all_elements(z_with_star, p):
    orders = {}
    for element in z_with_star:
        orders[element] = get_order(element, z_with_star, p)
    return orders


def print_orders(orders):
    result = ''
    # cnt = 0
    for key, value in orders.items():
        # cnt += 1
        result += f'O({key}) = {value}\n'
        # if cnt % 3 == 0:
        #     result += '\n'
    return result


def get_groups(orders):
    groups = set()
    for order in orders.values():
        groups.add(order)
    return list(groups)


def get_elements_for_group(group_order, orders, z):
    generate_element = 0
    result_group = set()
    for element, order in orders.items():
        if order == group_order:
            generate_element = element
    for i in range(1, len(get_z_with_star(z)) + 1):
        generate_element_pow = pow(generate_element, i) % len(z)
        if generate_element_pow in orders:
            result_group.add(generate_element_pow)
    return list(result_group)


def get_filled_groups(groups, orders, z):
    i = 0
    filled_groups = ''
    for group_order in reversed(groups):
        i += 1
        filled_groups += f'H{i}'
        element_for_fill = 0
        for element, order in orders.items():
            if order == group_order:
                if element_for_fill == 0:
                    element_for_fill = element
                filled_groups += f' = <{element}> '
        filled_groups += f'= {print_array(get_elements_for_group(group_order, orders, z))}'
        filled_groups += f' |H{i}| = {group_order}\n'
    return filled_groups


def get_answer_for_task4():
    p = int(input("Введите Z_: "))
    z = get_z(p)
    z_with_star = get_z_with_star(z)
    orders = get_orders_for_all_elements(z_with_star, p)
    groups = get_groups(orders)
    answer = ''
    answer += f'{print_z(z)}\n'
    answer += f'Z_{p}* = {print_array(z_with_star)}\n\n'
    answer += f'{print_orders(orders)}\n'
    answer += f'{get_filled_groups(groups, orders, z)}'
    return answer


print(get_answer_for_task4())
