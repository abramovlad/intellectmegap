import csv

with open('songs.csv', encoding='utf-8') as f, open('russian_artists.txt', 'w', encoding='utf-8') as ra, open(
        'foreign_artists.txt', 'w', encoding='utf-8') as fa:
    # Открываем файлы
    data = list(csv.reader(f, delimiter=';'))[1:]
    # Считываем данные в список data
    rus_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
    russian_artists = []
    foreign_artists = []
    for streams, artist_name, track_name, date in data:
        # Разделяем содержимое списка data
        if artist_name in russian_artists or artist_name in foreign_artists:
            continue
        # Условие наличия имени артиста
        for let in artist_name:
            if let in rus_alphabet:
                # Ищем русские буквы
                russian_artists.append(artist_name)
                break
        else:
            foreign_artists.append(artist_name)
    print(f'Количество российских исполнителей: {len(russian_artists)}')
    print(f'Количество иностранных исполнителей: {len(foreign_artists)}')
    print(*russian_artists, sep='\n', file=ra)
    print(*foreign_artists, sep='\n', file=fa)
