from typing import Callable, Dict, List, Optional

from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QCameraInfo

from models import LeftCamera, RightCamera
from views import AppView


class AppController:
    def __init__(self, app_view: AppView) -> None:
        self.app_view = app_view
        self.left_camera: Optional[LeftCamera] = None
        self.right_camera: Optional[RightCamera] = None
        self._connect()
        self._update_list_of_webcams()

    def _connect(self) -> None:
        self._connect_menu_actions()
        self._connect_step1_signals()
        self._connect_step2_signals()
        self._connect_step3_signals()

    def _connect_menu_actions(self) -> None:
        menus_and_submenus_actions: Dict[str, Dict[str, Callable]] = {
            "&File": {
                "&Save experiment": self._save_experiment,
                "&Open experiment": self._open_experiment,
                "&Quit": self._quit
            },
            "&Tools": {
                "&Update list of webcams": self._update_list_of_webcams
            }
        }
        for menu_name, submenus in menus_and_submenus_actions.items():
            menu_actions = self.app_view.menu_data[menu_name]
            for submenu_name, submenu_trigger in submenus.items():
                menu_actions[submenu_name].triggered.connect(submenu_trigger)

    def _save_experiment(self) -> None:
        raise NotImplementedError

    def _open_experiment(self) -> None:
        raise NotImplementedError

    def _quit(self) -> None:
        raise NotImplementedError

    def _update_list_of_webcams(self) -> None:
        # Clear the comboboxes
        self.app_view.step1_layout.left_camera_combo.clear()
        self.app_view.step1_layout.right_camera_combo.clear()
        # Find out available cameras
        available_cameras = QCameraInfo.availableCameras()
        available_cameras_descriptions: List[str] = [
            f"{camera_index}: {camera_info.description()}"
            for camera_index, camera_info in enumerate(available_cameras)
        ]
        # Update the comboboxes
        self.app_view.step1_layout.left_camera_combo.addItems(
            ["No camera selected"] + available_cameras_descriptions
        )
        self.app_view.step1_layout.right_camera_combo.addItems(
            ["No camera selected"] + available_cameras_descriptions
        )

    def _connect_step1_signals(self) -> None:
        self.app_view.step1_layout.left_camera_start_button.clicked.connect(
            self._start_left_camera
        )
        self.app_view.step1_layout.right_camera_start_button.clicked.connect(
            self._start_right_camera
        )

    def _start_left_camera(self) -> None:
        # Create Camera instance
        left_camera_index = int(
            self.app_view.step1_layout.left_camera_combo\
                .currentText()\
                .split(":")\
                [0]
        )
        self.left_camera = LeftCamera(left_camera_index)
        # Connect camera signals
        self.left_camera.left_camera_pixmap_changed_signal.connect(
            self._set_left_camera_label
        )
        self.app_view.step1_layout.left_camera_stop_button.clicked.connect(
            self._stop_left_camera
        )
        # Start the camera
        self.left_camera.start()
        # Update UI
        self.app_view.step1_layout.left_camera_start_button.setEnabled(False)
        self.app_view.step1_layout.left_camera_stop_button.setEnabled(True)

    def _set_left_camera_label(self, pixmap: QPixmap) -> None:
        self.app_view.step1_layout.left_camera_label.setPixmap(pixmap)

    def _stop_left_camera(self) -> None:
        if self.left_camera:
            self.left_camera.left_camera_pixmap_changed_signal.disconnect()
            self.app_view.step1_layout.left_camera_stop_button.disconnect()
            self.left_camera.stop()
            self.left_camera = None
            # Update UI
            self.app_view.step1_layout.left_camera_start_button.setEnabled(True)
            self.app_view.step1_layout.left_camera_stop_button.setEnabled(False)


    def _start_right_camera(self) -> None:
        # Create Camera instance
        right_camera_index = int(
            self.app_view.step1_layout.right_camera_combo\
                .currentText()\
                .split(":")\
                [0]
        )
        self.right_camera = RightCamera(right_camera_index)
        # Connect camera signals
        self.right_camera.right_camera_pixmap_changed_signal.connect(
            self._set_right_camera_label
        )
        self.app_view.step1_layout.right_camera_stop_button.clicked.connect(
            self._stop_right_camera
        )
        # Start the camera
        self.right_camera.start()
        # Update UI
        self.app_view.step1_layout.right_camera_start_button.setEnabled(False)
        self.app_view.step1_layout.right_camera_stop_button.setEnabled(True)

    def _set_right_camera_label(self, pixmap: QPixmap) -> None:
        self.app_view.step1_layout.right_camera_label.setPixmap(pixmap)

    def _stop_right_camera(self) -> None:
        if self.right_camera:
            self.right_camera.right_camera_pixmap_changed_signal.disconnect()
            self.app_view.step1_layout.right_camera_stop_button.disconnect()
            self.right_camera.stop()
            self.right_camera = None
            # Update UI
            self.app_view.step1_layout.right_camera_start_button.setEnabled(True)
            self.app_view.step1_layout.right_camera_stop_button.setEnabled(False)


    def _connect_step2_signals(self) -> None:
        self.app_view.step2_layout.left_camera_button.clicked.connect(
            self._set_left_camera_screenshot_label
        )
        self.app_view.step2_layout.right_camera_button.clicked.connect(
            self._set_right_camera_screenshot_label
        )

    def _set_left_camera_screenshot_label(self) -> None:
        pixmap = self.app_view.step1_layout.left_camera_label.pixmap()
        self.app_view.step2_layout.left_camera_label.setPixmap(pixmap)

    def _set_right_camera_screenshot_label(self) -> None:
        pixmap = self.app_view.step1_layout.right_camera_label.pixmap()
        self.app_view.step2_layout.right_camera_label.setPixmap(pixmap)

    def _connect_step3_signals(self) -> None:
        self.app_view.step3_layout.find_spots_button.clicked.connect(
            self._find_spots_button_clicked
        )
        self.app_view.step3_layout.find_led_coords_button.clicked.connect(
            self._find_led_coords_button_clicked
        )
        self.app_view.step3_layout.find_p_coords_button.clicked.connect(
            self._find_p_coords_button_clicked
        )

    def _find_spots_button_clicked(self) -> None:
        raise NotImplementedError

    def _find_led_coords_button_clicked(self) -> None:
        raise NotImplementedError

    def _find_p_coords_button_clicked(self) -> None:
        raise NotImplementedError
