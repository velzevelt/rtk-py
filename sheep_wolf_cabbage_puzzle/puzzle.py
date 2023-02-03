def main():
    class Actor:
        def __init__(self, nickname: str):
            self.nickname = nickname

    sheep = Actor('Овца')
    cabbage = Actor('Капуста')
    wolf = Actor('Волк')

    sheep.goal = cabbage
    wolf.goal = sheep

    start_side = [sheep, cabbage, wolf]
    finish_side = []

    def get_names(from_side):
        return {actor.nickname: actor for actor in from_side}

    def sail_entity(entity: object, side: list, destination: list) -> None:
        if entity in side and entity not in destination:
            side.remove(entity)
            destination.append(entity)

    def has_loosed(side):
        for actor in side:
            if not hasattr(actor, "goal"):
                continue
            if actor.goal in side:
                print(f"{actor.nickname} съел {actor.goal.nickname}")
                print("Игра завершена")
                return True
                
        return False

    def has_won(side):
        return len(side) == 3

    def restart_suggest():
        restart = input("Вы проиграли, начать заново д/н? ")
        if restart.lower() == "д":
            play_game(start_side, finish_side)
            return True
        return False

    def step_back_suggest(init_side, end_side, skip_first_move=False):
        step_back = input("Вы проиграли, сделать шаг назад д/н? ")
        if step_back.lower() == "д":
            play_game(init_side, end_side, skip_first_move)
            return True
        return False


    def make_move(first_side, second_side) -> None:
        name_1 = ", ".join(get_names(first_side).keys())
        name_2 = ", ".join(get_names(second_side).keys())
        print(f"На этом берегу: {name_1}")
        print(f"На том берегу: {name_2}")

        transfer = input("Кого переправить на тот берег? ")
        if transfer in get_names(first_side):
            transfer = get_names(first_side)[transfer]
            sail_entity(transfer, first_side, second_side)

    '''
    Победа достигается комбинацией:
        Овца
        Пропуск
        Капуста
        Овца
        Волк
        Пропуск
        Овца
    '''
    def play_game(init_side, end_side, skip_first_move=False):
        while True:

            if not skip_first_move:
                init_side_copy = init_side.copy()
                end_side_copy = end_side.copy()

                make_move(init_side, end_side)
                if has_loosed(init_side):
                    if not restart_suggest():
                        step_back_suggest(init_side_copy, end_side_copy)
                    break

                if has_won(end_side):
                    print("Вы решили задачу")
                    print("Игра завершена")
                    break

            init_side_copy = init_side.copy()
            end_side_copy = end_side.copy()

            make_move(end_side, init_side)
            if has_loosed(end_side):
                if not restart_suggest():
                    step_back_suggest(init_side_copy, end_side_copy, True)
                break
            if has_won(end_side):
                print("Вы решили задачу")
                print("Игра завершена")
                break

    play_game(start_side.copy(), finish_side.copy())
    



main()
