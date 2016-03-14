from PyQt4 import QtGui


def initial_window():
    window = QtGui.QWidget()
    window.setGeometry(50, 50, 500, 300)
    window.setWindowTitle("Feedra :: Content donwloader")
    window.show()
    return window


def run(argv):
    app = QtGui.QApplication(argv)
    window = initial_window()
    return app.exec_()
