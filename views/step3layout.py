from PyQt5.QtWidgets import QBoxLayout, QLabel, QPushButton, QVBoxLayout


class Step3Layout:
    def create(self) -> QBoxLayout:
        box_layout_3 = QVBoxLayout()
        box_layout_3.addWidget(QLabel("Box Layout 3"))
        box_layout_3.addWidget(QPushButton("Button 3"))
        return box_layout_3
