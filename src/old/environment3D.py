import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape

#physics stuff
viz.phys.enable()
viz.phys.setGravity([0,0,0]) 
viz.gravity(0)

# point
point = viz.add('ball.wrl')
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

def create3DEnvironment():	
	#ground = viz.add('tut_ground.wrl')  # Add ground
	#ground.collidePlane()   # Make collideable plane
		
	#viz.clearcolor(viz.WHITE)
	piazza = viz.addChild('piazza.osgb')
	
	#look from above
	viz.MainView.setPosition([0,1.8,0])
	#viz.MainView.setEuler([0,90,0])
	
	goal.setEuler(0,90,0)
	goal.color(viz.GREEN)
	
	point.setEuler(0,90,0)
	point.setPosition(0,20,0)
	point.color(viz.RED)	
	
	arrow.setPosition(0,20,0)
	arrow.color(viz.BLUE)




