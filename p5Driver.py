#!/usr/bin/python3

import sys
from p5Dict import *
# from p6Exec import *
from Executor import *

#------------------------------------------
#Name:          Vishalkumar Patel
#Course:        Programming Languages
#Assignment:    4 (Python-1)
#Due Date:      11/25/2018
#------------------------------------------

#open file received from stdin for reading
file = open(sys.argv[1],"r")
if len(sys.argv) > 2:
    if sys.argv[2] == '-v':
        verbose = True
print("BEEP source code in %s:" %(sys.argv[1]))

#read the whole file in one shot
inputLines = file.read().splitlines()

lines=[]
count=1

#iterate over all read lines from inputLines and
#process that line accordingly as required
#depending on the variable or label lines
#send them over to be processed as label and variables
#in p5Dict.py and save them in their respective
#dictionaries
for inputLine in inputLines:
    if inputLine[0:3] == 'VAR':
        token = inputLine.split()
        # varTypeD.update({token[2].upper():token[1]})
        if(len(token)) is 4:
            declareVar(token[2],token[1],token[3])
        else:
            declareVar(token[2],token[1],'')
    if (re.search(r'^[^ \W.*]*:',inputLine.strip())) is not None:
        labelAdder(inputLine.strip(),count)
    lines.append(inputLine)
    lineAdder(inputLine)
    #TODO: remove this comment below
    # print("%2d." %(count),inputLine)
    count+=1
file.close()

#print variables from our BEEP program's
#variable dictionary in sorted order
#TODO: remove comment
# printVariables()

#print lables from our BEEP program's
#label dictionary and if there are duplicate
#labels indicate it as an error and display 
#line number it appears on
#TODO: remove comment
# printLabels()

print('executing begins ...')
# now()

newExecutor = Executor(linelist,varValueD,varTypeD,labelD)
newExecutor.startInterpreting()
