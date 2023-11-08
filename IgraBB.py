import random
import json
import csv
import os
completed_quests = []

def рассказ():
    print("В далеко забытой деревне друг друга полюбили два человека. \n И появился у них сын. Это был я.")
    print("Я с детства был смышленым и очень любил своих лошадей, поэтому в будующем хотел стать конюхом.\n Однажды в день лунного праздника на деревню напали злые чудища, их деревенские жители прозвали \n пустотами, потому что после их нападков не остается ничего.")
    print("Но в этот раз их было намного больше чем обычно и они сносили всю деревню и убивали каждого на \n своем пути.")
    print("И вот они дошли до моего дома")
    print("Матушка посадила меня на печку, накрыла одеялами и сказала не высовываться, но я ее не послушался. ")
    print("Выглянув из-под одеяла, я услышал крик родителей и ржание лошадей, и от страха потерял сознание")
    print("И вот я проснулся уже в столице королевства в городе Митакихара")
    print("Я живу один и скоро уже смогу устроиться искателем приключений и сражаться с нечестью ")
    print("- Создатель: Вот ты и познакомился с ним. Я даю тебе право управлять его судьбой. Твоя задача с помощью \n своего жизненного опыта помочь ему в сражениях")

def начало():
    print("Ого, уже пора бежать в гильдию за первым заданием")
    print("Как здесь красиво!")

def гильдия():
    print("Вы вошли в гильдию.")
    print("Доступные задания:")
    print("1. Избавиться от гоблинов в лесу")
    print("2. Избавиться от слизней на поле")
    print("3. Уничтожить дракона в пещере")
    print("4. Найти украденный артефакт в заброшенном замке")
    print("5. Защитить деревню от орков")


    quest = input("Выберите номер задания: ")

    if quest == "1":
        print("Вы приняли задание 'Избавиться от гоблинов в лесу'")
        num_goblins = 3
        while num_goblins > 0:
            attack = input("Вы атакуете гоблинов! Куда вы нанесете удар? (голова, тело, ноги) ")
            if attack == "голова":
                print("Вы убиваете одного гоблина! Осталось", num_goblins-1, "гоблинов.")
                num_goblins -= 1
            elif attack == "тело":
                print("Вы убиваете одного гоблина! Осталось", num_goblins-1, "гоблинов.")
                num_goblins -= 1
            elif attack == "ноги":
                print("Вы убиваете одного гоблина! Осталось", num_goblins-1, "гоблинов.")
                num_goblins -= 1
            else:
                print("Вы промахнулись! Гоблины атакуют вас!")
        print("Вы успешно избавились от гоблинов!")
        completed_quests.append("Избавиться от гоблинов в лесу")
        save_data(completed_quests)
    elif quest == "2":
        print("Вы приняли задание 'Избавиться от слизней на поле'")
        num_slimes = 5
        your_hp = 100
        while num_slimes > 0 and your_hp > 0:
            attack = input("Вы атакуете слизней! Куда вы нанесете удар? (голова, тело, ноги) ")
            if attack == "голова":
                print("Вы убиваете одного слизня! Осталось", num_slimes-1, "слизней.")
                num_slimes -= 1
            elif attack == "тело":
                print("Вы убиваете одного слизня! Осталось", num_slimes-1, "слизней.")
                num_slimes -= 1
            elif attack == "ноги":
                print("Вы убиваете одного слизня! Осталось", num_slimes-1, "слизней.")
                num_slimes -= 1
            else:
                print("Вы промахнулись! Слизни атакуют вас!")
                your_hp -= 10
                print("Ваше здоровье:", your_hp)
        if num_slimes == 0:
            print("Вы успешно избавились от слизней!")
            completed_quests.append("Избавиться от слизней на поле")
            save_data(completed_quests)
        else:
            print("Вас победили слизни. Задание не выполнено.")
    elif quest == "3":
        print("Вы приняли задание 'Уничтожить дракона в пещере'")
        dragon_hp = 150
        your_hp = 150
        while dragon_hp > 0 and your_hp > 0:
            attack = input("Вы атакуете дракона! Куда вы нанесете удар? (голова, тело, ноги) ")
            if attack == "голова":
                print("Вы нанесли сильный удар по голове дракона! Оставшееся здоровье дракона:", dragon_hp-50)
                dragon_hp -= 50
            elif attack == "тело":
                print("Вы нанесли удар по телу дракона! Оставшееся здоровье дракона:", dragon_hp-30)
                dragon_hp -= 30
            elif attack == "ноги":
                print("Вы нанесли удар по ногам дракона! Оставшееся здоровье дракона:", dragon_hp-20)
                dragon_hp -= 20
            else:
                print("Вы промахнулись! Дракон атакует вас!")
                your_hp -= 30
                print("Ваше здоровье:", your_hp)
                if dragon_hp == 0:
                    print("Вы успешно уничтожили дракона! Задание выполнено.")
                    completed_quests.append("Уничтожить дракона в пещере")
                    save_data(completed_quests)
        else:
            print("Вас победил дракон. Задание не выполнено.")
    elif quest == "4":
        print("Вы приняли задание 'Найти украденный артефакт в заброшенном замке'")
        artifact_found = False
        rooms_explored = 0
        while not artifact_found and rooms_explored < 3:
            explore = input("Вы исследуете комнату? (да/нет) ")
            if explore == "да":
                print("Вы исследуете комнату...")
                artifact_chance = random.randint(1, 4)
                if artifact_chance <= 4:
                    artifact_found = True
                    print("Вы нашли украденный артефакт! Задание выполнено.")
                    completed_quests.append("Найти украденный артефакт в заброшенном замке")
                    save_data(completed_quests)
                else:
                    print("В комнате ничего интересного. Идем дальше.")
                rooms_explored += 1
            elif explore == "нет":
                print("Вы пропускаете эту комнату и идете дальше.")
                rooms_explored += 1
            else:
                print("Некорректный ввод. Повторите попытку.")
        if not artifact_found:
            print("Украденный артефакт не найден. Задание не выполнено.")

    elif quest == "5":
        print("Вы приняли задание 'Защитить деревню от орков'")
        num_orcs = random.randint(5, 10)
        your_hp = 100
        while num_orcs > 0 and your_hp > 0:
            attack = input("Вы атакуете орков! Куда вы нанесете удар? (голова, тело, ноги) ")
            if attack == "голова":
                print("Вы убиваете одного орка! Осталось", num_orcs-1, "орков.")
                num_orcs -= 1
            elif attack == "тело":
                print("Вы убиваете одного орка! Осталось", num_orcs-1, "орков.")
                num_orcs -= 1
            elif attack == "ноги":
                print("Вы убиваете одного орка! Осталось", num_orcs-1, "орков.")
                num_orcs -= 1
            else:
                print("Вы промахнулись! Орки атакуют вас!")
                your_hp -= 20
                print("Ваше здоровье:", your_hp)
        if num_orcs == 0:
            print("Вы успешно защитили деревню от орков!")
            completed_quests.append("Защитить деревню от орков")
            save_data(completed_quests)
        else:
            print("Вас победили орки. Задание не выполнено.")
    else:
        print("Некорректный выбор задания. Повторите попытку.")
    if len(completed_quests) == 4:
        print("Поздравляю! Вы выполнили все задания и завершили игру!")
    else:
        print("Выполненные задания:", completed_quests)

