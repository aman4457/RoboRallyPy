import random
from pathlib import Path


class ProgCard:
    def __init__(self, type, rule):
        self.type = type
        self.rule = rule

class UpgradeCard:
    def __init__(self, type, rule, cost):
        self.type = type
        self.rule = rule
        self.cost = cost

class DamageCard:
    def __init__(self, type, rule):
        self.type = type
        self.rule = rule

class MapTile:
    def __init__(self, type, rule, side0, side1, side2, side3):
        self.type = type
        self.rule = rule
        self.side0 = side0
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
class RobotInfo:
    def __init__(self, position, ArchiveTokenPos):
        self.position = position
        self.ArchiveTokenPos = ArchiveTokenPos

map = []
NumOfCheckpoints = 3
ProgDecks = []
NumOfRobots = 5
ProgHands = []
UpgrHands = []
Checkpoint = []
energy = []
PrioToken = 0
ProgDeckTemplate = [ProgCard("Program", "move1"), 
            ProgCard("Program", "move1"), 
            ProgCard("Program", "move1"), 
            ProgCard("Program", "move1"), 
            ProgCard("Program", "move2"), 
            ProgCard("Program", "move2"), 
            ProgCard("Program", "move2"), 
            ProgCard("Program", "move3"),
            ProgCard("Program", "ROR"),
            ProgCard("Program", "ROR"),
            ProgCard("Program", "ROR"),
            ProgCard("Program", "ROR"),
            ProgCard("Program", "ROL"),
            ProgCard("Program", "ROL"),
            ProgCard("Program", "ROL"),
            ProgCard("Program", "ROL"),
            ProgCard("Program", "UTurn"),
            ProgCard("Program", "Back"),
            ProgCard("Program", "PowerUp"),
            ProgCard("Program", "Again")]


