# -*- coding: utf-8 -*-

import logging

def do_stuff():
    # In Python 2.6, do not initialize the module logger at import,
    # because this will confuse you if you import the module before
    # loading the configuration in main.
    log = logging.getLogger(__name__)  # Getting loggers is "cheap".
    log.critical('Logging from another module.')
