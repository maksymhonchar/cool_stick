import platform

import cv2
import numpy as np
from PyQt5.QtCore import QThread


class VideoThread(QThread):

    def __init__(self, camera_index: int):
        super().__init__()
        self.camera_index = camera_index
        self.is_running = False

    def run(self) -> None:
        # Try to create video capturing from camera
        api_preference = self._get_video_capture_api_preference()
        video_capture = cv2.VideoCapture(self.camera_index, api_preference)
        # Continuously capture frames and emit them as QImage objects
        self.is_running = True
        while self.is_running:
            frame_read_ok, frame = video_capture.read()
            if frame_read_ok:
                self._emit_frame_changed_signal(frame)
        video_capture.release()
        print('video_capture released')

    def stop(self) -> None:
        self.is_running = False
        self.quit()
        self.wait()

    def _emit_frame_changed_signal(self, frame: np.ndarray) -> None:
        raise NotImplementedError

    @staticmethod
    def _get_video_capture_api_preference() -> int:
        if platform.system() == "Linux":
            return cv2.CAP_V4L2
        elif platform.system() == "Windows":
            if platform.architecture()[0] == "32bit":
                return cv2.CAP_DSHOW
            elif platform.architecture()[0] == "64bit":
                return cv2.CAP_MSMF
        default_api_preference = cv2.CAP_V4L2
        return default_api_preference
