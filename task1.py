import csv, datetime

with open('songs.csv',encoding='utf8')as file:
    #Открываем файл с данными и создаем список вида: <'Кол-во прослушиваний'>,<'Имя артиста'>,<'Название песни'>,<'Дата создания'>
    reader = csv.reader(file,delimiter=';',quotechar='"')
    songs=list(reader)[1:]

    #Находим нулевые прослушивания и меняем значение по формуле
    k=0
    for streams,artist_name,track_name,date in songs:
        if streams=='0':
            streams=1
            artist_date = [int(x) for x in date.split('.')]
            artist_date.reverse()
            d=str(datetime.date(2002,1,1)-datetime.date(artist_date[0],artist_date[1],artist_date[2])).split(' ')
            t=abs(int(d[0]))/(len(artist_name)+len(track_name))*10000
            songs[k][0]=int(t)
        k+=1

#Создаем новый файл и сохраняем в него измененные данные
with open('songs_new.csv','w',newline='',encoding='utf8')as f:
    w=csv.writer(f)
    w.writerow(['streams','artist_name','track_name','date'])
    w.writerows(songs)


with open('songs.csv',encoding='utf8')as file:
    #Открываем новый файл с данными и создаем список вида: <'Кол-во прослушиваний'>,<'Имя артиста'>,<'Название песни'>,<'Дата создания'>
    reader = csv.reader(file,delimiter=';',quotechar='"')
    songs=list(reader)[1:]
    #Ищем песни по дате выхода не позже 01.01.2002 и выводим их в формате: “<Название песни> - <артист> - <кол-во прослушиваний>”
    for streams,artist_name,track_name,date in songs:
        artist_date = [int(x) for x in date.split('.')]
        artist_date.reverse()
        if datetime.date(artist_date[0],artist_date[1],artist_date[2])<datetime.date(2002,1,1):
            print(f'{track_name} - {artist_name} - {streams}')