from typing import Callable, Dict, List

import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtMultimedia import QCameraInfo
from PyQt5.QtWidgets import QApplication

from models import Camera
from views import AppView


class AppController:
    def __init__(self, app_view: AppView) -> None:
        self.app_view = app_view
        self.step1_ui_items = self.app_view.step_data['step_1'].ui_items
        self.step2_ui_items = self.app_view.step_data['step_2'].ui_items
        self.step3_ui_items = self.app_view.step_data['step_3'].ui_items
        self._connect()
        self._update_list_of_webcams()

    def _connect(self) -> None:
        self._connect_file_menu_actions()
        self._connect_tools_menu_actions()
        self._connect_step1_signals()
        self._connect_step2_signals()
        self._connect_step3_signals()

    # file menu

    def _connect_file_menu_actions(self) -> None:
        file_menu_actions = self.app_view.menu_data["file"]
        file_menu_actions_triggers: Dict[str, Callable] = {
            "&Save experiment": self._save_experiment,
            "&Open experiment": self._open_experiment,
            "&Quit": self._quit
        }
        for action_text, trigger_func in file_menu_actions_triggers.items():
            file_menu_actions[action_text].triggered.connect(trigger_func)

    def _save_experiment(self) -> None:
        pass

    def _open_experiment(self) -> None:
        pass

    def _quit(self):
        self._save_experiment()
        QApplication.quit()

    # tools menu

    def _connect_tools_menu_actions(self) -> None:
        tools_menu_actions = self.app_view.menu_data["tools"]
        tools_menu_actions_triggers: Dict[str, Callable] = {
            "&Update list of webcams": self._update_list_of_webcams,
        }
        for action_text, trigger_func in tools_menu_actions_triggers.items():
            tools_menu_actions[action_text].triggered.connect(trigger_func)

    def _update_list_of_webcams(self) -> None:
        # todo: trigger stop btn
        # todo: clear comboboxes
        # todo: set combobox to default value
        # Find out ui items to update
        left_camera_combo = self.step1_ui_items['left_camera_combo']
        right_camera_combo = self.step1_ui_items['right_camera_combo']
        # Find out available cameras
        available_cameras_descriptions = [
            f'{camera_idx}: {camera_info.description()}'
            for camera_idx, camera_info
            in enumerate(QCameraInfo.availableCameras())
        ]
        # Update ui items
        left_camera_combo.addItem("No camera selected")
        right_camera_combo.addItem("No camera selected")
        for description in available_cameras_descriptions:
            left_camera_combo.addItem(description)
            right_camera_combo.addItem(description)

    # step 1 signals

    def _connect_step1_signals(self) -> None:
        self.step1_ui_items["left_camera_start_button"].clicked.connect(
            self.start_left_camera
        )
        self.step1_ui_items["right_camera_start_button"].clicked.connect(
            self.start_right_camera
        )

    def start_left_camera(self) -> None:
        # Update camera instance
        left_camera_combo = self.step1_ui_items['left_camera_combo']
        left_camera_index = int(left_camera_combo.currentText().split(":")[0])
        self.left_camera = Camera(left_camera_index)
        # Connect camera signals
        self.left_camera.video_thread.pixmap_changed_signal.connect(
            self.set_left_camera_label
        )
        self.step1_ui_items["left_camera_stop_button"].clicked.connect(
            self.left_camera.stop
        )
        # Start the camera
        self.left_camera.start()

    def set_left_camera_label(self, pixmap: QPixmap) -> None:
        self.step1_ui_items['left_camera_label'].setPixmap(pixmap)

    def start_right_camera(self) -> None:
        # Update camera instance
        right_camera_combo = self.step1_ui_items['right_camera_combo']
        right_camera_index = int(right_camera_combo.currentText().split(":")[0])
        self.right_camera = Camera(right_camera_index)
        # Connect camera signal to pixmap
        self.right_camera.video_thread.pixmap_changed_signal.connect(
            self.set_right_camera_label
        )
        self.step1_ui_items["right_camera_stop_button"].clicked.connect(
            self.right_camera.stop
        )
        # Start the camera
        self.right_camera.start()

    def set_right_camera_label(self, pixmap: QPixmap) -> None:
        self.step1_ui_items['right_camera_label'].setPixmap(pixmap)

    # step 2 signals

    def _connect_step2_signals(self) -> None:
        self.step2_ui_items["left_camera_button"].clicked.connect(
            self._set_left_camera_screenshot_label
        )
        self.step2_ui_items["right_camera_button"].clicked.connect(
            self._set_right_camera_screenshot_label
        )

    def _set_left_camera_screenshot_label(self) -> None:
        pixmap = self.step1_ui_items["left_camera_label"].pixmap()
        self.step2_ui_items["left_camera_label"].setPixmap(pixmap)

    def _set_right_camera_screenshot_label(self) -> None:
        pixmap = self.step1_ui_items["right_camera_label"].pixmap()
        self.step2_ui_items["right_camera_label"].setPixmap(pixmap)

    # step 3 signals

    def _connect_step3_signals(self) -> None:
        self.step3_ui_items["find_spots_button"].clicked.connect(
            self._find_spots_button_clicked
        )

    def _find_spots_button_clicked(self) -> None:
        pass
