import os
from collections import OrderedDict
from typing import Dict

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QLabel, QMainWindow, QScrollArea,
                             QVBoxLayout, QWidget)

from views.step1layout import Step1Layout
from views.step2layout import Step2Layout
from views.step3layout import Step3Layout
from views.steplayout import StepLayout


class AppView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # Init variables
        self.menu_data: Dict[str, Dict[str, QAction]] = OrderedDict()
        self.step_data: Dict[str, StepLayout] = OrderedDict()
        # Init UI
        self.init_ui()

    def init_ui(self) -> None:
        self._set_mainwindow_size()
        self._set_window_icon()
        self._set_window_title()
        self._add_menus()
        self._create_layout()
        self._add_status_bar()

    def _set_mainwindow_size(self) -> None:
        min_width = 640 * 2 + 40
        min_height = 800
        self.setMinimumSize(min_width, min_height)

    def _set_window_icon(self) -> None:
        window_icon_file_path = os.environ.get("WINDOW_ICON_FILE_PATH", "")
        if window_icon_file_path:
            window_icon_as_qicon = QIcon(window_icon_file_path)
            self.setWindowIcon(window_icon_as_qicon)

    def _set_window_title(self) -> None:
        window_title = os.environ.get("WINDOW_TITLE", "")
        if window_title:
            self.setWindowTitle(window_title)

    def _add_menus(self) -> None:
        self._add_file_menu()
        self._add_tools_menu()

    def _add_file_menu(self) -> None:
        # Save submenus
        self.menu_data["file"] = OrderedDict(
            {
                "&Save experiment": QAction("&Save experiment", self),
                "&Open experiment": QAction("&Open experiment", self),
                "&Quit": QAction("&Quit", self),
            }
        )
        # Add menu
        menu = self.menuBar().addMenu("&File")
        # Add submenus
        for _, submenu_action in self.menu_data["file"].items():
            menu.addAction(submenu_action)

    def _add_tools_menu(self) -> None:
        # Save submenus
        self.menu_data["tools"] = OrderedDict(
            {
                "&Update list of webcams": QAction("&Update list of webcams", self)
            }
        )
        # Add menu
        menu = self.menuBar().addMenu("&Tools")
        # Add submenus
        for _, submenu_action in self.menu_data["tools"].items():
            menu.addAction(submenu_action)

    def _create_layout(self) -> None:
        # Create a widget to hold the main layout
        main_widget = QWidget(self)
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(main_widget)
        main_layout = self._create_steps_layout()
        main_widget.setLayout(main_layout)
        # Set the main widget for the window
        self.setCentralWidget(scroll_area)

    def _create_steps_layout(self) -> QVBoxLayout:
        # Save layouts
        self.step_data.update(
            {
                'step_1': Step1Layout(self),
                'step_2': Step2Layout(self),
                'step_3': Step3Layout(self)
            }
        )
        # Add layouts
        main_layout = QVBoxLayout()
        for _, step_layout_cls in self.step_data.items():
            step_layout = step_layout_cls.create()
            main_layout.addLayout(step_layout)
        return main_layout

    def _add_status_bar(self) -> None:
        text = os.environ.get("STATUS_BAR_DEFAULT_TEXT", "")
        label = QLabel(text)
        self.statusBar().addWidget(label)
