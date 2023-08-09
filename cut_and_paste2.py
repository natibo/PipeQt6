import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        layout = QVBoxLayout()
        self.label = QLabel("Press the button to open the new window.")
        layout.addWidget(self.label)

        button = QPushButton("Open New Window")
        button.clicked.connect(self.open_new_window)
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_new_window(self):
        if check_condition():  # Replace this with your actual condition/function
            new_window = NewWindow(self)
            new_window.show()

class NewWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("New Window")

        layout = QVBoxLayout()
        label = QLabel("This is the new window.")
        layout.addWidget(label)

        self.setLayout(layout)

def check_condition():
    return True  # Replace with your actual condition

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
