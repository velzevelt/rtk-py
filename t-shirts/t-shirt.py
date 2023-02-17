import random


class Student:
    sizes = ('S', 'M', 'L', 'XL', 'XXL', 'XXXL')

    def __init__(self):
        self.desired_size = self.get_random_size()

    def get_random_size(self):
        return random.choice(sizes)


students = [Student() for i in range(5)]
print(students)
