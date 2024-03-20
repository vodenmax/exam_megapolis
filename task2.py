import csv,datetime

with open('songs.csv',encoding='utf8')as file:
    #Открываем файл с данными и создаем список вида: <'Кол-во прослушиваний'>,<'Имя артиста'>,<'Название песни'>,<'Дата создания'>
    songs = list(csv.reader(file,delimiter=';',quotechar='"'))
    songs=songs[1:]
    #Сортируем данные по столбцу дата в порядке возрастания
    for i in range(0,len(songs)-1):
        for j in range(i+1,len(songs)):
            date_j=[int(x) for x in songs[j][-1].split('.')]
            date_i=[int(x) for x in songs[i][-1].split('.')]
            date_i.reverse()
            date_j.reverse()
            if datetime.date(date_j[0],date_j[1],date_j[2])<datetime.date(date_i[0],date_i[1],date_i[2]):
                temp = songs[j]
                songs[j]=songs[i]
                songs[i]=temp

    #Выводим топ-5 самых ранних песен
    count=1
    for song in songs:
        print(f'{count} {song[2]}, {song[1]}, {song[3]}')
        count+=1
        if count==6:
            break

