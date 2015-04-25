import viz
import viztask
import vizact
import vizinfo
import vizproximity
import vizshape


def getParticipantInfo():

	#Add an InfoPanel with a title bar
	participantInfo = vizinfo.InfoPanel('',title='Participant Information',align=viz.ALIGN_CENTER, icon=False)

	#Add name and ID fields
	textbox_last = participantInfo.addLabelItem('Last Name',viz.addTextbox())
	textbox_first = participantInfo.addLabelItem('First Name',viz.addTextbox())
	textbox_id = participantInfo.addLabelItem('ID',viz.addTextbox())
	participantInfo.addSeparator(padding=(20,20))

	#Add gender and age fields
	radiobutton_male = participantInfo.addLabelItem('Male',viz.addRadioButton(0))
	radiobutton_female = participantInfo.addLabelItem('Female',viz.addRadioButton(0))
	droplist_age = participantInfo.addLabelItem('Age Group',viz.addDropList())
	ageList = ['20-30','31-40','41-50','51-60','61-70']
	droplist_age.addItems(ageList)
	participantInfo.addSeparator(padding=(20,20))
	
	#Add 2d 3D fields
	radiobutton_2D = participantInfo.addLabelItem('2D',viz.addRadioButton(1))
	radiobutton_3D = participantInfo.addLabelItem('3D',viz.addRadioButton(1))
	participantInfo.addSeparator(padding=(20,20))

	#Add submit button aligned to the right and wait until it's pressed
	submitButton = participantInfo.addItem(viz.addButtonLabel('Submit'),align=viz.ALIGN_RIGHT_CENTER)
	yield viztask.waitButtonUp(submitButton)

	#Collect participant data
	data = viz.Data()
	data.lastName = textbox_last.get()
	data.firstName = textbox_first.get()
	data.id = textbox_id.get()
	data.ageGroup = ageList[droplist_age.getSelection()]

	if radiobutton_male.get() == viz.DOWN:
		 data.gender = 'male'
	else:
		 data.gender = 'female'
		 
	if radiobutton_2D.get() == viz.DOWN:
		 data.environment = '2D'
	else:
		 data.environment = '3D'

	participantInfo.remove()

	# Return participant data
	viztask.returnValue(data)
