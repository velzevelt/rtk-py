def main():
    from abc import ABC, abstractmethod

    class Actor(ABC):
        def __init__(self, play_area):
            self.play_area = play_area

        def can_move(self):
            return self.play_area.pick_good_orange() is not None

        @abstractmethod
        def make_move(self, action):
            pass

        @abstractmethod
        def show_actions(self):
            pass

    class Cheburashka(Actor):

        def make_move(self, action):
            ...

        def show_actions(self):
            message = ""
            print(message)

    class Shapka(Actor):

        def make_move(self):
            ...

        def show_actions(self):
            message = ""
            print(message)

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
            return None

        def remove_orange(self, orange):
            self.area.remove(orange)



    n = int(input("Сколько апельсинов изначально? "))
    box = Box(n)
    # cheburashka = Cheburashka(box)
    # Shapka = Shapka(box)

    # while cheburashka.can_move() and Shapka.can_move():
    #     pass


main()
