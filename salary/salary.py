import random
import prettytable

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

print(salaries)
print(year_income, year_pension_allocation)
