# list files in dir tree by recursion 

______ sys, __

___ mylister(currdir):
    print('[' + currdir + ']')
    ___ file __ __.listdir(currdir):              # list files here
        p.. = __.p...j..(currdir, file)        # add dir path back
        if not __.p...isdir(p..):
            print(p..)
        else:
            mylister(p..)                        # recur into subdirs

if __name__ == '__main__':
    mylister(sys.argv[1])                         # dir name in cmdline
