_____ ?
_____ __
___ incNamePath(pa__):
    nameExt = __.pa__.b__(pa__)
    name, ext = __.pa__.s__(nameExt)
    dir = __.pa__.dirname(pa__)
    splt = name.split('_')
    nameNum = '01'
    __ le.(splt) > 1:
        num = splt[-1]
        __ num.isdigit
            nameNum = int(num) + 1
            nzero = le.(num)
            __ nzero < 2: nzero = 2
            __ nzero > le.(str(nameNum)):
                nameNum = str(nameNum).zfill(nzero)
            nName = '_'.join(splt[:-1]) + '_' + nameNum
        else:
            nName = '_'.join(splt) + '_' + nameNum
    else:
        nName = name + '_' + str(nameNum)
    result = '/'.join([dir,nName+ext])
    r_ result
    

map( lambda x: x['reload'].execute(), ?.allNodes('Read'))

___ r __ ?.allNodes('Read'):
    f = incNamePath(r['file'].getValue())
    w = ?.nodes.Write(inputs=[r], file=f)
#    w['Render'].execute()
    ?.execute(w, 1, 1)
