from array import *
import random
import prettytable

def generate_rate(min=0, max=0):
    return random.randint(min, max)

# Имеются данные о стоимости доллара по курсу Сбербанка по дням в течение месяца (массив заполняется случайными данными в диапазоне значений [10; 80]). Указать самый высокий и низкий курс доллара. Дополнительно реализовать обмен по самому выгодному курсу доллара с учетом введенной суммы для обмена. Дополнительно рассчитать средний курс доллара месяца и для каждого дня указать отклонение курса от этого среднего значения. Вычислить количество дней, когда курс превышал среднемесячное значение
def main():
    month_dollar_rate = array('i', [generate_rate(min=10, max=80) for i in range(31)])
    min_rate = min(month_dollar_rate)
    max_rate = max(month_dollar_rate)
    average_rate = sum(month_dollar_rate) // len(month_dollar_rate)

    while True:
        try:
            exchange_sum = int(input('Введите сумму для обмена: '))
            break
        except ValueError:
            print('Введите целое число')
        except KeyboardInterrupt:
            return

    formatted_rate = ["{0:+.02f}%".format(round(100 - (average_rate / i) * 100, 2)) for i in month_dollar_rate]
    out_table = prettytable.PrettyTable(('День', 'Значение', 'Отклонение'))
    out_table.add_rows([i + 1, val, formatted_rate[i]] for i, val in enumerate(month_dollar_rate))
    print(out_table)

    print(f'Минимальный курс: {min_rate}')
    print(f'Максимальный курс: {max_rate}')
    print(f'Среднее значение: {average_rate}')

    exchange_sum *= min_rate
    print(f'Новый счет: {exchange_sum}')



if __name__ == '__main__':
    main()
