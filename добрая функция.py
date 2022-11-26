import os
a = int(input('Сколько картинок создать? - '))


def f(t, i):
    print(t)
    from PIL import Image, ImageDraw, ImageFont
    font = ImageFont.truetype('C:windows/fonts/impact.ttf', size=100)
    im2 = Image.new('RGB', (1920, 1080), color=('lightgreen'))
    draw_text = ImageDraw.Draw(im2)
    draw_text.text(
        (300, 300),
        t,
        font=font,
        fill=('green'))
    # im2.show()

    im2.save(
        f'C:/Users/student/Desktop/Рибсам эд 142 задачки/добрая функция/добрый номер {n+1}.jpg')


t = []
print(t)
n = 0
for i in range(a):
    t = input('Что написать? - ')
    f(t, i)
