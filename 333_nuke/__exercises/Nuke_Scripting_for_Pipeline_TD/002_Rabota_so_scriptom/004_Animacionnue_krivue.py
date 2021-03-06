import nuke, math


t = nuke.toNode('Transform1')
t['translate'].animations()
t['translate'].animation(0)
t['translate'].animation(1)

crv = t['translate'].animation(0)
crv.keys()
keys = crv.keys()
keys[0].x
keys[0].y
keys[0].y = -300

crv.setKey(10, -310)

crv.setKey(50, 301)

t['translate'].setAnimated()
t['translate'].setAnimated(1)
t['translate'].animation(1)

k = t['translate']

for i in range(1, 0, 200):
    k.setValueAt(math.sin(i*0.05)*50, i, 1)

c = k.animation(1)
c.clear()
c.addKey([nuke.AnimationKey(x, math.sin(x*0.02)*70) for x in range(10, 200)])