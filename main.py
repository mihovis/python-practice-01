product_name = input("Введите название товара: ").strip()

if not product_name:
    print("Ошибка: название товара не может быть пустым.")
    exit()

try:
    price = float(input("Введите цену товара (руб.): "))
    kol = int(input("Введите количество товара: "))
except ValueError:
    print("Ошибка: цена и количество должны быть числами.")
    exit()

if price <= 0 or kol <= 0:
    print("Ошибка: цена и количество должны быть строго больше нуля.")
    exit()

print("\nВыберите способ доставки:")
print("1. Самовывоз")
print("2. Курьерская доставка (300 руб., бесплатно при заказе от 10 000 руб.)")
delivery_choice = input("Ваш выбор (1 или 2): ").strip()

if delivery_choice not in ("1", "2"):
    print("Ошибка: выбран некорректный способ доставки.")
    exit()

promo = input("\nВведите промокод (если есть, иначе Enter): ").strip().upper()

initial_cost = price * kol

if 5000 <= initial_cost <= 9999:
    discount = 5
elif 10000 <= initial_cost <= 14999:
    discount = 10
elif initial_cost >= 15000:
    discount = 15
else:
    discount = 0

if promo == "BONUS5":
    discount += 5
    print("Промокод применён: скидка увеличена на 5%!")

discount_rub = initial_cost * (discount / 100)
after_discount = initial_cost - discount_rub

delivery_cost = 0
delivery_name = "Самовывоз"

if delivery_choice == "2":
    delivery_name = "Курьер"
    if after_discount >= 10000:
        delivery_cost = 0
        delivery_name = "Курьер (бесплатно по акции от 10 000 руб.)"
    else:
        delivery_cost = 300

total_final = after_discount + delivery_cost

cashback_points = int(after_discount * 0.03)

print("Чек")
print(f"Товар:               {product_name}")
print(f"Цена за ед.:         {price} руб.")
print(f"Количество:          {kol} шт.")
print(f"Исходная стоимость:  {initial_cost} руб.")
print(f"Скидка ({discount}%):        -{discount_rub:.2f} руб.")
print(f"Способ доставки:     {delivery_name}")
print(f"Стоимость доставки:  {delivery_cost:.2f} руб.")

print(f"Итого:               {total_final:.2f} руб.")
print(f"Начислено бонусов:   +{cashback_points} баллов (3%)")
