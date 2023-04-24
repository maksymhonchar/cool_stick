import sys

from dotenv import load_dotenv
from PyQt5.QtWidgets import QApplication

from controllers import AppController
from views import AppView


def main():
    app = QApplication(sys.argv)

    app_view = AppView()
    controller = AppController(
        app_view=app_view
    )
    controller.app_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    load_dotenv()
    main()
