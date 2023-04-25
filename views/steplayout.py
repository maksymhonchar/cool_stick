from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout


class StepLayout(QVBoxLayout):

    def init_ui(self) -> None:
        raise NotImplementedError

    def _create_step_description(self, description: str, height: int = 50) -> QLabel:
        step_description_label = QLabel(description)
        step_description_label.setFixedHeight(height)
        return step_description_label

    def _create_separator_frame(self) -> QFrame:
        separator_frame = QFrame()
        separator_frame.setFrameShape(QFrame.HLine)
        separator_frame.setFrameShadow(QFrame.Sunken)
        separator_frame.setLineWidth(1)
        return separator_frame

    def _create_camera_label(self, width: int = 640, height: int = 480) -> QLabel:
        camera_label = QLabel()
        camera_label.setFixedSize(width, height)
        camera_label.setStyleSheet("background-color: grey;")
        return camera_label
