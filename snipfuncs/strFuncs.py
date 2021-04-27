#!/usr/bin/env python3

###############################################################################
# standard library imports

import os
import sys
import logging
from snipFuncs import manageFuncs

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

def lengthOfLongestSubstring(s: str) -> int:
    """Given a string s, returns the length of the longest substring without repeating characters."""
    if s == '':
        return 0
    max_start_ptr = 0
    max_end_ptr = 1
    start_ptr = 0
    end_ptr = 1
    for t in (s)[1:]:
        if t in (s)[start_ptr:end_ptr]:
            # update the pointer of the first and last
            start_ptr = start_ptr + (s)[start_ptr:end_ptr].index(t) + 1
            end_ptr += 1
        else:
            end_ptr += 1
        # Update Max pointers if necessary
        if (end_ptr - start_ptr) > (max_end_ptr - max_start_ptr):
            max_start_ptr = start_ptr
            max_end_ptr = end_ptr
    return max_end_ptr - max_start_ptr




###############################################################################
# Auxiliary Functions



###############################################################################
# User Classes

