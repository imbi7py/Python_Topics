# mynk -- a python library for enhancing a user's experience/workspace
# with the foundry's nuke
#
# @author: Robert Moggach <rob@moggach.com>
#
# fsq/tools.py -- provides functions for easily adding tools into the module
#                  namespace: add_tools_path
#

______ __
______ shutil
______ ___
______ types
______ imp
______ re
______ inspect

______ nuke

____ . ______ constants __ _c
____ . ______ LOG

# checkout https://github.com/dsc/bunch
____ .bunch ______ Bunch

MYNK_TOOLS_PATH _ __.path.j..(_c.DOTNUKE_PATH, 'tools', 'python')

MYNK_MENU_INDEX _ [
  'file',
  'edit',
]


c_ MyNkTools(object):

  @property
  ___  -n
    r_ 'mynk.tools'

  ___  - (, path_list_[]):
    path_list _ path_list
    tools_dict _ {}
    python_Bunch()
    prefix _ inspect.getmodule(). -n
    LOG.i..(' [MyNk] initializing custom user tools')
  
  ___ add_default_path
    __ no. path_list:
      path_list.ap..(MYNK_TOOLS_PATH)

  ___ add_path(, path):
    __ __.path.isdir(path):
      __ no. path __ path_list:
        path_list.ap..(path)

  ___ add_python_tools_from_path_list
    __ path_list:
      ___ path __ path_list:
        add_python_tools_from_path(path)
    ____
      add_default_path()
      add_python_tools_from_path_list()

  ___ add_python_tools_from_path(, path, dest_None):
    '''Recursively add python modules and packages at path
       to dotted python path at prefix'''
    # expand any tilde home directory shortcuts
    path _ __.path.expanduser(path)
    # __ no prefix list defined use the default internal python bunch
    __ dest is N..:
      dest _ python
    # we want a filesystem path so check for that first
    __ __.path.isdir(path):
      LOG.d..(u'Loading tools from path: {0}'.f..(path))
      # add path to system path
      ___.path.ap..(path)
      search_re _ re.compile(".*\.py$", re.IGNORECASE)
      files _ __.listdir(path)
      files.sort()
      ___ file_name __ files:
        # ignore hidden files
        __ no. file_name.startswith('.'):
          file_path _ __.path.j..(path, file_name)
          # __ file matches regex (is python file)
          __ search_re.search(file_name):
            module_name _ __.path.splitext( file_name )[0]
            ___
              module _ imp.load_source(module_name, file_path)
              setattr(dest, module_name, module)
              LOG.d..(u'Loaded Module [{0}]: {1}'.f..(module_name, file_path))
            _____ E.., detail:
              LOG.w..(u'Module [{0}] could not be loaded: {1}\n{2}'.f..(module_name, file_path, detail))
          # __ file is directory (org or package)
          ____ __.path.isdir(file_path):
            path_check _ __.path.j..(file_path, "__init__.py" )
            __ __.path.exists(path_check):
              package_name _ __.path.splitext(file_name)[0]
              ___
                package _ __import__(package_name)
                setattr(dest, package_name, package)
                LOG.d..(debug_msg _ u'Loaded Package [{0}]: {1}'.f..(package_name, file_path))
              _____ E.., detail:
                LOG.w..(u'Package [{0}] could not be loaded from path: {1}\n{2}'.f..(package_name, file_path, detail))
            ____
              dir_name _ __.path.splitext(file_name)[0]
              setattr(dest, dir_name, Bunch())
              new_path _ __.path.j..(path, dir_name)
              add_python_tools_from_path(new_path, eval('dest.{0}'.f..(dir_name)))
  
  ___ list_plugins
    '''
    A debugging function to print out details of the loaded plugins
    '''
    ___ i,j __ tools.__dict__.iteritems():
      __ isinstance( j, types.ModuleType ):
        __ hasattr( j, "version" ):
          LOG.i..( "  ---> Plugin: %s %s %s" % (str(i), str(j), str(j.version) ) )
        ____
          LOG.i..( "  ---> Unversioned Plugin: %s %s " % (str(i), str(j)) )

