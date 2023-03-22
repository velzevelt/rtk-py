import random
import prettytable
import enum

'''

Имеются зарплаты одного сотрудника фирмы по месяцам года (диапозон значений [1000; 5000]$).
Вывести данные на экран и выполнить следующие расчеты: общую сумму выплат за год; среднюю зарплату за год;
сумму отчислений в пенсионный фонд по месяцам и общую за год (2% от ежемесячной зарплаты).

*Дополнительно отобразить отклонения зарплаты каждого месяца от средней зарплаты за год.
*Дополнительно отобразить максимальную и минимальную зарплату и номер месяца, когда она была получена.


'''

# salaries per month
salaries = [random.randint(1000, 5000) for i in range(12)]

pension_allocations = [round(salary * 0.02) for salary in salaries]
year_income = sum(salaries)
year_pension_allocation = round(year_income * 0.02)
average_salary = year_income // len(salaries)

print(salaries)
print(year_income, year_pension_allocation)

# prepare table
table = prettytable.PrettyTable()
table.field_names = ['N', 'Месяц', 'Зарплата', 'Отчисления', 'Отклонение']

MONTHS_ALIAS = {
    0: 'Январь',
    1: 'Февраль',
    2: 'Март',
    3: 'Апрель',
    4: 'Май',
    5: 'Июнь',
    6: 'Июль',
    7: 'Август',
    8: 'Сентябрь',
    9: 'Октябрь',
    10: 'Ноябрь',
    11: 'Декабрь'
}

NUM_FORMAT = "{:}$"


# insert formatted data in table
for key, value in enumerate(salaries):
    deviation = "{0:+.02f}%".format( 100 - (average_salary / value) * 100, 2)
    table.add_row([key + 1, MONTHS_ALIAS[key], NUM_FORMAT.format(value), NUM_FORMAT.format(pension_allocations[key]), deviation])

print(table)

