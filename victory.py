def game():
    import random

    famous_people = {'Пушкин': "26.06.1799", 'Лермонтов': "15.10.1814",
                     'Есенин': "03.10.1895", 'Высоцкий': "25.01.1938"}

    rounds = int(input("Сколько раз? "))

    for i in range (rounds):
        name, date = random.choice(list(famous_people.items()))
        answer = input(f"когда родился {name}? ")
        if answer == date:
            print("да")
        else:
            print("нет")
    print("пока")