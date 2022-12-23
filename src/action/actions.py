#--------------------------------------------------------------------------
#
#   text_field.py
#
#   Description
#       base class for anything that is
#           - clickable
#---------------------------------------------------------------------------
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

STD_WIDTH_INC = 6
STD_HEIGHT_INC = 25
STD_START_WIDTH = STD_WIDTH_INC + 5
class TypeAction:

    def __init__(self, win):
        self.win = win
        self._setup_key_dict()
    
    def start_type_event(self, event):
        self.xPos = event.x()
        self.yPos = event.y()

        self.label = QLabel("", self.win)
        self.label.setStyleSheet("border: 1px solid red;")
        self.label.setAlignment(Qt.AlignTop)
        self.max_width = 0 
        self.line_char = 0

        self.width  = STD_START_WIDTH
        self.height = STD_HEIGHT_INC

        self.label.setGeometry(self.xPos, self.yPos, self.width, self.height)

        self.label.show()

    def _setup_key_dict(self):
        self._key_dict = {
            16777220 : self.enterKeyPressed,
            16777219 : self.backspaceKeyPressed
        }

    def enterKeyPressed(self):
        self.label.setText(self.label.text() + "\n")

        # reset the line char so position of text resets
        # to the begining
        self.line_char = 0

        # pressing enter key needs to save the max width so that
        # it can be used later. must check to see if we have gone
        # beyond the previous max width, if so then this becomes
        # the max width 
        if(self.width > self.max_width):
            self.max_width = self.width

        self.height = self.height + 25
        self.label.setGeometry(self.xPos, self.yPos, self.width, self.height)
        

    def backspaceKeyPressed(self):
        self.label.setText(self.label.text()[0:-1])

        # update the line pos to reflect correct pos after backspace
        self.line_char = self.line_char - STD_WIDTH_INC

        if(self.line_char >= self.max_width):
            # update the width of the border by each backspace that
            # occurs
            self.width = self.width - STD_WIDTH_INC

            self.label.setGeometry(self.xPos, self.yPos, self.width, self.height)

    def mouseEvent(self, event):
        self.start_type_event(event)
    
    def keyPressEvent(self, event):

        if event.key() in self._key_dict:
            self._key_dict[event.key()]()
        else:
            self.label.setText(self.label.text() + str(event.text()))
        
            # update the activate line char which will help to account for
            # returns
            self.line_char = self.line_char + STD_WIDTH_INC

            # only increment the width when it has exceeded the max width
            # this way we can account for new lines
            if(self.line_char >= self.max_width):
                self.width = self.width + STD_WIDTH_INC
                self.label.setGeometry(self.xPos, self.yPos, self.width, self.height)
        
        print("max width " + str(self.max_width))
        print("line char " + str(self.line_char))
    