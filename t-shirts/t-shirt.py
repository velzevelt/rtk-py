import random


class Student:
    sizes = ('S', 'M', 'L', 'XL', 'XXL', 'XXXL')
    sure_chance = .75  # шанс на то, что студент знает свой размер

    def __init__(self):
        self.desired_size = self.get_random_size()

    def get_random_size(self):
        if len(self.sizes) > 2:
            sure = random.random()
            if self.sure_chance > sure:
                return random.choice(self.sizes)
            else:
                first = random.choice(self.sizes)
                second = random.choice(self.sizes)
                while second == first:
                    second = random.choice(self.sizes)

                return [first, second]
        else:
            raise IndexError("Init error need at least 2 to process")


students = [Student() for i in range(5)]
