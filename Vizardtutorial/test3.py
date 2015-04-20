import viz
import vizact

#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.setMultiSample(4)

viz.go()

#Increase the Field of View
viz.MainWindow.fov(60)

viz.move([0,0,-8])

piazza = viz.addChild('piazza.osgb')

plants = []
for x in [-3, -1, 1, 3]:
    for z in [4, 2, 0, -2, -4]:
        plant = viz.addChild('plant.osgb',cache=viz.CACHE_CLONE)
        plant.setPosition([x,0,z])
        plants.append(plant)

spin = vizact.spin(0,1,0,15)

spinPlant = lambda plant: plant.addAction(spin)
vizact.ontimer2(0.5,19,spinPlant,vizact.choice(plants))