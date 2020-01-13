month_by_numbers = list(range(1, 13))

month_by_word = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                 'Ноябрь', 'Декабрь', ]

month_dict = {}

i = 0

while i < len(month_by_numbers):
    month_dict[month_by_numbers[i]] = month_by_word[i]
    i += 1

picked_month = int(input("Введите месяц в виде целого числа от 1 до 12: "))

if picked_month in range(1, 13):
    print(month_dict[picked_month])