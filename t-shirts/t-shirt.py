import random
from dataclasses import dataclass


@dataclass
class Size:
    size_alias: str
    quantity: int = 0


def get_random_qty(max_qty: int = 10):
    return random.randrange(0, max_qty)


sizes = (
    Size('S', get_random_qty(32)),
    Size('M', get_random_qty(32)),
    Size('L', get_random_qty(32)),
    Size('XL', get_random_qty(32)),
    Size('XXL', get_random_qty(32)),
    Size('XXXL', get_random_qty(32)),

)

class Student:
    sure_chance = .75  # шанс на то, что студент знает свой размер

    def __init__(self):
        self.desired_size = self.get_random_size()

    def get_random_size(self):
        if len(sizes) > 2:
            sure = random.random()
            if self.sure_chance > sure:
                return random.choice(sizes).size_alias
            else:
                max_bound = len(sizes) - 1
                rand_id = random.randrange(0, max_bound)
                first = sizes[rand_id]

                if rand_id != max_bound:
                    second = sizes[rand_id + 1]
                else:
                    second = sizes[rand_id - 1]

                return first.size_alias, second.size_alias
        else:
            raise IndexError("Init error need at least 2 to process")


needed_sizes = {}
for i in range(15):
    student = Student()

    if type(student.desired_size) is tuple:
        for val in student.desired_size:
            if val in needed_sizes:
                needed_sizes[val] += 1
            else:
                needed_sizes[val] = 1
    else:
        if student.desired_size in needed_sizes:
            needed_sizes[student.desired_size] += 1
        else:
            needed_sizes[student.desired_size] = 1

print(needed_sizes)