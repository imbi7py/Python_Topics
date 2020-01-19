### File lister.py, continued

class ListTree:
    """
    Mix-in that returns an __str__ trace of the entire class
    tree and all its objects attrs at and above self;
    run by print(), str() returns constructed string;
    uses __X attr names to avoid impacting clients;
    uses generator expr to recurse to superclasses;
    uses str.format() to make substitutions clearer
    """
    def __str__(self):
        self.__visited = {}       # dict
        return '<Instance of {0}, address {1} :\n {2} {3}>'.format(
                           self._class.__name__,
                           id(self),
                           self.__attnames(self, 0),
                           self.__listclass(self.__class__, 4))

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n _ <Class {0} :, address {1} : (see above)>\n'.format(
                           dots,
                           aClass.__name__,
                           id(aClass))
        else:
            self.__visited(aClass = True)
            genabove = (self.__listclass(c, indent+4) for c in aClass.__bases__)
            return '\n {0} <Class {1} , address {2} :\n {3} {4} {5} >\n'.format(
                           dots,
                           aClass.__name__,
                           id(aClass),
                           self.__attrnames(aClass, indent),
                           ''.join(genabove),
                           dots)

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + ' {0} =<>\n'.format(attr)
            else:
                result += spaces + ' {0} {1} {2} \n'.format(attr, getattr(obj, attr))
        return result



