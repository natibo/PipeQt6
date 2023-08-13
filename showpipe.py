import sqlite3
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QTableWidget, QTableWidgetItem, QWidget)
class Showpipe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pipes in your database")
        self.setGeometry(100, 100, 800, 600)

        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(10, 10, 780, 580)

        self.load_data()

    def load_data(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM pipes")
        rows = cursor.fetchall()

        if len(rows) > 0:
            num_rows = len(rows)
            num_cols = len(rows[0])
            self.table_widget.setRowCount(num_rows)
            self.table_widget.setColumnCount(num_cols)

            # Set column headers
            column_names = [description[0] for description in cursor.description]
            self.table_widget.setHorizontalHeaderLabels(column_names)

            # Populate table
            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        connection.close()