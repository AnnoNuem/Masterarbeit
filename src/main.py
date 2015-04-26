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
		environment.info.setText("Training")
		environment.info.visible(viz.ON)
		yield viztask.waitTime(2)
		environment.info.visible(viz.OFF)
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
		#2d Testing joystick
		parameters.dreiDEnvironment = False
		parameters.intro = False
		parameters.training = False
		parameters.joystick = True
		environment.info.setText("Testing")
		environment.info.visible(viz.ON)
		yield viztask.waitTime(2)
		environment.info.visible(viz.OFF)
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
	elif parameters.participantData.environment=='3D':
		#3d Environment Intro
		parameters.dreiDEnvironment = True
		parameters.intro = True
		parameters.training = False
		parameters.joystick = True
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
		environment.info.setText("Training")
		environment.info.visible(viz.ON)
		yield viztask.waitTime(2)
		environment.info.visible(viz.OFF)
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)
		
		#3d Testing joystick
		parameters.dreiDEnvironment = True
		parameters.intro = False
		parameters.training = False
		parameters.joystick = True
		environment.info.setText("Testing")
		environment.info.visible(viz.ON)
		yield viztask.waitTime(2)
		environment.info.visible(viz.OFF)
		logger.newTrialBlog()
		[variances,accuracys, numberOfTrials] = yield runSetOfTrials()
		statistics.computeTrialBlogStatistics(variances,accuracys, numberOfTrials)

	logger.close_logger()
	environment.info.setText("Experiment finished. Thank You")
	environment.info.visible(viz.ON)
	yield viztask.waitTime(2)
	environment.info.visible(viz.OFF)	

viztask.schedule(experiment)
