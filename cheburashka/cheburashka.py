def main():
    from abc import ABC, abstractmethod

    class Actor(ABC):
        actions_available = []

        class Action:
            def __init__(self, exist_condition, action_func, action_description):
                self.exist_condition = exist_condition
                self.action_func = action_func
                self.action_description = action_description

        def __init__(self, play_area, name):
            self.play_area = play_area
            self.name = name

        def can_move(self):
            return len(self.actions_available) != 0

        def make_move(self, action_id):
            if action_id in self.actions_available:
                self.actions_available[action_id]()
            else:
                return False

        def show_actions(self):
            message = "Я могу:\n"
            actions = [action for action in self.actions_available if action.exist_condition]
            for action_id, action in enumerate(actions):
                message += f"{action_id + 1}): {action.action_description}\n"
            return message

    class Cheburashka(Actor):
        def can_move(self):
            pass

    class Shapka(Actor):
        def can_move(self):
            ...

    class Box:
        area = []

        class Orange:
            rotten = False

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
