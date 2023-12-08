def get_card(database_file, search_value):
    database_file = 'card.xlsx'
    green = '\033[92m'
    cyan = '\033[95m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'
    red = '\033[91m'
    card = input(f'{green}{bold}{underline}Введите карту:{end} ')
    from time import sleep
    found = False
    with open(database_file, 'r') as file:
        lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 2:
            get_card = data[3]
            if search_value in get_card:
                name = data[2]
                rod = data[1]
                data = data[4]
                number = data[5]
                adress = data[6]
                print(f'''{red}{bold}

                [+]Номер карты: {card}
                [+]ФИО: {name}
                [+]Дата рождения: {rod}
                [+]Срок действия: {data}
                [+]Номер телефона: {number}
                [+]Адрес: {adress}

                      ''')
                sleep(4)
                found = True
    if not found:
        print("Ничего не найдено в базе данных по номеру телефона.")