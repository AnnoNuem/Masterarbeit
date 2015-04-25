import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape
import infoPanel
import random
import parameters
import environment
import windSpeed

#goal positions for training
position0Xtrain = 20
position0Ztrain = -20
position1Xtrain = 20
position1Ztrain = 20
position2Xtrain = -20
position2Ztrain = 20
position3Xtrain = -20
position3Ztrain = -20

#goal positions for training
position0Xtest = 10	
position0Ztest = 0
position1Xtest = -10
position1Ztest = 0
position2Xtest = 0
position2Ztest = 10
position3Xtest = 0
position3Ztest = -10

# own gravity applied as force since gravity should only be applied under certain conditions
gravity = -3

def createPositions():
	if parameters.intro:
		return [int(4*random.random()) for i in xrange(parameters.numberOfIntroTrials)]
	elif parameters.training: 
		return [int(4*random.random()) for i in xrange(parameters.numberOfTrainingTrials)]
	else:
		return [int(4*random.random()) for i in xrange(parameters.numberOfTestTrials)]
	
def UpdateMovement():

	elapsed = viz.elapsed()

	# Get the joystick position
	x,y,z = environment.joy.getPosition()

	# Get the twist of the joystick
	twist = environment.joy.getTwist()

	# Move the point based on xy-axis value
	move_amount = 10 * elapsed
	position = environment.point.getPosition()
	position = [position[0] + x*move_amount,position[1],position[2] + y*move_amount]
	# compute size direction and position of arrow
	environment.point.setPosition(position)
	if (parameters.intro or parameters.training):
		environment.arrow.setPosition(position[0] + 2, 21, position[2] + 2)
		environment.arrow.setAxisAngle( [0, 1, 0 , windSpeed.computeWindDirection(position)] ) 
		environment.arrow.setScale([windSpeed.computeWindSpeed(position) * 5 , 1, windSpeed.computeWindSpeed(position) * 5])

s = viztask.Signal()
vizact.onkeydown(' ',s.send)
	
def runSetOfTrials():
	positions = createPositions()
	move = vizact.ontimer(0, UpdateMovement)
	
	for i in positions:
		environment.point.setPosition(0,20,0)
		if i == 0:
			environment.goal.setPosition(position0Xtrain,0,position0Ztrain)
		elif i == 1:
			environment.goal.setPosition(position1Xtrain,0,position1Ztrain)
		elif i == 2:
			environment.goal.setPosition(position2Xtrain,0,position2Ztrain)
		elif i == 3:
			environment.goal.setPosition(position3Xtrain,0,position3Xtrain)
		
		#enable joystick movement
		environment.point.visible(viz.ON)
		environment.goal.visible(viz.ON)	
		if (parameters.training or parameters.intro):
			environment.arrow.visible(viz.ON)
		environment.thrust.disable()		
		move.setEnabled(viz.ON)
		#wait till key is pressed let object fall down
		yield s.wait()
		move.setEnabled(viz.OFF)
		#set force on the point + no gravity
		[x,z] = windSpeed.computeWindForce(environment.point.getPosition())
		environment.thrust.setForce([x,0,z])
		environment.thrust.enable();
		print(environment.point.getPosition())
		yield viztask.waitTime(1)
		#show fallen object
		print(environment.point.getPosition())
		environment.thrust.disable()
		environment.point.setVelocity([0,0,0])
		yield viztask.waitTime(0.5)
		#make point invisible wait and start next trial
		environment.point.visible(viz.OFF)
		environment.goal.visible(viz.OFF)
		if (parameters.training or parameters.intro):
			environment.arrow.visible(viz.OFF)
		yield viztask.waitTime(1)
		

	
			
	


