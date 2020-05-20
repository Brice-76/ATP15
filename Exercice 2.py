from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit,QHeaderView,QDialog

class LabeledTextField(QWidget) :
    def __init__(self,txt):
        QWidget.__init__(self)
        self.__layout= QHBoxLayout()
        self.__label=QLabel(txt)
        self.__text=QTextEdit()
        self.ajout()
        self.setMaximumSize(300,50)


    def ajout(self):
        self.__layout.addWidget(self.__label)
        self.__layout.addWidget(self.__text)
        self.setLayout(self.__layout)


class ConfigurationDialog(QDialog) :
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('Identification')
        self.__obj1=LabeledTextField('IP Adress')
        self.__obj2=LabeledTextField('User')
        self.__obj3=LabeledTextField('Password')
        self.__layout=QVBoxLayout()
        self.__layout.addWidget(self.__obj1)
        self.__layout.addWidget(self.__obj2)
        self.__layout.addWidget(self.__obj3)
        self.setLayout(self.__layout)


if __name__ == "__main__":
   app = QApplication([])
   win = ConfigurationDialog()
   win.show()
   app.exec_()
