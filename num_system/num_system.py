from warnings import warn

def decimal_to(n: int, to: int):
    if not (2 < to < 9):
        warn(f"{to}, перевод только от 2 до 9 систем счисления")
        return False
    
    result = ''
    n = abs(n)
    while n > 0:
        result = str(n % to) + result
        n //= to
    
    if not result:
        result = 0
    else:
        try:
            result = int(result)
        except ValueError:
            pass
    
    return result


print(decimal_to(100, 8))