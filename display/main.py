import sys, os
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from window_widget import WindowWidget

if __name__ == '__main__':
    sys.path.append(os.path.abspath(os.getcwd()))
    app = QApplication(sys.argv)

    window = WindowWidget()
   
    window.show()
    sys.exit(app.exec_())
