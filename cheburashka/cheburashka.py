def main():
    from abc import ABC, abstractmethod

    class Actor(ABC):
        def __init__(self, play_area, name):
            self.play_area = play_area
            self.name = name

        @abstractmethod
        def can_move(self):
            pass  # return self.play_area.pick_good_orange() is not None

        @abstractmethod
        def make_move(self, action_id):
            pass

        @abstractmethod
        def show_actions(self):
            message = "Я могу:\n"
            return message

    class Cheburashka(Actor):

        def can_move(self):
            pass

        def make_move(self, action):
            if action == 1:
                for i in range(2):
                    print("AWPODKAPWODK")
                    good_orange = self.play_area.pick_good_orange()
                    self.play_area.remove_orange(good_orange)
            elif action == 2:
                good_orange = self.play_area.pick_good_orange()
                self.play_area.remove_orange(good_orange)

                rotten_orange = self.play_area.pick_rotten_orange()
                self.play_area.remove_orange(rotten_orange)
            else:
                return False

        def show_actions(self):
            message = super
            message += "1) Съесть два хороших\n"
            message += "2) Съесть один хороший и выкинуть один гнилой"
            return message

    class Shapka(Actor):

        def can_move(self):
            ...

        def make_move(self):
            ...

        def show_actions(self):
            message = super
            message += "1) Съесть один хороший\n"
            message += "2) Заменить два хороших на два гнилых"
            return message

    class Orange:
        rotten = False

    class Box:
        area = []

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
            if orange is not None:
                self.area.remove(orange)
            else:
                raise Exception("Null Orange")

        def count_good_oranges(self):
            good_area = [orange for orange in self.area if not orange.rotten]
            return len(good_area)

        def count_rotten_oranges(self):
            rotten_area = [orange for orange in self.area if orange.rotten]
            return len(rotten_area)

    n = int(input("Сколько апельсинов изначально? "))
    box = Box(n)
    # cheburashka = Cheburashka(box, "Чебурашка")
    # Shapka = Shapka(box, "Шапокляк")

    # while cheburashka.can_move() and Shapka.can_move():
    #     pass


main()
