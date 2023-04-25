from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap

from models.videothread import VideoThread


class LeftCamera(VideoThread):
    left_camera_pixmap_changed_signal = pyqtSignal(QPixmap)

    def _emit_pixmap_changed_signal(self, pixmap: QPixmap) -> None:
        self.left_camera_pixmap_changed_signal.emit(pixmap)