def GenerateMilkRunBoard():
    X1 = []
    X1.append(MapTile("Normal","none","edge","","","Edge"))
    X1.append(MapTile("Blue", "move","edge","","out",""))
    X1.append(MapTile("Normal","none","edge","","",""))
    X1.append(MapTile("Blue", "move","edge","","out",""))
    X1.append(MapTile("Normal","none","edge","","",""))
    X1.append(MapTile("Green", "move","edge","","out",""))
    X1.append(MapTile("Normal","none","edge","","",""))
    X1.append(MapTile("Normal","none","edge","","",""))
    X1.append(MapTile("Normal","none","edge","","",""))
    X1.append(MapTile("Normal","none","edge","","",""))
    X1.append(MapTile("Normal","none","edge","","",""))
    X1.append(MapTile("Normal","none","edge","","",""))
    X1.append(MapTile("Normal","none","edge","","",""))
    X1.append(MapTile("Normal","none","edge","","",""))
    X1.append(MapTile("Normal","none","edge","Edge","",""))
    map.append(X1)
    X2 = []
    X2.append(MapTile("Normal","none","","","","Edge"))
    X2.append(MapTile("Blue", "move","in","","out",""))
    X2.append(MapTile("Checkpoint","update","","","",""))
    X2.append(MapTile("Blue", "move","in","","out",""))
    X2.append(MapTile("Normal","none","","","",""))
    X2.append(MapTile("Green", "move","in","","out",""))
    X2.append(MapTile("Blue","move","","in","out",""))
    X2.append(MapTile("Blue","move","","in","","out"))
    X2.append(MapTile("Blue","move","","in","","out"))
    X2.append(MapTile("Blue","move","","in","","out"))
    X2.append(MapTile("Blue","move","","in","","out"))
    X2.append(MapTile("Blue","move","","in","","out"))
    X2.append(MapTile("Normal","none","","","",""))
    X2.append(MapTile("Normal","none","","","",""))
    X2.append(MapTile("Normal","none","","Edge","",""))
    map.append(X2)
    X3 = []
    X3.append(MapTile("Normal","none","","","","Edge"))
    X3.append(MapTile("Blue", "move","in","","out",""))
    X3.append(MapTile("Normal","none","","","",""))
    X3.append(MapTile("Blue", "move","in","","out",""))
    X3.append(MapTile("Normal","none","","","",""))
    X3.append(MapTile("Green", "move","in","","out",""))
    X3.append(MapTile("Blue","move","in","","out",""))
    X3.append(MapTile("Normal","none","","","",""))
    X3.append(MapTile("Battery","Charge","","","",""))
    X3.append(MapTile("Normal","none","","","",""))
    X3.append(MapTile("Normal","none","","","",""))
    X3.append(MapTile("Normal","none","","","",""))
    X3.append(MapTile("Normal","none","","","wall",""))
    X3.append(MapTile("Normal","none","","","wall",""))
    X3.append(MapTile("Normal","none","","Edge","wall",""))
    map.append(X3)
    X4 = []
    X4.append(MapTile("Normal","none","","","","Edge"))
    X4.append(MapTile("Blue", "move","in","","out",""))
    X4.append(MapTile("Battery","Charge","","","",""))
    X4.append(MapTile("Blue", "move","in","","out",""))
    X4.append(MapTile("Normal","none","","","",""))
    X4.append(MapTile("Green", "move","in","","out",""))
    X4.append(MapTile("Blue","move","in","out","wall","wall"))
    X4.append(MapTile("Blue","move","","out","","in"))
    X4.append(MapTile("Blue","move","","out","","in"))
    X4.append(MapTile("Blue","move","","out","","in"))
    X4.append(MapTile("Blue","move","","out","","in"))
    X4.append(MapTile("Blue","move","","out","","in"))
    X4.append(MapTile("Normal","none","wall","","",""))
    X4.append(MapTile("Normal","none","wall","","",""))
    X4.append(MapTile("Normal","none","wall","Edge","",""))
    map.append(X4)
    X5 = []
    X5.append(MapTile("Normal","none","","","","Edge"))
    X5.append(MapTile("Blue", "move","in","","out",""))
    X5.append(MapTile("Normal","none","","","",""))
    X5.append(MapTile("Blue", "move","in","","out",""))
    X5.append(MapTile("Normal","none","","","",""))
    X5.append(MapTile("Green", "move","in","","out",""))
    X5.append(MapTile("Normal","none","","","",""))
    X5.append(MapTile("Normal","none","","","",""))
    X5.append(MapTile("Green","move","","in","out",""))
    X5.append(MapTile("Green","move","","in","","out"))
    X5.append(MapTile("Green","move","","in","","out"))
    X5.append(MapTile("Green","move","","in","","out"))
    X5.append(MapTile("Normal","none","","","",""))
    X5.append(MapTile("Start","Start","","","",""))
    X5.append(MapTile("Normal","none","","Edge","",""))
    map.append(X5)
    X6 = []
    X6.append(MapTile("Green","move","","","in","Edge"))
    X6.append(MapTile("Blue", "move","in","out","",""))
    X6.append(MapTile("Blue","move","","out","","in"))
    X6.append(MapTile("Blue", "move","out","","","in"))
    X6.append(MapTile("Green","move","","in","out",""))
    X6.append(MapTile("Green", "move","in","","","out"))
    X6.append(MapTile("Normal","none","","","",""))
    X6.append(MapTile("Green","move","","in","out",""))
    X6.append(MapTile("Green", "move","in","","","out"))
    X6.append(MapTile("Normal","none","","","",""))
    X6.append(MapTile("Normal","none","","","",""))
    X6.append(MapTile("Green","move","out","in","",""))
    X6.append(MapTile("Normal","none","","","wall",""))
    X6.append(MapTile("Start","Start","","","wall",""))
    X6.append(MapTile("Normal","none","","Edge","wall",""))
    map.append(X6)
    X7 = []
    X7.append(MapTile("Green","move","out","in","","Edge"))
    X7.append(MapTile("Green", "move","","in","","out"))
    X7.append(MapTile("Green","move","","","in","out"))
    X7.append(MapTile("Green", "move","","in","out",""))
    X7.append(MapTile("Green","move","in","","","out"))
    X7.append(MapTile("Normal", "none","","","",""))
    X7.append(MapTile("Normal","none","","","",""))
    X7.append(MapTile("Green","move","in","","out",""))
    X7.append(MapTile("Blue","move","wall","in","out","wall"))
    X7.append(MapTile("Blue","move","","in","","out"))
    X7.append(MapTile("Blue","move","","","in","out"))
    X7.append(MapTile("Normal","none","","","",""))
    X7.append(MapTile("Normal","none","wall","","",""))
    X7.append(MapTile("Start","Start","wall","","",""))
    X7.append(MapTile("Normal","none","wall","Edge","",""))
    map.append(X7)
    X8 = []
    X8.append(MapTile("Normal","none","","","","Edge"))
    X8.append(MapTile("Normal","none","","","",""))
    X8.append(MapTile("Green", "move","out","in","",""))
    X8.append(MapTile("Green","move","in","","","out"))
    X8.append(MapTile("Normal","none","","","",""))
    X8.append(MapTile("Normal","none","","","",""))
    X8.append(MapTile("Normal","none","","","",""))
    X8.append(MapTile("Green","move","in","","out",""))
    X8.append(MapTile("Blue","move","in","","out",""))
    X8.append(MapTile("Normal","none","","","",""))
    X8.append(MapTile("Blue","move","out","","in",""))
    X8.append(MapTile("Normal","none","","","",""))
    X8.append(MapTile("Normal","none","","","",""))
    X8.append(MapTile("Start","Start","","","",""))
    X8.append(MapTile("Normal","none","","Edge","",""))
    map.append(X8)
    X9 = []
    X9.append(MapTile("Blue","move","","in","","Edge"))
    X9.append(MapTile("Blue", "move","","in","","out"))
    X9.append(MapTile("Blue","move","","in","","out"))
    X9.append(MapTile("Blue", "move","","in","","out"))
    X9.append(MapTile("Blue","move","","in","","out"))
    X9.append(MapTile("Blue", "move","wall","wall","in","out"))
    X9.append(MapTile("Green","move","","in","out",""))
    X9.append(MapTile("Green","move","in","","","out"))
    X9.append(MapTile("Blue","move","in","","out",""))
    X9.append(MapTile("Battery","Charge","","","",""))
    X9.append(MapTile("Blue","move","out","","in",""))
    X9.append(MapTile("Normal","none","","","",""))
    X9.append(MapTile("Normal","none","","","wall",""))
    X9.append(MapTile("Start","Start","","","wall",""))
    X9.append(MapTile("Normal","none","","Edge","wall",""))
    map.append(X9)
    X10 = []
    X10.append(MapTile("Normal","none","","","","Edge"))
    X10.append(MapTile("Normal", "none","","","",""))
    X10.append(MapTile("Normal","none","","","",""))
    X10.append(MapTile("Battery","Charge","","","",""))
    X10.append(MapTile("Normal","none","","","",""))
    X10.append(MapTile("Blue", "move","out","","in",""))
    X10.append(MapTile("Green","move","in","","out",""))
    X10.append(MapTile("Reboot","Spawn","","","",""))
    X10.append(MapTile("Blue","move","in","","out",""))
    X10.append(MapTile("Normal","none","","","",""))
    X10.append(MapTile("Blue","move","out","","in",""))
    X10.append(MapTile("Normal","none","","","",""))
    X10.append(MapTile("Start","Start","wall","","",""))
    X10.append(MapTile("Normal","none","wall","","",""))
    X10.append(MapTile("Normal","none","wall","Edge","",""))
    map.append(X10)
    X11 = []
    X11.append(MapTile("Blue","move","","out","","Edge"))
    X11.append(MapTile("Blue", "move","","out","","in"))
    X11.append(MapTile("Blue","move","","out","","in"))
    X11.append(MapTile("Blue", "move","","out","","in"))
    X11.append(MapTile("Blue","move","","out","","in"))
    X11.append(MapTile("Blue", "move","out","","","in"))
    X11.append(MapTile("Green","move","in","","out",""))
    X11.append(MapTile("Normal","none","","","",""))
    X11.append(MapTile("Blue","move","in","","out",""))
    X11.append(MapTile("Normal","none","","","",""))
    X11.append(MapTile("Blue","move","out","","in",""))
    X11.append(MapTile("Normal","none","","","",""))
    X11.append(MapTile("Start","Start","","","",""))
    X11.append(MapTile("Normal","none","","","",""))
    X11.append(MapTile("Normal","none","","Edge","",""))
    map.append(X11)
    X12 = []
    X12.append(MapTile("Normal","none","","","Edge","Edge"))
    X12.append(MapTile("Normal","none","","","Edge",""))
    X12.append(MapTile("Normal","none","","","Edge",""))
    X12.append(MapTile("Normal","none","","","Edge",""))
    X12.append(MapTile("Normal","none","","","Edge",""))
    X12.append(MapTile("Green", "move","","in","Edge",""))
    X12.append(MapTile("Green","none","in","","Edge","out"))
    X12.append(MapTile("Normal","none","","","Edge",""))
    X12.append(MapTile("Blue","none","in","","Edge",""))
    X12.append(MapTile("Normal","none","","","Edge",""))
    X12.append(MapTile("Blue","none","out","","Edge",""))
    X12.append(MapTile("Normal","none","","","Edge",""))
    X12.append(MapTile("Start","Start","","","Edge",""))
    X12.append(MapTile("Normal","none","","","Edge",""))
    X12.append(MapTile("Normal","none","","Edge","Edge",""))
    map.append(X12)
    #for i in range(12):
    #    print(map[i][0].type, map[i][1].type, map[i][2].type, map[i][3].type, map[i][4].type, map[i][5].type, map[i][6].type, map[i][7].type, map[i][8].type, map[i][9].type, map[i][10].type, map[i][11].type, map[i][12].type, map[i][13].type, map[i][14].type)

