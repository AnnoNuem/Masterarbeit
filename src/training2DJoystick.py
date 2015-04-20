import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape
import infoPanel
import random
import parameters
import environment2D
import windSpeed

#goal positions
position0X = 20
position0Z = -20
position1X = 20
position1Z = 20
position2X = -20
position2Z = 20
position3X = -20
position3Z = -20


def createPositions():
	return [int(4*random.random()) for i in xrange(parameters.numberOfTrainingTrials)]
	
def UpdateMovement():

	elapsed = viz.elapsed()

	# Get the joystick position
	x,y,z = environment2D.joy.getPosition()

	# Get the twist of the joystick
	twist = environment2D.joy.getTwist()

	# Move the point based on xy-axis value
	move_amount = 5 * elapsed
	position = environment2D.point.getPosition()
	position = [position[0] + x*move_amount,position[1],position[2] + y*move_amount]
	# compute size direction and position of arrow
	environment2D.point.setPosition(position)
	environment2D.arrow.setPosition(position[0] + 1, 21, position[2] + 1)
	environment2D.arrow.setAxisAngle( [0, 1, 0 , windSpeed.computeWindDirection(position)] ) 
	environment2D.arrow.setScale([windSpeed.computeWindSpeed(position) * 2,0,windSpeed.computeWindSpeed(position) * 2])



s = viztask.Signal()
vizact.onkeydown(' ',s.send)
	
def training2DJoystick():
	positions = createPositions()
	joystickMove = vizact.ontimer(0, UpdateMovement)
	
	for i in positions:
		environment2D.point.setPosition(0,20,0)
		if i == 0:
			environment2D.goal.setPosition(position0X,0,position0Z)
		elif i == 1:
			environment2D.goal.setPosition(position1X,0,position1Z)
		elif i == 2:
			environment2D.goal.setPosition(position2X,0,position2Z)
		elif i == 3:
			environment2D.goal.setPosition(position3X,0,position3X)
		
		#enable joystick movement
		environment2D.point.visible(viz.ON)
		environment2D.goal.visible(viz.ON)	
		environment2D.arrow.visible(viz.ON)
		environment2D.thrust.disable()		
		joystickMove.setEnabled(viz.ON)
		#wait till key is pressed let object fall down
		yield s.wait()
		joystickMove.setEnabled(viz.OFF)
		#set force on the point + no gravity
		[x,z] = windSpeed.computeWindForce(environment2D.point.getPosition())
		environment2D.thrust.setForce([x,0,z])
		environment2D.thrust.enable();
		print(environment2D.point.getPosition())
		yield viztask.waitTime(1)
		#show fallen object
		print(environment2D.point.getPosition())
		environment2D.thrust.disable()
		environment2D.point.setVelocity([0,0,0])
		yield viztask.waitTime(0.5)
		#make point invisible wait and start next trial
		environment2D.point.visible(viz.OFF)
		environment2D.goal.visible(viz.OFF)
		environment2D.arrow.visible(viz.OFF)
		yield viztask.waitTime(1)
			
	


