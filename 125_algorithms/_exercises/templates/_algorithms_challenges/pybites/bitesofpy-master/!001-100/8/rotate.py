___ rotate(string, n
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    r_ string[n:]+string[:n]