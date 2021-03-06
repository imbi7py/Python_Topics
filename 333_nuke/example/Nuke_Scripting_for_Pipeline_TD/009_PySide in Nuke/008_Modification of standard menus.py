# linearAnim

import nuke

n = nuke.selectedNode()
k = n['translate']
k.setAnimated()
for i in range(100):
    k.setValueAt( i, i )

# change to function doit

def doit():
    k = nuke.thisKnob()
    if k.arraySize() > 1:
        index = getKnobIndex()
    else:
        index = 0
    k.setAnimated()
    for i in range(100):
        k.setValueAt( i, i, index)

# shtobu polychit' index knoba, kotoruj nahoditsja v kontexte, dostatochno vuzvat' ety fynkcijy
# no vuzuvat' ejo sledyet tol'ko dlja knobov gde kanalov bol'she odnogo

def getKnobIndex():

    tclGetAnimIndex = """

 set thisanimation [animations]
 if {[llength $thisanimation] > 1} {
  return "-1"
  } else {
   return [lsearch [in [join [lrange [split [in $thisanimation {animations}] .] 0 end-1] .] {animations}] $thisanimation]
  }
 """

    return int(nuke.tcl(tclGetAnimIndex))