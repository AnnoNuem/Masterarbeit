import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape

viz.res.addPath(r'C:\Users\axel\Desktop\Masterarbeit\resources')

#own imports
from participantInfo import getParticipantInfo
from joystick2D import training2DJoystick
from joystick2D import testing2DJoystick
from environment2D import create2DEnvironment
from environment3D import create3DEnvironment
from joystick3D import training3DJoystick
from joystick3D import testing3DJoystick
from environment3D import create3DEnvironment

#vizard adjustments
viz.setMultiSample(4)
viz.fov(60)
viz.go()

def experiment():

	#Proceed through experiment phases
	
	participant = yield getParticipantInfo()
	if participant.environment=='2D':
		create2DEnvironment()
		yield training2DJoystick()
		results = yield testing2DJoystick()
	elif participant.environment=='3D':
		create3DEnvironment()
		yield training3DJoystick()
		results = yield testing3DJoystick()

	create2DEnvironment()
	yield training2DJoystick()
	results = yield testing2DJoystick()
		
		
	#Log results to file
	try:
		with open(participant.id + '_experiment_data.txt','w') as f:

			#write participant data to file
			data = "Participant ID: {p.id}\nLast Name: {p.lastName}\nFirst Name: {p.firstName}\nGender: {p.gender}\nAge: {p.ageGroup}\nEnvironment: {p.environment}\n\n".format(p=participant)
			f.write(data)

			#write result of each trial
			for name,time in results:
				data = "The {} trial took {:.2f} seconds\n".format(name,time)
				f.write(data)
	except IOError:
		viz.logWarn('Could not log results to file. Make sure you have permission to write to folder')

viztask.schedule(experiment)
