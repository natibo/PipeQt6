#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QLineEdit, QHBoxLayout
import sqlite3
import json

# Define a class for the pipes and its attributes

class Pipe:

    def __init__(self, name='', maker='', shape='', store='', buyyear=0):
        self.name = name
        self.maker = maker
        self.shape = shape
        self.store = store
        self.buyyear = buyyear

# Insert an object into the database
    
def insert_pipe(pipe):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO pipes (name, maker, shape, store, buyyear) VALUES (?, ?, ?, ?, ?)',
              (pipe.name, pipe.maker, pipe.shape, pipe.store, pipe.buyyear))
    conn.commit()
    conn.close()
    
# Create a PyQt6 GUI to enter object attributes and add them to the database
    
class MainWindow(QMainWindow):
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
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

