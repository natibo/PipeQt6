import sys
from pipeclass import Pipe
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel

class AttributeWindow(QWidget):
    def __init__(self, obj):
        super().__init__()
        self.setWindowTitle("Attribute Window")
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()
        label = QLabel("Attributes:")
        attributes_label = QLabel(f"Attribute 1: {obj.attribute1}\n"
                                  f"Attribute 2: {obj.attribute2}\n"
                                  f"Attribute 3: {obj.attribute3}\n"
                                  f"Attribute 4: {obj.attribute4}\n"
                                  f"Attribute 5: {obj.attribute5}")
        layout.addWidget(label)
        layout.addWidget(attributes_label)

        self.setLayout(layout)

def show_attributes(obj):
    app = QApplication(sys.argv)

    attribute_window = AttributeWindow(obj)
    attribute_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    my_object = MyObject("Value 1", "Value 2", "Value 3", "Value 4", "Value 5")
    show_attributes(my_object)
