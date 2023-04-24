from typing import List, Callable, Dict

from PyQt5.QtMultimedia import QCameraInfo
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage, QPixmap

from views import AppView
from models import Camera


class AppController:
    def __init__(self, app_view: AppView) -> None:
        self.app_view = app_view
        self.step1_ui_items = self.app_view.step_data['step_1'].ui_items
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
        # Left camera items
        self.step1_ui_items["left_camera_start_button"].clicked.connect(
            self.start_left_camera
        )
        self.step1_ui_items["left_camera_stop_button"].clicked.connect(
            self.stop_left_camera
        )
        # Right camera items
        self.step1_ui_items["right_camera_start_button"].clicked.connect(
            self.start_right_camera
        )
        self.step1_ui_items["right_camera_stop_button"].clicked.connect(
            self.stop_right_camera
        )

    def start_left_camera(self) -> None:
        # Update camera instance
        left_camera_combo = self.step1_ui_items['left_camera_combo']
        left_camera_index = int(left_camera_combo.currentText().split(":")[0])
        self.left_camera = Camera(left_camera_index)
        # Connect camera signal to pixmap
        self.left_camera.video_thread.pixmap_changed_signal.connect(
            self.set_left_camera_frame
        )
        # Start the camera
        self.left_camera.video_thread.start()

    def stop_left_camera(self) -> None:
        self.left_camera.video_thread.stop()

    def set_left_camera_frame(self, image: QImage) -> None:
        image_as_qpixmap = QPixmap.fromImage(image)
        self.step1_ui_items['left_camera_label'].setPixmap(image_as_qpixmap)

    def start_right_camera(self) -> None:
        # Update camera instance
        right_camera_combo = self.step1_ui_items['right_camera_combo']
        right_camera_index = int(right_camera_combo.currentText().split(":")[0])
        self.right_camera = Camera(right_camera_index)
        # Connect camera signal to pixmap
        self.right_camera.video_thread.pixmap_changed_signal.connect(
            self.set_right_camera_frame
        )
        # Start the camera
        self.right_camera.video_thread.start()

    def stop_right_camera(self) -> None:
        self.right_camera.video_thread.stop()

    def set_right_camera_frame(self, image: QImage) -> None:
        image_as_qpixmap = QPixmap.fromImage(image)
        self.step1_ui_items['right_camera_label'].setPixmap(image_as_qpixmap)

    # step 2 signals

    def _connect_step2_signals(self) -> None:
        pass

    # step 3 signals

    def _connect_step3_signals(self) -> None:
        pass
