import sys, os
from PyQt4 import QtGui, QtCore
from package.general_config import GeneralConfig


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._general_config = GeneralConfig()
        self._set_window_appearance()
        self._setup_buttons()
        self._setup_left_toolbar()
        self._main_action.trigger()

        # Show Window
        self.show()

    def _set_window_appearance(self):
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Feedra :: Content downloader")
        self.setWindowIcon(QtGui.QIcon("img/rss-icon.png"))

    def _setup_buttons(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self._close_application)  # QtCore.QCoreApplication.instance().quit
        btn.resize(btn.sizeHint())
        btn.move(100, 100)

    def _setup_left_toolbar(self):
        self.left_tool_bar = self.addToolBar("Apps Toolbar")

        # Actions
        rss_action = QtGui.QAction(QtGui.QIcon(self._general_config.get_icon_path("rss")),
                                   "RSS", self)
        youtube_action = QtGui.QAction(QtGui.QIcon(self._general_config.get_icon_path("youtube")),
                                       "Youtube", self)
        soundcloud_action = QtGui.QAction(QtGui.QIcon(self._general_config.get_icon_path("soundcloud")),
                                          "Soundcloud", self)

        # Triggers
        rss_action.triggered.connect(self._load_rss_frame)
        youtube_action.triggered.connect(self._load_youtube_frame)
        soundcloud_action.triggered.connect(self._load_soundcloud_frame)

        # Actions append
        self.left_tool_bar.addAction(rss_action)
        self.left_tool_bar.addAction(youtube_action)
        self.left_tool_bar.addAction(soundcloud_action)

        # Main action binding
        self._main_action = rss_action

    def _load_rss_frame(self):
        print "Loading RSS Frame"

    def _load_youtube_frame(self):
        print "Loading Youtube Frame"

    def _load_soundcloud_frame(self):
        print "Loading Soundcloud Frame"

    @staticmethod
    def _close_application(self):
        print "Exiting Feedra."
        sys.exit()
