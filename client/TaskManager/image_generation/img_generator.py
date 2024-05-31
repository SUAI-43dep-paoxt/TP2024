import sys
import hashlib
from abc import ABC, abstractmethod
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow
from PySide6.QtGui import QPixmap
from PIL import Image, ImageDraw, ImageFont

class GenImageWidget():
    def __init__(self, data):
        super().__init__()

        self.data = data
        self.colors = None
        self.image = QLabel()

    def generate(self):
        file_path = self.generate_image()
        pixmap = QPixmap(file_path)
        self.image.setPixmap(pixmap.scaled(100, 100))
        return self.image

    @abstractmethod
    def generate_image(self):
        pass


    def hash_color(self):
        sha1 = hashlib.sha1()
        sha1.update(self.data.encode(encoding='UTF-8', errors='strict'))
        hashed_value = sha1.hexdigest()

        color_index = abs(int(hashed_value, 16)) % len(self.colors)
        selected_color = self.colors[color_index]
        return selected_color

class GenerateAvatar(GenImageWidget, QWidget):
    def __init__(self, first_name, middle_name='', last_name=''):
        super().__init__(first_name + middle_name + last_name)
        self.colors = ['#33FF57', '#5733FF', '#33FFAC', '#FF33D3', '#D333FF', '#FF5733']
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        pic = self.generate()
        layout = QVBoxLayout()
        layout.addWidget(pic)
        self.setLayout(layout)
        self.generate_image()


    def generate_image(self):
        # Создаем полностью прозрачное изображение с прозрачностью 0

        selected_color = self.hash_color()

        size = 100
        image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        draw.ellipse((0, 0, size, size),
                     fill=selected_color)  # добавляем значение прозрачности alpha=128
        try:
            initials = self.first_name[0].upper() + self.last_name[0].upper()
        except IndexError:
            initials = self.first_name[0:2]
        # font = PIL.ImageFont.truetype(font='Times New Roman', size=20, index=0, encoding='unic')
        text_color = (255, 255, 255)  # черный цвет

        text_position = (size // 2, size // 2)
        unicode_font = ImageFont.truetype("DejaVuSans.ttf", 20)
        draw.text(text_position, initials, font=unicode_font, fill=text_color, anchor="mm")
        print(initials)
        try:
            image.save(f"..\\images\\avatar.png")
            return f"..\\images\\avatar.png"
        except:
            image.save(f"images\\avatar.png")
            return f"images\\avatar.png"


class GenerateTag(GenImageWidget, QWidget):
    def __init__(self, tag):
        super().__init__(tag)
        self.colors = ['#33FF57', '#5733FF', '#33FFAC', '#FF33D3', '#D333FF', '#FF5733']
        self.tag = tag
        pic = self.generate()
        layout = QVBoxLayout()
        layout.addWidget(pic)
        self.setLayout(layout)

    def generate_image(self):

        selected_color = self.hash_color()

        size = 100
        pad = 25
        ratio = 2

        image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        x = size // ratio // 2
        # draw.ellipse((pad, pad, size - pad, size - pad), fill=selected_color)  # добавляем значение прозрачности alpha=128
        # draw.ellipse((0, size // 2 - x, size , size // 2 + x), fill=selected_color)  # добавляем значение прозрачности alpha=128
        draw.rectangle([0, size // 2 - x, size, size // 2 + x], fill=selected_color)

        if len(self.tag) < 3:
            short_tag = self.tag
        else:
            short_tag = self.tag[0:3]

        # font = PIL.ImageFont.truetype(font='Times New Roman', size=20, index=0, encoding='unic')
        text_color = (255, 255, 255)  # черный цвет

        text_position = (size // 2, size // 2)
        unicode_font = ImageFont.truetype("DejaVuSans.ttf", 20)
        draw.text(text_position, short_tag, font=unicode_font, fill=text_color, anchor="mm")

        # Сохраняем изображение в формате PNG
        image.save(f"tag_{self.tag}.png")
        return f"tag_{self.tag}.png"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()

    custom_widget = GenerateAvatar("Клюканов", "Иван", "Иванович")
    custom_widget2 = GenerateTag("Работа")
    custom_widget3 = GenerateTag("Разработка")
    custom_widget4 = GenerateTag("Тесты")

    layout = QVBoxLayout()  # Используем QVBoxLayout для вертикального размещения

    layout.addWidget(custom_widget)
    layout.addWidget(custom_widget2)
    layout.addWidget(custom_widget3)
    layout.addWidget(custom_widget4)

    central_widget = QWidget()
    central_widget.setLayout(layout)

    main_window.setCentralWidget(central_widget)
    main_window.show()
    sys.exit(app.exec())