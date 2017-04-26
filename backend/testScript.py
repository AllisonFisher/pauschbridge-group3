import lumiversepython as L
import core
import math
import time

PANEL_MIN = 1
PANEL_MAX = 62

SEQUENCE_MIN = 1
SEQUENCE_MAX = 240
class MoodRing(object):
    '''
    '''
    def __init__(self):
        from lumiversepython import Rig
        self.rig = Rig('/home/teacher/Lumiverse/PBridge.rig.json')
        self.rig.init()
        #self.rig.run()

        self.aggregate = []
        #self.rig = core.init()

    def setPanel(self, i, c):
        self.rig.select("$panel=" + str(i)).setRGBRaw(*c)

    def setPanelRange(self, p_range, c=[1,0,0]):
        clamped = [clamp(clr) for clr in c]
        for i in p_range:
            self.setPanel(i, c)

    def setSequence(self, i, c):
        self.rig.select("$sequence=" + str(i)).setRGBRaw(*c)

    def setSequenceRange(self, p_range, c=[1,0,0]):
        clamped = [clamp(clr) for clr in c]
        for i in p_range:
            self.setSequence(i, c)


    def addToAggregate(self, c):
        self.aggregate.append(c)

    def displayAggregate(self):
        n = len(self.aggregate)


    def displayRainbow(self):pass

    def mainLoop(self, endTime=None):
        green = [0.5, 0.65, 0]
        red = [1,0,0]
        while(1):
            for i in xrange(PANEL_MAX):
                if (i) % 2 == 0:
                    self.setPanel(i, [0.5,0.65,0])

                elif (i) % 2 == 1:
                    self.setPanel(i, [1,0,0])
                else:
                    self.setPanel(i, [1,0,0])

            self.rig.updateOnce()
            time.sleep(2)



def clamp(val):
    return max(0, min(1, val))



# application code starts here
m = MoodRing()
m.mainLoop()
'''for i in xrange(PANEL_MAX):
    if (i) % 2 == 0:
        m.setPanel(i, [0.5,0.65,0])

    elif (i) % 2 == 1:
        m.setPanel(i, [1,0,0])
    else:
        m.setPanel(i, [1,0,0])
'''
#m.setPanelRange(range(1, 62), [1,0,0])

