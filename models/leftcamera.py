import numpy as np
from PyQt5.QtCore import pyqtSignal

from models.videothread import VideoThread


class LeftCamera(VideoThread):
    left_camera_frame_changed_signal = pyqtSignal(np.ndarray)

    def _emit_frame_changed_signal(self, frame: np.ndarray) -> None:
        self.left_camera_frame_changed_signal.emit(frame)
