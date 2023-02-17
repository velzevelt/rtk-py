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
                first = random.choice(sizes)
                second = random.choice(sizes)
                while second == first:
                    second = random.choice(sizes)

                return first.size_alias, second.size_alias
        else:
            raise IndexError("Init error need at least 2 to process")


requested_sizes = []