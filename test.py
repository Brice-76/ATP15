from PySide2.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QTableWidget, QApplication,QWidget, QHBoxLayout, QTextEdit


class Mainwindow(QMainWindow) :
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(600,400)
        self.setWindowTitle('IHM')

        layout_principal=QVBoxLayout()
        self.setLayout(layout_principal)


if __name__ == "__main__":
   app = QApplication([])
   win = Mainwindow()
   win.show()
   app.exec_()
