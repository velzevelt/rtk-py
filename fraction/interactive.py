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
        frac = Fraction(1, 2)

        2. Просмотр значения
        str(frac)

        3. Сложение
        str( Fraction(1, 2) + Fraction(3, 4) )

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