from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QColor

class StatusIndicator(QWidget):
    def __init__(self, parent=None, status_text=''):
        super().__init__(parent)

        # 동그라미 생성
        self.indicator_label = QLabel(self)
        self.indicator_label.setFixedSize(50, 50)

        # 텍스트 생성
        self.text_label = QLabel(status_text, self)
        self.text_label.setStyleSheet('color: white')  # 텍스트 색상을 흰색으로 설정

        # 전체 레이아웃
        layout = QVBoxLayout(self)

        # 동그라미와 텍스트를 수평으로 배치
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.indicator_label)
        h_layout.addWidget(self.text_label)
        layout.addLayout(h_layout)

    def update_status(self, status):
        pixmap = QPixmap(self.indicator_label.size())
        pixmap.fill(QColor('black'))  # 동그라미의 배경을 검정색으로 설정

        painter = QPainter(pixmap)
        color = QColor('green') if status == 'On' else \
                QColor('red') if status == 'Off' else \
                QColor('blue') if status == 'Pause' else \
                QColor('gray')  # 동그라미의 색상을 검정색으로 설정

        painter.setBrush(color)
        painter.drawEllipse(0, 0, self.indicator_label.width(), self.indicator_label.height())
        painter.end()

        self.indicator_label.setPixmap(pixmap)

    def set_text(self, text):
        self.text_label.setText(text)