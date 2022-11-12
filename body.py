print ('Задача на размер звукового файла')
need = input("Что нужно найти? A- размер файла / D- частота дискретизации / Т- длинна записи / I- битовая глубина? - ")
if need == 'A' or need == 'А':
    print('Дано:')
    needAD = int (input('D- частота дискретизации Гц = '))
    needAT = int (input('Т- длинна записи сек = '))
    needAI = int (input('I- битовая глубина бит = '))
    needACh = int (input ('Сколько каналов? - '))
    needA = (needACh*needAD*needAT*needAI)/8/1024/1024
    print(f"А= {needA} (Мбайт)")
 
elif need != 'A' or need !='А':
    print (" [ERROR] - Tы что-то не так ввёл, перезапусти программу и введи заново")

else:
    if need == 'D':
        print('Дано:')
        needAD = int (input('D- частота дискретизации Гц = '))
        needAT = int (input('Т- длинна записи сек = '))
        needAI = int (input('I- битовая глубина бит = '))
        needACh = int (input ('Сколько каналов? - '))
