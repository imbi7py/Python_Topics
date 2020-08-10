"""
Find the largest file of a given type in an arbitrary directory tree.
Avoid repeat paths, catch errors, add tracing and line count size.
Also uses sets, file iterators and generator to avoid loading entire 
file, and attempts to work around undecodable dir/file name prints.
"""

______ __, pprint
from sys ______ argv, exc_info

trace = 1                                    # 0=off, 1=dirs, 2=+files
dirname, extname = __.curdir, '.py'          # default is .py files in cwd
__ len(argv) > 1: dirname = argv[1]          # ex: C:\, C:\Python31\Lib
__ len(argv) > 2: extname = argv[2]          # ex: .pyw, .txt
__ len(argv) > 3: trace   = int(argv[3])     # ex: ". .py 2"

___ tryprint(arg):
    try:
        print(arg)                           # unprintable filename?
    except UnicodeEncodeError:
        print(arg.encode())                  # try raw byte string
 
visited  = set()
allsizes = []
___ (thisDir, subsHere, filesHere) __ __.walk(dirname):
    __ trace: tryprint(thisDir)
    thisDir = __.p...normpath(thisDir)
    fixname = __.p...normcase(thisDir)
    __ fixname __ visited:
        __ trace: tryprint('skipping ' + thisDir)
    ____
        visited.add(fixname)
        ___ filename __ filesHere:
            __ filename.endswith(extname):
                __ trace > 1: tryprint('+++' + filename)
                fullname = __.p...j..(thisDir, filename)
                try:
                    bytesize = __.p...getsize(fullname)
                    linesize = sum(+1 ___ line __ o..(fullname, 'rb'))
                except Exception:
                    print('error', exc_info()[0])
                ____
                    allsizes.append((bytesize, linesize, fullname))

___ (title, key) __ [('bytes', 0), ('lines', 1)]:
    print('\nBy %s...' % title)
    allsizes.sort(key=lambda x: x[key])
    pprint.pprint(allsizes[:3])
    pprint.pprint(allsizes[-3:])
