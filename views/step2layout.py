from PyQt5.QtWidgets import QBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QFrame


class Step2Layout:
    def create(self) -> QBoxLayout:
        box_layout_2 = QVBoxLayout()
        box_layout_2.addWidget(QLabel("Box Layout 2"))
        box_layout_2.addWidget(QPushButton("Button 2"))

        # Add separator line
        line_separator = self._create_line_separator()
        box_layout_2.addWidget(line_separator)

        return box_layout_2

    def _create_line_separator(self) -> QWidget:
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setLineWidth(1)
        return line
