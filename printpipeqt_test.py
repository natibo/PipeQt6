#!/usr/bin/env python3

import sys
import sqlite3
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QTableWidget, QTableWidgetItem, QWidget)

class Printpipe(QMainWindow):
    def __init__(self, table_name):
        super().__init__()
        self.table_name = table_name
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Pipes in your database")
        self.setGeometry(100, 100, 800, 600)

        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(10, 10, 780, 580)

        self.load_data()

    def load_data(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {self.table_name}")
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

def windowpipe():
    app = QApplication(sys.argv)
    table_name = "pipes"  # Replace with your table name
    window2 = Printpipe(table_name)
    window2.show()
    # sys.exit(app.exec())
    app.exec()
