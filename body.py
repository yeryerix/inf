print('Задача на размер звукового файла')
need = input("Что нужно найти? \n  A - размер файла (Мб) \n  D - частота дискретизации (Гц)\n  Т - длина записи (сек)\n  I - битовая глубина? (бит)\n- ")
if need == 'A' or need == 'А' or need == 'a' or need == 'а' or need == 'Ф' or need == 'ф' or need == 'F' or need == 'f':
    print('Дано:')
    needAD = int(input('D - частота дискретизации (Гц) = '))
    needAT = int(input('Т - длина записи (сек) = '))
    needAI = int(input('I - битовая глубина (бит) = '))
    needACh = int(input('Сколько каналов? - '))
    needA = (needACh*needAD*needAT*needAI)/8/1024/1024
    print(f"А = {needA} (Мбайт) \nРабота закончена...")

elif need == 'D' or need == 'd' or need == 'в' or need == 'В':
    print('Дано:')
    needDA = float(input('A - размер файла (Мб) = '))
    needDT = int(input('Т - длина записи (сек) = '))
    needDI = int(input('I - битовая глубина (бит) = '))
    needDCh = int(input('Сколько каналов? - '))
    needD = (needDA/(needDCh*needDT*needDI)*8*1024*1024)
    print(f'D = {needD} (Гц) \nРабота закончена...')

elif need == 'T' or need == 't' or need == 'Т' or need == 'т' or need == 'Е' or need == 'е' or need == 'N' or need == 'n':
    print('Дано:')
    needTA = float(input('A - размер файла (Мб) = '))
    needTD = int(input('D - частота дискретизации (Гц) = '))
    needTI = int(input('I - битовая глубина (бит) = '))
    needTCh = int(input('Сколько каналов? - '))
    needT = (needTA/(needTCh*needTD*needTI)*8*1024*1024)
    print(f'T = {needT} (сек) \nРабота закончена...')

elif need == 'I' or need == 'i' or need == 'Ш' or need == 'ш':
    print('Дано:')
    needIA = float(input('A - размер файла (Мб) = '))
    needID = int(input('D - частота дискретизации (Гц) = '))
    needIT = int(input('Т - длина записи (сек) = '))
    needICh = int(input('Сколько каналов? - '))
    needI = (needIA/(needICh*needID*needIT)*8*1024*1024)
    print(f'I = {needI} (бит) \nРабота закончена...')

else:
    print(" [ERROR] - Tы что-то не так ввёл, перезапусти программу и введи заново")

    
