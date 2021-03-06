______ ?
______ n_s_

___ newUserKnob(knob, v.. ):
    knob.sV..(v.. )
    r_ knob

___ allReads
    readNodes _ # list
    ___ i __ ?.aN..
        __ i.C..  __ 'Read':
            readNodes.ap..(i)
    r_ readNodes

___ selectRead
    ___ i __ allReads
        i.knob('selected').sV..('True')

___ setLocalize
    p..

___ setFrameRange
    f _ n_s_.PP..('Set read nodes frame range')
    f.nodesSelection _ ?.E_K..('nodesSel', 'Nodes selections', ['All read nodes', 'Selected nodes only', 'Exclude selected nodes'])
    f.divText _ ?.T_K..('divText', '')
    f.firstFrame _ newUserKnob(?.I_K..('first_frame', 'frame range', 1), __.(?.r.. .firstFrame()))
    f.before _ ?.E_K..('before', '', ['hold', 'loop', 'bounce', 'black'])
    f.lastFrame _ newUserKnob(?.I_K..('last_frame', '', 100), __.(?.r.. .lastFrame()))
    f.after _ ?.E_K..('after', '', ['hold', 'loop', 'bounce', 'black'])

    #Set nodes selection and after as end line
    ___ s __ (f.nodesSelection, f.after):
        s.sF..(0x2000)
    ___ k __ (f.nodesSelection, f.divText, f.firstFrame, f.before, f.lastFrame, f.after):
        f.aK..(k)

    #show dialog
    __ f.sMD..:
        __ f.nodesSelection.v.. __ 'All read nodes':
            Sel _ allReads()
        ____ f.nodesSelection.v.. __ 'Selected nodes only':
            Sel _ ?.sN..
        ____
            Sel _ allReads()
            ___ i __ ?.sN..:
                ___
                    Sel.r__(i)
                ______ ValueError:
                    p..

        ___ r __ Sel:
            ___
                r['first'].sV..(f.firstFrame.v.. ())
                r['before'].sV..(f.before.v.. ())
                r['last'].sV..(f.lastFrame.v.. ())
                r['after'].sV..(f.after.v.. ())
            ______ ValueError:
                ?.m..('No nodes selected!')
            ______ NameError:
                p..

___ setError
    e _ n_s_.PP..('Missing frames setting')
    e.nodesSelection _ ?.E_K..('nodesSel', 'Nodes selections', ['All read nodes', 'Selected nodes only', 'Exclude selected nodes'])
    e.divText _ ?.T_K..('divText', '')
    e.onError _ ?.E_K..('onError', 'missing frames', ['error', 'black', 'checkerboard', 'nearest frame'])
    e.reload _ newUserKnob(?.B_K..('reload', 'Reload changed nodes', '0'), 0)
    ___ k __ (e.nodesSelection, e.divText, e.onError, e.reload):
        k.sF..(0x1000)
        e.aK..(k)

    #show dialog
    __ e.sMD..:
        __ e.nodesSelection.v.. __ 'All read nodes':
            Sel _ allReads()
        ____ e.nodesSelection.v.. __ 'Selected nodes only':
            Sel _ ?.sN..
        ____
            Sel _ allReads()
            ___ i __ ?.sN..:
                ___
                    Sel.r__(i)
                ______ ValueError:
                    ?.m..('No nodes selected!')
                ______ NameError:
                    p..

        ___ r __ Sel:
            ___
                r['on_error'].sV..(__.(e.onError.gV..()))
                __ e.reload.v..:
                    r.knob('reload').execute()
            ______ ValueError:
                ?.m..('No nodes selected!')
            ______ NameError:
                p..


