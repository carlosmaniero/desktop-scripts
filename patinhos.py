#!/usr/bin/env python
# coding: utf-8
import subprocess
import sys

total = int(sys.argv[1])

while total != 0:
    subprocess.call(['espeak', '-v', 'pt', '"{} patinhos foram passear além da montanha para brincar."'.format(total)])
    total -= 1
    if total > 1:
        subprocess.call(['espeak', '-v', 'pt', '"A mamãe chamou qua qua qua qua só {} patinhos voltaram de lá"'.format(total)])
    else:
        subprocess.call(['espeak', '-v', 'pt', '"A mamãe chamou qua qua qua qua só {} patinho voltaram de lá"'.format(total)])
