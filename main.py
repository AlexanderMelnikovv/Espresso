import sys
import sqlite3
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
from PyQt5 import uic


class InfoCoffee(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.show_info()

    def show_info(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        data = cur.execute('''SELECT variety_coffee, degree_of_roasting, ground_or_grains, 
                            taste, price, volume FROM info_coffee''').fetchall()
        self.tableWidget.setColumnCount(len(data))
        self.tableWidget.setRowCount(len(data[0]))
        self.tableWidget.setHorizontalHeaderLabels('Сорт', 'Степень обжарки', 'Молотый/В зёрнах',
                                                   'Описание вкуса', 'Цена', 'Объём упаковки')
        for i, elem in enumerate(data):
            for j, value in elem:
                self.tableWidget.setItem(i, j, QTableWidgetItem(value))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffee_window = InfoCoffee()
    coffee_window.show()
    sys.exit(app.exec())
