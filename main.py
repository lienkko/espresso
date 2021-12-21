import sys
import sqlite3
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        self.result = cur.execute("SELECT * FROM info").fetchall()
        self.tableWidget.setRowCount(len(self.result))
        for i in range(len(self.result)):
            for f in range(7):
                self.tableWidget.setItem(i, f, QTableWidgetItem(str(self.result[i][f])))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())