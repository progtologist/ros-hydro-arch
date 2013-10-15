#!/usr/bin/env python

import sys
import os

program = sys.argv[1]

file = open(str(sys.argv[1])+'-applications','r')

for line in file:
    if '\n' == line[-1]:
        line = line[:-1]
    command = 'cd ' + str(program) + '/' + str(line) + ' && ' + 'makepkg -f' + ' && ' + 'sudo pacman -U --noconfirm ' + str(line) + '-release-1-x86_64.pkg.tar.xz'
    print(command)
    os.system(command)