def меню():
    print("==== Меню ====")
    print("1. Пойти в гильдию")
    print("2. Выйти из игры")

def save_data(data):
    with open('save_data.json', 'w') as file:
        json.dump(data, file)

def load_data():
    try:
        with open('save_data.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

def delete_save():
    try:
        os.remove('save_data.json')
        print("Сохранение удалено.")
    except FileNotFoundError:
        print("Сохранение не найдено.")

def write_to_csv(data):
    fieldnames = ['Завершенные задания']
    with open('game_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for quest in data:
            writer.writerow({'Завершенные задания': quest})

def main():
    рассказ()
    print("\n=== Начало игры ===\n")
    начало()

    saved_data = load_data()
    completed_quests = saved_data
    if os.path.exists('save_data.json'):


        print("Обнаружено сохранение.\n")
        print("=== Продолжение игры ===\n")
        print("Выполненные задания:", completed_quests)
        choice = input("Хотите просмотреть сохраненные данные? (да/нет) ")
        if choice == "да":
            if len(completed_quests) > 0:
                print("\nВыполненные задания:")
                for quest in completed_quests:
                    print(quest)
            else:
                print("\nНет выполненных заданий.")

            decision = input("\nХотите удалить сохранение? (да/нет) ")
            if decision == "да":
                delete_save()
            else:
                print("Продолжаем игру...")
                гильдия()
        else:
            гильдия()

    while True:
        меню()
        choice = input("Введите номер опции: ")

        if choice == "1":
            гильдия()
        elif choice == "2":
            print("Выход из игры...")
            save_data(completed_quests)
            write_to_csv(completed_quests)
            break
        else:
            print("Ошибка: выберите допустимую опцию.")
main()
