def check_num1(a: str):
    '''
    проверка первого числа
    '''
    cnt = 0
    res = True
    for i in range(len(a)):
        if i == 0 and (a[i] == '-' or a[i].isdigit()):
            res = True
        elif not a[i].isdigit() and a[i] != '.':
            res = False
        elif a[i] in '.':
            cnt += 1
        if cnt > 1:
            res = False

    '''
    определение кол-ва знаков после запятой
    '''
    b = a.find('.')
    if b == -1:
        round1 = 0
    else:
        round1 = len(a) - (a.find('.') + 1)
    return res, round1


def check_num2(a: str):
    '''
    проверка второго числа
    '''
    cnt = 0
    res = True
    for i in range(len(a)):
        if i == 0 and (a[i] == '-' or a[i].isdigit()):
            res = True
        elif not a[i].isdigit() and a[i] != '.':
            res = False
        elif a[i] in '.':
            cnt += 1
        if cnt > 1:
            res = False
    '''
    определение кол-ва знаков после запятой
    '''
    b = a.find('.')
    if b == -1:
        round2 = 0
    else:
        round2 = len(a) - (a.find('.') + 1)
    return res, round2


def round_res1(num1, num2):
    '''
    определение кол-ва знаков 
    после запятой для результата
    '''
    round_res = 0
    b = num1.find('.')
    round1 = 0
    if b != -1:
        round1 = len(num1) - (num1.find('.') + 1)
    c = num2.find('.')
    round2 = 0
    if c != -1:
        round2 = len(num2) - (num2.find('.') + 1)
    if round1 >= round2:
        round_res = round1
    else:
        round_res = round2
    return round_res


def check_action(y):
    '''
    проверка знака вычисления
    '''
    operations = ['+', '-', '*', '/']
    if y in operations:
        return True
    else:
        return False


def sum(x, y):
    '''
    расчёт сложения
    '''
    return x + y


def sub(x, y):
    '''
    расчёт вычитания
    '''
    return x - y


def mult(x, y):
    '''
    расчёт умножения
    '''
    return x * y


def div(x, y):
    '''
    расчёт деления
    '''
    return x / y


def calc(a, b, oper):
    '''
    расчёт результата
    '''
    res = ''
    if oper == '+':
        res = float(sum(a, b))
    elif oper == '-':
        res = float(sub(a, b))
    elif oper == '*':
        res = float(mult(a, b))
    elif oper == '/' and b == 0:
        res = 'делить на ноль нельзя'
    else:
        res = float(div(a, b))
    return res


print('\n Калькулятор натуральных и вещественных чисел \n')

first_num = input(
    'введите первое число (вещественное число вводится через точку): ')
while not check_num1(first_num):
    first_num = input(
        'введены не корректные данные \n введите первое число (вещественное число вводится через точку): ')


operation = input('введите арифметическое действие (+ - / *): ')
while not check_action(operation):
    operation = input(
        'введены не корректные данные \n введите арифметическое действие (+ - / *): ')


second_num = input(
    'введите второе число (вещественное число вводится через точку):')
while not check_num2(second_num):
    second_num = input(
        'введены не корректные данные \n введите второе число (вещественное число вводится через точку): ')


x = float(first_num)
y = float(second_num)
round_result = int(round_res1(first_num, second_num))
print(x)
print(operation)
print(y)

print(calc(x, y, operation))
print(
    f'результат {x} {operation} {y} => {round(calc(x, y, operation), round_result)}')
