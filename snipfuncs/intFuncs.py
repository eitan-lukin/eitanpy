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

def twoSumInList(nums: List[int], target: int) -> List[int]:
    """Given a list of integers and a target integer, return indices of the two 
    integers in the list such that they add up to the target integer. 
    Returns after finding the first solution."""
    some_dict = {} 
    for i, num in enumerate(nums):
        try:
            return [some_dict[target-num], i]
        except KeyError:
            some_dict[num] = i
            continue




###############################################################################
# Auxiliary Functions



###############################################################################
# User Classes

