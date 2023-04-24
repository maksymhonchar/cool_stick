from PyQt5.QtWidgets import QBoxLayout, QLabel, QPushButton, QVBoxLayout

from views.steplayout import StepLayout


class Step3Layout(StepLayout):

    def create(self) -> QBoxLayout:
        # Create step description
        step_description = "Step 3: Conduct the Experiment"
        step_description_label = self._create_step_description_label(step_description)
        # Create controls to find bright spots
        brightest_points_layout = self._create_brightest_points_layout()
        # Create controls to find LED coordinates
        led_coordinates_layout = self._create_led_coordinates_layout()
        # Create controls to find P point coordinates
        p_point_coordinates_layout = self._create_p_point_coordinates_layout()
        # Create step layout
        step_layout = QVBoxLayout()
        step_layout.addWidget(step_description_label)
        step_layout.addLayout(brightest_points_layout)
        step_layout.addLayout(led_coordinates_layout)
        step_layout.addLayout(p_point_coordinates_layout)
        return step_layout

    def _create_brightest_points_layout(self) -> QVBoxLayout:
        # Create ui items
        self.find_spots_button = QPushButton("Find the bright spots", self.parent)
        self.find_spots_button.setFixedSize(self.find_spots_button.sizeHint())
        self.find_spots_label = QLabel("Top 5 brightest points: unknown")
        # Save ui items
        self.ui_items.update(
            {
                "find_spots_button": self.find_spots_button,
                "find_spots_label": self.find_spots_label
            }
        )
        # Create layout
        algorithm_layout = QVBoxLayout()
        # Add items to layout
        algorithm_layout.addWidget(self.find_spots_button)
        algorithm_layout.addWidget(self.find_spots_label)
        return algorithm_layout

    def _create_led_coordinates_layout(self) -> QVBoxLayout:
        # Create ui items
        self.find_led_coords_button = QPushButton("Find out x1 LED coordinates", self.parent)
        self.find_led_coords_button.setFixedSize(self.find_led_coords_button.sizeHint())
        self.find_led_coords_label = QLabel("x1 LED coordinates: unknown")
        # Save ui items
        self.ui_items.update(
            {
                "find_led_coords_button": self.find_led_coords_button,
                "find_led_coords_label": self.find_led_coords_label
            }
        )
        # Create layout
        algorithm_layout = QVBoxLayout()
        # Add items to layout
        algorithm_layout.addWidget(self.find_led_coords_button)
        algorithm_layout.addWidget(self.find_led_coords_label)
        return algorithm_layout

    def _create_p_point_coordinates_layout(self) -> QVBoxLayout:
        # Create ui items
        self.find_p_coords_button = QPushButton("Find out P point coordinates", self.parent)
        self.find_p_coords_button.setFixedSize(self.find_p_coords_button.sizeHint())
        self.find_p_coords_label = QLabel("P point coordinates: unknown")
        # Save ui items
        self.ui_items.update(
            {
                "find_p_coords_button": self.find_p_coords_button,
                "find_p_coords_label": self.find_p_coords_label
            }
        )
        # Create layout
        algorithm_layout = QVBoxLayout()
        # Add items to layout
        algorithm_layout.addWidget(self.find_p_coords_button)
        algorithm_layout.addWidget(self.find_p_coords_label)
        return algorithm_layout
