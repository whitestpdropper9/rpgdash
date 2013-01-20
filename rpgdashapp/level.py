import math

scalingFactor = 1.5
exponent = 2.0

def levelToXP(level):
	xp = math.pow(levels, exponent)/scalingFactor
	return  xp

def XPToLevel(xp):
	level = math.pow(scalingFactor*xp, (1.0/exponent))
	return int(math.floor(level))

def XPToSpecificLevel(xp):
	level = math.pow(scalingFactor*xp, (1.0/exponent))
	return level 
