import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class CirclesWithText(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 200)
        self.setWindowTitle('Circles with Text')

        # QVBoxLayout 생성
        layout = QVBoxLayout(self)

        # 상단 섹션: QLabel을 담은 위젯 추가
        label_widget = QWidget(self)
        # label_layout = QVBoxLayout(label_widget)
        label = QLabel(parent=label_widget, text="This is the top section")
        label.setAlignment(Qt.AlignCenter)
        # label_layout.addWidget(label)
        layout.addWidget(label, 4)  # 80% (4/5)

        # 하단 섹션: 동그라미를 담은 위젯 추가
        circles_widget = QWidget(self)
        circles_layout = QHBoxLayout(circles_widget)

        # tmp_layout = QHBoxLayout()
        circles_layout.addWidget(CircleWidget())
        circles_layout.addWidget(CircleWidget())
        circles_layout.addWidget(CircleWidget())
        layout.addWidget(circles_widget, 1)  # 20% (1/5)

    def paintEvent(self, event):    
        pass  # 기존의 paintEvent는 사용하지 않음

class CircleWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 안티앨리어싱 적용

        # 동그라미 그리기
        circle_radius = 50
        painter.setBrush(QColor(255, 0, 0))
        painter.drawEllipse(self.width() // 2 - circle_radius,
                            self.height() // 2 - circle_radius,
                            2 * circle_radius, 2 * circle_radius)

        # 텍스트 추가 (동그라미 위에 중앙 정렬)
        painter.setPen(Qt.black)
        font = QFont("Arial", 12)
        painter.setFont(font)
        text = "Circle"
        text_width = painter.fontMetrics().width(text)
        text_x = self.width() // 2 - text_width // 2
        text_y = self.height() // 2 - circle_radius - 10  # 위쪽에 10픽셀 떨어진 위치
        painter.drawText(text_x, text_y, text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CirclesWithText()
    window.show()
    sys.exit(app.exec_())
