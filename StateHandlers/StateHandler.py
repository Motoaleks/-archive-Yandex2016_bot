from enum import Enum
class StateHandler:
    class State(Enum):
        start=0
        main=1
        choose_acc=2
        balance_show=3
        inpute_sum=4
        add_acc=5
        add_name=6
        add_numb=7
    def __init__(self):
        self.id=-1
        self.state_menu=[]
    def EnterState(self, ui):
        pass
    def EvaluateState(self, ui, msg):
        pass