import numpy as np
from PyQt5.QtCore import pyqtSignal

from models.videothread import VideoThread


class RightCamera(VideoThread):
    right_camera_frame_changed_signal = pyqtSignal(np.ndarray)

    def _emit_frame_changed_signal(self, frame: np.ndarray) -> None:
        self.right_camera_frame_changed_signal.emit(frame)
