from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

# incrementing contstants
STD_WIDTH_INC = 6
STD_HEIGHT_INC = 25
STD_START_WIDTH = STD_WIDTH_INC + 5

class Paragraph(QLabel):
    def __init__(self, win, xPos, yPos):
        super(Paragraph, self).__init__("", win)

        self.xPos = xPos
        self.yPos = yPos

        self.max_width          = 0 
        self.line_char          = 0
        self._prev_line_char    = 0


        self.width  = STD_START_WIDTH
        self.height = STD_HEIGHT_INC

        self._init_ui()

        self.show()

    def _init_ui(self):

        self.setStyleSheet("border: 1px solid red;")
        self.setAlignment(Qt.AlignTop)
        self.setGeometry(self.xPos, self.yPos, self.width, self.height)

    """ Event Handlers """

    def handleDelete(self):
        self.setText(self.text()[0:-1])
        self.decLineWidth()
        
        if(self.line_char >= self.max_width):
            # update the width of the border by each backspace that
            # occurs
            self.width = self.width - STD_WIDTH_INC

            self.setGeometry(self.xPos, self.yPos, self.width, self.height)

    def handleCarriageReturn(self):
        self.setText(self.text() + "\n")

        # reset the line char so position of text resets
        # to the begining
        self.resetLine()

        # pressing enter key needs to save the max width so that
        # it can be used later. must check to see if we have gone
        # beyond the previous max width, if so then this becomes
        # the max width 
        if(self.width > self.max_width):
            self.max_width = self.width

        self.height = self.height + STD_HEIGHT_INC
        self.setGeometry(self.xPos, self.yPos, self.width, self.height)

    def handleInputKey(self, text):
        self.setText(self.text() + text)

        # update the activate line char which will help to account for
        # returns
        self.line_char = self.line_char + STD_WIDTH_INC

        print("line char" + str(self.line_char))
        print("max width" + str(self.max_width))

        # only increment the width when it has exceeded the max width
        # this way we can account for new lines
        if(self.line_char >= self.max_width):
            self.width = self.width + STD_WIDTH_INC
            self.setGeometry(self.xPos, self.yPos, self.width, self.height)


    """ Helper Functions """

    def resetLine(self):
        self._prev_line_char = self.line_char
        self.line_char = 0

    def decLineWidth(self):
        self.line_char = self.line_char - STD_WIDTH_INC
        if(self.line_char < 0):
            self.line_char = self._prev_line_char





