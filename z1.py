import datetime
import csv

with open('songs.csv', encoding='utf-8') as f:
    # Открываем файл в переменную f
    data = list(csv.reader(f, delimiter=';'))[1:]
    # Считываем данные в список data
    for streams, artist_name, track_name, date in data:
        day, month, year = map(int, date.split('.'))
        # Разделяем содержимое списка date
        current_date = datetime.datetime(year, month, day)

        if current_date <= datetime.datetime(2002, 1, 1):
            # Условие: не позже 01.01.2002
            print(f'{track_name} - {artist_name} - {streams}')

with open('songs.csv', encoding='utf-8') as f, open('songs_new.csv', 'w', encoding='utf-8', newline='') as w:
    # Открываем файлы
    data = list(csv.reader(f, delimiter=';'))
    # Считываем данные в список data
    writer = csv.writer(w, delimiter=';')
    writer.writerow(data[0])
    # Записываем в файл w заголовки
    for streams, artist_name, track_name, date in data[1:]:
        if streams == '0':
            # Условие: кол-во прослушиваний равно нулю
            day, month, year = map(int, date.split('.'))
            streams = int(abs((datetime.datetime(2023, 5, 12) -
                               datetime.datetime(year, month, day)).days / (
                                          len(track_name) + len(artist_name))) * 10000)
            # Вычисляем по формуле
        writer.writerow([streams, artist_name, track_name, date])
        # Записываем в файл w
