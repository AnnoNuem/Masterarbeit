# wind speed computing 

import math

xscale = 0.05
zscale = 0.01

#compute wind forces in x and z direction at given cordinate
def computeWindForce(position):
	return [(position[0]+ 20) * xscale, (position[2]+ 20)* zscale]

def computeWindDirection(position):
	x = (position[0]+ 20) * xscale
	z = (position[2]+ 20) * zscale
	hypo = math.sqrt(x * x + z * z)
	direction = math.asin(z/hypo)
	return  - math.degrees(direction) + 90
	
def computeWindSpeed(position):
	return (position[0]+ 20)* xscale +(position[2]+ 20)* zscale