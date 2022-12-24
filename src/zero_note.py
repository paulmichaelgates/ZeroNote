#--------------------------------------------------------------------------
#
#   main.py
#
#   Description
#       main page when launching application
#---------------------------------------------------------------------------

# project side imports
import sys

from tools.keybind import init_std_kb
from action.actions import TypeAction

from state import App

# pyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut

# screen info
from screeninfo import get_monitors

""" defines the main window """
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._init_window()
        self._init_UI()

    """ 
        initialize the main window with all necessary 
        components
    """
    def _init_window(self):
        self.app = App(self)
        self._init_shortcuts()
    

    def _init_shortcuts(self):
        self.app.initCurrentActionShortcuts()

    def _init_UI(self):
        self.setStyleSheet("background-color: #222424")


    """ super class overidden functions 

        will redirect to class to handle
        events based on application state
    """
    def mousePressEvent(self, event):
        self.app.mouseEvent(event)
    
    def keyPressEvent(self, event):
        self.app.keyPressEvent(event)

    def mouseMoveEvent(self, event):
        self.app.moveComponent(event)

""" deal with starting dimensions """
def set_app_dimensions(win):
    monitors = get_monitors()

    monitor_1 = monitors[0]

    win.setGeometry(100, 100, monitor_1.width, monitor_1.height)
    win.setWindowTitle("Main window")

def start():
    app = QApplication(sys.argv)
    win = MainWindow()

    # set up back end logic of application
    init_std_kb(win)
    
    # set up the look and feel of application
    set_app_dimensions(win)

    win.show()
    sys.exit(app.exec_())

# starts the actual application
start()