# mynk -- a python library for enhancing a user's experience/workspace
# with the foundry's nuke
#
# @author: Robert Moggach <rob@moggach.com>
#
# mynk/gui.py -- provides functions for building mynk toolbar and menu: init_gui, add_toolbar, add_menu
#
# SHORT CUT SYNTAX
# 'Ctrl-s'    "^s"
# 'Ctrl-Shift-s'  "^+s"
# 'Alt-Shift-s'   "#+s"
# 'Shift+F4'    "+F4"
#
# convert camel case to titles re.sub("([a-z])([A-Z])","\g<1> \g<2>", key).title()

______ re
______ os
______ shutil
from types ______ ModuleType
______ inspect

______ nuke

from . ______ constants as _c
from . ______ LOG
from . ______ config

______ mynk

c_ MyNkGui(object):
  ___  -
    nuke.pluginAddPath(os.path.join(_c.MYNK_PATH, 'icons'), addToSysPath_False)
    LOG.i..(' [MyNk] initializing custom user menus etc.')

  ___ add_tool_menus(self, tool_str):
    ___
      tool _ eval(tool_str)
      menus _ getattr(tool, '__menus__' ,None)
    except AttributeError:
      LOG.warning(' [MyNk] tool has no __menus__ attribute: {0}'.format(tool_str))
    else:
      __ menus is None:
        r_
      else:
        for key,val __ menus.iteritems():
          title _ key
          __ val:
            cmd _ val['cmd'] __ val['cmd'].startswith('nuke') else '{0}.{1}'.format(tool_str, val['cmd'])
            hotkey _ val['hotkey']
            icon _ val['icon']
            for menu __ [menu,nuke_toolbar]:
              menu.addCommand(title,cmd,hotkey,icon)
          else:
            menu.addMenu(title)
            
  ___ add_toolbunch_to_menu(self, toolbunch_str):
    for key,val __ eval(toolbunch_str).toDict().iteritems():
      dottedpath _ '{0}.{1}'.format(toolbunch_str,key)
      __ inspect.ismodule(val):
        add_tool_menus(dottedpath)
      else:
        add_toolbunch_to_menu(dottedpath)

  ___ init_gui
    nuke_menu _ nuke.menu('Nuke')
    menu _ nuke_menu.addMenu('MyNk', icon_'mynk.png')
    nuke_toolbar _ nuke.menu("Nodes")
    nuke_toolbar _ nuke_toolbar.addMenu("MyNk", "mynkx.png")

  ___ add_entry_to_toolbar(self, entry):
    pass

  ___ add_entry_to_menu(self, entry):
    pass

  ___ add_entry_list(self, entry_list):
   for entry __ entry_list:
     pass
 
  ___ setFavorites
    nuke.removeFavoriteDir('Nuke')
    nuke.addFavoriteDir('DotNuke', os.path.expanduser('~/.nuke'), 0)
    nuke.addFavoriteDir('Jobs', '/', 0)
    nuke.addFavoriteDir('Fonts', '/', nuke.FONT)
  
  ___ restoreWindowLayout(self, layout_1):
    nuke.restoreWindowLayout(layout)

