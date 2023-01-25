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

    def has_won():
        print("Вы решили задачу")
        print("Игра завершена")
        return len(finish_side) == 3

    def make_move(first_side, second_side) -> None:
        name_1 = ", ".join(get_names(first_side).keys())
        name_2 = ", ".join(get_names(second_side).keys())
        print(f"На этом берегу: {name_1}")
        print(f"На том берегу: {name_2}")

        transfer = input("Кого переправить на тот берег? ")
        if transfer in get_names(first_side):
            transfer = get_names(first_side)[transfer]
            sail_entity(transfer, first_side, second_side)

    while True:
        make_move(start_side, finish_side)
        if has_loosed(start_side):
            break
        if has_won():
            break

        make_move(finish_side, start_side)
        if has_loosed(finish_side):
            break
        if has_won():
            break

    



main()
