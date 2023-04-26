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
        str( Fraction(1, 2) + Fraction(4, 10) )
        str( Fraction(3, 2) + 0.4)
        
        4. Умножение
        frac = Fraction(1, 2) * 3
        frac = Fraction(1, 2) * Fraction(3, 1)
        
        5. Деление
        frac1 = Fraction(1, 2) / 3
        frac2 = Fraction(1, 2) // 3
        Обратите внимание, frac1 == frac2,
        т.е операторы ведут себя идентично для данного объекта
        
        4. Упрощение
        str( Fraction(3, 6).simplify() )

    Доступны большинство мат. операций для Fraction
    
    Для выхода из интерактивного режима:
     1) Ctrl+D
     2) Команда exit()
    
    *********************************************
    """
    return message

if __name__ == '__main__':
    main()