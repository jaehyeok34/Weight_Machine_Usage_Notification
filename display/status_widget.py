from PyQt5.QtWidgets        import *
from PyQt5.QtGui            import *
from display.circle_widget  import CircleWidget
from display.palette        import Palette
from display.display_info   import DisplayInfo

class StatusWidget(QWidget):
    STATUS = ["사용중", "일시정지", "종료"]

    def __init__(
        self, parent: QWidget,

        # for circle 
        radius: int, 

        # for text
        textColor: QColor, fontSize: int,
    ) -> None:
        super().__init__(parent)
        self.__circles: list[CircleWidget] = []
        self.__layout = QHBoxLayout(self)

        self.__initCircles(radius, textColor, fontSize)

    def __initCircles(self, radius: int, textColor: QColor, fontSize: int) -> None:
        for i in range(3):
            circle = CircleWidget(
                parent      = self,
                radius      = radius,
                circleColor = Palette.GRAY,
                text        = StatusWidget.STATUS[i],
                textColor   = textColor,
                fontSize    = fontSize
            )
            self.__circles.append(circle)
            self.__layout.addWidget(circle)

    def updateStatus(self, status: DisplayInfo.Status):
        colors = [Palette.GREEN, Palette.BLUE, Palette.RED]
        for i in range(len(self.__circles)):
            if i == status:
                self.__circles[i].updateCircleColor(colors[i])
            else:
                self.__circles[i].updateCircleColor(Palette.GRAY)