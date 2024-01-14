def vopr():
    from victory import game

    print("Привет")
    name = input("Как зовут? ")

    ready = input("Готов? ")
    while(ready!="да"):
        if ready == "нет":
            print("Готовься")
        else:
            print("Че сказал?")
        ready = input("Готов? ")

    game()