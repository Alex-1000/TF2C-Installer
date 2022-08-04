'''
Sourcemod folder operation handler. Finds sourcemod folder,
does manual folder selection and symlinking.
Also finds downloader and archive extractor
if there are any installed on PC.
'''

import os
from platform import system

import cli

if system() == 'Windows':
    import winreg

# Future gettext support
def _(x): return x

def find_sourcemod():
    '''
    Searches through registery (Windows)
    or ~/.steam/registery.vdf (Linux)
    to find sourcemod folder.
    '''
    try:
        if system() == 'Windows':
            registery = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKeyEx(registery, r'SOFTWARE\Valve\Steam', access=winreg.KEY_ALL_ACCESS)
            sourcepath = winreg.QueryValueEx(key, 'SourceModInstallPath')[0]
            winreg.CloseKey(key)
            return sourcepath
        else:
            sourcepath = None
            with open(os.path.expanduser(r'~/.steam/registry.vdf'), encoding="utf-8") as file:
                for _, line in enumerate(file):
                    if 'SourceModInstallPath' in line:
                        sourcepath = line[line.index('/home'):-1].replace(r'\\', '/').replace('"', '')
                        break
                file.close()
            return sourcepath
    except:
        return None

def select_folder():
    '''
    Function for handling install folder selection.
    '''
    path = find_sourcemod()
    if path is not None:
        cli.message(_('Sourcemod folder found at {}, do you want to install game there?'), path, 'yellow')
        cli.question(_('Y - yes | N - no | L - create symlink:'), [ cli.yes_answers, cli.no_answers , _('l link symlink').split() ], style='yellow')
    return path

# TODO: make actual symlinking
# Function template:
# #def sourcemod_symlink(original_path, new_path = None):
#    '''
#    Creates symlink from sourcemod location
#    to new sourcemod folder.
#    '''
