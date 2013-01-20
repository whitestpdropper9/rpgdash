import math

a = 1.0
b = 1.5
c = 0.0
d = 0.0
exponent = 2

def levelsToHours(levels):
	#hours = (math.exp(10, ((levels-d)/a)) - c) / b
	hours = (math.pow(((levels-d)/a), exponent) - c) / b
	return hours

def hoursToLevels(hours):
	#level = (a * math.log(b*hours + c)) + d
	level = (a*math.pow(((b*hours) + c), (1.0/exponent))) + d
	return level

for i in range(1,21):
	level = i
	hours = levelsToHours(level)
	print "level: " + str(level) + " - " + "hours: " + str(hours)
