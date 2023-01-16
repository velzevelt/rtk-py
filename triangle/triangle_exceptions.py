class NonExistingTriangleError(Exception):
    standart_message = 'Треугольника с такими сторонами не существует'

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return self.message
        else:
            return self.standart_message


class TooFewSidesError(NonExistingTriangleError):
    standart_message = 'Передано недостаточно сторон'
