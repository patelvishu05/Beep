#!/usr/bin/python3

import re

# line = 'afterIf: GOTO loop'
line1 = 'GOTO afterIf'
line = line1.split()

print(len(line))
print(line[len(line)-1])