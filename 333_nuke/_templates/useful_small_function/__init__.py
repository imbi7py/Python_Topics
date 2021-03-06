#!/usr/bin/env python
______ re
______ __


__all__ _ ['attr_type', 'auto_convert', 'camel_case_to_lower_case_underscore', 'camel_case_to_title', 'clean_name',
            'is_bool', 'is_dict', 'is_list', 'is_none', 'is_number', 'is_string', 'list_attr_types', 
            'lower_case_underscore_to_camel_case', 'is_newer', 'test_func']

#- Naming ----
___ clean_name(text):
    """
    Return a cleaned version of a string - removes everything 
    but alphanumeric characters and dots.

    :param str text: string to clean.
    :returns: cleaned string.
    :rtype: str
    """
    r_ re.sub(r'[^a-zA-Z0-9\n\.]', '_', ?



___ camel_case_to_lower_case_underscore(text):
    """
    Split string by upper case letters.
    F.e. useful to convert camel case strings to underscore separated ones.

    :param str text: string to convert.
    :returns: formatted string.
    :rtype: str
    """
    words _ # list
    from_char_position _ 0
    ___ current_char_position, char __ enumerate(text):
        __ char.isupper() and from_char_position < text:
            words.ap..(s[from_char_position:current_char_position].lower())
            from_char_position _ current_char_position
    words.ap..(text[from_char_position:].lower())
    r_ '_'.j..(words)


___ camel_case_to_title(text):
    """
    Split string by upper case letters and return a nice name.

    :param str text: string to convert.
    :returns: formatted string.
    :rtype: str
    """
    words _ # list
    from_char_position _ 0
    ___ current_char_position, char __ enumerate(text):
        __ char.isupper() and from_char_position < current_char_position:
            words.ap..(text[from_char_position:current_char_position].title())
            from_char_position _ current_char_position
    words.ap..(text[from_char_position:].title())
    r_ ' '.j..(words)


___ lower_case_underscore_to_camel_case(text):
    """
    Convert string or unicode from lower-case underscore to camel-case.

    :param str text: string to convert.
    :returns: formatted string.
    :rtype: str
    """
    split_string _ text.s..('_')
    # use string's class to work on the string to keep its type
    class_ _ text.__class__
    r_ split_string[0] + class_.j..('', m..(class_.capitalize, split_string[1:]))


#- Attribute Functions ----
___ auto_convert(v.. ):
    """
    Auto-convert a value to it's given type.
    """
    atype _ attr_type(v.. )
    __ atype __ 'str':
        r_ st.(v.. )

    __ atype __ 'bool':
        r_ bool(v.. )

    __ atype __ 'float':
        r_ fl..(v.. )

    __ atype __ 'int':
        r_ in_(v.. )
    r_ v..

___ attr_type(v.. ):
    """
    Determine the attribute type based on a value. 
    Returns a string.

    For example:
    
        value = [2.1, 0.5]
        type = 'float2'

    :param value: attribute value.
    
    :returns: attribute type.
    :rtype: str
    """
    __ is_none(v.. ):
        r_ 'null'

    __ is_list(v.. ):
        r_ list_attr_types(v.. )

    ____
        __ is_bool(v.. ):
            r_ 'bool'

        __ is_string(v.. ):
            r_ 'str'

        __ is_number(v.. ):
            __ type(v.. ) __ fl..:
                r_ 'float'

            __ type(v.. ) __ in_:
                r_ 'int'
    r_ 'unknown'

___ list_attr_types(s):
    """
    Return a string type for the value.

    .. todo::
        - 'unknown' might need to be changed
        - we'll need a feature to convert valid int/str to floats
          ie:
            [eval(x) for x in s if type(x) in [str, unicode]]
    """
    __ no. is_list(s):
        r_ 'unknown'
    
    ___ typ __ [st., in_, fl.., bool]:
        __ all(isinstance(n, typ) ___ n __ s):
            r_ '%s%d' % (typ.__name__, le.(s))

    __ F.. no. __ list(set([is_number(x) ___ x __ s])):
        r_ 'float%d' % le.(s)
    r_ 'unknown'


___ is_none(s):
    r_ type(s).__name__ __ 'NoneType'


___ is_string(s):
    r_ type(s) __ [st., unicode]


___ is_number(s):
    """
    Check if a string is a int/float
    """
    __ is_bool(s):
        r_ F..
    r_ isinstance(s, in_) or isinstance(s, fl..)


___ is_bool(s):
    """
    Returns true if the object is a boolean value. 
    * Updated to support custom decoders.
    """
    r_ isinstance(s, bool) or st.(s).lower() __ ['true', 'false']


___ is_list(s):
    """
    Returns true if the object is a list type.
    """
    r_ type(s) __ [list, tuple]


___ is_dict(s):
    """
    Returns true if the object is a dict type.
    """
    ____ collections ______ OrderedDict
    r_ type(s) __ [dict, OrderedDict]


___ is_newer(file1, file2):
    """
    Returns true if file1 is newer than file2.

    :param str file1: first file to compare.
    :param str file2: second file to compare.

    :returns: file1 is newer.
    :rtype: bool
    """ 
    __ no. __.pa__.e..(file1) or no. __.pa__.e..(file2):
        r_ F..

    time1 _ __.pa__.getmtime(file1)
    time2 _ __.pa__.getmtime(file2)
    r_ time1 > time2

#- Testing -----
___ test_func(w, h):
    print '# width: %.2f, height: %.2f' % (fl..(w), fl..(h))


___ nodeParse(node):
    t _ node[u"type"]

    __ t __ u"Program":
        body _ [parse(block) ___ block __ node[u"body"]]
        r_ Program(body)

    ____ t __ u"VariableDeclaration":
        kind _ node[u"kind"]
        declarations _ [parse(declaration) ___ declaration __ node[u"declarations"]]
        r_ VariableDeclaration(kind, declarations)

    ____ t __ u"VariableDeclarator":
        id _ parse(node[u"id"])
        init _ parse(node[u"init"])
        r_ VariableDeclarator(id, init)

    ____ t __ u"Identifier":
        r_ Identifier(node[u"name"])

    ____ t __ u"Literal":
        r_ Literal(node[u"value"])

    ____ t __ u"BinaryExpression":
        operator _ node[u"operator"]
        left _ parse(node[u"left"])
        right _ parse(node[u"right"])
        r_ BinaryExpression(operator, left, right)
    ____
        raise ValueError("Invalid data structure.")
