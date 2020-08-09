VALID_COLORS = ['blue', 'yellow', 'red']


___ print_colors(
    """In the w___ loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check:
       - if 'quit' was entered for color, print 'bye' and break.
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    w___ True:
        inp = input("Enter a colour:").lower()
        __ inp __ "quit":
            print("bye")
            break

        __ inp not in VALID_COLORS:
            print("Not a valid color")
            continue

        print(inp)
