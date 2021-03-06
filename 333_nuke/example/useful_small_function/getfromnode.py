'''
Functions to access values from Nuke Nodes
'''

import os
import re
import nuke
import getseq

import dd.xplatform

from dd.runtime.api import relativeImport, load
from dd.runtime import info
load('ddlogger')
import ddlogger
LOGGER = ddlogger.getLogger('getfromnode')

load('nukepipeline')
if info.getVersionToBeLoaded("nukepipeline") >= "3.1.0":
    relativeImport('matchnode', 'nukepipeline/common/utils')
else:
    relativeImport('matchnode', 'common/utils')
from matchnode import byClass


def filePath(node=None, proxy=False, regex=None, force_match=True):
    
    """
    Retrieves the file path of any node that has one associated with it.
    regex can be used to filter only to nodes with file knobs whose
    Class() fits the pattern
    """
    
    result = None

    # check node, use selected Node in dag if no arg
    if not node:
        node = nuke.selectedNode()
        
    # check for regex, eliminate non-matching node
    if regex:
        if not byClass(node, regex, force_match):
            node = None
    
    # check for node elimination
    if node:
        try:
            my_knob = node.knob('file')
            try:
                # attempt to get file knob from linked (gizmos < 5.2v1)
                result = my_knob.getLinkedKnob().getValue()
            except AttributeError:
                # attempt to get file knob value directly (gizmos >= 5.2v1)
                result = my_knob.getValue()
            # end try
        except AttributeError:
            try:
                # grab filename directly from node with nuke.filename
                result = nuke.filename(node)
            except NameError:
                # do nothing if nuke.filename errors out (earlier Nuke version)
                pass
            # end try
        except:
            raise
        # end try
        
        # check if proxy enabled, if so return Proxy knob instead of File
        if proxy:
            if nuke.root().proxy():
                if 'proxy' in node.knobs():
                    try:
                        # attempt to get proxy knob from linked (gizmos < 5.2v1)
                        if node.getLinkedKnob().knob('proxy').value():
                            result = node.getLinkedKnob().knob('proxy').value()
                    except AttributeError:
                        # attempt to get proxy knob value directly (gizmos >= 5.2v
                        if node.knob('proxy').value():
                            result = node.knob('proxy').value()
        # end if

        # check if a TCL expression might exist in the result (ie: containts [{($)}])

        expression_check = re.search('[\[\{\(\]\}\)\$]', str(result))
        # if an expression might exist, attempt to evaluate
        if expression_check:
            # make a copy of the result to process
            eval_result = result

            # create a tmp write node to do the evaluation in
            # if you can figure out a better way to evaluate as Nuke does, be my guest
            tmp = nuke.createNode('Write', inpanel=False)

            try:
                # LOGIC (IF ANY) BEHIND THE FOLLOWING:
                # knob.evaluate() always evaluates fully, so %V is replaced with the
                # full view name, %v is always replaced with the lowercase first
                # letter of the view, and the %d range string (ie %04d, %03d) is
                # always replaced with the then-current frame value.
                # This is not desireable for most uses, but it is still desireable
                # to evaluate any internal TCL expressions before returning the
                # filePath (otherwise you get the lengthy tcl gibberish instead
                # of a meaningful value) ... hence what follows.
                # NOTE: If someone is actually trying to include the View or
                # Range variable characters inside their pre-evaluation expression,
                # we're hosed.

                # we need the %v or %V variable to remain unevaluated
                view_test = re.search('(%[V|v])', eval_result)
                # if it exists, log old value and replace with !VIEW! placeholder
                if view_test:
                    old_view = view_test.groups()[0]
                    eval_result = re.sub(old_view, '!VIEW!', eval_result)

                # we need the %d frame range variable to remain unevaluated
                range_test = re.search('(%[0-9]+d)', eval_result)
                # if it exists, log old value and replace with !RANGE! placeholder
                if range_test:
                    old_range = range_test.groups()[0]
                    eval_result = re.sub(old_range, '!RANGE!', eval_result)

                # let nuke do the actual evaluation work
                tmp.knob('file').setValue(eval_result)
                eval_result = tmp.knob('file').evaluate()

                # put the stored range variable back
                if range_test:
                    eval_result = re.sub('!RANGE!', old_range, eval_result)

                # put the stored view variable back
                if view_test:
                    eval_result = re.sub('!VIEW!', old_view, eval_result)

                # evaluation succeeded
                result = eval_result
            except:
                # evaluation failed, leave result alone and let the gods sort it out
                pass
            finally:
                # one way or another, clean up the tmp node
                nuke.delete(tmp)

    if result != None:
        result = dd.xplatform.xpath(os.path.normpath(result))
        LOGGER.debug('Discovered path %s for node %s' % (
            result, node.knob('name').value()))
        return result
    else:
        LOGGER.debug('Discovered no path for node %s' % node.knob('name').value())
        return None
