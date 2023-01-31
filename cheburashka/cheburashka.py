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
            message = "Я могу:\n"

    class Cheburashka(Actor):

        def make_move(self, action):
            ...

        def show_actions(self):
            message = super
            message += "1) Съесть два хороших\n"
            message += "2) Съесть один хороший и выкинуть один гнилой"
            print(message)

    class Shapka(Actor):

        def make_move(self):
            ...

        def show_actions(self):
            message = super
            message += "1) Съесть один хороший\n"
            message += "2) Заменить два хороших на два гнилых"
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

        def pick_rotten_orange(self):
            for orange in self.area:
                if orange.rotten:
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
