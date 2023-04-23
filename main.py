import sys

from dotenv import load_dotenv
from PyQt5.QtWidgets import QApplication

from controllers import MainController
from models import ExperimentModel
from views import MainView


def main():
    app = QApplication(sys.argv)

    experiment_model = ExperimentModel()
    main_view = MainView()
    controller = MainController(
        main_view=main_view,
        experiment_model=experiment_model
    )
    controller.main_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    load_dotenv()
    main()
