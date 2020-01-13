my_products = []

while True:

    add_some_product = input("Хотите добавить новый товар?(y/n): ")

    if add_some_product.lower() == 'y':

        name = input("Введите название товара: ")
        price = int(input("Введите цену товара: "))
        amount = int(input("Введите количество товара: "))
        unit = input("Введите единицу измерения товара: ")

        if len(my_products) == 0:

            product_tuple = (1, {"название": name, "цена": price, "количество": amount, "eд": unit})
            my_products.append(product_tuple)

        elif len(my_products) > 0:

            product_number = len(my_products) + 1

            product_tuple = (product_number, {"название": name, "цена": price, "количество": amount, "eд": unit})
            my_products.append(product_tuple)

    elif add_some_product.lower() == 'n':
        print(my_products)
        break

my_products_dict = {
    "название": [],
    "цена": [],
    "количество": [],
    "eд": []
}

for i in my_products:

    product_dict = i[1]

    for k,v in my_products_dict.items():
        value = my_products_dict[k]
        value.append(product_dict[k])

        my_products_dict[k] = value

print(my_products_dict)