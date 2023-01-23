from warnings import warn

def decimal_to(n: int, system: int):
    '''Переводит число из десятичной в систему'''
    if not (2 <= system <= 9):
        warn(f"{system}, перевод только от 2 до 9 систем счисления")
        return False
    
    result = ''
    n = abs(n)
    while n > 0:
        result = str(n % system) + result
        n //= system
    
    if not result:
        result = 0
    else:
        try:
            result = int(result)
        except ValueError:
            pass
    
    return result


def n_to(n: str, system: int):
    '''Переводит число в систему счисления'''

    if not (2 <= system <= 36):
        warn(f"{system}, перевод только от 2 до 36 систем счисления")
        return False
    
    return int(n, system)


def n_to_decimal(n: str, base: int):
    '''
    Переводит число в десятичную систему
    '''
    result = 0
    n = str(n)
    num_len = len(n)
    # 1 = 1
    for i in range(0, num_len):
        result += int(n[i]) * base**i
    
    return result
    


# 1 = 1 * 2**0
# 100 = 1 * 2**2 + 0 * 2**1 + 0 * 2**0 = 1 * 4 = 4