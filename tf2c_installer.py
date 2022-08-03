'''
Master module. Handles arguments and runs functions for actual work.
'''

import os
import sys


def background_check():
    '''
    Checks if program is launched from background, and exits if it does.
    '''
    if not sys.stdin or not sys.stdin.isatty():
        sys.exit(402)


