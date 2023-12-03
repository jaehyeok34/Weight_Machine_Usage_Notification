from PyQt5.QtWidgets    import *
from PyQt5.QtCore       import Qt
    
class TextWidget(QWidget):
    def __init__(self, parent: QWidget, text: str, color: str, fontSize: int) -> None:
        super().__init__(parent)

        self.__layout       = QVBoxLayout(self)
        self.__textLable    = QLabel(
            parent  = self,
            text    = text,
        )
        self.__textLable.setAlignment(Qt.AlignCenter)
        self.__textLable.setStyleSheet(                             
            f"color: {color}; font-size: {fontSize}px"
        )

        self.__layout.setAlignment(Qt.AlignCenter)
        self.__layout.addWidget(self.__textLable)

    def updateText(self, text: str) -> None:
        self.__textLable.setText(text)