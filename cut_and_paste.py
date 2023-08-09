import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 300, 200)

        button = QPushButton("Check Condition", self)
        button.setGeometry(50, 50, 200, 50)
        button.clicked.connect(self.check_condition)

    def check_condition(self):
        condition_met = True  # Replace this with your actual condition

        if condition_met:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Message Box")
            msg_box.setText("Condition is met. This is a message box outside of the main window.")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
