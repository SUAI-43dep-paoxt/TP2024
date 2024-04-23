import PIL.ImageColor
from PIL import Image, ImageDraw, ImageFont

def make_avatar (first_name, middle_name = '', last_name = ''):
    name = first_name + middle_name + last_name
    hashed_value = hash(name)

    colors = ['#33FF57', '#5733FF', '#33FFAC', '#FF33D3', '#D333FF', '#FF5733']

    color_index = abs(hashed_value) % len(colors)

    selected_color = colors[color_index]

    # Создаем полностью прозрачное изображение с прозрачностью 0

    size = 100
    pad = 25

    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    draw.ellipse((pad, pad, size - pad, size - pad), fill=selected_color)  # добавляем значение прозрачности alpha=128

    try:
        initials = first_name[0].upper() + last_name[0].upper()
    except IndexError:
        initials = name[0:2]

    print(initials)

    #font = PIL.ImageFont.truetype(font='Times New Roman', size=20, index=0, encoding='unic')
    font = ImageFont.load_default(size=20)  # можно использовать другой шрифт, если нужно
    text_color = (255, 255, 255)  # черный цвет

    text_position = (size // 2, size // 2)
    draw.text(text_position, initials, font=font, fill=text_color, anchor="mm")

    # Сохраняем изображение в формате PNG
    image.save('avatar.png')


#make_avatar("Глеба",'',"Cильный")
make_avatar("ATest",'',"NName")




