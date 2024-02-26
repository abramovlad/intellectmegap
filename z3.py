import csv

with open('songs.csv', encoding='utf-8') as f:
    # Открываем файл в переменную f
    data = list(csv.reader(f, delimiter=';'))[1:]
    # Считываем данные в список data
    while True:
        searching_name = input('Введите имя артиста: ')
        if searching_name == '0':
            break
        # Условие выхода
        for streams, artist_name, track_name, date in data:
            # Разделяем содержимое списка data
            if searching_name == artist_name:
                answer = f'У {artist_name} найдена песня: {track_name}'
                break
        else:
            answer = 'К сожалению, ничего не удалось найти'
        print(answer)
