import parameters
import time

def open_logger():
	try:
		parameters.filename = parameters.participantData.id + '_experiment_aschaffland.txt'
		with open(parameters.filename ,'w') as f:
			#write participant data to file
			data = "Participant ID: {p.id}\nLast Name: {p.lastName}\nFirst Name: {p.firstName}\nGender: {p.gender}\nAge: {p.ageGroup}\nEnvironment: {p.environment}\n\n".format(p=parameters.participantData)
			data += '\nExperiment start: ' + time.strftime('%X')
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
	write_logger('\nExperiment end' + time.strftime('%X'))