import sys, os
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from window_widget import WindowWidget

if __name__ == '__main__':
    sys.path.append(os.path.abspath(os.getcwd()))
    app = QApplication(sys.argv)


    window = WindowWidget(
        winsize         =   (100, 100, 400, 400),
        title           =   "display",
        winbackColor    =   "black",
        updateTime      =   3000,
        text            =   "Hello World",
        textColor       =   "white",
        fontSize        =   30,
        radius          =   30,
    )
    window.showMaximized()

    sys.exit(app.exec_())
