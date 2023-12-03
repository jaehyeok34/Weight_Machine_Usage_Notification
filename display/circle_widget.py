from PyQt5.QtWidgets    import *
from PyQt5.QtGui        import *

class CircleWidget(QWidget):
    def __init__(
        self, parent: QWidget, 

        # for circle
        radius: int, circleColor: QColor, 

        # for text
        text: str, textColor: QColor, fontSize: int
    ) -> None:
        super().__init__(parent)

        self.__radius           = radius
        self.__circleColor      = circleColor
        self.__text             = text
        self.__textColor        = textColor
        self.__fontSize         = fontSize

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
    
        # 동그라미 그리기
        painter.setBrush(self.__circleColor)
        painter.drawEllipse(
            (self.width() // 2) - self.__radius,
            (self.height() // 2) - self.__radius,
            (self.__radius * 2),
            (self.__radius * 2),
        )

        # 텍스트 추가 (동그라미 위에 중앙 정렬)
        painter.setPen(self.__textColor)
        painter.setFont(QFont("Arial", self.__fontSize))
        tWidth = painter.fontMetrics().width(self.__text)
        tX = (self.width() // 2) - (tWidth // 2)
        tY = (self.height() // 2) - (self.__radius + 10)  # 위쪽에 10픽셀 떨어진 위치
        painter.drawText(tX, tY, self.__text)

    def updateCircleColor(self, color: QColor):
        self.__circleColor = color
        self.update()