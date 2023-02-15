class State:
    def __init__(self, num, action_name):
        self.num = num
        self.action_name = action_name


def multiply_by_two(num):
    return num * 2


def add_one_to_end(num):
    return num * 10 + 1


a = 5
b = 20

states = [State(a, None)]


def get_strategy(num, current_state_id: int = 0, action: callable = multiply_by_two):
    temp = action(num)

    if temp < b:
        states.append(State(temp, action))
        return get_strategy(temp, current_state_id + 1)
    elif temp == b:
        states.append(State(temp, str(action.__name__)))
        return [state.action_name for state in states]
    else:
        prev_id = current_state_id - 1
        if prev_id > 0:
            return get_strategy(states[prev_id].num, prev_id, add_one_to_end)
        else:
            return False


res = get_strategy(a)
print(res)