def generateProgDecks():
    hands = []
    for i in range(NumOfRobots):
        tmp = ProgDeckTemplate
        random.shuffle(tmp)
        hands.append(tmp)
    return hands

def generateDamageDeck():
    DamageDeck = [DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("SPAM",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire",""),
                  DamageCard("Haywire","")]
    random.shuffle(DamageDeck)
    return DamageDeck

def ResetCheckpointTracker():
    for i in range(NumOfRobots):
        Checkpoint.append(0)
    #print(Checkpoint)
    return

def ResetEnergyTracker():
    for i in range(NumOfRobots):
        energy.append(3)
    #print(energy)
    return

def randomizePrioToken():
    PrioToken = random.randint(0, NumOfRobots)
    #print(PrioToken)
    return

def generateUpgradeDeck():
        UpgradeCardDeck = [UpgradeCard("Permanent", "Brakes", "2"),
            UpgradeCard("Permanent", "ChaosTheory", "2"),
            UpgradeCard("Permanent", "CrabLegs", "5"),
            UpgradeCard("Permanent", "DeflectorShield", "2"),
            UpgradeCard("Permanent", "DoubleBarrelLaser", "2"),
            UpgradeCard("Permanent", "Drifting", "4"),
            UpgradeCard("Permanent", "EnergyConversion", "3"),
            UpgradeCard("Permanent", "Firewall", "1"),
            UpgradeCard("Permanent", "FlashDrive", "4"),
            UpgradeCard("Permanent", "HoverUnit", "1"),
            UpgradeCard("Permanent", "LaserKata", "1"),
            UpgradeCard("Permanent", "MemoryCards", "3"),
            UpgradeCard("Permanent", "MiniHowitzer", "3"),
            UpgradeCard("Permanent", "ModularChasis", "1"),
            UpgradeCard("Permanent", "PowerSlide", "4"),
            UpgradeCard("Permanent", "PressorBeam", "3"),
            UpgradeCard("Permanent", "RailGun", "2"),
            UpgradeCard("Permanent", "RammingGear", "2"),
            UpgradeCard("Permanent", "RearLaser", "2"),
            UpgradeCard("Permanent", "Scrambler", "4"),
            UpgradeCard("Permanent", "Self-Diagnostics", "2"),
            UpgradeCard("Permanent", "SpamFilter", "3"),
            UpgradeCard("Permanent", "Spiky", "2"),
            UpgradeCard("Permanent", "TractorBeam", "3"),
            UpgradeCard("Temporary", "AbortSwitch", "1"),
            UpgradeCard("Temporary", "AllAboard", "1"),
            UpgradeCard("Temporary", "Boink", "1"),
            UpgradeCard("Temporary", "CalibrationProtocol", "2"),
            UpgradeCard("Temporary", "DisplacingBlast", "2"),
            UpgradeCard("Temporary", "LuckyBooster", "1"),
            UpgradeCard("Temporary", "Magnetic", "1"),
            UpgradeCard("Temporary", "MemorySwap", "2"),
            UpgradeCard("Temporary", "Overclocked", "2"),
            UpgradeCard("Temporary", "PiercingDrill", "1"),
            UpgradeCard("Temporary", "PressureRelease", "2"),
            UpgradeCard("Temporary", "Re-Initalize", "1"),
            UpgradeCard("Temporary", "Recharge", "0"),
            UpgradeCard("Temporary", "Rewire", "1"),
            UpgradeCard("Temporary", "Switch", "2"),
            UpgradeCard("Temporary", "Zoop", "1")]
        random.shuffle(UpgradeCardDeck)
        return UpgradeCardDeck

def DealUpgrCards(RoboNum, upgradeDeck):
    TMP = []
    TMP.append(upgradeDeck.pop(0))
    TMP.append(upgradeDeck.pop(0))
    TMP.append(upgradeDeck.pop(0))
    #print(TMP[0].rule, TMP[1].rule, TMP[2].rule)
    return TMP
robots = []
placementorder = []
def generateRobot():
    for i in range(NumOfRobots):
        robots.append(RobotInfo((0,0),(0,0)))

def generatePlacementOrder():
    for i in range(NumOfRobots):
        placementorder.append(i)
    random.shuffle(placementorder)
pointNums = []
startpoints = []
startpointsHuman = []
def PlaceRobotsAndArchiveTokens():
    for y in range(12):
        for x in range(15):
            if map[y][x].type == "Start":
                startpoints.append((x, y))
                startpointsHuman.append((x+1, y+1))
    for i in range(len(startpoints)):
        pointNums.append(i+1)
    i = 0
    while i < NumOfRobots:
        print(startpointsHuman)
        pointNum = int(input ("team: " + str(placementorder[i]) + " startpoint num: "))
        if pointNum < 9 and pointNum > 0 and pointNums.count(pointNum) != 0:
            pointNums.remove(pointNum)
            print(startpoints[pointNum - 1])
            robots[placementorder[i]].position = startpoints[pointNum - 1]
            robots[placementorder[i]].ArchiveTokenPos = startpoints[pointNum - 1]
            print(robots[placementorder[i]].position)
            i += 1
        else:
            print("Position Taken or Invalid")



    
def initalize():
    generateRobot()
    GenerateMilkRunBoard()
    ProgDecks = generateProgDecks()
    DamageDeck = generateDamageDeck()
    upgradeDeck = generateUpgradeDeck()
    for i in range(NumOfRobots):
        UpgrHands.append(DealUpgrCards(i, upgradeDeck))
    ResetCheckpointTracker()
    ResetEnergyTracker()
    generatePlacementOrder()
    PlaceRobotsAndArchiveTokens()
    randomizePrioToken()
initalize()


#for i in range(len(upgradeDeck )):
 #   print(upgradeDeck[i].rule)

#for i in range(len(DamageDeck)):
#    print(DamageDeck[i].type)

#for i in range(NumOfRobots):
    #print(UpgrHands[i][0].rule, UpgrHands[i][1].rule, UpgrHands[i][2].rule)

#for i in range(len(ProgDeckTemplate)):
   # print(ProgDeckTemplate[i].type, ProgDeckTemplate[i].rule)

