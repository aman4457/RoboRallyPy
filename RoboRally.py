import random
from pathlib import Path
import socket
import pickle
import time

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
    def __init__(self, position, ArchiveTokenPos, rotation):
        self.position = position
        self.ArchiveTokenPos = ArchiveTokenPos

map = []
NumOfCheckpoints = 3
ProgDecks = []
NumOfRobots = 1
ProgHands = []
ProgDiscs = []
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

def startServer():
    startingPort = 8000
    server_ip = ""

    for i in range(NumOfRobots):
        global client_socket_dynamic, client_address_dynamic 
        dynamic_var_name = "botServer" + str(i)
        port = startingPort + i
        server_ip = ""
        client_socket_dynamic = "client_socket" + str(i)
        client_address_dynamic = "client_address" + str(i)
        globals()[dynamic_var_name] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        globals()[dynamic_var_name].bind((server_ip, port))
        globals()[dynamic_var_name].listen(0) 
        print(f"Listening on {server_ip}:{port}")
        # accept incoming connections
        globals()[client_socket_dynamic], globals()[client_address_dynamic] = globals()[dynamic_var_name].accept()
        #print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        #request = pickle.dumps("test")



def GenerateMilkRunBoard():
    X1 = []
    X1.append(MapTile("Start","Start","edge","","","edge"))
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
    X1.append(MapTile("Normal","none","edge","edge","",""))
    map.append(X1)
    X2 = []
    X2.append(MapTile("Normal","none","","","","edge"))
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
    X2.append(MapTile("Normal","none","","edge","",""))
    map.append(X2)
    X3 = []
    X3.append(MapTile("Normal","none","","","","edge"))
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
    X3.append(MapTile("Normal","none","","edge","wall",""))
    map.append(X3)
    X4 = []
    X4.append(MapTile("Normal","none","","","","edge"))
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
    X4.append(MapTile("Normal","none","wall","edge","",""))
    map.append(X4)
    X5 = []
    X5.append(MapTile("Normal","none","","","","edge"))
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
    X5.append(MapTile("Normal","none","","edge","",""))
    map.append(X5)
    X6 = []
    X6.append(MapTile("Green","move","","","in","edge"))
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
    X6.append(MapTile("Normal","none","","edge","wall",""))
    map.append(X6)
    X7 = []
    X7.append(MapTile("Green","move","out","in","","edge"))
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
    X7.append(MapTile("Normal","none","wall","edge","",""))
    map.append(X7)
    X8 = []
    X8.append(MapTile("Normal","none","","","","edge"))
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
    X8.append(MapTile("Normal","none","","edge","",""))
    map.append(X8)
    X9 = []
    X9.append(MapTile("Blue","move","","in","","edge"))
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
    X9.append(MapTile("Normal","none","","edge","wall",""))
    map.append(X9)
    X10 = []
    X10.append(MapTile("Normal","none","","","","edge"))
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
    X10.append(MapTile("Normal","none","wall","edge","",""))
    map.append(X10)
    X11 = []
    X11.append(MapTile("Blue","move","","out","","edge"))
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
    X11.append(MapTile("Normal","none","","edge","",""))
    map.append(X11)
    X12 = []
    X12.append(MapTile("Normal","none","","","edge","edge"))
    X12.append(MapTile("Normal","none","","","edge",""))
    X12.append(MapTile("Normal","none","","","edge",""))
    X12.append(MapTile("Normal","none","","","edge",""))
    X12.append(MapTile("Normal","none","","","edge",""))
    X12.append(MapTile("Green", "move","","in","edge",""))
    X12.append(MapTile("Green","none","in","","edge","out"))
    X12.append(MapTile("Normal","none","","","edge",""))
    X12.append(MapTile("Blue","none","in","","edge",""))
    X12.append(MapTile("Normal","none","","","edge",""))
    X12.append(MapTile("Blue","none","out","","edge",""))
    X12.append(MapTile("Normal","none","","","edge",""))
    X12.append(MapTile("Start","Start","","","edge",""))
    X12.append(MapTile("Normal","none","","","edge",""))
    X12.append(MapTile("Normal","none","","edge","edge",""))
    map.append(X12)
    #for i in range(12):
    #    print(map[i][0].type, map[i][1].type, map[i][2].type, map[i][3].type, map[i][4].type, map[i][5].type, map[i][6].type, map[i][7].type, map[i][8].type, map[i][9].type, map[i][10].type, map[i][11].type, map[i][12].type, map[i][13].type, map[i][14].type)

