#!usr/bin/env python2


'''

CppGen!

by Mitchell Nordine

Generate .cpp and .header with template contents from argument.

Usage:
    CPPTemplate.py
    CPPTemplate.py [-h | --help] [-v | --version]
    CPPTemplate.py <directory> <name>...
    CPPTemplate.py -d <name>...

Options:
    -h --help           Show this screen.
    -v --version        Show version.
    -d --thisDirectory  Place generated files in this directory.

'''


import os, sys
from shutil import copyfile
from docopt import docopt
from pprint import pprint
from datetime import datetime


def getHeaderTemplate():
    '''Location of template .h file to use.'''
    return os.getcwd()+'/template.h'


def getCPPTemplate():
    '''Location of template .cpp file to use.'''
    return os.getcwd()+'/template.cpp'


def editNewFile(newPath, name):
    '''Replace TEMPLATE with name in all of it's occurences and
    replaces DATE with the date and time in all of it's occurences.'''
    f = open(newPath, 'r')
    s = f.read()
    f.close()
    s = s.replace('TEMPLATE', name)
    s = s.replace('DATE', datetime.now().strftime("%I:%M%p on %B %d, %Y"))
    f = open(newPath, 'w')
    f.write(s)
    f.close()


def makeHeader(path, name, template):
    '''Makes the new .h file at "path" directory copied from "template".'''
    newPath = path+"/"+name+'.h'
    copyfile(template, newPath)
    editNewFile(newPath, name)


def makeCPP(path, name, template):
    '''Makes the new .cpp file at "path" directory copied from "template".'''
    newPath = path+"/"+name+'.cpp'
    copyfile(template, newPath)
    editNewFile(newPath, name)


def cleanPath(path):
    while path[-1] is " " or path[-1] is "/":
        path = path[:-1]
    path = os.path.expanduser(path)
    path = os.path.normpath(path)
    return path


def main():
    args = docopt(__doc__, version='CPP & Header Generator -- ULTIMATE EDITION')
    if not args['<name>']:
        name = raw_input("What name should the files be?: ")
        path = raw_input("What directory should the files go in?: ")
        path = cleanPath(path)
        s = 'Making da '+name+'.cpp...'
        print(s)
        makeCPP(path, name, getCPPTemplate())
        s = 'Making yo flippin '+name+'.h...'
        print(s)
        makeHeader(path, name, getHeaderTemplate())
    elif args['--thisDirectory']:
        for name in args['<name>']:
            makeCPP(os.getcwd(), name, getCPPTemplate())
            makeHeader(os.getcwd(), name, getHeaderTemplate())
    else:
        for name in args['<name>']:
            makeCPP(cleanPath(args['<directory>']), name, getCPPTemplate())
            makeHeader(cleanPath(args['<directory>']), name, getHeaderTemplate())
    print('Your dinner is SERVED Biytch!')


if __name__ == "__main__":
    main() 

