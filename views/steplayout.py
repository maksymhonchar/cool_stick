from typing import Dict

from PyQt5.QtWidgets import QBoxLayout, QFrame, QLabel, QWidget


class StepLayout:

    def __init__(self, parent: QWidget):
        self.parent = parent
        self.ui_items: Dict[str, QWidget] = {}

    def create(self) -> QBoxLayout:
        raise NotImplementedError

    def _create_step_description_label(self, description: str) -> QLabel:
        step_description_label = QLabel(description)
        step_description_label.setFixedHeight(50)
        return step_description_label

    def _create_separator_frame(self) -> QFrame:
        separator_frame = QFrame()
        separator_frame.setFrameShape(QFrame.HLine)
        separator_frame.setFrameShadow(QFrame.Sunken)
        separator_frame.setLineWidth(1)
        return separator_frame
