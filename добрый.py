from PIL  import Image, ImageDraw, ImageFont

im = Image.new('RGB', (1920,1080), color=('lightgreen'))

font = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', size=300)
draw_text = ImageDraw.Draw(im)
draw_text.text(
    (30,300),
    '       добрый',
    font=font,
    fill='green'
    )
im.show()
