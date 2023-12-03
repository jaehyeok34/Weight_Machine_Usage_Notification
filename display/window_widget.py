from PyQt5.QtWidgets        import *
from PyQt5.QtCore           import QTimer

from display.text_widget    import TextWidget
from display.status_widget  import StatusWidget
from display.display_args   import DisplayArgs
from display.display_info   import DisplayInfo
from display.palette        import Palette

class WindowWidget(QWidget):
    def __init__(
            self, machines: list[DisplayInfo], args: DisplayArgs
    ) -> None:
        super().__init__()

        # display에 띄울 정보를 담고있는 자료구조
        self.__machines = machines

        # window 설정(크기, 제목, 배경색상)
        WindowWidget.__initWindow(                 
            self, 
            size        = args.winsize, 
            title       = args.title, 
            backColor   = args.winbackColor,
        )

        # 메인 레이아웃 설정(부모 위젯 객체: window)
        self.__layout       = QVBoxLayout(self)
        self.__textWidget   = TextWidget(
            self, args.text, args.textColor, args.fontSize
        )
        self.__statusWidget = StatusWidget(
            self, args.radius, Palette.getColor(args.textColor), args.fontSize
        )
        
        self.__layout.addWidget(self.__textWidget, 4)
        self.__layout.addWidget(self.__statusWidget, 1)

        self.__index = 0
        self.__timer = QTimer(self)
        self.__timer.timeout.connect(self.updateWindow)
        self.__timer.start(args.updateTime)

    def __initWindow(self, size: tuple, title: str, backColor: str) -> None:
        self.setGeometry(*size)                                 # display 크기 설정
        self.setWindowTitle(title)                              # 제목 설정
        self.setStyleSheet(f"background-color: {backColor}")    # 배경색 설정

    def updateWindow(self) -> None:
        machine = self.__machines[self.__index]
        self.__textWidget.updateText(
            f"{machine.id}번 {machine.name} {StatusWidget.STATUS[machine.status]}"
        )
        self.__statusWidget.updateStatus(machine.status)

        self.__index = (self.__index + 1) % len(self.__machines)