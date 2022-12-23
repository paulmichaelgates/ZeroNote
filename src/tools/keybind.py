#--------------------------------------------------------------------------
#
#   tools_menu.py
#
#   Description
#       contains the tools menu for the application
#---------------------------------------------------------------------------

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QShortcut, QMessageBox
from PyQt5.QtGui import QKeySequence

NOTES_SK = "Ctrl+n"
HIGHLIGHT_SEARCH = "Ctrl+s"

def init_std_kb(win):

    # typing notes
    win.msgSc = QShortcut(QKeySequence(NOTES_SK), win)
    win.msgSc.activated.connect(lambda : QMessageBox.information(win,
                               "message", 'typing mode'))

    # searching
    win.msgSc = QShortcut(QKeySequence("Ctrl+f"), win)
    win.msgSc.activated.connect(lambda : QMessageBox.information(win,
                                'Message', 'search mode'))

