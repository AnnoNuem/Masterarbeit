import viz
import parameters
from math import pow
from math import sqrt
from logger import writeTrialBlogStatistics

#compute accuracy by comparing x and z cordinate of hit and goal
def computeAccuracy(hitPosition, goalPosition):
	return (abs(hitPosition[0]-goalPosition[0]) + abs(hitPosition[2] - goalPosition[2]))/2
	
#compute variance between straig line from start to drop position and actual path in order to define explorer exploider behaviour
def computeVariance(dropPosition, positions):
	#compute straight line between start and drop position
	#start is [0,0,0] thus y-intercept is zero and line can be described with drop Position vector only
	distances = []
	sumDistances = 0
	i = 0
	# prevent division by zero
	if dropPosition[0] ==  0 and dropPosition[2] == 0:
		dropPosition[0] = 0.00001
	for position in positions:
		k = (position[0] * dropPosition[0] + position[2] * dropPosition[2])/(pow(dropPosition[0],2) + pow(dropPosition[2],2))
		distance = sqrt(pow((k*dropPosition[0] - position[0]),2) + pow((k*dropPosition[2] - position[2]),2))
		distances.append(distance)
		sumDistances+= distance
		i+=1
	variance = sumDistances/i
	return variance
	
#compute average accuracy and variance over trial blog
def computeTrialBlogStatistics(variances,accuracys, numberOfTrials):
	sumAccuracy = 0
	sumVariance = 0
	for variance in variances:
		sumVariance+= variance
	for accuracy in accuracys:
		sumAccuracy+= accuracy
	meanAccuracy = sumAccuracy/numberOfTrials
	meanVariance = sumVariance/numberOfTrials
	writeTrialBlogStatistics(meanVariance,meanAccuracy,numberOfTrials)
		
	
	