"""
################################################################################
Usage: "python cpall.py dirFrom dirTo".
Recursive copy of a directory tree.  Works like a "cp -r dirFrom/* dirTo"
Unix command, and assumes that dirFrom and dirTo are both directories.
Was written to get around fatal error messages under Windows drag-and-drop
copies (the first bad file ends the entire copy operation immediately),
but also allows for coding more customized copy operations in Python.
################################################################################
"""

______ __, ___
maxfileload _ 1000000
blksize _ 1024 * 500

___ copyfile(pathFrom, pathTo, maxfileload_maxfileload):
    """
    Copy one file pathFrom to pathTo, byte for byte;
    uses binary file modes to supress Unicde decode and endline transform
    """
    __ __.p...getsize(pathFrom) <_ maxfileload:
        bytesFrom _ o..(pathFrom, 'rb').r..   # read small file all at once
        o..(pathTo, 'wb').w..(bytesFrom)
    ____
        fileFrom _ o..(pathFrom, 'rb')           # read big files in chunks
        fileTo   _ o..(pathTo,   'wb')           # need b mode for both
        w__ True:
            bytesFrom _ fileFrom.read(blksize)    # get one block, less at end
            __ no. bytesFrom: break               # empty after last chunk
            fileTo.w..(bytesFrom)

___ copytree(dirFrom, dirTo, verbose_0):
    """
    Copy contents of dirFrom and below to dirTo, return (files, dirs) counts;
    may need to use bytes for dirnames if undecodable on other platforms;
    may need to do more file type checking on Unix: skip links, fifos, etc.
    """
    fcount _ dcount _ 0
    ___ filename __ __.l_d_(dirFrom):                  # for files/dirs here
        pathFrom _ __.p...j..(dirFrom, filename)
        pathTo   _ __.p...j..(dirTo,   filename)        # extend both paths
        __ no. __.p...isdir(pathFrom):                   # copy simple files
            ___
                __ verbose > 1: print('copying', pathFrom, 'to', pathTo)
                copyfile(pathFrom, pathTo)
                fcount +_ 1
            ______:
                print('Error copying', pathFrom, 'to', pathTo, '--skipped')
                print(___.exc_info()[0], ___.exc_info()[1])
        ____
            __ verbose: print('copying dir', pathFrom, 'to', pathTo)
            ___
                __.mkdir(pathTo)                          # make new subdir
                below _ copytree(pathFrom, pathTo)        # recur into subdirs
                fcount +_ below[0]                        # add subdir  counts
                dcount +_ below[1]
                dcount +_ 1
            ______:
                print('Error creating', pathTo, '--skipped')
                print(___.exc_info()[0], ___.exc_info()[1])
    r_ (fcount, dcount)

___ getargs():
    """
    Get and verify directory name arguments, returns default None on errors
    """
    ___
        dirFrom, dirTo _ ___.a..[1:]
    ______:
        print('Usage error: cpall.py dirFrom dirTo')
    ____
        __ no. __.p...isdir(dirFrom):
            print('Error: dirFrom is not a directory')
        ____ no. __.p...e..(dirTo):
            __.mkdir(dirTo)
            print('Note: dirTo was created')
            r_ (dirFrom, dirTo)
        ____
            print('Warning: dirTo already exists')
            __ hasattr(__.p.., 'samefile'):
                same _ __.p...samefile(dirFrom, dirTo)
            ____
                same _ __.p...a..(dirFrom) __ __.p...a..(dirTo)
            __ same:
                print('Error: dirFrom same as dirTo')
            ____
                r_ (dirFrom, dirTo)

__ __name__ __ '__main__':
    ______ ti__
    dirstuple _ getargs()
    __ dirstuple:
        print('Copying...')
        start _ ti__.clock()
        fcount, dcount _ copytree(*dirstuple)
        print('Copied', fcount, 'files,', dcount, 'directories', end_' ')
        print('in', ti__.clock() - start, 'seconds')
