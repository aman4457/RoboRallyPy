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
    def __init__(self, type, rule, rotationBeltsOnly, side0, side1, side2, side3):
        self.type = type
        self.rule = rule
        self.rotationBeltsOnly = rotationBeltsOnly
        self.side0 = side0
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

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


def GenerateBoard():
    True

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
    
def PlaceRobotsAndArchiveTokens():
    True
def initalize():
    ProgDecks = generateProgDecks()
    DamageDeck = generateDamageDeck()
    upgradeDeck = generateUpgradeDeck()
    for i in range(NumOfRobots):
        UpgrHands.append(DealUpgrCards(i, upgradeDeck))
    ResetCheckpointTracker()
    ResetEnergyTracker()
    randomizePrioToken()
    PlaceRobotsAndArchiveTokens()

initalize()


#for i in range(len(upgradeDeck )):
 #   print(upgradeDeck[i].rule)

#for i in range(len(DamageDeck)):
#    print(DamageDeck[i].type)

#for i in range(NumOfRobots):
    #print(UpgrHands[i][0].rule, UpgrHands[i][1].rule, UpgrHands[i][2].rule)

#for i in range(len(ProgDeckTemplate)):
   # print(ProgDeckTemplate[i].type, ProgDeckTemplate[i].rule)

