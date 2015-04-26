import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape


viz.res.addPath(r'C:\Users\axel\Desktop\Masterarbeit\resources')

#own imports
from participantInfo import getParticipantInfo
from gameLogic import runSetOfTrials
from environment import createEnvironment
import parameters
import logger
import environment
import statistics

#vizard adjustments
viz.setMultiSample(4)
viz.fov(60)
viz.go()

def setAngularCoordinates():
	if parameters.flavour == 1:
		parameters.angularCoordinate1 = 45
		parameters.angularCoordinate2 = 135
		parameters.angularCoordinate3 = 225
		parameters.angularCoordinate4 = 315
	elif parameters.flavour == 2:
		parameters.angularCoordinate1 = 60
		parameters.angularCoordinate2 = 150
		parameters.angularCoordinate3 = 240
		parameters.angularCoordinate4 = 330
	elif parameters.flavour == 3:
		parameters.angularCoordinate1 = 75
		parameters.angularCoordinate2 = 165
		parameters.angularCoordinate3 = 255
		parameters.angularCoordinate4 = 345
	else:
		parameters.angularCoordinate1 = 90
		parameters.angularCoordinate2 = 180
		parameters.angularCoordinate3 = 270
		parameters.angularCoordinate4 = 0
	

def experiment():

	# get participant data via gui
	parameters.participantData = yield getParticipantInfo()
	
	#init logger and create file
	logger.open_logger()
	
	if parameters.participantData.environment=='2D':
#2d Environment Intro
		parameters.dreiDEnvironment = False
		parameters.intro = True
		parameters.training = False
		parameters.joystick = True
		parameters.flavour = 4
		parameters.radialCoordinate = parameters.radialCoordinateTraining
		setAngularCoordinates()
		environment.info.setText("Introduction")
		environment.info.visible(viz.ON)
		yield viztask.waitTime(2)
		environment.info.visible(viz.OFF)
		createEnvironment()
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
#2d training jostick
		parameters.dreiDEnvironment = False
		parameters.intro = False
		parameters.training = True
		parameters.joystick = True
		parameters.flavour = 1
		parameters.radialCoordinate = parameters.radialCoordinateTraining
		setAngularCoordinates()
		environment.info.setText("Training")
		environment.info.visible(viz.ON)
		yield viztask.waitTime(2)
		environment.info.visible(viz.OFF)
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
#2d Testing joystick 0 degree
		parameters.dreiDEnvironment = False
		parameters.intro = False
		parameters.training = False
		parameters.joystick = True
		parameters.flavour = 1
		parameters.radialCoordinate = parameters.radialCoordinateTesting
		setAngularCoordinates()
		environment.info.setText("Testing")
		environment.info.visible(viz.ON)
		yield viztask.waitTime(2)
		environment.info.visible(viz.OFF)
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
#2d Testing joystick 15 degree
		parameters.dreiDEnvironment = False
		parameters.intro = False
		parameters.training = False
		parameters.joystick = True
		parameters.flavour = 2
		parameters.radialCoordinate = parameters.radialCoordinateTesting
		setAngularCoordinates()
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
#2d Testing joystick 30 degree
		parameters.dreiDEnvironment = False
		parameters.intro = False
		parameters.training = False
		parameters.joystick = True
		parameters.flavour = 3
		parameters.radialCoordinate = parameters.radialCoordinateTesting
		setAngularCoordinates()
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
#2d Testing joystick 45 degree
		parameters.dreiDEnvironment = False
		parameters.intro = False
		parameters.training = False
		parameters.joystick = True
		parameters.flavour = 4
		parameters.radialCoordinate = parameters.radialCoordinateTesting
		setAngularCoordinates()
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
######		
	elif parameters.participantData.environment=='3D':
#3d Environment Intro
		parameters.dreiDEnvironment = True
		parameters.intro = True
		parameters.training = False
		parameters.joystick = True
		parameters.flavour = 4
		parameters.radialCoordinate = parameters.radialCoordinateTraining
		setAngularCoordinates()
		environment.info.setText("Introduction")
		environment.info.visible(viz.ON)
		yield viztask.waitTime(2)
		environment.info.visible(viz.OFF)
		createEnvironment()
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
#3d training jostick
		parameters.dreiDEnvironment = True
		parameters.intro = False
		parameters.training = True
		parameters.joystick = True
		parameters.flavour = 1
		parameters.radialCoordinate = parameters.radialCoordinateTraining
		setAngularCoordinates()
		environment.info.setText("Training")
		environment.info.visible(viz.ON)
		yield viztask.waitTime(2)
		environment.info.visible(viz.OFF)
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
#3d Testing joystick 0 degree
		parameters.dreiDEnvironment = True
		parameters.intro = False
		parameters.training = False
		parameters.joystick = True
		parameters.flavour = 1
		parameters.radialCoordinate = parameters.radialCoordinateTesting
		setAngularCoordinates()
		environment.info.setText("Testing")
		environment.info.visible(viz.ON)
		yield viztask.waitTime(2)
		environment.info.visible(viz.OFF)
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
#3d Testing joystick 15 degree
		parameters.dreiDEnvironment = True
		parameters.intro = False
		parameters.training = False
		parameters.joystick = True
		parameters.flavour = 2
		parameters.radialCoordinate = parameters.radialCoordinateTesting
		setAngularCoordinates()
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
#3d Testing joystick 30 degree
		parameters.dreiDEnvironment = True
		parameters.intro = False
		parameters.training = False
		parameters.joystick = True
		parameters.flavour = 3
		parameters.radialCoordinate = parameters.radialCoordinateTesting
		setAngularCoordinates()
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
#3d Testing joystick 45 degree
		parameters.dreiDEnvironment = True
		parameters.intro = False
		parameters.training = False
		parameters.joystick = True
		parameters.flavour = 4
		parameters.radialCoordinate = parameters.radialCoordinateTesting
		setAngularCoordinates()
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)

	logger.close_logger()
	environment.info.setText("Experiment finished. Thank You")
	environment.info.visible(viz.ON)
	yield viztask.waitTime(2)
	environment.info.visible(viz.OFF)	

viztask.schedule(experiment)
