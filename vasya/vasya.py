def get_strategy(a: int, b: int) -> list | None:
    steps = []
    instrusctions = {
        'add_1': 'Приписать единицу',
        'mul_2': 'Умножить на два',
        'no': 'Ничего делать не нужно. a == b'
    }
    
    if b == a:
        return instrusctions['no']
    if a == 0:
        if b == 0:
            return None
        else:
            a += 1
            steps.append('add_1')
            if a == b:
                return steps
    

    one_qty = 0
    temp = b

    while temp >= 10 and temp % 10 != 0:
        one_qty += 1
        temp //= 10

    # Теперь в temp хранится обрезанное число
    # Нужно сравнить с а, попытаться получить из a temp с помощью умножения
    while a < temp:
        steps.append('mul_2')
        a *= 2
    
    if a == temp:
        for i in range(one_qty):
            steps.append('add_1')
        return steps
    else:
        return None


def main():
    res = get_strategy(a=0, b=4444)
    print(res)


if __name__ == '__main__':
    main()