def generateProgDecks():
    for i in range(NumOfRobots):
        tmp = []
        tmp = ProgDeckTemplate.copy()
        random.shuffle(tmp)
        ProgDecks.append(tmp)
    return ProgDecks

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

#def randomizePrioToken():
    #PrioToken = random.randint(0, NumOfRobots)
   # print(PrioToken)
    #return

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
        robots.append(RobotInfo((0,0),(0,0),0))

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
        test = pickle.dumps(startpointsHuman)
        dynamic_var_name = "botServer" + str(placementorder[i])
        client_socket_dynamic = "client_socket" + str(placementorder[i])
        client_address_dynamic = "client_address" + str(placementorder[i])
        globals()[client_socket_dynamic].send(test)
        #pointNum = int(input ("team: " + str(placementorder[i]) + " startpoint num: "))
        pointNum = int(pickle.loads(globals()[client_socket_dynamic].recv(1024)))
        globals()[client_socket_dynamic].send(pickle.dumps("team: " + str(placementorder[i]) + " N = 0 E = 1 S = 2 W = 3 facing: "))
        rotate = int(pickle.loads(globals()[client_socket_dynamic].recv(1024)))
        if pointNum < 9 and pointNum > 0 and pointNums.count(pointNum) != 0 and rotate >= 0 and rotate < 4:
            pointNums.remove(pointNum)
            #print(startpoints[pointNum - 1])
            robots[placementorder[i]].position = startpoints[pointNum - 1]
            robots[placementorder[i]].ArchiveTokenPos = startpoints[pointNum - 1]
            robots[placementorder[i]].rotation = rotate
            print(robots[placementorder[i]].position)
            i += 1
            globals()[client_socket_dynamic].send(pickle.dumps("success"))
        else:
            globals()[client_socket_dynamic].send(pickle.dumps("Position Taken or Invalid"))
            #print("Position Taken or Invalid")

def UpgradePhase():
    return

ProgRegisters = []

def ProgrammingPhase():
    #k = 0
    drawProgCards()
    placeProgCards()
    """
    for j in range(NumOfRobots):
        for i in range(5):
            print(ProgRegisters[j][i].rule, end=" ")
        print("")
    """
    return

def drawProgCards():
    for i in range(NumOfRobots):
        temptst = []
        for j in range(9):
            #print(i)
            #print(ProgDecks[i])
            #print(ProgDecks[0], " test ", ProgDecks[1])
            try:
                if len(ProgHands[i]) != 9:
                    temptst.append(ProgDecks[i].pop(0))
                    #print(temptst[j].rule)
                    #k += 1
            except:
                temptst.append(ProgDecks[i].pop(0))
                #print(temptst[j].rule)
                #k += 1
        ProgHands.append(temptst)

def placeProgCards():
    for i in range(NumOfRobots):
        dynamic_var_name = "botServer" + str(placementorder[i])
        client_socket_dynamic = "client_socket" + str(placementorder[i])
        client_address_dynamic = "client_address" + str(placementorder[i])
        TMP = []
        SendProgHands = [ProgHands[i][0], ProgHands[i][1], ProgHands[i][2], ProgHands[i][3], ProgHands[i][4], ProgHands[i][5], ProgHands[i][6], ProgHands[i][7], ProgHands[i][8]]
        globals()[client_socket_dynamic].send(pickle.dumps(SendProgHands))
        #j = 0
        #@while j < 5:
        #    for k in range(len(ProgHands[i])):
        #        print(ProgHands[i][k].rule, end=" ")
        #    print("")
        #    #print(ProgHands[i][0].rule, ProgHands[i][1].rule, ProgHands[i][2].rule, ProgHands[i][3].rule, ProgHands[i][4].rule, ProgHands[i][5].rule, ProgHands[i][6].rule, ProgHands[i][7].rule, ProgHands[i][8].rule)
        #    try:
        #        inputy = int(input("Team:" + str(i) + " Which Program Card: "))
        #        test = ProgHands[i].pop(inputy - 1)
        #        print(test.rule)
        #        TMP.append(test)
        #        j += 1
        #    except:
        #        print("invalid")
        #ProgRegisters.append(TMP)
    for i in range(NumOfRobots):
        dynamic_var_name = "botServer" + str(placementorder[i])
        client_socket_dynamic = "client_socket" + str(placementorder[i])
        client_address_dynamic = "client_address" + str(placementorder[i])
        test = ""
        time.sleep(1)
        globals()[client_socket_dynamic].send(pickle.dumps("ready"))
        TMP = pickle.loads(globals()[client_socket_dynamic].recv(1024))
        print(TMP)
        ProgRegisters.append(TMP)
