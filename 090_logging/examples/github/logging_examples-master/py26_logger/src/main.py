#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Python2.6+ compatible logging setup module to be used as point-of-entry to a
program."""

import os
import optparse
import logging
import logging.config

import example_package.example_module
# We imported example_module before setting logging configuration.
# This can cause issues, see the module for explanation.


def run():
    load_logging_conf('logging.conf')
    # All loggers MUST be started AFTER this point, including for imported modules!
    # Start the logger for this module.
    log = logging.getLogger(__name__)

    opts, args = parse_cli_args()

    set_debug_verbosity(opts.verbose)

    log.debug('test debug message')
    log.info('test info message')
    log.warn('test warn message')
    log.error('test error message')
    log.critical('test critical message')

    example_package.example_module.do_stuff()


def load_logging_conf(log_cfg_filename):
    """Load logging configuration at '<src_dir>/../logs/<filename>' (os agnostic)."""
    src_dir = os.path.dirname(os.path.realpath(__file__))
    cfg_file_path = os.sep.join((src_dir, '..', 'logs', log_cfg_filename))

    logging.config.fileConfig(cfg_file_path)


def parse_cli_args():
    """Parse command line args.  Additional options can be added."""
    parser = optparse.OptionParser()
    parser.add_option('-v', '--verbose', dest="verbose",
                      action='count', default=0,
                      help='increase debug logging level')

    return parser.parse_args()

def set_debug_verbosity(verbosity_counter):
    """Deactivates the debug handler if verbosity_counter is 0, else sets
    the logging level appropriately."""

    debug_handler = logging.root.handlers[1]

    if verbosity_counter == 0:
        logging.root.removeHandler(debug_handler)
    elif verbosity_counter == 1:
        debug_handler.level = logging.INFO
    elif verbosity_counter == 2:
        debug_handler.level = logging.DEBUG
    else:
        debug_handler.level = logging.NOTSET


if __name__ == '__main__':
    run()
