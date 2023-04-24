import platform

import cv2
import numpy as np
from PyQt5.QtCore import QByteArray, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap


class VideoThread(QThread):
    pixmap_changed_signal = pyqtSignal(QPixmap)

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
                frame_as_pixmap = self.frame_to_qpixmap(frame)
                self.pixmap_changed_signal.emit(frame_as_pixmap)
        video_capture.release()

    def stop(self) -> None:
        self.is_running = False
        self.quit()
        self.wait()

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

    @staticmethod
    def frame_to_qpixmap(frame: np.ndarray) -> QPixmap:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        qbyte_array = QByteArray(rgb_frame.tobytes())
        frame_as_qimage = QImage(
            qbyte_array,
            w,
            h,
            bytes_per_line,
            QImage.Format_RGB888,
        )
        frame_as_qpixmap = QPixmap.fromImage(frame_as_qimage)
        return frame_as_qpixmap
