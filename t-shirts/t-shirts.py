import random
from functools import lru_cache


def main():
    def get_random_qty(max_qty: int = 10):
        return random.randrange(0, max_qty)

    sizes = {
        'S': get_random_qty(15),
        'M': get_random_qty(15),
        'L': get_random_qty(15),
        'XL': get_random_qty(15),
        'XXL': get_random_qty(15),
        'XXXL': get_random_qty(15),

    }

    class Student:
        sure_chance = .75  # шанс на то, что студент знает свой размер

        def __init__(self):
            self.desired_size = self.get_random_size()

        @lru_cache(maxsize=32)
        def get_random_size(self):
            if len(sizes) > 2:
                sure = random.random()
                if self.sure_chance > sure:
                    keys = list(sizes.keys())
                    return random.choice(keys)
                else:
                    keys = list(sizes.keys())
                    max_bound = len(keys) - 1
                    rand_id = random.randrange(0, max_bound)
                    first = keys[rand_id]
                    if rand_id != max_bound:
                        second = keys[rand_id + 1]
                    else:
                        second = keys[rand_id - 1]

                    return random.choice([first, second])
            else:
                raise IndexError("Init error need at least 2 to process")

    needed_sizes = {}
    for i in range(6):
        student = Student()
        if student.desired_size in needed_sizes:
            needed_sizes[student.desired_size] += 1
        else:
            needed_sizes[student.desired_size] = 1

    for val in needed_sizes:
        if val in sizes:
            if needed_sizes[val] > sizes[val]:
                print('Футболок не хватает')
                return

    print('Футболок хватит всем')
    for size in needed_sizes:
        print(f'Размер {size}, нужно раздать {needed_sizes[size]}')


if __name__ == '__main__':
    main()
