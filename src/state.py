# project imports
from action.actions import TypeAction
from ui.components import ZStateLabel

from debug.print import debugPrint
from inspect import currentframe, getframeinfo

class StateManager:
    def __init__(self, win):
        self._init_state_dict()
        self.win = win
        self.updateCurrentState('type')
        self._state_label = ZStateLabel(self._getAppStateStr(), win)
        self._state_label.show()

    # dict contains all application states: 
    #   format ["key", <Handler Class>]
    def _init_state_dict(self):
        self._state_dict = { 'type' : TypeAction }

    """ Public Functions """

    def mouseEvent(self, event):
        self._current_state.mouseEvent(event)

    def keyPressEvent(self, event):
        self._current_state.keyPressEvent(event)

    # get the starting action class type from the in class
    # dict and set the state to an instance of said class
    def updateCurrentState(self, typeKey):
    
        if typeKey in self._state_dict:
            stateClassType = self._state_dict.get(typeKey)
            self._current_state = stateClassType(self.win)

            self._mode_str = typeKey
        
        else:
            frameinfo = getframeinfo(currentframe())

            msg = "FILE: " + str(frameinfo.filename) + " \nLINE: " + str(frameinfo.lineno) + "\n"
            msg = msg + "the requested type is not avaiable. program may be in invalid state\n"
            debugPrint(msg)


    def _getAppStateStr(self):
        return "active state: " + self._mode_str

    def initCurrentActionShortcuts(self):
        self._current_state.initShortcuts()

    def moveActiveComponent(self, event):
        print("MOVE")
        self._current_state.acceptMoveOn(event)

""" Current App State """
class App:

    def __init__(self, win):
        self.state_manager = StateManager(win)

    def getStateString():
        return "State String"

    def mouseEvent(self, event):
        self.state_manager.mouseEvent(event)

    def keyPressEvent(self, event):
        self.state_manager.keyPressEvent(event)

    def initCurrentActionShortcuts(self):
        self.state_manager.initCurrentActionShortcuts()

    def moveComponent(self, event):
        self.state_manager.moveActiveComponent(event)