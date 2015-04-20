import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape
import infoPanel
import random
import parameters
import environment3D
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

#training or testing
training = False

# own gravity applied as force since gravity should only be applied under certain conditions
gravity = -3


def createPositions():
	if training:
		return [int(4*random.random()) for i in xrange(parameters.numberOfTrainingTrials)]
	else: 
		return [int(4*random.random()) for i in xrange(parameters.numberOfTestTrials)]
	
def UpdateMovement():

	elapsed = viz.elapsed()

	# Get the joystick position
	x,y,z = environment3D.joy.getPosition()

	# Get the twist of the joystick
	twist = environment3D.joy.getTwist()

	# Move the point based on xy-axis value
	move_amount = 10 * elapsed
	position = environment3D.point.getPosition()
	position = [position[0] + x*move_amount,position[1],position[2] + y*move_amount]
	# compute size direction and position of arrow
	environment3D.point.setPosition(position)
	if (training == True):
		environment3D.arrow.setPosition(position[0] + 2, 21, position[2] + 2)
		environment3D.arrow.setAxisAngle( [0, 1, 0 , windSpeed.computeWindDirection(position)] ) 
		environment3D.arrow.setScale([windSpeed.computeWindSpeed(position) * 5 , 1, windSpeed.computeWindSpeed(position) * 5])

s = viztask.Signal()
vizact.onkeydown(' ',s.send)
	
def training3DJoystick():
	training = True
	positions = createPositions()
	joystickMove = vizact.ontimer(0, UpdateMovement)
	environment3D.point.setVelocity([0,0,0])
	
	for i in positions:
		environment3D.point.setPosition(0,20,0)
		if i == 0:
			environment3D.goal.setPosition(position0Xtrain,0,position0Ztrain)
		elif i == 1:
			environment3D.goal.setPosition(position1Xtrain,0,position1Ztrain)
		elif i == 2:
			environment3D.goal.setPosition(position2Xtrain,0,position2Ztrain)
		elif i == 3:
			environment3D.goal.setPosition(position3Xtrain,0,position3Xtrain)
		
		#enable joystick movement
		environment3D.point.visible(viz.ON)
		environment3D.goal.visible(viz.ON)	
		environment3D.arrow.visible(viz.ON)
		environment3D.thrust.disable()		
		joystickMove.setEnabled(viz.ON)
		#wait till key is pressed let object fall down
		yield s.wait()
		joystickMove.setEnabled(viz.OFF)
		#set force on the point + gravity
		[x,z] = windSpeed.computeWindForce(environment3D.point.getPosition())
		environment3D.thrust.setForce([x,gravity,z])
		environment3D.thrust.enable();
		print(environment3D.point.getPosition())
		yield viztask.waitTime(1)
		#show fallen object
		print(environment3D.point.getPosition())
		environment3D.thrust.disable()
		environment3D.point.setVelocity([0,0,0])
		yield viztask.waitTime(0.5)
		#make point invisible wait and start next trial
		environment3D.point.visible(viz.OFF)
		environment3D.goal.visible(viz.OFF)
		environment3D.arrow.visible(viz.OFF)
		yield viztask.waitTime(1)
		
def testing3DJoystick():
	training = False
	positions = createPositions()
	joystickMove = vizact.ontimer(0, UpdateMovement)
	
	for i in positions:
		environment3D.point.setPosition(0,20,0)
		if i == 0:
			environment3D.goal.setPosition(position0Xtest,0,position0Ztest)
		elif i == 1:
			environment3D.goal.setPosition(position1Xtest,0,position1Ztest)
		elif i == 2:
			environment3D.goal.setPosition(position2Xtest,0,position2Ztest)
		elif i == 3:
			environment3D.goal.setPosition(position3Xtest,0,position3Xtest)
		
		#enable joystick movement
		environment3D.point.visible(viz.ON)
		environment3D.goal.visible(viz.ON)	
		environment3D.thrust.disable()		
		joystickMove.setEnabled(viz.ON)
		#wait till key is pressed let object fall down
		yield s.wait()
		joystickMove.setEnabled(viz.OFF)
		#set force on the point + gravity
		[x,z] = windSpeed.computeWindForce(environment3D.point.getPosition())
		environment3D.thrust.setForce([x,gravity,z])
		environment3D.thrust.enable();
		print(environment3D.point.getPosition())
		yield viztask.waitTime(1)
		#show fallen object
		print(environment3D.point.getPosition())
		environment3D.thrust.disable()
		environment3D.point.setVelocity([0,0,0])
		yield viztask.waitTime(0.5)
		#make point invisible wait and start next trial
		environment3D.point.visible(viz.OFF)
		environment3D.goal.visible(viz.OFF)
		yield viztask.waitTime(1)
	
			
	