# end filePath
   

def filePathWithRange(node=None, proxy=False, regex=None, force_match=True):
    
    """
    Retrieves the file path of any node that has one associated with it.
    regex can be used to filter only to nodes with file knobs whose
    Class() fits the pattern.
    """
    
    result = None

    # check node, use selected Node in DAG if no arg
    if not node:
        node = nuke.selectedNode()

    # check node again (in case user has no selection made)
    # get file path from node
    if node:
        path = filePath(node, proxy, regex, force_match)
        # if file path found, append frame range data
        # use getseq instad of root range
        # makes more sense eh? #61881 / #64178
        if path:
            first_frame, last_frame = getseq.getRange(path)
            LOGGER.debug('Discovered range of %s-%s' % (first_frame, last_frame))
            result = '%s %s-%s' % (path, first_frame, last_frame)

    # return the path and range discovered
    return result
#  end filePathWithRange


def filePaths(nodes=None, proxy=False, regex=None, force_match=True):
    
    """
    Returns a list of the file paths (if any) associated with the nodes in the
    nodes.  Filter using regex to restrict the results to 
    nodes whose Class() matches the pattern.
    """
    
    result = []

    # check nodes, use selected Nodes in DAG if no arg
    if not nodes:
        nodes = nuke.selectedNodes()

    # loop through nodes and get path for each Node
    for i in nodes:
        try:
            result.append(filePath(i, proxy, regex, force_match))
        except AttributeError:
            pass
    
    return result
# end filePaths


def filePathsWithRanges(nodes=None, proxy=False, regex=None, force_match=True):
    
    """
    Returns a list of the file paths (if any) associated with the nodes in the
    nodes.  Filter using regex to restrict the results to 
    nodes whose Class() matches the pattern.
    """
    
    result = []

    # check nodes, use selected Nodes in DAG if no arg
    if not nodes:
        nodes = nuke.selectedNodes()

    # loop through nodes and get path and range for each Node
    for i in nodes:
        try:
            range = filePathWithRange(i, proxy, regex, force_match)
            if range:
                result.append(range)
        except AttributeError:
            pass
    
    return result
# end filePaths

def fileType(node):
    """
    Returns the file extension of the node given
    """
    result = os.path.splitext(filePath(node))[1].lstrip('.')
    LOGGER.debug('Filetype for node %s is %s' % (node.knob('name').value(), result))
    return result
# end fileType

def format(node):
    
    """
    Returns the format of the specified Node, if in the nuke.formats() list
    """
    
    my_format = None
    
    # check for node; default to selected Node in DAG if no arg
    if not node:
        node = nuke.selectedNode()
    # endif

    # check for Node again (see if user has failed to make selection)
    if node:
        # grab height from node
        my_height = node.height()
        
        # grab width from node
        my_width = node.width()
        
        # grab pixel aspect ratio from node as float
        my_pixel_aspect = float(nuke.value('%s.pixel_aspect' % node.fullName()))
        
        # this is the format to search for
        my_format = (my_height, my_width, my_pixel_aspect)
        
        # scan nuke.formats for matching format
        for i in nuke.formats():
            thisFormat = (i.height(), i.width(), i.pixelAspect())
            # if matching format found, assign my_format to the match
            if thisFormat == my_format:
                my_format = i
                break
                
    # return whatever is the current value of my_format
    LOGGER.debug('Format for node %s is %s' % (node.knob('name').value(), my_format))
    return my_format
# end format


# end getfromnode
