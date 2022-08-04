'''
Master module. Handles arguments and runs functions for actual work.
'''

import signal
#import os
import sys

import cli
import setup

# Future gettext support
def _(x): return x

def handler(signum, frame):
    '''
    Ctrl-C exit handler.
    '''
    cli.message('\nExiting...', style='red')
    # TODO: delete temp files if user said so
    sys.exit(572)

def background_check():
    '''
    Checks if program is launched from background, and exits if it does.
    '''
    if not sys.stdin or not sys.stdin.isatty():
        sys.exit(402)

def install(step = 0, path = None):
    '''
    Main function, responsible for calling other functions
    and transfering their result to eachother.
    "step" is current step.
    "path" is install path variable.
    '''
    signal.signal(signal.SIGINT, handler)
    try:
        background_check()
        if step == 0:
            path = setup.select_folder()
        if step > 0:
            pass
    except Exception as ex:
        if ex is not SystemExit:
            cli.console.print_exception()
            cli.message('----- ' + _('Exception details above') + ' -----', style='bold red')
            cli.message(_('Please, contact {} on Discord or open issue in Github repository:'), 'TheGamer#3173', style='red')
            cli.message('https://github.com/Alex-1000/TF2C-Installer', style='blue')

if __name__ == '__main__':
    install()
