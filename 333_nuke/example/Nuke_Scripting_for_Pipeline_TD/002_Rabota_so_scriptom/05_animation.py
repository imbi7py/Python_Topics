import nuke
#read animation 
t = nuke.selectedNode()
k = t['scale']
a = k.animations()
a = k.animation(0)
keys = a.keys()
keys[1].x
keys[1].y
a.setKey(10, 10)
# create animation
import math
r = t['rotate']
#variant 1
r.clearAnimated()
r.setAnimated()
for i in range(300):
    r.setValueAt(math.sin(i*0.07)*50, i, 0)
#vriant 2
r.clearAnimated()
r.setAnimated()
c = r.animation(0)
c.addKey( [nuke.AnimationKey(i, math.sin(i*0.07)*50) for i in range(300)] )

#change one frame
c = r.animation(0)
key = c.keys()[21]

key.y = 50
r.setValueAt(40, 21,0)





