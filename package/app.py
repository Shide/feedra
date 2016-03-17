from PyQt4 import QtGui
from package.ui.main_window import MainWindow


def run(argv):
    app = QtGui.QApplication(argv)
    main_window = MainWindow()
    return app.exec_()
