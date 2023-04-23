from PyQt5.QtWidgets import (
    QBoxLayout,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Step1Layout:
    def __init__(self, parent: QWidget) -> None:
        self.parent = parent

    def create(self) -> QBoxLayout:
        # Create step description
        self.step_description_label = self._create_step_description_label()
        # Create left/right cameras UI
        self.cameras_layout = self._create_cameras_layout()
        # Create separator line
        self.steps_separator_frame = self._create_separator_frame()
        # Create step layout
        step_layout = QVBoxLayout()
        step_layout.addWidget(self.step_description_label)
        step_layout.addLayout(self.cameras_layout)
        step_layout.addWidget(self.steps_separator_frame)
        return step_layout

    def _create_step_description_label(self) -> QLabel:
        step_description_label = QLabel("Step 1: Get Video Input")
        step_description_label.setFixedHeight(50)
        return step_description_label

    def _create_cameras_layout(self) -> QHBoxLayout:
        cameras_layout = QHBoxLayout()
        left_camera_layout = self._create_left_camera_layout()
        right_camera_layout = self._create_right_camera_layout()
        cameras_layout.addLayout(left_camera_layout)
        cameras_layout.addLayout(right_camera_layout)
        return cameras_layout

    def _create_left_camera_layout(self) -> QVBoxLayout:
        # Create ui items
        left_camera_label = QLabel(self.parent)
        left_camera_label.setFixedSize(640, 480)
        left_camera_label.setStyleSheet("background-color: grey;")
        left_camera_combo = QComboBox(self.parent)
        left_camera_start_button = QPushButton("LC: Start stream", self.parent)
        left_camera_stop_button = QPushButton("LC: Stop stream", self.parent)
        # Create controls layout
        left_camera_controls_layout = QHBoxLayout()
        left_camera_controls_layout.addWidget(left_camera_combo)
        left_camera_controls_layout.addWidget(left_camera_start_button)
        left_camera_controls_layout.addWidget(left_camera_stop_button)
        # Create camera layout
        left_camera_layout = QVBoxLayout()
        left_camera_layout.addLayout(left_camera_controls_layout)
        left_camera_layout.addWidget(left_camera_label)
        return left_camera_layout

    def _create_right_camera_layout(self) -> QVBoxLayout:
        # Create ui items
        right_camera_label = QLabel(self.parent)
        right_camera_label.setFixedSize(640, 480)
        right_camera_label.setStyleSheet("background-color: grey;")
        right_camera_combo = QComboBox(self.parent)
        right_camera_start_button = QPushButton("RC: Start stream", self.parent)
        right_camera_stop_button = QPushButton("RC: Stop stream", self.parent)
        # Create controls layout
        right_camera_controls_layout = QHBoxLayout()
        right_camera_controls_layout.addWidget(right_camera_combo)
        right_camera_controls_layout.addWidget(right_camera_start_button)
        right_camera_controls_layout.addWidget(right_camera_stop_button)
        # Create camera layout
        right_camera_layout = QVBoxLayout()
        right_camera_layout.addLayout(right_camera_controls_layout)
        right_camera_layout.addWidget(right_camera_label)
        return right_camera_layout

    def _create_separator_frame(self) -> QFrame:
        separator_frame = QFrame()
        separator_frame.setFrameShape(QFrame.HLine)
        separator_frame.setFrameShadow(QFrame.Sunken)
        separator_frame.setLineWidth(1)
        return separator_frame
