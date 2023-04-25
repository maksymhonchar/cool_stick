import os
from collections import OrderedDict
from typing import Dict

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QLabel, QMainWindow, QScrollArea,
                             QVBoxLayout, QWidget)

from views.step1layout import Step1Layout
from views.step2layout import Step2Layout
from views.step3layout import Step3Layout


class AppView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # Init variables
        self.menu_data: Dict[str, Dict[str, QAction]] = OrderedDict()
        self.step1_layout = Step1Layout()
        self.step2_layout = Step2Layout()
        self.step3_layout = Step3Layout()
        # Init UI
        self.init_ui()

    def init_ui(self) -> None:
        self._set_mainwindow_size()
        self._set_window_icon()
        self._set_window_title()
        self._add_menus()
        self._add_layout()
        self._add_status_bar()

    def _set_mainwindow_size(self) -> None:
        min_width = 640 * 2 + 40
        min_height = 800
        self.setMinimumSize(min_width, min_height)

    def _set_window_icon(self) -> None:
        window_icon_file_path = os.environ.get("WINDOW_ICON_FILE_PATH_ENV_VAR")
        if window_icon_file_path:
            window_icon_as_qicon = QIcon(window_icon_file_path)
            self.setWindowIcon(window_icon_as_qicon)

    def _set_window_title(self) -> None:
        window_title = os.environ.get("WINDOW_TITLE_ENV_VAR")
        if window_title:
            self.setWindowTitle(window_title)

    def _add_menus(self) -> None:
        menus_and_submenus_names = (
            ("&File", ("&Save experiment", "&Open experiment", "&Quit", )),
            ("&Tools", ("&Update list of webcams", )),
        )
        for (menu_name, submenus) in menus_and_submenus_names:
            # Add menu
            menu = self.menuBar().addMenu(menu_name)
            self.menu_data[menu_name] = OrderedDict()
            # Add submenus
            for submenu_name in submenus:
                submenu_qaction = QAction(submenu_name, self)
                menu.addAction(submenu_qaction)
                self.menu_data[menu_name].update({submenu_name: submenu_qaction})

    def _add_layout(self) -> None:
        # Create main layout
        main_layout = QVBoxLayout()
        for step_layout in [self.step1_layout, self.step2_layout, self.step3_layout]:
            step_layout.init_ui()
            main_layout.addLayout(step_layout)
        # Create a widget to hold the main layout
        main_widget = QWidget(self)
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(main_widget)
        main_widget.setLayout(main_layout)
        # Set the main widget for the window
        self.setCentralWidget(scroll_area)

    def _add_status_bar(self) -> None:
        status_bar_text = os.environ.get("STATUS_BAR_DEFAULT_TEXT_ENV_VAR")
        self.status_bar_label = QLabel(status_bar_text)
        self.statusBar().addWidget(self.status_bar_label)
