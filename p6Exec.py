#!/usr/bin/python3
import re
# from p6Driver import *
from p5Dict import *
from exceptionHandler import *

def tokenizePrint(line):
    matchObj = line.split()
    for item in matchObj:
        if item.upper().startswith("\"") and item.endswith("\""):
            print(item[1:-1],end=" ")
        else:
            if item.upper() in varValueD:
                if varValueD[item.upper()].startswith("\""):
                    print(varValueD[item.upper()][1:-1],end=" ")
                else:
                    print(varValueD[item.upper()],end=" ")
    print()
#---------------------------------------------------------
def isVar(sentence):
    if sentence[0:3] == 'VAR':
        return True

def isPrint(sentence):
    if sentence[0:5] == 'PRINT':
        return True

def isAssign(sentence):
    if sentence[0:6] == 'ASSIGN':
        return True

def isGoto(sentence):
    if sentence[:4] == 'GOTO':
        return True

def isLabel(sentence):
    token = sentence.split(':')
    if token[0].upper() in labelD:
        return True
#-----------------------------------------------------------------
def addTokens(wordTokens):
    #format: ASSIGN dime + dime 1
    #           0   1   2   3   4
    sumToken = int(varValueD[wordTokens[3].upper()])
    sumToken += int(wordTokens[4])
    varValueD[wordTokens[1].upper()] = str (sumToken)

def multiplyTokens(wordTokens):
    stringProduct = (varValueD[wordTokens[3].upper()][1:-1]) * (int(varValueD[wordTokens[4].upper()]))
    varValueD[wordTokens[1].upper()] = str (stringProduct)

def greaterThan(wordTokens):
    #general format: Loop25: if > 25 working LAfter25
    #tokens-------->  0       1 2 3   4         5
    # print("--->",wordTokens)
    try:
        if wordTokens[3].upper() in varValueD:
            number1 = int (varValueD[wordTokens[3].upper()])
        else:
            number1 = int (wordTokens[3])
    except:
        raise InvalidValueType("'%s' is not numeric" % (number1)) 
    try:
        if wordTokens[4].upper() in varValueD:
            number2 = int ( varValueD[wordTokens[4].upper()])
        else:
            number2 = int (wordTokens[4])
    except:
        raise InvalidValueType("'%s' is not numeric" % (number2)) 
    return number1 > number2

def concatTokens(wordTokens):
    #format: ASSIGN working & working 25
    #tok---->   0     1     2    3     4
    if (str(wordTokens[3]).upper() in varValueD):
        if(str(wordTokens[4]).upper() in varValueD):
            a = str(varValueD[wordTokens[3].upper()])
            b = str(varValueD[wordTokens[4].upper()])
        else:
            a = str(varValueD[wordTokens[3].upper()])
            b = str(wordTokens[4])
    elif (str(wordTokens[4]).upper() in varValueD):
        a = str(wordTokens[3])
        b = str(varValueD[wordTokens[4].upper()])
    else:
        a = str(wordTokens[3])
        b = str(wordTokens[4])
    return a + b

def subtractTokens(wordTokens):
    #format: ASSIGN working - working 25
    #tok---->   0     1     2    3     4
    diffToken = int(varValueD[wordTokens[3].upper()])
    diffToken -= int(wordTokens[4])
    varValueD[wordTokens[1].upper()] = str (diffToken)

def greaterThanEqual(wordTokens):
    print()

def assignFromVar(wordTokens):
    #format: ASSIGN working money
    #tokens:    0       1   2
    varValueD[wordTokens[1].upper()] = varValueD[wordTokens[2].upper()]

def gotoFinder(labelName):
    lineNumber = 0
    for i in range(len(linelist)):
        tempLine = linelist[i].strip()
        if tempLine.startswith(labelName + ":"):
            return lineNumber
        # if tempLine[:len(labelName)] == labelName:
        #     return lineNumber
        lineNumber+=1

def labelLoops(line,currentLineNumber):
    # Loop25: if > 25 working LAfter25
    #   0      1 2  3   4       5
    #     ASSIGN quarter + quarter 1
    #     ASSIGN working - working 25
    #     GOTO Loop25
    # LAfter25: PRINT "quarters=" quarter
    
    tokens = line.strip().split()
    labelName = tokens[0]
    
    terminatingCondition = 0
    loopCondition = True
    returnCount = 0

    if '>' in tokens:
        if not greaterThan(tokens):
            while loopCondition and not greaterThan(tokens):
                tempLine = linelist[currentLineNumber].strip()
                returnCount+=1
                if isAssign(tempLine):
                    evalAssign(tempLine)
                if isGoto(tempLine):
                    jumpLineNumber = gotoFinder(labelName[:-1])
                    currentLineNumber = jumpLineNumber-1
                    returnCount = 1
                currentLineNumber+=1
               
        else:
            return gotoFinder(tokens[-1]) - currentLineNumber
    return returnCount
                

def evalAssign(sentence):
    tokens = sentence.split()
    if '+' in tokens:
        addTokens(tokens)
    elif '*' in tokens:
        multiplyTokens(tokens)
    elif '>=' in tokens:
        greateThanEqual(tokens)
    elif '>' in tokens:
        greaterThan(tokens)
    elif '&' in tokens:
        concatTokens(tokens)
    elif '-' in tokens:
        subtractTokens(tokens)
    elif (len(tokens)) == 3:
        assignFromVar(tokens)



def now():
    for line in range(len(linelist)):
        lines = linelist[line]
        # print(line,lines)
        
        if isPrint(lines):
            tokenizePrint(lines)
        if isAssign(lines):
            evalAssign(lines)
        if isLabel(lines):
            if 'PRINT' in lines:
                tokenizePrint("".join((lines.split(':'))[1]).strip())
            else:
                line+=labelLoops(lines,line)
