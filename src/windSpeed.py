# wind speed computing 

import math

xscale = 0.03
zscale = 0.03
xbias = 0.01
zbias = 0.01

#compute wind forces in x and z direction at given cordinate
def computeWindForce(position):
	return [(position[0]+ 20) * xscale + xbias, (position[2]+ 20)* zscale + xbias]

def computeWindDirection(position):
	x = (position[0]+ 20) * xscale + xbias
	z = (position[2]+ 20) * zscale + zbias
	hypo = math.sqrt(x * x + z * z)
	direction = math.asin(z/hypo)
	return  - math.degrees(direction) + 90
	
def computeWindSpeed(position):
	return (position[0]+ 20)*  xbias +(position[2]+ 20)* zscale + zbias