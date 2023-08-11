import sys
import sqlite3
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLabel, QCheckBox,
                             QPushButton, QTableWidget, QTableWidgetItem, QWidget)
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
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bo's Pipe Database")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("What would you like to do?:", self.central_widget)
        self.layout.addWidget(self.label)

        self.checkbox1 = QCheckBox("Show Pipe Collection", self.central_widget)
        self.layout.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox("Add a New Pipe to the Collection", self.central_widget)
        self.layout.addWidget(self.checkbox2)

        self.checkbox3 = QCheckBox("Edit a Pipe in the Collection", self.central_widget)
        self.layout.addWidget(self.checkbox3)

        self.checkbox4 = QCheckBox("Delete a Pipe from the Collection", self.central_widget)
        self.layout.addWidget(self.checkbox4)

        self.button = QPushButton("Perform Action", self.central_widget)
        self.button.clicked.connect(self.perform_action)
        self.layout.addWidget(self.button)

        self.central_widget.setLayout(self.layout)

    def perform_action(self):
        actions = []

        if self.checkbox1.isChecked():
            self.w = Showpipe()
            self.w.show()

        if self.checkbox2.isChecked():
            actions.append("Option 2 is checked.")

        if self.checkbox3.isChecked():
            actions.append("Option 3 is checked.")

        if self.checkbox4.isChecked():
            actions.append("Option 4 is checked.")

        if actions:
            result_text = "\n".join(actions)
            self.show_result_message(result_text)
        else:
            self.show_result_message("No options selected.")

    def show_result_message(self, message):
        result_label = QLabel(message, self)
        result_label.setGeometry(100, 180, 200, 60)
        result_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        result_label.setStyleSheet("background-color: lightgray;")
        result_label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
