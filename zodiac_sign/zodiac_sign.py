class MyDate:
        # [0] день_начало
        # [1] месяц_начало
        # [2] день_конец
        # [3] месяц_конец
    intervals = {
           "Овен": (21, 3, 20, 4),

           "Телец": (21, 4, 20, 5),

           "Близнецы": (21, 5, 20, 6),

           "Рак": (21, 6, 22, 7),

           "Лев": (23, 7, 22, 8),

           "Дева": (23, 8, 22, 9),

           "Весы": (23, 9, 22, 10),

           "Скорпион": (23, 10, 22, 11),

           "Стрелец": (23, 11, 21, 12),

           "Козерог": (22, 12, 19, 1),

           "Водолей": (20, 1, 19, 2),

           "Рыбы": (20, 2, 20, 3),
        }
    
    def __init__(self, day: int, month: int):
        self.day = int(day)
        self.month = int(month)
    
    
    def get_sign(self):
        result = "Знак не найден"
        
        # [0] день_начало
        # [1] месяц_начало
        # [2] день_конец
        # [3] месяц_конец
        for key, val in self.intervals.items():
            if self.month == val[1]:
                if self.day >= val[0]:
                    result = key
                    break
            elif self.month == val[3]:
                if self.day <= val[2]:
                    result = key
                    break
        
        return result




day = input('День ')
month = input('Месяц ')

date = MyDate(day, month)
sign = date.get_sign()
print(sign)