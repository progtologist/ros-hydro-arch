#!/usr/bin/env python

import sys
import os

program = sys.argv[1]

file = open(str(sys.argv[1])+'-applications','r')

for line in file:
    if '\n' == line[-1]:
        line = line[:-1]
    command = 'sudo pacman -R --noconfirm ' + str(line)
    print(command)
    os.system(command)