againBuffer = ""

def ActivationPhase():
    for i in range(5):
        for j in range(NumOfRobots):
            k = placementorder[j]
            test = ProgRegisters[k][i].rule
            if test == "Again":
                print("Again:", againBuffer)
                test = againBuffer
            if test == "move1":
                againBuffer = "move1"
                #print(againBuffer)
                if robots[placementorder[j]].rotation == 0:
                    #print(map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side0)
                    if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side0 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side0 != "edge":
                        #print(robots[placementorder[j]].position)
                        robots[placementorder[j]].position = (robots[placementorder[j]].position[0], robots[placementorder[j]].position[1] - 1)
                        print(robots[placementorder[j]].position)
                    else:
                        print("wall or edge")
                if robots[placementorder[j]].rotation == 1:
                    if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side1 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side1 != "edge":
                        #print(robots[placementorder[j]].position)
                        robots[placementorder[j]].position = (robots[placementorder[j]].position[0] + 1, robots[placementorder[j]].position[1])
                        print(robots[placementorder[j]].position)
                    else:
                        print("wall or edge")
                if robots[placementorder[j]].rotation == 2:
                    if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side2 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side2 != "edge":
                        #print(robots[placementorder[j]].position)
                        robots[placementorder[j]].position = (robots[placementorder[j]].position[0], robots[placementorder[j]].position[1] + 1)
                        print(robots[placementorder[j]].position)
                    else:
                        print("wall or edge")
                if robots[placementorder[j]].rotation == 3:
                    if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side3 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side3 != "edge":
                        #print(robots[placementorder[j]].position)
                        robots[placementorder[j]].position = (robots[placementorder[j]].position[0] - 1, robots[placementorder[j]].position[1])
                        print(robots[placementorder[j]].position)
                    else:
                        print("wall or edge")
            elif test == "move2":
                againBuffer = "move2"
                #print(againBuffer)
                if robots[placementorder[j]].rotation == 0:
                    #print(map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side0)
                    for i in range(2):
                        if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side0 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side0 != "edge":
                            #print(robots[placementorder[j]].position)
                            robots[placementorder[j]].position = (robots[placementorder[j]].position[0], robots[placementorder[j]].position[1] - 1)
                            print(robots[placementorder[j]].position)
                        else:
                            print("wall or edge")
                    
                if robots[placementorder[j]].rotation == 1:
                    for i in range(2):
                        if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side1 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side1 != "edge":
                            #print(robots[placementorder[j]].position)
                            robots[placementorder[j]].position = (robots[placementorder[j]].position[0] + 1, robots[placementorder[j]].position[1])
                            print(robots[placementorder[j]].position)
                        else:
                            print("wall or edge")
                if robots[placementorder[j]].rotation == 2:
                    for i in range(2):
                        if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side2 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side2 != "edge":
                            #print(robots[placementorder[j]].position)
                            robots[placementorder[j]].position = (robots[placementorder[j]].position[0], robots[placementorder[j]].position[1] + 1)
                            print(robots[placementorder[j]].position)
                        else:
                            print("wall or edge")
                if robots[placementorder[j]].rotation == 3:
                    for i in range(2):
                        if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side3 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side3 != "edge":
                            #print(robots[placementorder[j]].position)
                            robots[placementorder[j]].position = (robots[placementorder[j]].position[0] - 1, robots[placementorder[j]].position[1])
                            print(robots[placementorder[j]].position)
                        else:
                            print("wall or edge")
            elif test == "move3":
                againBuffer = "move3"
                #print(againBuffer)
                if robots[placementorder[j]].rotation == 0:
                    #print(map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side0)
                    for i in range(3):
                        if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side0 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side0 != "edge":
                            #print(robots[placementorder[j]].position)
                            robots[placementorder[j]].position = (robots[placementorder[j]].position[0], robots[placementorder[j]].position[1] - 1)
                            print(robots[placementorder[j]].position)
                        else:
                            print("wall or edge")
                    
                if robots[placementorder[j]].rotation == 1:
                    for i in range(3):
                        if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side1 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side1 != "edge":
                            #print(robots[placementorder[j]].position)
                            robots[placementorder[j]].position = (robots[placementorder[j]].position[0] + 1, robots[placementorder[j]].position[1])
                            print(robots[placementorder[j]].position)
                        else:
                            print("wall or edge")
                if robots[placementorder[j]].rotation == 2:
                    for i in range(3):
                        if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side2 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side2 != "edge":
                            #print(robots[placementorder[j]].position)
                            robots[placementorder[j]].position = (robots[placementorder[j]].position[0], robots[placementorder[j]].position[1] + 1)
                            print(robots[placementorder[j]].position)
                        else:
                            print("wall or edge")
                if robots[placementorder[j]].rotation == 3:
                    for i in range(3):
                        if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side3 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side3 != "edge":
                            #print(robots[placementorder[j]].position)
                            robots[placementorder[j]].position = (robots[placementorder[j]].position[0] - 1, robots[placementorder[j]].position[1])
                            print(robots[placementorder[j]].position)
                        else:
                            print("wall or edge")
            elif test == "ROR":
                againBuffer = "ROR"
                robots[placementorder[j]].rotation += 1
                if robots[placementorder[j]].rotation == 4:
                    robots[placementorder[j]].rotation = 0
                print(robots[placementorder[j]].rotation)
            elif test == "ROL":
                robots[placementorder[j]].rotation -= 1
                if robots[placementorder[j]].rotation == -1:
                    robots[placementorder[j]].rotation = 3
                print(robots[placementorder[j]].rotation)
            elif test == "UTurn":
                robots[placementorder[j]].rotation += 2
                if robots[placementorder[j]].rotation == 4:
                    robots[placementorder[j]].rotation = 0
                if robots[placementorder[j]].rotation == -1:
                    robots[placementorder[j]].rotation = 3
                print("UTurn")
            elif test == "Back":
                if robots[placementorder[j]].rotation == 2:
                    #print(map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side0)
                    if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side0 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side0 != "edge":
                        #print(robots[placementorder[j]].position)
                        robots[placementorder[j]].position = (robots[placementorder[j]].position[0], robots[placementorder[j]].position[1] - 1)
                        print(robots[placementorder[j]].position)
                    else:
                        print("wall or edge")
                if robots[placementorder[j]].rotation == 3:
                    if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side1 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side1 != "edge":
                        #print(robots[placementorder[j]].position)
                        robots[placementorder[j]].position = (robots[placementorder[j]].position[0] + 1, robots[placementorder[j]].position[1])
                        print(robots[placementorder[j]].position)
                    else:
                        print("wall or edge")
                if robots[placementorder[j]].rotation == 0:
                    if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side2 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side2 != "edge":
                        #print(robots[placementorder[j]].position)
                        robots[placementorder[j]].position = (robots[placementorder[j]].position[0], robots[placementorder[j]].position[1] + 1)
                        print(robots[placementorder[j]].position)
                    else:
                        print("wall or edge")
                if robots[placementorder[j]].rotation == 1:
                    if map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side3 != "wall" and map[robots[placementorder[j]].position[1]][robots[placementorder[j]].position[0]].side3 != "edge":
                        #print(robots[placementorder[j]].position)
                        robots[placementorder[j]].position = (robots[placementorder[j]].position[0] - 1, robots[placementorder[j]].position[1])
                        print(robots[placementorder[j]].position)
                    else:
                        print("wall or edge")
                print("Back")
            elif test == "PowerUp":
                if energy[placementorder[j]] < 10:
                    energy[placementorder[j]] += 1 
                print(energy[placementorder[j]])
            """match test:
                case "move1":
                    print("move1")
                case "move2":
                    print("move2")
                case "move3":
                    print("move3")
                case "ROR":
                    print("ROR")
                case "ROL":
                    print("ROL")
                case "UTurn":
                    print("UTurn")
                case "Back":
                    print("Back")
                case "PowerUp":
                    print("PowerUp")
                case "Again":
                    print("Again")
                case _:
                    True
            """
                
    return
    
def initalize():
    startServer()
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
    #print(placementorder)
    return 1

initalize()
UpgradePhase()
#for i in range(20):
    #print(ProgDecks[0][i].rule, ProgDecks[1][i].rule)


ProgrammingPhase()
ActivationPhase()


#for i in range(len(upgradeDeck )):
 #   print(upgradeDeck[i].rule)

#for i in range(len(DamageDeck)):
#    print(DamageDeck[i].type)

#for i in range(NumOfRobots):
    #print(UpgrHands[i][0].rule, UpgrHands[i][1].rule, UpgrHands[i][2].rule)



