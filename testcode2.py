#!/usr/bin/env python3

import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox)
import sqlite3
from pipeclass import Pipe


def insert_pipe(pipe):
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

    else:

        warning_box = QMessageBox()
        warning_box.setIcon(QMessageBox.Icon.Warning)
        warning_box.setWindowTitle('Warning')
        warning_box.setText('There is already a pipe with that name in the database')
        warning_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        warning_box.exec()


# Create a PyQt6 GUI to enter object attributes and add them to the database
class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Insert a New Pipe into the Database')
        self.setGeometry(200, 200, 500, 300)

        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit()

        self.maker_label = QLabel('Maker:')
        self.maker_input = QLineEdit()

        self.shape_label = QLabel('Shape:')
        self.shape_input = QLineEdit()

        self.store_label = QLabel('Store:')
        self.store_input = QLineEdit()

        self.buyyear_label = QLabel('Year Purchased:')
        self.buyyear_input = QLineEdit()

        self.add_button = QPushButton('Add Pipe')
        self.add_button.clicked.connect(self.add_pipe)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.maker_label)
        layout.addWidget(self.maker_input)
        layout.addWidget(self.shape_label)
        layout.addWidget(self.shape_input)
        layout.addWidget(self.store_label)
        layout.addWidget(self.store_input)
        layout.addWidget(self.buyyear_label)
        layout.addWidget(self.buyyear_input)
        layout.addWidget(self.add_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_pipe(self):
        name = self.name_input.text()
        maker = self.maker_input.text()
        shape = self.shape_input.text()
        store = self.store_input.text()
        buyyear = int(self.buyyear_input.text())

        pipe = Pipe(name, maker, shape, store, buyyear)
        insert_pipe(pipe)

        self.name_input.clear()
        self.maker_input.clear()
        self.shape_input.clear()
        self.store_input.clear()
        self.buyyear_input.clear()


# Start the application

if __name__ == '__main__':
    #     create_table()
    app = QApplication(sys.argv)
    # window = QWidget()
    # window.show()
    # sys.exit(app.exec())
    sub_window = SubWindow()
    sub_window.show()
    sys.exit(app.exec())
