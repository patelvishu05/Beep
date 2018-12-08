#!/usr/bin/python3
from exceptionHandler import *

class Executor():
    linelist=[]
    varValueD={}
    varTypeD={}
    labelD={}
    
    def __init__(self,linelist,varValueD,varTypeD,labelD):
        self.linelist = linelist
        self.varValueD = varValueD
        self.varTypeD = varTypeD
        self.labelD = labelD

    #------------------------------------------------
    def isVar(self,sentence):
        if sentence[0:3] == 'VAR':
            return True

    def isPrint(self,sentence):
        if sentence[0:5] == 'PRINT':
            return True

    def isAssign(self,sentence):
        if sentence[0:6] == 'ASSIGN':
            return True

    def isGoto(self,sentence):
        if 'GOTO' in sentence:
            return True

    def isLabel(self,sentence):
        token = sentence.split(':')
        if token[0].upper() in self.labelD:
            return True
    
    def isIfStatement(self,sentence):
        if sentence.strip()[:2].upper() == 'IF':
            return True
    #------------------------------------------------

    def tokenizePrint(self,line):
        matchObj = line.split()
        for item in matchObj:
            if item.upper().startswith("\"") and item.endswith("\""):
                print(item[1:-1],end=" ")
            else:
                if item.upper() in self.varValueD:
                    if self.varValueD[item.upper()].startswith("\""):
                        print(self.varValueD[item.upper()][1:-1],end=" ")
                    else:
                        print(self.varValueD[item.upper()],end=" ")
        print("")

    def greaterThan(self,wordTokens):
        #general format: if > 25 working LAfter25
        #tokens-------->  0 1  2  3       4 
        # print("--->",wordTokens)
        try:
            if wordTokens[2].upper() in self.varValueD:
                number1 = int (self.varValueD[wordTokens[2].upper()])
            else:
                number1 = int (wordTokens[2])
        except:
            raise InvalidValueType("'%s' is not numeric" % (number1)) 
        try:
            if wordTokens[3].upper() in self.varValueD:
                number2 = int ( self.varValueD[wordTokens[3].upper()])
            else:
                number2 = int (wordTokens[3])
        except:
            raise InvalidValueType("'%s' is not numeric" % (number2)) 
        return number1 > number2
    

    def greaterThanEqual(self,wordTokens):
        try:
            if wordTokens[2].upper() in self.varValueD:
                number1 = int (self.varValueD[wordTokens[2].upper()])
            else:
                number1 = int (wordTokens[2])
        except:
            raise InvalidValueType("'%s' is not numeric" % (number1)) 
        try:
            if wordTokens[3].upper() in self.varValueD:
                number2 = int ( self.varValueD[wordTokens[3].upper()])
            else:
                number2 = int (wordTokens[3])
        except:
            raise InvalidValueType("'%s' is not numeric" % (number2)) 
        return number1 >= number2


    def addTokens(self,wordTokens):
        #format: ASSIGN dime + dime 1
        #           0   1   2   3   4
        sumToken = 0
        if wordTokens[3].isdigit():
            sumToken = int (wordTokens[3])
        else:
            try:
                sumToken = int(self.varValueD[wordTokens[3].upper()])
            except Exception:
                print(wordTokens[3],"does not have a value or is not defined.")

        if wordTokens[4].isdigit():
            sumToken += int (wordTokens[4])
        else:
            try:
                sumToken += int(self.varValueD[wordTokens[4].upper()])
            except Exception:
                print(wordTokens[4],"does not have a value or is not defined.")
        
        try:
            self.varValueD[wordTokens[1].upper()] = str (sumToken)
        except:
            raise VarNotDefined(wordTokens[1].upper()," variable is not defined.")


    def subtractTokens(self,wordTokens):
        #format: ASSIGN dime + dime 1
        #           0   1   2   3   4
        sumToken = 0
        if wordTokens[3].isdigit():
            sumToken = int (wordTokens[3])
        else:
            try:
                sumToken = int(self.varValueD[wordTokens[3].upper()])
            except Exception:
                print(wordTokens[3],"does not have a value or is not defined.")

        if wordTokens[4].isdigit():
            sumToken -= int (wordTokens[4])
        else:
            try:
                sumToken -= int(self.varValueD[wordTokens[4].upper()])
            except Exception:
                print(wordTokens[4],"does not have a value or is not defined.")
        
        try:
            self.varValueD[wordTokens[1].upper()] = str (sumToken)
        except:
            raise VarNotDefined(wordTokens[1].upper()," variable is not defined.")


    def multiplyTokens(self,wordTokens):
        stringProduct = ""
        try:
            stringProduct = (self.varValueD[wordTokens[3].upper()][1:-1]) * (int(self.varValueD[wordTokens[4].upper()]))
        except Exception:
            print(wordTokens[4], "is not a Number")
        
        try:
            self.varValueD[wordTokens[1].upper()] = str (stringProduct)
        except:
            raise VarNotDefined(wordTokens[1].upper()," variable is not defined.")

    def assignFromVar(self,wordTokens):
        #format: ASSIGN working money
        #tokens:    0       1   2
        self.varValueD[wordTokens[1].upper()] = self.varValueD[wordTokens[2].upper()]

    def concatTokens(self,wordTokens):
        a = ""
        b = ""
        try:
            if (str(wordTokens[3]).upper() in self.varValueD):
                if(str(wordTokens[4]).upper() in self.varValueD):
                    a = str(self.varValueD[wordTokens[3].upper()])
                    b = str(self.varValueD[wordTokens[4].upper()])
                else:
                    a = str(self.varValueD[wordTokens[3].upper()])
                    b = str(self.wordTokens[4])
            elif (str(wordTokens[4]).upper() in self.varValueD):
                a = str(wordTokens[3])
                b = str(self.varValueD[wordTokens[4].upper()])
            else:
                a = str(wordTokens[3])
                b = str(wordTokens[4])
        except Exception:
            print("Invalid values supplied for concatenation")

        try:
            self.varValueD[wordTokens[1].upper()] = a + b
        except:
            raise VarNotDefined(wordTokens[1].upper()," variable is not defined.")


    def evalAssign(self,sentence):
        tokens = sentence.split()
        if '+' in tokens:
            self.addTokens(tokens)
        elif '*' in tokens:
            self.multiplyTokens(tokens)
        elif '>=' in tokens:
            self.greaterThanEqual(tokens)
        elif '>' in tokens:
            self.greaterThan(tokens[len(tokens)-5:])
        elif '&' in tokens:
            self.concatTokens(tokens)
        elif '-' in tokens:
            self.subtractTokens(tokens)
        elif (len(tokens)) == 3:
            self.assignFromVar(tokens)
    
    def evalIfStatement(self,line,currentLineNumber):
        print(line,"<<<<")
        tokens = line.strip().split()
        loopCondition = True
        # returnCount = 0
        if '>' in tokens:
            if not self.labelCondition(tokens[2],(tokens[len(tokens)-5:])):
                while loopCondition:
                    # print(3,line)
                    if not self.labelCondition(tokens[2],(tokens[len(tokens)-5:])):
                        tempLine = self.linelist[currentLineNumber].strip()
                        currentLineNumber+=1
                        # returnCount += 1
                        if self.isAssign(tempLine):
                            self.evalAssign(tempLine)
                        if self.isPrint(tempLine):
                            self.tokenizePrint(tempLine)
                        if self.isGoto(tempLine):
                            jumpLineNumber = self.gotoFinder((re.match(r'.*GOTO (.*)',tempLine)).group(1))
                            return jumpLineNumber 
                    else:
                        return self.gotoFinder(tokens[-1])
            else:
                return self.gotoFinder(tokens[-1])


    def labelCondition(self,operator,tokens):
        if operator == '>':
            return self.greaterThan(tokens)
        return self.greaterThanEqual(tokens)

    def labelLoops(self,line,currentLineNumber):
        print(line)
        tokens = line.strip().split()
        labelName = tokens[0]
        loopCondition = True
        if not self.labelCondition(tokens[2],(tokens[len(tokens)-5:])):
            while loopCondition:
                # print(self.linelist[currentLineNumber])
                if not self.labelCondition(tokens[2],(tokens[len(tokens)-5:])):
                    tempLine = self.linelist[currentLineNumber].strip()
                    if self.isAssign(tempLine):
                        self.evalAssign(tempLine)
                    if self.isPrint(tempLine):
                        self.tokenizePrint(tempLine)
                    if self.isGoto(tempLine):
                        jumpLineNumber = self.gotoFinder(labelName[:-1])
                        currentLineNumber = jumpLineNumber - 1
                        return currentLineNumber
                    if self.isIfStatement(tempLine):
                        currentLineNumber = self.evalIfStatement(tempLine,currentLineNumber) - 1
                    currentLineNumber+=1
                else:
                    return self.gotoFinder(tokens[-1])
        else:
            return self.gotoFinder(tokens[-1])


    def gotoFinder(self,labelName):
        lineNumber = 0
        for i in range(len(self.linelist)):
            tempLine = self.linelist[i].strip().upper()
            if tempLine.startswith(labelName.upper() + ":"):
                # print(labelName.upper(),"<<<",lineNumber)
                return lineNumber
            lineNumber+=1


    def startInterpreting(self,verbose):
        fileLines = self.linelist
        # print("execution begins...") TODO: add to driver
        line = 0

        while line < len(fileLines):
            actualLine = fileLines[line]
            if verbose:
                print("executing line %d: %s" %(line,actualLine))
            try:
                if self.isPrint(actualLine):
                    self.tokenizePrint(actualLine)
                if self.isAssign(actualLine):
                    self.evalAssign(actualLine)
                if self.isLabel(actualLine):
                    if 'PRINT' in actualLine:
                        self.tokenizePrint("".join((actualLine.split(':'))[1:]).strip())
                    else:
                        line = self.labelLoops(actualLine,line) - 1
                if self.isIfStatement(actualLine):
                    line = self.evalIfStatement(actualLine,line) - 1
            except (InvalidValueType,TooFewOperands, LabelNotDefined, InvalidExpression, VarNotDefined) as e:
                print("Error at line %d: %s"%(index+1, e.args[1]))
                break
            line+=1 
            



        