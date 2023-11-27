import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt

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

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 창의 크기와 위치 설정
        self.setGeometry(100, 100, 400, 400)

        # 창의 제목 설정
        self.setWindowTitle('MyWindow')

        # 전체 레이아웃
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # 여백 제거
        self.setStyleSheet('background-color: black;')  # 전체 창의 배경을 검정색으로 설정

        # 텍스트를 출력하는 레이블 추가 (상단 80%)
        self.text_label = QLabel('Hello, PyQt!', self)
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setStyleSheet('color: white')  # 텍스트 색상을 흰색으로 설정
        layout.addWidget(self.text_label, 80)

        # 상태를 나타내는 동그라미 및 텍스트 추가 (하단 20%)
        self.status_layout = QVBoxLayout()
        self.status_layout.setContentsMargins(0, 0, 0, 0)  # 여백 제거
        layout.addLayout(self.status_layout, 20)

        # 상태 객체 생성 및 추가
        self.on_indicator = StatusIndicator(self, 'On')
        self.off_indicator = StatusIndicator(self, 'Off')
        self.pause_indicator = StatusIndicator(self, 'Pause')

        self.status_layout.addWidget(self.on_indicator)
        self.status_layout.addWidget(self.off_indicator)
        self.status_layout.addWidget(self.pause_indicator)

        # 초기 상태 설정
        self.set_status('Off')

    def set_status(self, status):
        self.on_indicator.update_status('On' if status == 'On' else '')
        self.off_indicator.update_status('Off' if status == 'Off' else '')
        self.pause_indicator.update_status('Pause' if status == 'Pause' else '')

if __name__ == '__main__':
    # PyQt 어플리케이션 생성
    app = QApplication(sys.argv)

    # 사용자 정의 창 생성
    window = MyWindow()

    # 창을 화면에 표시
    window.show()

    # 어플리케이션 실행
    sys.exit(app.exec_())
