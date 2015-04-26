
demo = True

if demo:
	numberOfTrainingTrials = 2
	numberOfTestTrials = 2
	numberOfIntroTrials = 2
else:
	numberOfTrainingTrials = 1
	numberOfTestTrials = 1
	numberOfIntroTrials = 1




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
#goal positions for training
position0Xtrain = 2
position0Ztrain = -2
position1Xtrain = 2
position1Ztrain = 2
position2Xtrain = -2
position2Ztrain = 2
position3Xtrain = -2
position3Ztrain = -2

#goal positions for training
position0Xtest = 1
position0Ztest = 0
position1Xtest = -1
position1Ztest = 0
position2Xtest = 0
position2Ztest = 1
position3Xtest = 0
position3Ztest = -1

# joystick speed
joySpeed = 2;

#fieldsize
fieldsizeX = 2.5
fieldsizeZ = 2.5

