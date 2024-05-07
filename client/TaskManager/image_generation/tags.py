import PIL.ImageColor
from PIL import Image, ImageDraw, ImageFont

def make_tag (tag):

    hashed_value = hash(tag)
    colors = ['#33FF57', '#5733FF', '#33FFAC', '#FF33D3', '#D333FF', '#FF5733']

    color_index = abs(hashed_value) % len(colors)
    selected_color = colors[color_index]

    # Создаем полностью прозрачное изображение с прозрачностью 0

    size = 100
    pad = 25
    ratio = 2

    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    x = size // ratio // 2
    #draw.ellipse((pad, pad, size - pad, size - pad), fill=selected_color)  # добавляем значение прозрачности alpha=128
    # draw.ellipse((0, size // 2 - x, size , size // 2 + x), fill=selected_color)  # добавляем значение прозрачности alpha=128
    draw.rectangle([0, size // 2 - x, size , size // 2 + x], fill=selected_color)

    if len(tag) < 3:
        short_tag = tag
    else:
        short_tag = tag[0:3]

    #font = PIL.ImageFont.truetype(font='Times New Roman', size=20, index=0, encoding='unic')
    font = ImageFont.load_default(size=20)  # можно использовать другой шрифт, если нужно
    text_color = (255, 255, 255)  # черный цвет

    text_position = (size // 2, size // 2)
    draw.text(text_position, short_tag, font=font, fill=text_color, anchor="mm")

    # Сохраняем изображение в формате PNG
    image.save(f"tag_{tag}.png")


#make_avatar("Глеба",'',"Cильный")
make_tag("JOB")
make_tag("Development")
make_tag("Testing")






