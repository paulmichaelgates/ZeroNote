from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# incrementing contstants
STD_WIDTH_INC = 6
STD_HEIGHT_INC = 12
STD_START_WIDTH = 10
STD_START_HEIGHT = 30
FONT_SIZE_PAR = 12
STD_MIN_WIDTH = 50
STD_MIN_HEIGHT = 50

class ZStateLabel(QLabel):

    def __init__(self, txt, win):
        super(ZStateLabel, self).__init__(txt, win)

        self._init_ui()

        self.win = win

    def _init_ui(self):
        self.setStyleSheet("color: green")
        self.setGeometry(0, 0, 500, 50)

class Paragraph(QTextEdit):

    def __init__(self, win, xPos, yPos, action):
        super(Paragraph, self).__init__("", win)

        self.win = win
        self.typeAction = action

        self.xPos = xPos
        self.yPos = yPos

        self._char_count = 0

        self.min_width = STD_MIN_WIDTH
        self.min_height = STD_MIN_HEIGHT

        self.width  = self.min_width
        self.height = self.min_height

        self._size_scalar_fact = 1

        self.max_width          = 0 
        self.line_char          = 0
        self._prev_line_char    = 0

        self.textChanged.connect(lambda: self.handleTextChanged())

        self._init_ui()

        self.show()

        self._setup_key_dict()

    """ Initialization Functions """
    def _setup_key_dict(self):
        self._key_dict = {
            16777220 : self.handleCarriageReturnPressed,
            16777219 : self.handleBackspaceKeyPressed
        }

    def _init_ui(self):
        
        self._font_size = FONT_SIZE_PAR
        self.font = QFont('Times', self._font_size)

        self.setFont(self.font)

        self.setStyleSheet("border: 1px solid red; background-color: #222424")
        self.setAlignment(Qt.AlignTop)

        self.updateDimensions()
        
    """ Event Handlers """

    def mousePressEvent(self, event):
        self.typeAction.setCurrentParagraph(self)
        self.win.setMouseTracking(True)

        print("mouse press event")

    def mouseReleaseEvent(self, event):
        self.win.setMouseTracking(False)

        print("mouse release event")

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)

        print("move moved")

    def acceptMoveOn(self, event):
        print("accepting move")
        self.xPos = event.x()
        self.yPos = event.y()

        self.move(self.xPos, self.yPos)                     

    def handleBackspaceKeyPressed(self):
        #self.setText(self.text()[0:-1])
        self.decLineWidth()
        
        if(self.line_char >= self.max_width):
            # update the width of the border by each backspace that
            # occurs
            self.width = self.width - STD_WIDTH_INC

            self.updateDimensions()

    def handleCarriageReturnPressed(self):
        #self.setText(self.text() + "\n")

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
        self.updateDimensions()

    def handleTextChanged(self):
        prevCharCount = self._char_count
        self._char_count = len( self.toPlainText() )

        print("character count = " + str(self._char_count))

        # update the activate line char which will help to account for
        # returns
        self.line_char = self.line_char + STD_WIDTH_INC

        # only increment the width when it has exceeded the max width
        # this way we can account for new lines
        if(prevCharCount < self._char_count):
            self.width = self.width + STD_WIDTH_INC
        elif(self.width >= STD_MIN_WIDTH):
            self.width = self.width - STD_WIDTH_INC
        
        self.updateDimensions()

    """ State Change Functions """

    def resetLine(self):
        self._prev_line_char = self.line_char
        self.line_char = 0

    def decLineWidth(self):
        self.line_char = self.line_char - STD_WIDTH_INC
        if(self.line_char < 0):
            self.line_char = self._prev_line_char

    def updateDimensions(self):
        self.setGeometry(self.xPos, self.yPos, 
                        self.width*self._size_scalar_fact, self.height*self._size_scalar_fact)

    def toggleBoldFont(self):
        isBold = self.font.bold()
        self.font.setBold(not isBold)
        self.setFont(self.font)

    def toggleItalFont(self):
        self.setFontItalic(self.fontItalic)

    def toggleFontSize(self):
        self._scaleBounds()

        self._font_size = FONT_SIZE_PAR * self._size_scalar_fact 

        self.font = QFont('Times', self._font_size)
        self.setFont( self.font)

    def _scaleBounds(self):
        self._size_scalar_fact = ( ( self._size_scalar_fact + 1 ) % 3 ) + 1
        self.updateDimensions()



