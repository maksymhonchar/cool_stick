from typing import Callable, Dict, List, Optional, Tuple

import cv2
import numpy as np
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice
from PyQt5.QtGui import QColor, QImage, QPainter, QPixmap
from PyQt5.QtMultimedia import QCameraInfo

from models import LeftCamera, RightCamera
from views import AppView


class AppController:
    def __init__(self, app_view: AppView) -> None:
        self.app_view = app_view
        self.left_camera: Optional[LeftCamera] = None
        self.left_camera_data: Optional[np.ndarray] = None
        self.right_camera: Optional[RightCamera] = None
        self.right_camera_data: Optional[np.ndarray] = None
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
        left_camera_index = int(self.app_view.step1_layout.left_camera_combo.currentText().split(":")[0])
        self.left_camera = LeftCamera(left_camera_index)
        # Connect camera signals
        self.left_camera.left_camera_frame_changed_signal.connect(
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

    def _set_left_camera_label(self, frame: np.ndarray) -> None:
        self.app_view.step1_layout.left_camera_label.setPixmap(
            self._frame_to_qpixmap(frame)
        )
        self.left_camera_data = frame

    def _stop_left_camera(self) -> None:
        if self.left_camera:
            self.left_camera.left_camera_frame_changed_signal.disconnect()
            self.app_view.step1_layout.left_camera_stop_button.disconnect()
            self.left_camera.stop()
            self.left_camera = None
            # Update UI
            self.app_view.step1_layout.left_camera_start_button.setEnabled(True)
            self.app_view.step1_layout.left_camera_stop_button.setEnabled(False)

    def _start_right_camera(self) -> None:
        # Create Camera instance
        right_camera_index = int(self.app_view.step1_layout.right_camera_combo.currentText().split(":")[0])
        self.right_camera = RightCamera(right_camera_index)
        # Connect camera signals
        self.right_camera.right_camera_frame_changed_signal.connect(
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

    def _set_right_camera_label(self, frame: np.ndarray) -> None:
        self.app_view.step1_layout.right_camera_label.setPixmap(
            self._frame_to_qpixmap(frame)
        )
        self.right_camera_data = frame

    def _stop_right_camera(self) -> None:
        if self.right_camera:
            self.right_camera.right_camera_frame_changed_signal.disconnect()
            self.app_view.step1_layout.right_camera_stop_button.disconnect()
            self.right_camera.stop()
            self.right_camera = None
            # Update UI
            self.app_view.step1_layout.right_camera_start_button.setEnabled(True)
            self.app_view.step1_layout.right_camera_stop_button.setEnabled(False)

    @staticmethod
    def _frame_to_qpixmap(frame: np.ndarray) -> QPixmap:
        h, w, ch = frame.shape
        print(f"channels count: {ch=}")
        bytes_per_line = ch * w
        qimage = QImage(
            frame.data,
            w,
            h,
            bytes_per_line,
            QImage.Format_BGR888,
        )
        qpixmap = QPixmap.fromImage(qimage)
        return qpixmap

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
        # self.left_camera_data = self.left_camera_data
        pixmap.save("_set_left_camera_screenshot_label.png", "PNG")

    def _set_right_camera_screenshot_label(self) -> None:
        pixmap = self.app_view.step1_layout.right_camera_label.pixmap()
        self.app_view.step2_layout.right_camera_label.setPixmap(pixmap)
        pixmap.save("_set_right_camera_screenshot_label.png", "PNG")

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
        # 
        left_camera_label = self.app_view.step2_layout.left_camera_label
        left_camera_screenshot = left_camera_label.pixmap()
        if (left_camera_screenshot is not None) or left_camera_screenshot.isNull():
            screenshot_as_ndarray = left_camera_label.frame_data
            most_highlighted_spots = self._find_most_highlighted_spots(
                screenshot_as_ndarray,
                n_points=25
            )
            print(most_highlighted_spots)

    @staticmethod
    def _find_most_highlighted_spots(frame: np.ndarray, n_points: int = 1) -> Tuple:
        gray = np.dot(frame[..., :3], [0.2989, 0.5870, 0.1140])
        positions = np.unravel_index(
            np.argsort(gray.ravel())[-n_points:],
            gray.shape
        )
        return positions

    def _draw_centroids(self, frame: np.ndarray, positions: Tuple) -> QPixmap:
        # Draw a red dot at each position
        dot_size = 15
        dot_color = QColor(255, 0, 0)
        qimage = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QImage.Format_RGB888)
        qpixmap = QPixmap(qimage.width(), qimage.height())
        # qpixmap.fill(QColor(255, 255, 255))
        painter = QPainter(qpixmap)
        painter.setPen(dot_color)
        for x, y in zip(positions[1], positions[0]):
            painter.drawEllipse(x - dot_size // 2, y - dot_size // 2, dot_size, dot_size)
        painter.end()
        return qpixmap

    def _find_led_coords_button_clicked(self) -> None:
        raise NotImplementedError

    def _find_p_coords_button_clicked(self) -> None:
        raise NotImplementedError
