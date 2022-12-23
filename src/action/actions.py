#--------------------------------------------------------------------------
#
#   text_field.py
#
#   Description
#       base class for anything that is
#           - clickable
#---------------------------------------------------------------------------
from ui.components import Paragraph

class TypeAction:

    def __init__(self, win):
        self.win = win
        self._setup_key_dict()
    
    def start_type_event(self, event):
        self.xPos = event.x()
        self.yPos = event.y()

        self.active_paragraph = Paragraph(self.win, event.x(), event.y())
    
    def _setup_key_dict(self):
        self._key_dict = {
            16777220 : self.enterKeyPressed,
            16777219 : self.backspaceKeyPressed
        }

    def enterKeyPressed(self):
        self.active_paragraph.handleCarriageReturn()
        
    def backspaceKeyPressed(self):
        self.active_paragraph.handleDelete()

    def mouseEvent(self, event):
        self.start_type_event(event)
    
    def keyPressEvent(self, event):

        # if the key is reserved (in dict) then there is a special
        # callback function associated that must be called
        # otherwise, the key is simply pushed onto the Paragraph
        # object for direct handling (which usually means adding
        # text to paragraph)
        if event.key() in self._key_dict:
            self._key_dict[event.key()]()
        else:
            self.active_paragraph.handleInputKey(str(event.text()))
