'''
Module for handling all CLI interactions with user.
'''

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

def question(msg, answers = [yes_answers, no_answers], args = None, style = None):
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
                return answers.index(option)
        message(_('Invalid answer. Please, enter ' + short_answers), style='bold blue')
