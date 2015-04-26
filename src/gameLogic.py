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
import logger
import statistics

hitPosition = -1
collided = False
data = -1
positionList = []

# check if space is pressed and send signal which calls update movement
s = viztask.Signal()
vizact.onkeydown(' ',s.send)

def onCollide(e):
	global hitPosition
	global collided
	if not collided:
		hitPosition = environment.point.getPosition()
		collided = True
		print(environment.point.getPosition())
	
def createPositions():
	if parameters.intro:
		return [int(4*random.random()) for i in xrange(parameters.numberOfIntroTrials)]
	elif parameters.training: 
		return [int(4*random.random()) for i in xrange(parameters.numberOfTrainingTrials)]
	else:
		return [int(4*random.random()) for i in xrange(parameters.numberOfTestTrials)]
	
def UpdateMovement():
	global positionList
	elapsed = viz.elapsed()

	# Get the joystick position
	x,y,z = environment.joy.getPosition()

	# Get the twist of the joystick
	twist = environment.joy.getTwist()

	# Move the point based on xy-axis value
	move_amount = parameters.joySpeed * elapsed
	position = environment.point.getPosition()
	if parameters.joystick:
		if ((position[0] + x*move_amount) > parameters.fieldsizeX):
			position[0] = parameters.fieldsizeX
		elif((position[0] + x*move_amount) < -parameters.fieldsizeX):
			position[0] = -parameters.fieldsizeX
		else:
			position[0]+= x*move_amount
		if ((position[2] + y*move_amount) > parameters.fieldsizeZ):
			position[2] = parameters.fieldsizeZ
		elif((position[2] + y*move_amount) < -parameters.fieldsizeZ):
			position[2] = -parameters.fieldsizeZ
		else:
			position[2]+= y*move_amount	
	else:
		position = [position[0] + x*move_amount,position[1],position[2] + y*move_amount]
	environment.point.setPosition(position)
	# compute size direction and position of arrow
	if parameters.dreiDEnvironment:
		environment.shadow.setPosition(position[0], parameters.shadow_height, position[2])
	if (parameters.intro or parameters.training):
		if parameters.dreiDEnvironment:
			#environment.arrow.setPosition(position[0], parameters.arrow_height3D, position[2])
			environment.arrow.setPosition(0, parameters.arrow_height3D,0)
		else:
			environment.arrow.setPosition(position[0], parameters.arrow_height2D, position[2])
		environment.arrow.setAxisAngle( [0, 1, 0 , windSpeed.computeWindDirection(position)] ) 
		environment.arrow.setScale([windSpeed.computeWindSpeed(position) * parameters.arrow_size + parameters.arroa_min_size, windSpeed.computeWindSpeed(position) * parameters.arrow_size + parameters.arroa_min_size, windSpeed.computeWindSpeed(position) * parameters.arrow_size + parameters.arroa_min_size])
	positionList.append(position)


	
def runSetOfTrials():
	global data
	global collided
	global positionList
	global hitPosition
	collided = False
	viz.callback( viz.COLLIDE_BEGIN_EVENT, onCollide )
	positions = createPositions()
	move = vizact.ontimer(0, UpdateMovement)
	
	for i in positions:
		data = ""
		positionList = []
		logger.newTrial()
		environment.point.setPosition(0,parameters.point_height,0)
		if i == 0:
			environment.goal.setPosition(parameters.position0Xtrain,parameters.goal_height,parameters.position0Ztrain)
		elif i == 1:
			environment.goal.setPosition(parameters.position1Xtrain,parameters.goal_height,parameters.position1Ztrain)
		elif i == 2:
			environment.goal.setPosition(parameters.position2Xtrain,parameters.goal_height,parameters.position2Ztrain)
		elif i == 3:
			environment.goal.setPosition(parameters.position3Xtrain,parameters.goal_height,parameters.position3Xtrain)
		
		data += ( "\nGoal Position: " + str(environment.goal.getPosition()))
		#enable joystick movement
		environment.point.visible(viz.ON)
		environment.goal.visible(viz.ON)	
		if parameters.dreiDEnvironment:
			environment.shadow.visible(viz.ON)
		if (parameters.training or parameters.intro):
			environment.arrow.visible(viz.ON)
		environment.thrust.disable()		
		move.setEnabled(viz.ON)
		#wait till key is pressed let object fall down
		yield s.wait()
		if parameters.dreiDEnvironment:
			environment.shadow.visible(viz.OFF)
		dropPosition = environment.point.getPosition()
		data += ('\nDrop Position: ' + str(dropPosition))		
		move.setEnabled(viz.OFF)
		#set force on the point + no gravity
		[x,z] = windSpeed.computeWindForce(environment.point.getPosition())
		if parameters.dreiDEnvironment:
			environment.thrust.setForce([x,parameters.gravity,z])
		else:
			environment.thrust.setForce([x,0,z])
		environment.thrust.enable();
		#print(environment.point.getPosition())
		yield viztask.waitTime(1)
		#show fallen object
		environment.thrust.disable()
		environment.point.setVelocity([0,0,0])
		yield viztask.waitTime(1)
		#save hit position use global hit position if 3D based on collision or get last position of point in 2d
		if  not parameters.dreiDEnvironment:
				hitPosition = environment.point.getPosition()
		data+= '\nHit Position: ' + str(hitPosition)
		#compute statistics
		accuracy = statistics.computeAccuracy(hitPosition, environment.goal.getPosition())
		variance = statistics.computeVariance(dropPosition, positionList)
		data+= '\nAccuracy: ' + str(accuracy)
		data+= '\nVariance: ' + str(variance)
		#make point invisible wait and start next trial
		environment.point.visible(viz.OFF)
		environment.goal.visible(viz.OFF)
		if (parameters.training or parameters.intro):
			environment.arrow.visible(viz.OFF)
		yield viztask.waitTime(1)
		parameters.trialNumber+= 1
		data+= "\n" + str(positionList)
		logger.write_logger(data)
		

	
			
	


