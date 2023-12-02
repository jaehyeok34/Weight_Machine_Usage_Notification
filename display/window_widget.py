from PyQt5.QtWidgets import  *
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor

from text_widget import TextWidget
from status_widget import StatusWidget

sensor_datas = ["3번 벤치 사용 가능", "5번 벤치 사용중", "7번 벤치 일시정지"]

class WindowWidget(QWidget):
    def __init__(
            self,
            # for window widget
            winsize: tuple, title: str, winbackColor: str,

            # for text widget & text of status widget
            text: str, textColor: str, fontSize: int,  

            # for status widget
            radius: int, 
    ) -> None:
        super().__init__()

        # window 설정(크기, 제목, 배경색상)
        WindowWidget.__initWindow(                 
            self, 
            size        =   winsize, 
            title       =   title, 
            backColor   =   winbackColor
        )

        # 메인 레이아웃 설정(부모 위젯 객체: window)
        self.__layout       =   QVBoxLayout(self)
        self.__textWidget   =   TextWidget(self, text, textColor, fontSize)
        self.__statusWidget =   StatusWidget(self, radius, QColor(textColor), fontSize)
        
        self.__layout.addWidget(self.__textWidget, 4)
        self.__layout.addWidget(self.__statusWidget, 1)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateWindow)
        self.timer.start(5000)


    def __initWindow(self, size: tuple, title: str, backColor: str) -> None:
        self.setGeometry(*size)                                 # display 크기 설정
        self.setWindowTitle(title)                              # 제목 설정
        self.setStyleSheet(f"background-color: {backColor}")    # 배경색 설정

    def updateWindow(self) -> None:
        self.__textWidget.updateText("Hello")
        self.__statusWidget.updateStatus()