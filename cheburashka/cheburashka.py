def main():
    class Cheburashka:
        pass

    class Gena:
        pass

    class Orange:
        rotten = False

    def make_move(active_player):
        pass


    def can_move(active_player):
        pass

    def create_box(n) -> list:
        box = [Orange() for i in range(n)]
        return box

    cb = Cheburashka()
    gena = Gena()
    n = int(input("Сколько апельсинов изначально? "))
    box = create_box(n)

    while can_move(cb) or can_move(gena):
        pass
