print ("это supertest  по Эдуард егэ 2023 кто не напишет того растворим в ашхлор")
s = 0
print ("1. Что у с Артёмом Трущуком?")
print ("1. Всё норм 2. Ничего такого 3. Бензин 4. Каждую ночь")
a = int (input ())
if a == 3:
    s += 1
    print ("правильна")
else:
    print ("НИправильна")

print ("2. Биология это что?")
print ("1. Кринге 2. Что 3. Ты кто 4. т-РНК")
a = int (input ())
if a == 1 or a== 2 or a==3 or a==4:
    s += 1
    print ("правильна")
else:
    print ("НИправильна")
    
print ("3. Есть кошка-девочка?")
print ("1. и миска риса  2. ниправильна 3. мяу 4. хочу")
a = int (input ())
if a == 3:
    s += 1
    print ("правильна")
else:
    print ("НИправильна")
    
print ("4. Когда ДРшка?")
print ("1. Завтра 2. Послезавтра 3. триста лет назад 4. где-то в январе")
a = int (input ())
if a == 4:
    s += 1
    print ("правильна")
else:
    print ("НИправильна")

print ("5. кто я")
print ("1. ты 2. да я 3. да мы с тобой 4. сульфат железа (III)")
a = int (input ())
if a == 4:
    s += 1
    print ("правильна")
else:
    print ("НИправильна")

print ("6. Есть домашние животные?")
print ("1. да 2. нет 3. сестра 4. Анастасия Попова")
a = int (input ())
if a == 3:
    s += 1
    print ("молодчинка")
else:
    print ("НИправильна, Настя")

print ("7. *Свист автомобильных покрышек*")
print ("1. Это кто 2. Это что 3. Генетическая хрень 4. Это Эд забыл сменку")
a = int (input ())
if a == 4:
    s += 1
    print ("правильна")
else:
    print ("НИправильна")
    
print ("8. помргите")
print ("1. Это Евгений Борщ? 2. помргу 3. Ерик го бегать")
a = int (input ())
if a == 1 or a==2 or a==3:
    s += 1
    print ("правильна")
else:
    print ("НИправильна")
    
print ("9. Обчная одежда хозяина")
print ("1. Пиджак 2. Болотоходы 3. уже 9 вопрос мне сложно что-то придумать камон")
a = int (input ())
if a == 1:
    s += 1
    print ("правильна")
else:
    print ("НИправильна")

print ("10. мяу")
print ('Напиши "Эд крутой" и не парься')
a = (input ())
if a == 'Эд крутой':
    s += 1
    print ("Уважаю")
else:
    print ("._.")

if s >=0 and s <=3:
    print ("понятно... неуч...")

if s >=4 and s <=6:
    print ("эх, а я верил в тебя")

if s >=7 and s <=9:
    print ("а ты хорош")

if s == 10:
    print ("Ты определённо Рина")
print ('Кол-во баллов', s)
    








    