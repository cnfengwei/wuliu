from PyQt6.QtWidgets import QApplication
import sys
from loginwindow import LoginWindow
from main import MainWindow
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream



if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    main_window = MainWindow()
    # loading style file
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    ## loading style file, Example 2
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    #window = LoginWindow(main_window)
    #window.show()
    main_window.show()

    sys.exit(app.exec())