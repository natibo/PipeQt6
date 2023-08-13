import sys
from PyQt6.QtWidgets import (QApplication, QMessageBox,
                             QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton)
from showpipe import Showpipe
import sqlite3
from pipeclass import Pipe
from testcode import Showone


class InputForm(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.name = QLineEdit()
        self.maker = QLineEdit()
        self.shape = QLineEdit()
        self.store = QLineEdit()
        self.buyyear = QLineEdit()

        layout.addWidget(QLabel("What is the Name of your new pipe?:"))
        layout.addWidget(self.name)

        layout.addWidget(QLabel("Who is the maker or carver of your new pipe?: "))
        layout.addWidget(self.maker)

        layout.addWidget(QLabel("What is the shape of your new pipe?:"))
        layout.addWidget(self.shape)

        layout.addWidget(QLabel("Where did you buy this pipe:"))
        layout.addWidget(self.store)

        layout.addWidget(QLabel("When did you buy the pipe?:"))
        layout.addWidget(self.buyyear)

        submit_button = QPushButton("Create Object")
        submit_button.clicked.connect(self.insert_pipe)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def test_pipe(pipe):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS pipes
         (pipe_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
         name TEXT, maker TEXT, shape TEXT, store TEXT, buyyear INT);""")

        # see if pipe already exist, if not write to database, if no diplay warning window
        testpipe = pipe.name
        query = c.execute("SELECT * FROM pipes WHERE name = ?", (testpipe,))
        result = c.fetchone()

        if not result:

            c.execute('INSERT INTO pipes (name, maker, shape, store, buyyear) VALUES (?, ?, ?, ?, ?)',
                      (pipe.name, pipe.maker, pipe.shape, pipe.store, pipe.buyyear))
            conn.commit()
            conn.close()
            pipex = Pipe(pipe.name, pipe.maker, pipe.shape, pipe.store, pipe.buyyear)
            pipe.w = Showpipe()
            pipe.w.show()
            pipe.checkbox1.setChecked(False)

        else:

            warning_box = QMessageBox()
            warning_box.setIcon(QMessageBox.Icon.Warning)
            warning_box.setWindowTitle('Warning')
            warning_box.setText('There is already a pipe with that name in the database')
            warning_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            warning_box.exec()

    def insert_pipe(self):
        name = self.name.text()
        age = self.maker.text()
        address = self.shape.text()
        email = self.store.text()
        phone = self.buyyear.text()
        pipex = Pipe(name, age, address, email, phone)
        # self.w = Showone(pipex)
        # self.w.show()
        # print("Pipe object created with attributes:")
        # print("Name:", pipex.name)
        # print("Maker-Carver:", pipex.maker)
        # print("Shape:", pipex.shape)
        # print("Store", pipex.store)
        # print("Buy Year", pipex.buyyear)

def main():
    app = QApplication(sys.argv)
    window = InputForm()
    window.setWindowTitle("New Pipe Creator")
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
