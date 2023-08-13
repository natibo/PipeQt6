import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class Person:
    def __init__(self, name, age, address, email, phone):
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.phone = phone

class InputForm(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.address_input = QLineEdit()
        self.email_input = QLineEdit()
        self.phone_input = QLineEdit()

        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)

        layout.addWidget(QLabel("Age:"))
        layout.addWidget(self.age_input)

        layout.addWidget(QLabel("Address:"))
        layout.addWidget(self.address_input)

        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_input)

        layout.addWidget(QLabel("Phone:"))
        layout.addWidget(self.phone_input)

        submit_button = QPushButton("Create Object")
        submit_button.clicked.connect(self.create_person_object)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def create_person_object(self):
        name = self.name_input.text()
        age = self.age_input.text()
        address = self.address_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()

        person = Person(name, age, address, email, phone)
        print("Person object created with attributes:")
        print("Name:", person.name)
        print("Age:", person.age)
        print("Address:", person.address)
        print("Email:", person.email)
        print("Phone:", person.phone)

def main():
    app = QApplication(sys.argv)
    window = InputForm()
    window.setWindowTitle("Person Object Creator")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
