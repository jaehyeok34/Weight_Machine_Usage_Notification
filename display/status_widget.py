from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
from circle_widget import CircleWidget


class StatusWidget(QWidget):
    def __init__(
        self, parent: QWidget,

        # for circle 
        radius: int, 
        
        # for text
        textColor: QColor, fontSize: int,
    ) -> None:
        super().__init__(parent)

        self.__useCircle    =   CircleWidget(
            parent      =   self,
            radius      =   radius,
            circleColor =   QColor(0, 255, 0),
            text        =   "사용중",   
            textColor   =   textColor,
            fontSize    =   fontSize
        )
        self.__pauseCircle  =   CircleWidget(
            parent      =   self,
            radius      =   radius,
            circleColor =   QColor(0, 0, 255),
            text        =   "일시정지",   
            textColor   =   textColor,
            fontSize    =   fontSize
        )
        self.__endCircle    =   CircleWidget(
            parent      =   self,
            radius      =   radius,
            circleColor =   QColor(255, 0, 0),
            text        =   "종료",   
            textColor   =   textColor,
            fontSize    =   fontSize
        )

        self.__layout       =   QHBoxLayout(self)
        self.__layout.addWidget(self.__useCircle)
        self.__layout.addWidget(self.__pauseCircle)
        self.__layout.addWidget(self.__endCircle)

    def updateStatus(self):
        self.__useCircle.updateCircleColor(QColor(255, 255, 0))
        self.__pauseCircle.updateCircleColor(QColor(255, 0, 0))
        self.__endCircle.updateCircleColor(QColor(0, 255, 255))