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

	# Move the viewpoint based on xy-axis value
	move_amount = 5 * elapsed
	position = environment2D.point.getPosition()
	position = [position[0] + x*move_amount,0,position[2] + y*move_amount]
	environment2D.point.setPosition(position)
	
	
#    viz.MainView.move([x*move_amount,0,y*move_amount], viz.BODY_ORI)
#
#    # Turn the viewpoint left/right based on twist value
#    turn_amount = 90 * elapsed
#    viz.MainView.setEuler([twist*turn_amount,0,0], viz.BODY_ORI, viz.REL_PARENT)

def training2DJoystick():
	positions = createPositions()
	
	for i in positions:
		environment2D.point.setPosition(0,0,0)
		if i == 0:
			environment2D.goal.setPosition(position0X,0,position0Z)
		elif i == 1:
			environment2D.goal.setPosition(position1X,0,position1Z)
		elif i == 2:
			environment2D.goal.setPosition(position2X,0,position2Z)
		elif i == 3:
			environment2D.goal.setPosition(position3X,0,position3X)
		vizact.ontimer(0, UpdateMovement)
		yield viztask.waitTime(0.5)
			
	


