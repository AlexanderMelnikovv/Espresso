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
        print(data)
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(['Сорт', 'Степень обжарки', 'Молотый/В зёрнах',
                                                    'Описание вкуса', 'Цена', 'Объём упаковки'])
        for i, elem in enumerate(data):
            for j, value in enumerate(elem):
                if j == 1:
                    value = cur.execute(f'''SELECT degree from roasting
                                            WHERE id = {value}''').fetchall()
                    value = value[0][0]
                if j == 2:
                    value = cur.execute(f'''SELECT title from grains_or_ground
                                            WHERE id = {value}''').fetchall()
                    value = value[0][0]
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        self.tableWidget.resizeColumnsToContents()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffee_window = InfoCoffee()
    coffee_window.show()
    sys.exit(app.exec())
