import os
def f(t,n):
    print(t)
    from PIL import Image, ImageDraw, ImageFont
    font = ImageFont.truetype ('C:windows/fonts/impact.ttf', size=100)
    im2 = Image.new ('RGB', (1920,1080), color=('lightgreen'))
    draw_text = ImageDraw.Draw(im2)
    draw_text.text(
        (300,300),
        t,
        font=font,
        fill=('green'))
    #im2.show()
    
    im2.save(f'C:/Users/user/Documents/name{n}.jpg')

t=('Сок',
   'добрый',
   '1Л',
   'яблочный')
print(t)
n=0
for i in range (4):
    f(t[i],i)
