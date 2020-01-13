text = input("Введите любое предлодение: ")

text_list = text.split(" ")

i = 1

for w in text_list:
    print(f"{i}: {w}")
    i += 1