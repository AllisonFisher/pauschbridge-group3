import lumiversepython as L
import core
import math
import time
import random
#from flask import Flask

PANEL_MIN = 1
PANEL_MAX = 57

SEQ_MIN = 1
SEQ_MAX = 200

AGGREGATE_WIDTH_MIN = 2
AGGREGATE_WIDTH_MAX = 2

class MoodRing(object):
    '''
    '''
    def __init__(self, dummyAggregate = True):
        #from lumiversepython import Rig
        #self.rig = Rig('/home/teacher/Lumiverse/PBridge.rig.json')
        #self.rig.init()
        #self.rig.run()

        self.ticks = 0
        self.aggregate = []
        if dummyAggregate:
            # self.aggregate = [[1,0,0], [.2,.2,.7], [.5, 0, .5]]
            self.aggregate = [core.rand_color() for i in xrange(6)]
            print len(self.aggregate)
            #print self.aggregate
        self.rig = core.init(False, False)

    def setPanel(self, i, c, side='both'):
        p = core.getPanel(self.rig, i, side)
        p.setRGBRaw(*c)

    def setPanelRange(self, p_range, c=[1,0,0], side='both'):
        #clamped = [clamp(clr) for clr in c]
        for i in p_range:
            self.setPanel(i, c, side)

    def getSeq(self, i, side='both'):
        s = core.getSequence(self.rig, i, side)
        result = s.getRGBRaw()
        return result

    def setSeq(self, i, c, side='both'):
        s = core.getSequence(self.rig, i, side)
        s.setRGBRaw(*c)

    def setSeqRange(self, s_range, c=[1,0,0], side='both'):
        clamped = [clamp(clr) for clr in c]
        for i in s_range:
            self.setSeq(i, c, side)

    def addToAggregate(self, c):
        self.aggregate.append(c)


    def getRainbowLoopColors(self):
        progress = self.ticks % (256 * 6)
        if 0 <= progress and progress < 256:
            redLevel = 255
            greenLevel = progress
            blueLevel = 0
        elif 256 <= progress and progress < 512:
            redLevel = 255 - (progress-256)
            greenLevel = 255
            blueLevel = 0
        elif 512 <= progress and progress < (256 * 3):
            redLevel = 0
            greenLevel = 255
            blueLevel = (progress % 256)
        elif (256 * 3) <= progress and progress < (256 * 4):
            redLevel = 0
            greenLevel = 255 - (progress % 256)
            blueLevel = 255
        elif (256 * 4) <= progress and progress < (256 * 5):
            redLevel = (progress % 256)
            greenLevel = 0
            blueLevel = 255
        else:
            redLevel = 255
            greenLevel = 0
            blueLevel = 255 - (progress % 256)

        return [scale(redLevel), scale(greenLevel), scale(blueLevel)]

    def fadeColorSteps(self, colorFrom, colorTo, steps=40):
        stepR = (colorTo[0] - colorFrom[0]) / float(steps)
        stepG = (colorTo[1] - colorFrom[1]) / float(steps)
        stepB = (colorTo[2] - colorFrom[2]) / float(steps)

        return [stepR, stepG, stepB]
        #return [colorFrom[0] + stepR, colorFrom[1] + stepG, colorFrom[2] + stepB]

    def drawHappyShowHere(self, seqRange):
        red = [.9, .1, 0]
        orange = [.5, .5, 0]
        blue = [0,0,1]
        self.setSeqRange(seqRange, blue)
        # first, define the show
        # then, move it across the bridge

    def drawHappyShow(self, origin='left'):
        if self.ticks % 10 == 0:
            pos = ((self.ticks) % SEQ_MAX)
            #seq = scale(pos, SEQ_MAX)
            self.drawHappyShowHere(range(pos, pos+10))
        else:
            tick = (self.ticks / 10) * 10
            pos = ((tick) % SEQ_MAX)
            #seq = scale(pos, SEQ_MAX)
            self.drawHappyShowHere(range(pos, pos+10))





    def drawRainbow(self):
        c = self.getRainbowLoopColors()
        self.setPanelRange(range(PANEL_MIN, PANEL_MAX), c)

    '''def drawAggregateFaded(self):
        n = len(self.aggregate)
        span = AGGREGATE_WIDTH_MIN
        colors = self.aggregate.append(self.aggregate[0])
        deltas = []
        for i in xrange(n):
            deltas.append fadeColorSteps(colors[i], colors[i+1])
        for sp in xrange(1, SEQ_MAX, span):
            pos = ((sp + self.ticks) % SEQ_MAX) + 1'''

    def drawAggregate(self):
        if self.ticks % 40 == 0: #every second
            n = len(self.aggregate)
            span = AGGREGATE_WIDTH_MIN
            for i in xrange(1, SEQ_MAX, span):
                pos = ((i + self.ticks) % SEQ_MAX) + 1 # + 1 since we 1-index
                self.setSeqRange(range(pos, pos+span), self.aggregate[(i)%n], 'top')
                if pos > span:
                   self.setSeqRange(range(pos-span+1, pos+1), self.aggregate[(i)%n], 'bottom')
        else:
            lastTick = (self.ticks / 40) * 40
            n = len(self.aggregate)
            span = AGGREGATE_WIDTH_MIN
            for i in xrange(1, SEQ_MAX, span):
                pos = ((i + lastTick) % SEQ_MAX) + 1 # + 1 since we 1-index
                self.setSeqRange(range(pos, pos+span), self.aggregate[(i)%n], 'top')
                if pos > span:
                   self.setSeqRange(range(pos-span+1, pos+1), self.aggregate[(i)%n], 'bottom')



    def drawAXO(self):
        for i in xrange(PANEL_MAX):
            if (i) % 2 == 0:
                self.setPanel(i, [0.5,0.65,0])

            elif (i) % 2 == 1:
                self.setPanel(i, [1,0,0])
            else:
                self.setPanel(i, [1,0,0])
        self.rig.updateOnce()


    def redrawAll(self):
        self.drawAggregate()
        #self.drawAggregateFaded()
        self.drawHappyShow()
        #self.drawRainbow()
        self.rig.updateOnce()

    def mainLoop(self, endTime=None):
        while(1):
            self.redrawAll()
            self.ticks += 1
            time.sleep(0.025) #40 ticks per second

def clamp(val):
    return max(0, min(1, val))

def scale(val, base=255.0):
    return (float(val)/base)



# application code starts here
m = MoodRing()
m.mainLoop()
#m.drawAXO()
#m.mainLoop()
'''for i in xrange(PANEL_MAX):
    if (i) % 2 == 0:
        m.setPanel(i, [0.5,0.65,0])

    elif (i) % 2 == 1:
        m.setPanel(i, [1,0,0])
    else:
        m.setPanel(i, [1,0,0])
'''
#m.setPanelRange(range(1, 62), [1,0,0])

