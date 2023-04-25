from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout

from views.steplayout import StepLayout


class Step3Layout(StepLayout):

    def init_ui(self) -> None:
        # Create step description
        step_description = "Step 3: Conduct the Experiment"
        step_description_label = self._create_step_description(step_description)
        self.addWidget(step_description_label)
        # Create controls to find bright spots
        brightest_points_layout = self._create_brightest_points_layout()
        self.addLayout(brightest_points_layout)
        # Create controls to find LED coordinates
        led_coordinates_layout = self._create_led_coordinates_layout()
        self.addLayout(led_coordinates_layout)
        # Create controls to find P point coordinates
        p_point_coordinates_layout = self._create_p_point_coordinates_layout()
        self.addLayout(p_point_coordinates_layout)

    def _create_brightest_points_layout(self) -> QVBoxLayout:
        # Create widgets
        self.find_spots_button = QPushButton("Find the bright spots")
        self._set_fixed_size(self.find_spots_button)
        self.find_spots_label = QLabel("Top 5 brightest points: unknown")
        # Create layout
        algorithm_layout = QVBoxLayout()
        algorithm_layout.addWidget(self.find_spots_button)
        algorithm_layout.addWidget(self.find_spots_label)
        return algorithm_layout

    def _create_led_coordinates_layout(self) -> QVBoxLayout:
        # Create widgets
        self.find_led_coords_button = QPushButton("Find out x1 LED coordinates")
        self._set_fixed_size(self.find_led_coords_button)
        self.find_led_coords_label = QLabel("x1 LED coordinates: unknown")
        # Create layout
        algorithm_layout = QVBoxLayout()
        algorithm_layout.addWidget(self.find_led_coords_button)
        algorithm_layout.addWidget(self.find_led_coords_label)
        return algorithm_layout

    def _create_p_point_coordinates_layout(self) -> QVBoxLayout:
        # Create widgets
        self.find_p_coords_button = QPushButton("Find out P point coordinates")
        self._set_fixed_size(self.find_p_coords_button)
        self.find_p_coords_label = QLabel("P point coordinates: unknown")
        # Create layout
        algorithm_layout = QVBoxLayout()
        algorithm_layout.addWidget(self.find_p_coords_button)
        algorithm_layout.addWidget(self.find_p_coords_label)
        return algorithm_layout
    
    @staticmethod
    def _set_fixed_size(button: QPushButton) -> None:
        button.setFixedSize(button.sizeHint())
