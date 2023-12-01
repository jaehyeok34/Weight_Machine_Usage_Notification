import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import  *
import sys

from PyQt5.QtWidgets import QWidget  


# class WidgetManager:
#     def getWindow(
#         winSize:    tuple       =   (100, 100, 400, 400),
#         title:      str         =   "default title",
#         backColor:  str         =   "black"
#     ) -> QWidget:
#         window = QWidget()
#         window.setGeometry(*winSize)
#         window.setWindowTitle(title)
#         window.setStyleSheet(f"background-color: {backColor}")

#         return window
    
#     def getLayout(
#         parent:     QWidget,
#         axis:       str         =   "v",
#         margins:    tuple       =   (0, 0, 0, 0)
#     ) -> QBoxLayout | bool:
#         if parent is None:
#             return False
            
#         layout = None
#         axis = axis.lower()
#         if axis in ["v", "ver", "vertical"]:
#             layout = QVBoxLayout(parent)

#         elif axis in ["h", "hor", "horizontal"]:
#             layout = QHBoxLayout(parent)
        
#         else:
#             return False
        
#         layout.setContentsMargins(*margins)
#         return layout

class WindowWidget(QWidget):
    def __init__(
        self, 
        parent:     QWidget | None      =   ...,
        size:       tuple   | None      =   ...,
        title:      str     | None      =   ...,
        backColor:  str     | None      =   ...
    ) -> None:
        super().__init__(parent)
        print(parent, size, title, backColor)


window = WindowWidget()

# app = QApplication(sys.argv)

# window = WidgetManager.getWindow()
# mainLayout = WidgetManager.getLayout(window)

# window.show()

# sys.exit(app.exec_())
