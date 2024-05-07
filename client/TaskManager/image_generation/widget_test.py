import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, \
    QMainWindow
from PySide6.QtGui import QPixmap
from image_generation.avatar import make_avatar

#TODO новый класс tagwidget для соло тэгов.
#TODO Посмотреть почему цвет меняеться
#TODO Посмотреть как сгладить круг более плавным убрать
#TODO Поменять формат на svg или в pillow сделать больше разрешенее а в виджете скейлить вниз
class AvatarWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.avatar_label = QLabel('Avatar:')
        self.avatar_image = QLabel()
        self.avatar_button = QPushButton('Сгенерировать аватар')

        self.first_name = None
        self.middle_name = None
        self.last_name = None

        self.avatar_button.clicked.connect(self.choose_avatar)

        layout = QVBoxLayout()
        layout.addWidget(self.avatar_label)
        layout.addWidget(self.avatar_image)
        layout.addWidget(self.avatar_button)

        self.setLayout(layout)

    def set_user_info(self, first_name, middle_name='', last_name=''):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name


    def choose_avatar(self):

        file_path = make_avatar(self.first_name, self.middle_name, self.last_name)

        if file_path:
            pixmap = QPixmap(file_path)
            self.avatar_image.setPixmap(pixmap.scaled(100, 100))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = QMainWindow()
    central_widget = QWidget()
    fio = "Иванов Иван Иванович"  # пример данных ФИО пользователя

    custom_widget = AvatarWidget()
    custom_widget.set_user_info("OИванов", "Иван", "KИванович")

    layout = QVBoxLayout(central_widget)
    layout.addWidget(custom_widget)
    main_window.setCentralWidget(central_widget)
    main_window.show()

    sys.exit(app.exec())
