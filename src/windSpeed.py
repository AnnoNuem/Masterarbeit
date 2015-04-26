# wind speed computing 

import math
import parameters


def getXY(position):
	x = (position[0] + parameters.fieldsizeX ) * parameters.xscale + parameters.xbias
	z = (position[2] + parameters.fieldsizeZ ) * parameters.zscale + parameters.zbias
	return [x,z]
	
	
#compute wind forces in x and z direction at given cordinate
def computeWindForce(position):
	[x,z] = getXY(position)
	return [x,z]

def computeWindDirection(position):
	[x,z] = getXY(position)
	hypo = math.sqrt(x * x + z * z)
	direction = math.asin(z/hypo)
	return  - math.degrees(direction) + 90 
	
def computeWindSpeed(position):
	[x,z] = getXY(position)
	return math.sqrt(x*x+z*z)