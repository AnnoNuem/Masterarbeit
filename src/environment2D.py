import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape

#physics stuff
viz.phys.enable()
viz.phys.setGravity([0,0,0]) 

# point
point = vizshape.addCircle(radius = 0.5, slices=100)
pointPhys = point.collideSphere()   # Define ball's physical properties 
thrust = point.addThruster(force=[0,0,0]) 

#goal
goal = vizshape.addCircle(slices=100, radius=2)

#arrow
arrow = vizshape.addArrow()


viz.mouse(viz.OFF)

# Load DirectInput plug-in
dinput = viz.add('DirectInput.dle')

# Add first available joystick
joy = dinput.addJoystick()

# Set dead zone threshold so small movements of joystick are ignored
joy.setDeadZone(0.2)

def create2DEnvironment():	
	#ground = viz.add('tut_ground.wrl')  # Add ground
	#ground.collidePlane()   # Make collideable plane
		
	viz.clearcolor(viz.WHITE)
	
	#look from above
	viz.MainView.setPosition([0,50,0])
	viz.MainView.setEuler([0,90,0])
	
	goal.setEuler(0,90,0)
	goal.color(viz.GREEN)
	
	point.setEuler(0,90,0)
	point.setPosition(0,20,0)
	point.color(viz.RED)	
	
	arrow.setPosition(0,20,0)
	arrow.color(viz.BLUE)




#	#Create proximity manager and set debug on. Toggle debug with d key
#	manager = vizproximity.Manager()
#	manager.setDebug(viz.ON)
#	debugEventHandle = vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)
#
#	#Add main viewpoint as proximity target
#	target = vizproximity.Target(viz.MainView)
#	manager.addTarget(target)
#
#	#fade to true color when viewpoint moves near
#	def EnterSphere(e, sphere, color):
#		sphere.runAction(vizact.fadeTo(color,time=1))
#
#	#fade to white when viewpoint moves away
#	def ExitSphere(e, sphere):
#		sphere.runAction(vizact.fadeTo(viz.WHITE,time=1))
#
#	#add spheres and create a proximity sensor around each one
#	sphereSensors = []
#	def AddSphere(name, color, position):
#
#		sphere = vizshape.addSphere(radius=0.2)
#		sphere.setPosition(position)
#
#		sensor = vizproximity.addBoundingSphereSensor(sphere,scale=5)
#		sensor.name = name
#		sphereSensors.append(sensor)
#		manager.addSensor(sensor)
#
#		manager.onEnter(sensor, EnterSphere, sphere, color)
#		manager.onExit(sensor, ExitSphere, sphere)
#
#	AddSphere('red', viz.RED, [0,1.8,4])
#	AddSphere('blue', viz.BLUE, [3.5,1.8,2])
#	AddSphere('yellow', viz.YELLOW, [3.5,1.8,-2])
#	AddSphere('green', viz.GREEN, [0,1.8,-4])
#	AddSphere('purple', viz.PURPLE, [-3.5,1.8,-2])
#	AddSphere('gray', viz.GRAY, [-3.5,1.8,2])
#
#	#Add a sensor in the center of the room for the participant to return to after each trial
#	centerSensor = vizproximity.Sensor(vizproximity.CircleArea(1.5,center=(0.0,0.0)),None)
#	manager.addSensor(centerSensor)