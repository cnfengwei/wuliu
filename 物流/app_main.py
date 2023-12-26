from PySide6.QtWidgets import QApplication
import sys
from loginwindow import LoginWindow
from main import MainWindow




if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    main_window = MainWindow()

    # window = LoginWindow(main_window)
    # window.show()
    main_window.show()

    sys.exit(app.exec())