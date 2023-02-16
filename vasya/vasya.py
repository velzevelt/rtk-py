from functools import lru_cache
import sys

class State:
    def __init__(self, num, action_name):
        self.num = num
        self.action_name = action_name


def multiply_by_two(num):
    return num * 2


def add_one_to_end(num):
    return num * 10 + 1


sys.setrecursionlimit(3000)


@lru_cache(maxsize=64)
def get_strategy(num: int, current_state_id: int = 1, action: callable = multiply_by_two):
    """
        Функция рекурсивно перебирает все возможные варианты для достижения цели. Неэффективный метод
    """
    if num == b:
        return [alias['nothing_to_do']]
    else:
        if num == 0:
            action = add_one_to_end
        temp = action(num)
        if temp < b:
            states.append(State(temp, action.__name__))
            return get_strategy(temp, current_state_id + 1, multiply_by_two)
        elif temp == b:
            states.append(State(temp, action.__name__))
            return get_result()
        else:
            prev_id = current_state_id - 1
            if prev_id >= 0:
                prev_num = states[prev_id].num
                return get_strategy(prev_num, prev_id, add_one_to_end)
            else:
                return False


def get_result():
    final_states = states[1:]
    return [[alias[state.action_name], state.num] for state in final_states]


def get_stategy_2(num):
    """ Функция анализирует числа и выбирает оптимальный путь """
    if num == b:
        return [alias['nothing_to_do']]
    else:
        if b % 2 == 0:
            pass


while True:
    try:
        a = int(input('Изначальное число: '))
        b = int(input('Желаемое число: '))
        break
    except ValueError:
        print('Пожалуйста, введите целые числа')

states = [State(a, None)]
alias = {
    'multiply_by_two': 'Умножить на два',
    'add_one_to_end': 'Приписать единицу в конец',
    'nothing_to_do': 'Ничего делать не нужно, изначальное и желаемое числа равны'
}


res = get_strategy(a)
if isinstance(res, list):
    print('Победная стратегия найдена:')
    for key, instruction in enumerate(res):
        print(f'{key + 1}) {instruction}')
else:
    print('Победная стратегия отсутсвует')