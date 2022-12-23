#--------------------------------------------------------------------------
#
#   text_field.py
#
#   Description
#       base class for anything that is
#           - clickable
#---------------------------------------------------------------------------
from PyQt5.QtWidgets import QLabel

class TypeAction:

    def __init__(self, win):
        self.win = win

    def mouseEvent(self, event):
        self.start_type_event(event)
    
    def start_type_event(self, event):
        self.xPos = event.x()
        self.yPos = event.y()

        self.label = QLabel("label", self.win)

        self.width = 100
        self.height = 100

        self.label.setGeometry(self.xPos, self.yPos, self.width, self.height)

        self.label.show()
    
    def keyPressEvent(self, event):
        self.label.setText(self.label.text() + str(event.key()))

        self.width  = self.width + 5
        self.label.setGeometry(self.xPos, self.yPos, self.width, self.height)


    
    