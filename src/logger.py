import parameters
import time

def open_logger():
	try:
		parameters.filename = parameters.participantData.id + '_experiment_aschaffland.txt'
		with open(parameters.filename ,'w') as f:
			#write participant data to file
			data = "Participant ID: {p.id}\nLast Name: {p.lastName}\nFirst Name: {p.firstName}\nGender: {p.gender}\nAge: {p.ageGroup}\nEnvironment: {p.environment}\n\n".format(p=parameters.participantData)
			data += "\nNumber of Init Trials: {p.numberOfIntroTrials} \nNumber of Training Trials: {p.numberOfTrainingTrials} \nNumber of Test Trials: {p.numberOfTestTrials} \nExperiment start: ".format(p=parameters) + time.strftime('%X')
			f.write(data)
	except IOError:
		viz.logWarn('Could not log results to file. Make sure you have permission to write to folder')

def write_logger(data):
	try:
		with open(parameters.filename ,'a') as f:
			f.write(str(data))
	except IOError:
		viz.logWarn('Could not log results to file. Make sure you have permission to write to folder')
		
def close_logger():
	write_logger('\nExperiment end: ' + time.strftime('%X'))
	
def newTrialBlog():
	write_logger('\n\n###New Block of trials: 3D=' + str(parameters.dreiDEnvironment) + ', Intro=' + str(parameters.intro) + ', training=' + str(parameters.training) + ', joystick=' + str(parameters.joystick))
	
def newTrial():
	write_logger('\n##New Trial. Number=' + str(parameters.trialNumber))