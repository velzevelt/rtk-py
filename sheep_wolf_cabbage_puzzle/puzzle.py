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

    def ship_entity(entity: object, side: list, destination: list) -> None:
        if entity in side and entity not in destination:
            side.remove(entity)
            destination.append(entity)

    def has_loosed():
        for actor in finish_side:
            if actor.goal in finish_side:
                return f"{actor.nickname} съел {actor.goal.nickname}"
        return False

    def make_move(first_side, second_side) -> None:
        print(f"На изначальном берегу: {first_side.keys()}")
        print(f"На том берегу: {second_side.keys()}")

        transfer = input("Кого переправить на тот берег? ")
        if transfer in first_side:
            transfer = first_side[transfer]
            ship_entity(transfer, first_side, second_side)

    while not has_loosed():
        make_move()
        loosed = has_loosed()
        if loosed:
            print(loosed)
            print('Игра завершена')
            break


main()
