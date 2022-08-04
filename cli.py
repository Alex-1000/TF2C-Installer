'''
Module for handling all CLI interactions with user.
'''

import os

from rich.console import Console


# Future gettext support
def _(x): return x

# Rich library object representing console.
global console
console = Console()

# Default "yes" answers for questions.
global yes_answers
yes_answers = _('y yes').split()

# Default "no" answers for questions.
global no_answers
no_answers = _('n no').split()

def message(msg, args = None, style = None):
    '''
    Displays message with arguemnts and formatting.
    '''
    msg = msg.replace('{}', '[italic]{}[/italic]')
    if args is not None:
        msg = msg.format(args)
    console.print(msg, style=style)

def question(msg, answers = [ yes_answers, no_answers ], args = None, style = None):
    '''
    Displays question, then asks user
    until he selects one of valid answers.
    Returns index of option from "answers" variable.
    '''
    message(msg, args, style)
    short_answers = ''
    for i, answer in enumerate(answers):
        short_answers += answer[0]
        if i < len(answers) - 1:
            short_answers += ' or '
    short_answers += '.'
    while True:
        answer = input().lower().strip()
        for option in answers:
            if answer in option:
                return option[0]
        message(_('Invalid answer. Please, enter ' + short_answers), style='bold blue')

def select_directory(msg, args = None, style = None):
    while True:
        message(msg, args, style)
        directory = input('> ')
        if directory.count("~") > 0:
            directory = os.path.expanduser(directory)
        if directory.count("$") > 0:
            directory = os.path.expandvars(directory)
        if os.path.isdir(directory):
            return directory
        elif os.path.exists(directory):
            message(_('You have selected file. Please, select directory instead.'), style='bold blue')
            continue
        if question(_('Directory does not exist. Do you want to create it? (y/n)'), style='yellow') == 'y':
            os.mkdir(directory)
            return directory
