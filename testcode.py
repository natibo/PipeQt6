import sqlite3
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QTableWidget, QTableWidgetItem, QWidget)
from pipeclass import Pipe
class Showone(QWidget, Pipe):
    def __init__(self, Pipe):
        super().__init__()
        self.setWindowTitle("Your New Pipe")
        self.setGeometry(100, 100, 800, 600)

        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(10, 10, 780, 580)

        self.load_data()

    def load_data(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM pipes WHERE name = ?", (Pipe,))
        row = cursor.fetchone()
        # num_cols = 5
        self.table_widget.setRowCount(1)
        self.table_widget.setColumnCount(5)

        # Set column headers
        column_names = [description[0] for description in cursor.description]
        self.table_widget.setHorizontalHeaderLabels(column_names)

            # Populate table
        for row_idx, row in enumerate(row):
            for col_idx, value in enumerate(row):
                self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        # connection.close()