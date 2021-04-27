#!/usr/bin/env python3

###############################################################################
# standard library imports

import os
import sys
import logging

###############################################################################
# Initialize Logging
consolelevel = logging.DEBUG
logger = logging.getLogger(__name__)
logger.setLevel(consolelevel)
# create formatter and add it to the handlers
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(consolelevel)
ch.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)

###############################################################################
# related third party imports

###############################################################################
# local application/library specific imports

###############################################################################
# User Constants

###############################################################################
# User Functions

def sendErrorAndExit(s):
    """Send error to stdout through the logger module and exit with return code 1"""
    logger.error(s)
    sys.exit(1)

###############################################################################
# Auxiliary Functions



###############################################################################
# User Classes

