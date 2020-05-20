from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView
class Mainwindow(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumSize(600,400)
        self.setWindowTitle('IHM')

        self.__txt=QTextEdit()
        self.__button_panel=Button_Panel()

        self.__table= QTableWidget()
        self.__table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.__table.setRowCount(10)
        self.__table.setColumnCount(10)
        self.__layout_principal=QVBoxLayout()
        self.__layout_principal.addWidget(self.__button_panel)
        self.__layout_principal.addWidget(self.__txt)
        self.__layout_principal.addWidget(self.__table)

        self.setLayout(self.__layout_principal)

class Button_Panel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.__layout=QHBoxLayout()
        self.__button_1=QPushButton('Configure')
        self.__button_2=QPushButton('Connect')
        self.__button_3=QPushButton('Disconnect')
        self.__layout.addWidget(self.__button_1)
        self.__layout.addWidget(self.__button_2)
        self.__layout.addWidget(self.__button_3)
        self.setLayout(self.__layout)








if __name__ == "__main__":
   app = QApplication([])
   win = Mainwindow()
   win.show()
   app.exec_()
