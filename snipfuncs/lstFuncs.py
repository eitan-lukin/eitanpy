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

def findMedianArrays(nums1: List[int], nums2: List[int]) -> float:
    """Receives two arrays of ints and returns the median of the merged arrays after sorting."""
    nums1.extend(nums2)
    nums1.sort()
    if len(nums1) % 2 == 0:
        return (nums1[len(nums1)//2 - 1] + nums1[len(nums1)//2])/2
    else:
        return nums1[len(nums1)//2]



###############################################################################
# Auxiliary Functions



###############################################################################
# User Classes

