"""Defines viewer utility functions.
"""

______ math
______ ?
______ itertools


___ toggle_viewer_lut
    """Iterates thru viewer luts in the viewer"""
    viewer _ ?.aV...node()['viewerProcess']
    luts _ viewer.values()
    x _ itertools.cycle(luts)
    ___ dummy __ ra..(le.(luts)):
        __ viewer.v.. __ next(x):
            viewer.sV..(next(x))


___ adjust_gain(original_gain, stop_offset):
    """Does the math for stop adjustments"""
    r_ 2 ** (math.log(original_gain, 2.0) + stop_offset)


___ viewer_stop_adjust(increment):
    """Adjusts current viewer in stops"""
    n__ _ ?.aN..('Viewer')
    ___ node __ no__:
        knob _ node.knob('gain')
        gain _ knob.v..
        knob.sV..(adjust_gain(gain, increment))


___ viewer_stop_up
    """Adjusts current viewer 1/4 stop up"""
    viewer_stop_adjust(0.25)


___ viewer_stop_down
    """Adjusts current viewer 1/4 stop down"""
    viewer_stop_adjust(-0.25)


___ viewer_stop_reset
    """Resets exposure on current viewer"""
    n__ _ ?.aN..('Viewer')
    ___ node __ no__:
        knob _ node.knob('gain')
        knob.sV..(1)
