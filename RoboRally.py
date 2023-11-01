import random
NumOfRobots = 5
ProgDeckTemplate = [card("Program", "move1"), 
            card("Program", "move1"), 
            card("Program", "move1"), 
            card("Program", "move1"), 
            card("Program", "move2"), 
            card("Program", "move2"), 
            card("Program", "move2"), 
            card("Program", "move3"),
            card("Program", "ROR"),
            card("Program", "ROR"),
            card("Program", "ROR"),
            card("Program", "ROR"),
            card("Program", "ROL"),
            card("Program", "ROL"),
            card("Program", "ROL"),
            card("Program", "ROL"),
            card("Program", "UTurn"),
            card("Program", "Back"),
            card("Program", "PowerUp"),
            card("Program", "Again")]
class card:
    def __init__(self, type, rule):
        self.type = type
        self.rule = rule
#for i in range(len(ProgDeckTemplate)):
   # print(ProgDeckTemplate[i].type, ProgDeckTemplate[i].rule)
hands = []
for i in range(NumOfRobots):
    tmp = ProgDeckTemplate
    random.shuffle(tmp)
    hands.append(tmp)
for i in range(NumOfRobots):
    for j in range(len(ProgDeckTemplate)):
        print(hands[i][j].type, hands[i][j].rule, i)
