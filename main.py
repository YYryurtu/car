import random


car_mark = random.randint(1,4)
if car_mark == 1:
    print("Tesla")
elif car_mark == 2:
    print("Mazda")
elif car_mark == 3:
    print("Nissa")
elif car_mark == 4:
    print("Honda")

print("Tesla,"
      "Mazda,"
      "Nissan,"
      "Honda")
a = input("Введи название машины из списка: ")
if a == "Mazda":
    pass
elif a == "Tesla":
    pass
elif a == "Nissa":
    pass
elif a == "Honda":
    pass
else:
    print("Попробуй ещё раз")

b = input("Введи speed машины: ")