def log_instruction(instruction, old_val, new_val) -> str:
    instrusctions = {
        'add_1': 'Приписать единицу',
        'mul_2': 'Умножить на два',
        'nothing': 'Ничего делать не нужно. Изначальное и желаемое числа равны'
    }

    return f'{instrusctions[instruction]} ({old_val} -> {new_val})'


def get_strategy(a: int, b: int) -> list | None:
    steps = []
    
    def add_1(num): return num * 10 + 1
    def mul_2(num): return num * 2

    if a < 0 or b < 0:
        from warnings import warn
        warn('Функция не работает с отрицательными числами')
        return None

    if b == a:
        return log_instruction(instruction='nothing', old_val=a, new_val=b)
    if a == 0:
        if b == 0:
            return None
        else:
            cache = add_1(a)
            steps.append(log_instruction(instruction=add_1.__name__, old_val=a, new_val=cache))
            a = cache
            if a == b:
                return steps

    # Если число четное, необходимо сокращать его
    del_qty = 0
    temp = b
    while temp % 2 == 0:
        del_qty += 1
        temp //= 2

    # Если число содержит единицы на конце, необходимо их обрезать
    one_qty = 0
    while temp >= 10 and temp % 10 == 1:
        one_qty += 1
        temp //= 10
    
    
    # Нужно сравнить с а, попытаться получить из a temp с помощью умножения
    while a < temp:
        cache = mul_2(a)
        steps.append(log_instruction(instruction=mul_2.__name__, old_val=a, new_val=cache))
        a = cache
    

    if a == temp:
        for i in range(del_qty):
            cache = mul_2(a)
            steps.append(log_instruction(instruction=mul_2.__name__, old_val=a, new_val=cache))
            a = cache

        for i in range(one_qty):
            cache = add_1(a)
            steps.append(log_instruction(instruction=add_1.__name__, old_val=a, new_val=cache))
            a = cache
        
        return steps
    else:
        return None


def main():
    while True:
        try:
            a = int(input('Введите изначальное число: '))
            b = int(input('Введите желаемое число: '))
            break
        except ValueError:
            print('Пожалуйста, введите челое число')
        except KeyboardInterrupt:
            return
    
    res = get_strategy(a=16, b=6411*2)
    print(f'Изначальное число: {a}, Желаемое число: {b}')
    
    out = 'Стратегия не найдена'
    if isinstance(res, list):
        out = ''
        for key, instruction in enumerate(res):
            out += f'{key + 1}) {instruction}\n'
    
    print(out)


if __name__ == '__main__':
    main()