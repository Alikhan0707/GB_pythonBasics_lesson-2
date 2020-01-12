data = []

i = 0

while True:
    data_from_user = input("Введите любое число! Для выхода из цикла введите 'q': ")

    if data_from_user == 'q':
        break
    else:
        data.append(int(data_from_user))

print(data)

while i < len(data):
    if len(data) % 2 == 0:
        remove_data = data.pop(i)
        data.insert((i + 1), remove_data)
        i += 2
    elif len(data) % 2 != 0 and len(data) - i > 1:
        remove_data = data.pop(i)
        data.insert((i + 1), remove_data)
        i += 2
    elif len(data) % 2 != 0 and len(data) - i == 1:
        break

print(data)