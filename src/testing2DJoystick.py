import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape
import random
import parameters

def testing2DJoystick():

	results = []
	trials = [3,2,0,4,1]


#	for i in trials:
#
#		#Check to see if participant is already in room center. If not
#		#wait until the centerSensor is activated
#		if centerSensor not in manager.getActiveSensors():
#			yield vizproximity.waitEnter(centerSensor)
#
#		#Get sensor for this trial
#		sensor = sphereSensors[i]
#
#		#Instruct participant where to go
#		instruction = 'Walk to the {} sphere'.format(sensor.name)
#		info.setText(instruction)
#
#		#store the time at which this trial started
#		startTime = viz.tick()
#
#		#The yielded command returns a viz.Data object with information
#		#about the proximity event such as the sensor, target involved
#		yield vizproximity.waitEnter(sensor)
#		info.setText('Please return to the center of the room')
#
#		#calculate the time it took for the subject to find the correct object
#		elapsedTime = viz.tick() - startTime
#
#		#save results
#		results.append((sensor.name, elapsedTime))
#
#	info.setText('Thank You. You have completed the experiment')

	#return results
	viztask.returnValue(results)