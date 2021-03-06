______ ___

___ filter_files(name, function):         # filter file through function
    input  _ o..(name, 'r')              # create file objects
    output _ o..(name + '.out', 'w')     # explicit output file too
    ___ line __ input:
        output.w..(function(line))      # write the modified line
    input.close()
    output.close()                        # output has a '.out' suffix

___ filter_stream(function):              # no explicit files
    w__ True:                           # use standard streams
        line _ ___.stdin.readline()       # or: input()
        __ no. line: break
        print(function(line), end_'')     # or: sys.stdout.write()

__ __name__ __ '__main__':
    filter_stream(lambda line: line)      # copy stdin to stdout if run



"""
def filter_files(name, function):
    with open(name, 'r') as input, open(name + '.out', 'w') as output:
        for line in input:
            output.write(function(line))      # write the modified line
"""

"""
def filter_stream(function):
    for line in sys.stdin:
        print(function(line), end='')
"""

