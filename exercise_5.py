rate_list = []

while True:
    rate = input("Оцените от 1 до 10! Введите 'q' для выхода из цикла: ")

    if len(rate_list) >= 0 and rate.lower() == 'q':

        print(rate_list)
        break

    elif len(rate_list) >= 0 and int(rate) is not int and rate.lower() != 'q' and int(rate) not in range(1, 11):

        print("Введите число от 1 до 10")

    elif len(rate_list) > 0 and int(rate) in rate_list:

        rate_list.reverse()
        elem_index = rate_list.index(int(rate))
        rate_list.insert(elem_index, int(rate))
        rate_list.reverse()
        print(rate_list)

    elif len(rate_list) == 0 and int(rate) in range(1, 11):

        rate_list.append(int(rate))
        rate_list.sort()
        print(rate_list)

    elif len(rate_list) > 0 and int(rate) not in rate_list and int(rate) in range(1, 11):

        for e in rate_list:

            if e < int(rate):

                e_index = rate_list.index(e)
                rate_list.insert(e_index, int(rate))
                print(rate_list)
                break

