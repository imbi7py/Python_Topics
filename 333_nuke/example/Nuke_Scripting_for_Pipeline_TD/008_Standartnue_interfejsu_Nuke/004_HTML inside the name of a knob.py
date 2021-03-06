import os
node = nuke.selectedNode()

node['icon'].setValue('C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/004_Pipeline/icons/cgninjas.png')
k = nuke.Text_Knob('tutor', 'Tutorial')
node.addKnob(k)
node["tutor"].setLabel('<h4><a style="color:lightgray;" href="http://cgninjas.ru">CGNINJAS<a></h4>')

#######################
h = nuke.Double_Knob('sue', '')
h.setLabel('<h2>H </h2><img src="%s/icons/hue.png">' % os.environ['NUKE_PATH'].replace('\\','/'))
node.addKnob(h)

s = nuke.Double_Knob('sat', '')
s.setLabel('<h2>S </h2><img src="%s/icons/saturation.png">' % os.environ['NUKE_PATH'].replace('\\','/'))
node.addKnob(s)

v = nuke.Double_Knob('val', '')
v.setLabel('<h2>V </h2><img src="%s/icons/lightness.png">' % os.environ['NUKE_PATH'].replace('\\','/'))
node.addKnob(v)


#######################
node.addKnob(nuke.Text_Knob('',''))
#######################

###### node icon
node['icon'].setValue('C:/pipeline/icons/cgninjas_node.png')

###### Label HTML
# link

k = nuke.Text_Knob('tutor', 'Tutorial')
node.addKnob(k)
k.setLabel('<h4><a style="color:lightgray;" href="http://cgninjas.ru">CGNINJAS<a></h4>')

###########################
# image label

h = nuke.Double_Knob('sue', '')
h.setLabel('<h2>H </h2><img src="%s/icons/h.png">' % os.environ['NUKE_PATH'].replace('\\','/'))
node.addKnob(h)

s = nuke.Double_Knob('sat', '')
s.setLabel('<h2>S </h2><img src="%s/icons/s.png">' % os.environ['NUKE_PATH'].replace('\\','/'))
node.addKnob(s)

v = nuke.Double_Knob('val', '')
v.setLabel('<h2>V </h2><img src="%s/icons/v.png">' % os.environ['NUKE_PATH'].replace('\\','/'))
node.addKnob(v)

########################
node.addKnob(nuke.Text_Knob('',''))
##########################

# interactive label

power = nuke.Double_Knob('power', 'Power')
node.addKnob(power)

def powerKnob(a):
    k = nuke.thisKnob()
    if k.name() == 'power' and a=='Blur':
        v = k.getValue()
        img = int((v*5)+1)
        k.setLabel('<img src="%s/icons/power%s.png">' % (os.environ['NUKE_PATH'].replace('\\','/'), img))

nuke.addKnobChanged(powerKnob, 'Blur')
nuke.removeKnobChanged(powerKnob, 'Blur')

########################################################################################################################

set cut_paste_input [stack 0]
version 10.0 v4
push $cut_paste_input
Blur {
 channels rgba
 name Blur1
 label "---------------\n\[value size]"
 selected true
 xpos 219
 ypos -135
 icon "C:/Users/serge/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/004_Pipeline/icons/cgninjas.png"
 addUserKnob {20 User}
 addUserKnob {26 tutor l "<h4><a style=\"color:lightgray;\" href=\"http://cgninjas.ru\">CGNINJAS<a></h4>"}
 addUserKnob {7 hue l "<h2>H </h2><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/hue.png\">"}
 addUserKnob {7 sat l "<h2>S </h2><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/saturation.png\">"}
 addUserKnob {7 val l "<h2>V </h2><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/lightness.png\">"}
 addUserKnob {26 "" +STARTLINE}
 addUserKnob {7 power l "<h3>POWER</h3><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/power/power6.png\">"}
 power 1
}
