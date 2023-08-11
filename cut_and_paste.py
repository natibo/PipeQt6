import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class PopupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Popup Warning Example')

        self.warning_button = QPushButton('Show Warning', self)
        self.warning_button.setGeometry(50, 50, 200, 50)
        self.warning_button.clicked.connect(self.show_warning)

    def show_warning(self):
        condition = True  # Replace with your actual condition

        if condition:
            warning_box = QMessageBox()
            warning_box.setIcon(QMessageBox.Icon.Warning)
            warning_box.setWindowTitle('Warning')
            warning_box.setText('This is a warning message!')
            warning_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            warning_box.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PopupWindow()
    window.show()
    sys.exit(app.exec())
