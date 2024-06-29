alice_in_wonderland = """
"Would you tell me, please,
 which way I ought to go from here?"\n
"That depends a good deal on where
 you want to get to," said the Cat.\n
"I don't much care where ——" said Alice.\n
"Then it doesn't matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you're sure to do that," said
the Cat, "if you only walk long enough."
"""
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""


# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436_402
azov_sea = 37_800
seas_square = black_sea + azov_sea
print(f"Square of the seas is {seas_square} km2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
goods_total_num = 375_291
first_second = 250_449
second_third = 222_950
third_storage = goods_total_num - first_second
first_storage = goods_total_num - second_third
second_storage = goods_total_num - (first_storage + third_storage)
storage_list = [first_storage, second_storage, third_storage]
for storage in storage_list:
    print(storage)


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payment_amount = 1179
grace_period = 18
pc_cost = payment_amount * grace_period
print(f"PC cost is {pc_cost} hryvnias")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a_task = 8000 % 8
b_task = 9907 % 9
c_task = 2789 % 5
d_task = 7248 % 6
e_task = 7128 % 5
f_task = 19224 % 9
results_list = [a_task, b_task, c_task, d_task, e_task, f_task]
new_list = []
for res in results_list:
    new_list.append(res)
print(new_list)


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza = 274
middle_pizza = 218
juice_drink = 35
cake = 350
water_for_bd = 21
order_sum = (big_pizza * 4) + (middle_pizza * 2) + (juice_drink * 4) + (water_for_bd * 3) + cake
print(f"Irynka needs {order_sum} hryvnas for this order")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos_num = 232
photos_on_page = 8
pages_for_photos = photos_num / photos_on_page
print(f"Igor needs {int(pages_for_photos)} pages for his album")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
trip_distance = 1600
gasoline_cons = 9
tank_volume = 48
gas_for_trip = (gasoline_cons / 100) * trip_distance
tank_count = gas_for_trip / tank_volume
print(f"Family needs {gas_for_trip} liters of gas and they should full their tank {int(tank_count)} times")
