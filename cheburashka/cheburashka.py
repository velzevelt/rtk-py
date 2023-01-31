def main():
    from abc import ABC, abstractmethod

    class Actor(ABC):
        def __init__(self, play_area):
            self.play_area = play_area

        @abstractmethod
        def can_move(self):
            pass

        @abstractmethod
        def make_move(self):
            pass

    class Cheburashka(Actor):
        actions = [
            "Cъесть два",
            "Съесть один, выкинуть гнилой"
        ]
        def can_move(self):
            ...

        def make_move(self, action="Съесть два"):
            ...

    class Shapka(Actor):
        def can_move(self):
            ...

        def make_move(self):
            ...

    class Orange:
        rotten = False

    class Box:
        area = []
        good_count = 0

        def __init__(self, n):
            self.area = [Orange() for i in range(n)]
            self.good_count = len(self.area)

        def pick_good_orange(self):
            for orange in self.area:
                if orange.rotten:
                    continue
                else:
                    return orange



    n = int(input("Сколько апельсинов изначально? "))
    box = Box(n)
    # cheburashka = Cheburashka(box)
    # Shapka = Shapka(box)

    # while cheburashka.can_move() and Shapka.can_move():
    #     pass


main()
