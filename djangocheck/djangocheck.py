import najha.functional as f
import os
import sys

from importlib import import_module

def loadSettings(projectPath):
    projectPath = os.path.abspath(projectPath)
    if not os.path.exists(projectPath):
        raise Exception(f'Path does not exist: {projectPath}')
    sys.path.append(projectPath)
    settings = import_module('settings')
    return settings


def checkDebug(settings):
    print(f'Checking DEBUG:')
    return settings.DEBUG == False


checkers = [
    checkDebug,
]


def run(*args):
    projectFolderPath = args[0]
    settings = loadSettings(projectFolderPath)
    for checker in checkers:
        print(checker(settings))


if __name__ == '__main__':
    projectFolderPath = sys.argv[1]
    run(projectFolderPath)
