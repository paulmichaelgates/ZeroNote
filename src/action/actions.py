#--------------------------------------------------------------------------
#
#   text_field.py
#
#   Description
#       base class for anything that is
#           - clickable
#---------------------------------------------------------------------------

# project imports
from ui.components import Paragraph

# PyQt5 imports
from PyQt5.QtGui import QKeySequence, QFont
from PyQt5.QtWidgets import QShortcut

class TypeAction:

    def __init__(self, win):
        self.win = win
        self._setup_key_dict()
    
    def start_type_event(self, event):
        self.xPos = event.x()
        self.yPos = event.y()

        self.active_paragraph = Paragraph(self.win, event.x(), event.y(), self)

    def _setup_key_dict(self):
        self._key_dict = {
            16777220 : self.enterKeyPressed,            # return key
            16777219 : self.backspaceKeyPressed         # backspace key
        }

    """ public functions """

    def setCurrentParagraph(self, par):
        self.active_paragraph = par

    """ initialize all shorcuts for this action mode """
    def initShortcuts(self):

        self.win.rszFont = QShortcut(QKeySequence('Ctrl+L'), self.win)
        self.win.rszFont.activated.connect(lambda: self.active_paragraph.toggleFontSize())

        self.win.italFont = QShortcut(QKeySequence('Ctrl+B'), self.win)
        self.win.italFont.activated.connect(lambda: self.active_paragraph.toggleBoldFont())

    def enterKeyPressed(self):
        self.active_paragraph.handleCarriageReturn()
        
    def backspaceKeyPressed(self):
        self.active_paragraph.handleDelete()

    def mouseEvent(self, event):
        self.start_type_event(event)
    
    def acceptMoveOn(self, event):
        self.active_paragraph.acceptMoveOn(event)

    def keyPressEvent(self, event):

        # if the key is reserved (in dict) then there is a special
        # callback function associated that must be called
        # otherwise, the key is simply pushed onto the Paragraph
        # object for direct handling (which usually means adding
        # text to paragraph)
        if event.key() in self._key_dict:
            self._key_dict[event.key()]()