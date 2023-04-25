from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout

from views.steplayout import StepLayout


class Step2Layout(StepLayout):

    def init_ui(self) -> None:
        # Create step description
        step_description = "Step 2: Get Experiment Images"
        step_description_label = self._create_step_description(step_description)
        self.addWidget(step_description_label)
        # Create left/right cameras screenshots
        camera_screenshots_layout = self._create_camera_screenshots_layout()
        self.addLayout(camera_screenshots_layout)
        # Create separator line
        separator_frame = self._create_separator_frame()
        self.addWidget(separator_frame)

    def _create_camera_screenshots_layout(self) -> QHBoxLayout:
        cameras_layout = QHBoxLayout()
        left_camera_layout = self._create_left_camera_layout()
        cameras_layout.addLayout(left_camera_layout)
        right_camera_layout = self._create_right_camera_layout()
        cameras_layout.addLayout(right_camera_layout)
        return cameras_layout

    def _create_left_camera_layout(self) -> QVBoxLayout:
        # Create widgets
        self.left_camera_button = QPushButton("Left Camera: Take Picture")
        self.left_camera_label = self._create_camera_label()
        # Create camera layout
        left_camera_layout = QVBoxLayout()
        left_camera_layout.addWidget(self.left_camera_button)
        left_camera_layout.addWidget(self.left_camera_label)
        return left_camera_layout

    def _create_right_camera_layout(self) -> QVBoxLayout:
        # Create widgets
        self.right_camera_button = QPushButton("Right Camera: Take Picture")
        self.right_camera_label = self._create_camera_label()
        # Create camera layout
        right_camera_layout = QVBoxLayout()
        right_camera_layout.addWidget(self.right_camera_button)
        right_camera_layout.addWidget(self.right_camera_label)
        return right_camera_layout
