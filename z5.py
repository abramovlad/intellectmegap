import csv
import collections

with open('songs.csv', encoding='utf-8') as f:
    # Открываем файл в переменную f
    data = list(csv.reader(f, delimiter=';'))[1:]
    # Считываем данные в список data
    hash_table = collections.defaultdict(int)
    # Создаем словарь
    already = []
    for streams, artist_name, track_name, date in data:
        # Разделяем содержимое списка data
        if track_name not in already:
            hash_table[artist_name] += 1
            already.append(track_name)
    c = 0
    for i in hash_table:
        c += 1
        if c == 11:
            break
        print(f'{i} выпустил {hash_table[i]} песен.')
