def get_strategy(a: int, b: int) -> list | None:
    steps = []
    
    if b == a:
        return ["Nothing to do"]
    if a == 0:
        if b == 0:
            return None
        else:
            a += 1
            steps.append('Add 1')
            if a == b:
                return steps
    

    # Считаем количество единиц в конце числа b
    one_qty = 0
    temp = b

    while temp >= 10 and temp % 10 == 1:
        one_qty += 1
        temp //= 10

    # Теперь в temp хранится обрезанное от единиц число
    # Нужно сравнить с а, попытаться получить из a temp с помощью умножения
    while a < temp:
        steps.append('Mul 2')
        a *= 2
    
    if a == temp:
        for i in range(one_qty):
            steps.append('Add 1')
        return steps
    else:
        return None


def main():
    res = get_strategy(a=3, b=6)
    print(res)


if __name__ == '__main__':
    main()