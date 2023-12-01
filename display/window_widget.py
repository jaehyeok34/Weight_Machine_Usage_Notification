from PyQt5.QtWidgets import  *
from PyQt5.QtCore import Qt
from status_indicator_widget import StatusIndicator

class WindowWidget(QWidget):
    def __init__(
            self,
            winsize:        tuple   =   ...,
            title:          str     =   ...,
            winbackColor:   str     =   ...,
            text: str           =   "text",
            textColor: str      =   "white",
            fontSize: int       =   "30px"
    ):
        super().__init__()

        # window 설정
        WindowWidget.__initWindow(self, winsize, title, winbackColor)

        # 메인 레이아웃 설정
        self.__mainLayout = WindowWidget.__getLayout(self, self)

        # 텍스트 레이블(상단 80%)
        self.__textLabel = WindowWidget.__getLable(self, text, textColor, fontSize)

        # 상태 레이아웃(하단 20%)
        self.__statusLayout = WindowWidget.__getLayout(self)

        # 메인 레이아웃에 위젯 추가
        self.__addWidget(
            target  =   self.__mainLayout, 
            widgets =   [self.__textLabel, self.__statusLayout],
            ratio   =   [80, 20]
        )

        # # 상태 객체 생성 및 추가
        # self.on_indicator = StatusIndicator(self, 'On')
        # self.off_indicator = StatusIndicator(self, 'Off')
        # self.pause_indicator = StatusIndicator(self, 'Pause')

        # self.statusLayout.addWidget(self.on_indicator)
        # self.statusLayout.addWidget(self.off_indicator)
        # self.statusLayout.addWidget(self.pause_indicator)

        # # 초기 상태 설정
        # self.set_status('Off')

    def __initWindow(self, size: tuple = ..., title: str = ..., backColor: str = ...) -> None:
        # 매개변수 설정
        size, title, backColor = WindowWidget.__getParams(
            defalt = ((100, 100, 400, 400), "window", "black"),
            params = [size, title, backColor]
        )

        # window 설정
        self.setGeometry(*size)                                 # display 크기 설정
        self.setWindowTitle(title)                              # 제목 설정
        self.setStyleSheet(f"background-color: {backColor}")    # 배경색 설정

    def __getLayout(self, parent: object = ..., margins: tuple = ...) -> QBoxLayout:
        # 매개변수 설정
        margins, = WindowWidget.__getParams(((0, 0, 0, 0), ), [margins])

        # 레이아웃 설정
        layout = None
        if parent is not Ellipsis:
            layout = QVBoxLayout(parent)
        else:
            layout = QVBoxLayout()

        layout.setContentsMargins(*margins)
        return layout

    def __getLable(self, text: str = ..., color: str = ..., fontSize: int = ...) -> QLabel:
        text, color, fontSize = WindowWidget.__getParams(
            defalt = ("text", "white", 30),
            params = [text, color, fontSize]
        )

        lable = QLabel(text)
        lable.setAlignment(Qt.AlignCenter)
        lable.setStyleSheet(                             
            f"color: {color}; font-size: {fontSize}px"
        )  
        return lable
    
    def __getParams(defalt: tuple, params: list) -> tuple:
        # default 파라미터 설정
        for i, param in enumerate(params):
            if param is Ellipsis:
                params[i] = defalt[i]

        return tuple(params)
    
    def __addWidget(self, target: QBoxLayout, widgets: tuple, ratio: tuple) -> None:
        for i, widget in enumerate(widgets):
            if (type(widget) is QVBoxLayout) or (type(widget) is QHBoxLayout):
                target.addLayout(widget, ratio[i])
            else:
                target.addWidget(widget, ratio[i])

    def set_status(self, status):
        self.on_indicator.update_status('On' if status == 'On' else '')
        self.off_indicator.update_status('Off' if status == 'Off' else '')
        self.pause_indicator.update_status('Pause' if status == 'Pause' else '')
