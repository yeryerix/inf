def f():
    i=0
    print("это supertest по Эдуард егэ 2023 кто не напишет того растворим в ашхлор")
    s = 0
    q=["1. Что у с Артёмом Трущуком? \n 1. Всё норм 2. Ничего такого 3. Бензин 4. Каждую ночь",
    '2. Биология это что? \n 1. Кринге 2. Что 3. Ты кто 4. т-РНК',
    '3. Есть кошка-девочка? \n 1. и миска риса  2. ниправильна 3. мяу 4. хочу кабачок',
    '4. Когда ДРшка? \n 1. Завтра 2. Послезавтра 3. триста лет назад 4. где-то в январе',
    '5. кто я \n 1. ты 2. да я 3. да мы с тобой 4. сульфат железа (III)',
    '6. Есть домашние животные? \n 1. да 2. нет 3. сестра 4. Анастасия Попова',
    '7. *Свист автомобильных покрышек* \n 1. Это кто 2. Это что 3. Генетическая хрень 4. Это Эд забыл сменку',
    '8. помргите \n 1. Это Евгений Борщ? 2. помргу 3. Ерик го бегать',
    '9. Обычная одежда хозяина \n 1. Пиджак 2. Болотоходы 3. уже 9 вопрос мне сложно что-то придумать камон',
    '10. мяу \n Просто напиши "Эд крутой" и не парься']

    a=['3',
    '1',
    '3',
    '4',
    '4',
    '3',
    '4',
    '2',
    '1',
    'Эд крутой']


    for i in range(len(q)):  # len = длина 
        print(q[i])
        
        if input()==a[i]:
            print('ok')
            s=s+1
        else:
            print('Неправильно')
    
    print('Првильных ответов: ',s,'/10')

    i=int(input ('Повторить?  1-да  - ' ))
    if i==1:
        f()
f()
