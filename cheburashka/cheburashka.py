def main():
    class Actor:
        actions_available = []

        class Action:
            def __init__(self, exist_condition: callable, action_func: callable, action_description: str):
                self.exist_condition = exist_condition
                self.action_func = action_func
                self.action_description = action_description

        def __init__(self, play_area, name: str):
            self.play_area = play_area
            self.name = name

        def can_move(self):
            available_count = [action for action in self.actions_available if action.exist_condition()]
            return len(available_count) != 0

        def make_move(self, action_id: int):
            action_id -= 1

            try:
                if self.actions_available[action_id].exist_condition():
                    self.actions_available[action_id].action_func()
                    return True
                else:
                    return False
            except IndexError:
                return False

        def show_actions(self):
            message = f"{self.name}:\n"
            actions = [action for action in self.actions_available if action.exist_condition()]
            for action_id, action in enumerate(actions):
                message += f"{action_id + 1}) {action.action_description}\n"
            return message

    class Cheburashka(Actor):
        def __init__(self, play_area, name):
            super().__init__(play_area, name)
            eat_two_action = Actor.Action(
                lambda: self.play_area.count_good_oranges() >= 2,
                self.eat_two,
                "Съесть два хороших апельсина"
            )
            eat_one_throw_rotten_action = Actor.Action(
                lambda: self.play_area.count_good_oranges() >= 1 and self.play_area.count_rotten_oranges() >= 1,
                self.eat_one_throw_rotten,
                "Съесть один хороший, выбросить один гнилой"
            )
            self.actions_available = [eat_two_action, eat_one_throw_rotten_action]

        def eat_two(self):
            for i in range(2):
                good_orange = self.play_area.pick_good_orange()
                self.play_area.remove_orange(good_orange)

        def eat_one_throw_rotten(self):
            good_orange = self.play_area.pick_good_orange()
            self.play_area.remove_orange(good_orange)

            rotten_orange = self.play_area.pick_rotten_orange()
            self.play_area.remove_orange(rotten_orange)

    class Shapka(Actor):
        def __init__(self, play_area, name):
            super().__init__(play_area, name)
            eat_one_action = Actor.Action(
                lambda: self.play_area.count_good_oranges() >= 1,
                self.eat_one,
                "Съесть один хороший"
            )
            replace_two_rotten_action = Actor.Action(
                lambda: self.play_area.count_good_oranges() >= 2,
                self.replace_two_rotten,
                "Заменить два хороших апельсина на два гнилых"
            )
            self.actions_available = [eat_one_action, replace_two_rotten_action]

        def eat_one(self):
            good_orange = self.play_area.pick_good_orange()
            self.play_area.remove_orange(good_orange)

        def replace_two_rotten(self):
            for i in range(2):
                good_orange = self.play_area.pick_good_orange()
                good_orange.rotten = True

    class Box:
        area = []

        class Orange:
            rotten = False

        def __init__(self, n):
            self.area = [self.Orange() for i in range(n)]
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

        def count_oranges(self):
            return len(self.area)

    def autoplay():
        pass

    def start_game():
        while True:
            try:
                n = int(input("Сколько апельсинов изначально? "))
                break
            except ValueError:
                print("Пожалуйста, введите целое число")

        box = Box(n)
        cheburashka = Cheburashka(box, "Чебурашка")
        shapka = Shapka(box, "Шапокляк")

        active_player = cheburashka

        while active_player.can_move():
            print(active_player.show_actions())
            while True:
                try:
                    action = int(input(f'Что должен сделать {active_player.name}? '))
                    if not active_player.make_move(action):
                        raise ValueError
                    break
                except ValueError:
                    print("Пожалуйста, выберите номер действия из доступного списка")
                    print(active_player.show_actions())

            print(f"Апельсинов осталось: {box.count_oranges()}")

            winner = active_player
            active_player = shapka if active_player == cheburashka else cheburashka

        print(f"Победитель: {winner.name}")

    start_game()



main()
