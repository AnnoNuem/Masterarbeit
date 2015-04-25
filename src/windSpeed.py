# wind speed computing 

import math

xscale = 0.015
zscale = 0.015
xbias = 0.005
zbias = 0.005

#compute wind forces in x and z direction at given cordinate
def computeWindForce(position):
	return [(position[0]+ 2) * xscale + xbias, (position[2]+ 2)* zscale + xbias]

def computeWindDirection(position):
	x = (position[0]+ 2) * xscale + xbias
	z = (position[2]+ 2) * zscale + zbias
	hypo = math.sqrt(x * x + z * z)
	direction = math.asin(z/hypo)
	return  - math.degrees(direction) + 90
	
def computeWindSpeed(position):
	return (position[0]+ 2)*  xbias +(position[2]+ 2)* zscale + zbias