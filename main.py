import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QPushButton, QFrame


class Example(QFrame):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")
        title = self.connection.execute('SELECT * FROM coffees WHERE id = 1').description
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(str(i[0]) for i in title)
        res = self.connection.cursor().execute(f"""SELECT c.id, c.name_sort, c.degree, t.name_type, c.taste, c.price, c.volume
                                                   FROM coffees c INNER JOIN types t ON t.id = c.type = t.id;""").fetchall()
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()
        self.show()

    def nm(self):
        w = self.lineEdit.text()
        k = self.lineEdit_2.text()
        r = self.lineEdit_3.text()
        if len(w) != 0 and len(k) != 0 and len(r) != 0:
            res = self.connection.cursor().execute(f"""SELECT * FROM films WHERE title {k} AND year {w} AND duration {r}""").fetchall()
        elif len(w) != 0 and len(k) != 0:
            res = self.connection.cursor().execute(f"""SELECT * FROM films WHERE title {k} AND year {w}""").fetchall()
        elif len(w) != 0 and len(r) != 0:
            res = self.connection.cursor().execute(f"""SELECT * FROM films WHERE year {w} AND duration {r}""").fetchall()
        elif len(k) != 0 and len(r) != 0:
            res = self.connection.cursor().execute(f"""SELECT * FROM films WHERE title {k} AND duration {r}""").fetchall()
        elif len(w) != 0:
            res = self.connection.cursor().execute(f"""SELECT * FROM films WHERE year {w}""").fetchall()
        elif len(r) != 0:
            res = self.connection.cursor().execute(f"""SELECT * FROM films WHERE duration {r}""").fetchall()
        elif len(k) != 0:
            res = self.connection.cursor().execute(f"""SELECT * FROM films WHERE title {k}""").fetchall()
        if len(res) != 0:
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(res):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())