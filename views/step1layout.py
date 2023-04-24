from PyQt5.QtWidgets import (QBoxLayout, QComboBox, QHBoxLayout, QLabel,
                             QPushButton, QVBoxLayout)

from views.steplayout import StepLayout


class Step1Layout(StepLayout):

    def create(self) -> QBoxLayout:
        # Create step description
        step_description = "Step 1: Get Video Input"
        step_description_label = self._create_step_description_label(step_description)
        # Create left/right cameras UI
        cameras_layout = self._create_cameras_layout()
        # Create separator line
        steps_separator_frame = self._create_separator_frame()
        # Create step layout
        step_layout = QVBoxLayout()
        step_layout.addWidget(step_description_label)
        step_layout.addLayout(cameras_layout)
        step_layout.addWidget(steps_separator_frame)
        return step_layout

    def _create_cameras_layout(self) -> QHBoxLayout:
        cameras_layout = QHBoxLayout()
        left_camera_layout = self._create_left_camera_layout()
        right_camera_layout = self._create_right_camera_layout()
        cameras_layout.addLayout(left_camera_layout)
        cameras_layout.addLayout(right_camera_layout)
        return cameras_layout

    def _create_left_camera_layout(self) -> QVBoxLayout:
        # Create ui items
        self.left_camera_label = self._create_camera_label()
        self.left_camera_combo = QComboBox(self.parent)
        self.left_camera_start_button = QPushButton("LC: Start stream", self.parent)
        self.left_camera_stop_button = QPushButton("LC: Stop stream", self.parent)
        # Save ui items
        self.ui_items.update(
            {
                'left_camera_label': self.left_camera_label,
                'left_camera_combo': self.left_camera_combo,
                'left_camera_start_button': self.left_camera_start_button,
                'left_camera_stop_button': self.left_camera_stop_button,
            }
        )
        # Create controls layout
        left_camera_controls_layout = QHBoxLayout()
        left_camera_controls_layout.addWidget(self.left_camera_combo)
        left_camera_controls_layout.addWidget(self.left_camera_start_button)
        left_camera_controls_layout.addWidget(self.left_camera_stop_button)
        # Create camera layout
        left_camera_layout = QVBoxLayout()
        left_camera_layout.addLayout(left_camera_controls_layout)
        left_camera_layout.addWidget(self.left_camera_label)
        return left_camera_layout

    def _create_right_camera_layout(self) -> QVBoxLayout:
        # Create ui items
        self.right_camera_label = self._create_camera_label()
        self.right_camera_combo = QComboBox(self.parent)
        self.right_camera_start_button = QPushButton("RC: Start stream", self.parent)
        self.right_camera_stop_button = QPushButton("RC: Stop stream", self.parent)
        # Save ui items
        self.ui_items.update(
            {
                'right_camera_label': self.right_camera_label,
                'right_camera_combo': self.right_camera_combo,
                'right_camera_start_button': self.right_camera_start_button,
                'right_camera_stop_button': self.right_camera_stop_button,
            }
        )
        # Create controls layout
        right_camera_controls_layout = QHBoxLayout()
        right_camera_controls_layout.addWidget(self.right_camera_combo)
        right_camera_controls_layout.addWidget(self.right_camera_start_button)
        right_camera_controls_layout.addWidget(self.right_camera_stop_button)
        # Create camera layout
        right_camera_layout = QVBoxLayout()
        right_camera_layout.addLayout(right_camera_controls_layout)
        right_camera_layout.addWidget(self.right_camera_label)
        return right_camera_layout

    def _create_camera_label(self, width: int = 640, height: int = 480) -> QLabel:
        camera_label = QLabel(self.parent)
        camera_label.setFixedSize(width, height)
        camera_label.setStyleSheet("background-color: grey;")
        return camera_label
