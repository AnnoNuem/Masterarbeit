import viz


#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

#Increase the Field of View
viz.MainWindow.fov(60)

#viz.MainView.move([3,0,-7])
viz.MainView.setPosition([0,20,0])
viz.MainView.setEuler([0,90,0])

piazza = viz.addChild('piazza.osgb')
#viz.collision(viz.ON)
import vizshape
vizshape.addAxes()


plant = viz.addChild('plant.osgb')
plant.setPosition([4, 0, 6])