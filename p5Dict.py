#!/usr/bin/python3
import re

#------------------------------------------
#Name:          Vishalkumar Patel
#Course:        Programming Languages
#Assignment:    4 (Python-1)
#Due Date:      11/25/2018
#------------------------------------------

#initial declaration of list and dictionaries
#with specified required variable names
linelist=[]
varValueD={}
varTypeD={}
labelD={}

#labelAdder adds label to the label dictionary 
#variable labelD
def labelAdder(line,count):
    c = []
    c.append(count)
    token = line.split(':')
    if token[0].upper() not in labelD:
        labelD.update({token[0].upper():c})
    else:
        labelD[token[0].upper()].append(count)

#declareVar initializes the variable value and
#types into their respective dictionaries
def declareVar(token, varType, varValue):
    varTypeD.update({token.upper():varType.upper()})
    if varValue is None:
        varValueD.update({ token.upper() :''})
    else:
        varValueD.update({token.upper() : varValue})

#just maintains another list of all lines
#from the file provided from standard in
def lineAdder(line):
    linelist.append(line)

#print variables from our BEEP program's
#variable dictionary in sorted order
def printVariables():
    print("Variables:")
    print( "\t%-10s %-10s %-5s" %('Variable','Type','Value'))
    for key in sorted(varTypeD):
        print( "\t%-10s %-10s %-5s" %(key,varTypeD[key],varValueD[key]))

#print lables from our BEEP program's
#label dictionary and if there are duplicate
#labels indicate it as an error and display 
#line number it appears on
def printLabels():
    print("Labels:")
    print("\t%-10s %-10s" %('Label','Statement'))
    for key in sorted(labelD):
        if len(labelD[key]) > 1:
            print('\t***Error: label ',key.upper(),' appears on multiple lines: ',end=" ")
            for x in range(len(labelD[key])):
                if x == len(labelD[key]) - 1:
                    print(' and',labelD[key][x])
                else:
                    print(labelD[key][x],end=",")
        else:
            print("\t%-10s %-10s" %(key,labelD[key][0]))
