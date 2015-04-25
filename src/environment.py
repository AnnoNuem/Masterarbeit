import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape
import projector

import parameters

#physics stuff
viz.phys.enable()
viz.phys.setGravity([0,0,0]) 
viz.gravity(0)



info = vizinfo.InfoPanel("")

point = -1
arrow = -1
goal = -1
thrust = -1
shadow = -1


# Load DirectInput plug-in
dinput = viz.add('DirectInput.dle')

# Add first available joystick
joy = dinput.addJoystick()

# Set dead zone threshold so small movements of joystick are ignored
joy.setDeadZone(0.2)

def createEnvironment():	
	global point 
	global arrow 
	global goal	 
	global thrust
	global shadow

	#create 3D environment
	if parameters.dreiDEnvironment:

		piazza = viz.addChild('piazza.osgb')
	
		#look from above
		viz.MainView.setPosition([0,1.8,-5])
		viz.MainView.setEuler([0,20,0])
		viz.collision(viz.ON)
		# gorund for collision
		ground = viz.add('tut_ground.wrl')  # Add ground
		ground.collidePlane()   # Make collideable plane 
		ground.disable(viz.RENDERING)
		ground.disable(viz.DEPTH_WRITE)
		
		# point
		point = viz.add('ball.wrl')
		pointPhys = point.collideSphere()   # Define ball's physical properties 
	
		point.setEuler(0,90,0)
		point.setPosition(0,parameters.point_height,0)
		point.color(viz.RED)
		point.setScale(0.5,0.5,0.5)
		point.enable( viz.COLLIDE_NOTIFY )
		
		#goal
		goal = vizshape.addCircle(slices=100, radius=0.3)		
		goal.setEuler(0,90,0)
		goal.color(viz.GREEN)		
		goal.setPosition(0,parameters.goal_height,0)
		goal.setScale(parameters.goal_scale3D,parameters.goal_scale3D,parameters.goal_scale3D)
		
		#shadow
		shadow = vizshape.addCircle(slices=100, radius=0.3)		
		shadow.setEuler(0,90,0)
		shadow.color(viz.GRAY)		
		shadow.setPosition(0,parameters.shadow_height,0)
		shadow.setScale(parameters.shadow_scale3D,parameters.shadow_scale3D,parameters.shadow_scale3D)

		#arrow
		arrow = vizshape.addArrow()	
		arrow.setPosition(0,parameters.arrow_height3D,0)
		arrow.color(viz.BLUE)
		
		#thrust
		thrust = point.addThruster(force=[0,0,0]) 

	#or create 2d environment
	else:
		viz.clearcolor(viz.WHITE)

		#look from above
		viz.MainView.setPosition([0,8,0])
		viz.MainView.setEuler([0,90,0])
		
		point = viz.add('ball.wrl')
		pointPhys = point.collideSphere()   # Define ball's physical properties 
		thrust = point.addThruster(force=[0,0,0]) 
		#goal
		goal = vizshape.addCircle(slices=100, radius=0.2)
		#arrow
		arrow = vizshape.addArrow()
		viz.mouse(viz.OFF)
		
		goal.setEuler(0,90,0)
		goal.color(viz.GREEN)
		goal.visible(False)
		goal.setScale(parameters.goal_scale2D,parameters.goal_scale2D,parameters.goal_scale2D)
		
		point.setEuler(0,90,0)
		point.setPosition(0,parameters.point_height,0)
		point.color(viz.RED)	
		point.visible(False)
		point.enable( viz.COLLIDE_NOTIFY )
		
		arrow.setPosition(0,parameters.arrow_height2D,0)
		arrow.color(viz.BLUE)
		arrow.visible(False)