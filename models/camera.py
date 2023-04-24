from models.videothread import VideoThread


class Camera:

    def __init__(self, camera_index: int) -> None:
        self.video_thread = VideoThread(camera_index)
