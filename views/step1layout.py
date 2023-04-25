from typing import List
from PyQt5.QtWidgets import QComboBox, QHBoxLayout, QPushButton, QVBoxLayout

from views.steplayout import StepLayout


class Step1Layout(StepLayout):

    def init_ui(self) -> None:
        # Create step description
        step_description = "Step 1: Get Video Input"
        step_description_label = self._create_step_description(step_description)
        self.addWidget(step_description_label)
        # Create left/right cameras video streams
        camera_videos_layout = self._create_camera_videos_layout()
        self.addLayout(camera_videos_layout)
        # Create separator line
        separator_frame = self._create_separator_frame()
        self.addWidget(separator_frame)

    def _create_camera_videos_layout(self) -> QHBoxLayout:
        cameras_layout = QHBoxLayout()
        left_camera_layout = self._create_left_camera_layout()
        cameras_layout.addLayout(left_camera_layout)
        right_camera_layout = self._create_right_camera_layout()
        cameras_layout.addLayout(right_camera_layout)
        return cameras_layout

    def _create_left_camera_layout(self) -> QVBoxLayout:
        # Create widgets
        self.left_camera_label = self._create_camera_label()
        self.left_camera_combo = QComboBox()
        self.left_camera_combo.addItem("No camera selected")
        self.left_camera_start_button = QPushButton("LC: Start stream")
        self.left_camera_stop_button = QPushButton("LC: Stop stream")
        self.left_camera_stop_button.setEnabled(False)
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
        # Create widgets
        self.right_camera_label = self._create_camera_label()
        self.right_camera_combo = QComboBox()
        self.right_camera_combo.addItem("No camera selected")
        self.right_camera_start_button = QPushButton("RC: Start stream")
        self.right_camera_stop_button = QPushButton("RC: Stop stream")
        self.right_camera_stop_button.setEnabled(False)
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
