import os
from typing import Dict, List

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction,
    QBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QScrollArea,
)

from views.step1layout import Step1Layout
from views.step2layout import Step2Layout
from views.step3layout import Step3Layout


class MainView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # Init variables
        self.menu_data: Dict[str, Dict[str, QAction]] = {}
        # Init UI
        self.init_ui()

    def init_ui(self) -> None:
        self._set_window_icon()
        self._set_window_title()
        self._add_menus()
        self._create_layout()
        self._add_status_bar()

    def _set_window_icon(self) -> None:
        window_icon_file_path = os.environ.get("WINDOW_ICON_FILE_PATH", "")
        window_icon_as_qicon = QIcon(window_icon_file_path)
        self.setWindowIcon(window_icon_as_qicon)

    def _set_window_title(self) -> None:
        window_title = os.environ.get("WINDOW_TITLE", "")
        self.setWindowTitle(window_title)

    def _add_menus(self) -> None:
        self._add_file_menu()

    def _add_file_menu(self) -> None:
        # Add menu
        menu = self.menuBar().addMenu("&File")
        # Add submenus
        submenus = [
            QAction("&Save experiment", self),
            QAction("&Open experiment", self),
            QAction("&Quit", self),
        ]
        menu.addActions(submenus)
        # Save submenus
        self.menu_data["file"] = {
            submenu.text(): submenu
            for submenu in submenus
        }

    def _create_layout(self) -> None:
        # Create a widget to hold the main layout
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        main_layout = self._create_main_layout()
        scroll_area.setLayout(main_layout)
        # Set the main widget for the window
        self.setCentralWidget(scroll_area)

    def _create_main_layout(self) -> QVBoxLayout:
        main_layout = QVBoxLayout()
        layouts_for_steps: List[QBoxLayout] = [
            Step1Layout(self).create(),
            Step2Layout().create(),
            Step3Layout().create(),
        ]
        for step_layout in layouts_for_steps:
            main_layout.addLayout(step_layout)
        return main_layout

    def _add_status_bar(self) -> None:
        text = os.environ.get("STATUS_BAR_DEFAULT_TEXT", "")
        label = QLabel(text)
        self.statusBar().addWidget(label)
