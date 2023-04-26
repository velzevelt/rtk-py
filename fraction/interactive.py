import code
from fraction import Fraction

def main():
    code.interact(local=dict(globals(), **locals()), banner=greet()) 

def greet():
    message = """ 
    *********************************************
    
    Взаимодействие посредством InteractiveConsole
    Доступны все возможности python

    Примеры:
        1. Создание дроби
        frac = Fraction(3, 10)
        frac = Fraction(0.3)

        2. Просмотр значения
        str(frac) или print(frac)

        3. Сложение
        frac = Fraction(1, 2) + Fraction(4, 10)
        frac = Fraction(3, 2) + 0.4
        
        4. Умножение
        frac = Fraction(1, 2) * 3
        frac = Fraction(1, 2) * Fraction(3, 1)
        
        5. Деление
        frac1 = Fraction(1, 2) / 3
        frac2 = Fraction(1, 2) // 3
        Обратите внимание, что frac1 == frac2,
        т.е операторы / и // ведут себя идентично для данного объекта
        
        6. Упрощение
        print( Fraction(3, 6).simplify() )

    Доступны большинство мат. операций для Fraction
    
    Для выхода из интерактивного режима:
     1) Ctrl+D
     2) Ctrl+Z+Enter
     3) Команда exit()
    
    *********************************************
    """
    return message


if __name__ == '__main__':
    main()