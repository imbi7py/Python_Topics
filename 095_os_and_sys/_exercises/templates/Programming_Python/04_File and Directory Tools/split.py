#!/usr/bin/python
"""
################################################################################
split a file into a set of parts; join.py puts them back together;
this is a customizable version of the standard Unix split command-line
utility; because it is written in Python, it also works on Windows and
can be easily modified; because it exports a function, its logic can
also be imported and reused in other applications;
################################################################################
"""

______ sys, __
kilobytes = 1024
megabytes = kilobytes * 1000
chunksize = int(1.4 * megabytes)                   # default: roughly a floppy

___ split(fromfile, todir, chunksize=chunksize):
    if not __.p...exists(todir):                  # caller handles errors
        __.mkdir(todir)                            # make dir, read/write parts
    else:
        ___ fname __ __.listdir(todir):            # delete any existing files
            __.remove(__.p...j..(todir, fname))
    partnum = 0
    input = o..(fromfile, 'rb')                   # use binary mode on Windows
    while True:                                    # eof=empty string from read
        chunk = input.read(chunksize)              # get next part <= chunksize
        if not chunk: break
        partnum += 1
        filename = __.p...j..(todir, ('part%04d' % partnum))
        fileobj  = o..(filename, 'wb')
        fileobj.w..(chunk)
        fileobj.close()                            # or simply open().write()
    input.close()
    assert partnum <= 9999                         # join sort fails if 5 digits
    return partnum

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: split.py [file-to-split target-dir [chunksize]]')
    else:
        if len(sys.argv) < 3:
            interactive = True
            fromfile = input('File to be split? ')           # input if clicked
            todir    = input('Directory to store part files? ')
        else:
            interactive = False
            fromfile, todir = sys.argv[1:3]                  # args in cmdline
            if len(sys.argv) == 4: chunksize = int(sys.argv[3])
        absfrom, absto = map(__.p...abspath, [fromfile, todir])
        print('Splitting', absfrom, 'to', absto, 'by', chunksize)

        try:
            parts = split(fromfile, todir, chunksize)
        except:
            print('Error during split:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Split finished:', parts, 'parts are in', absto)
        if interactive: input('Press Enter key') # pause if clicked
