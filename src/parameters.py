
demo = True

if demo:
	numberOfIntroTrials = 2
	numberOfTrainingTrials = 2
	numberOfTestTrials = 2
else:
	numberOfIntroTrials = 10
	numberOfTrainingTrials = 20
	numberOfTestTrials = 5


participantData = -1
filename = -1
#trial number. all trials are numerated from the beginning on.
trialNumber = 1

gravity = -0.05

# true if traing, false if testing
training = False

# true for introduction trails else false
intro = False

# true for 3d environment false for 2d environment
dreiDEnvironment = False

# true for joystick false for tracking
joystick = False

# object parameters
point_height = 1
pointRadius = 0.2
arrow_height2D = 1.3
arrow_height3D = 0.3
arrow_size = 10;
arroa_min_size = 0.5;
goal_height = 0.01
goal_scale2D = 2
goal_scale3D = 1
shadow_scale3D =  0.3
shadow_height = 0.02

# goal positions
radialCoordinateTesting = 1
radialCoordinateTraining = 2
#goal positions for training and intro. set in main
radialCoordinate = -1
angularCoordinate1 = -1
angularCoordinate2 = -1
angularCoordinate3 = -1
angularCoordinate4 = -1


# joystick speed
joySpeed = 2;

#fieldsize
fieldsizeX = 2.5
fieldsizeZ = 2.5

#flavour
#defines how much the goals in testing are rotated arround origin
# 1 = 0degree standard
# 2 = 15deg
# 3 = 30deg
# 4 = 45deg
flavour = 1

#wind parameters. set in main
xscale = 0.0
zscale = 0.01
xbias = 0.00
zbias = 0.005


