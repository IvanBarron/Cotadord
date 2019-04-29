import sys
import re
#from utils import Utils
VARIABLE =  97

def clearArgs(args):
    digitos = []
    for i in args:
        if i == __file__:
            pass
        else:
            if(isNumber(i)):
                digitos.append(int(i.lstrip('0')))
            else:
                print('El argumento %s no es valido, se excluirá',i)
    return digitos

def isNumber(arg):
    isNumber = bool(re.match('^[0-9]+$',arg))
    return isNumber

def verifyRepeated(digits):
    for i in digits:
        if(digits.count(i)>1):
            print('No se pueden utilizar valores repetidos.')
            exit()

def getMax(digits):
    maxNum = max(digits)
    return maxNum

def getVariables(list):
    variable = len('{0:b}'.format(getMax(list)))
    return variable

def generateTable(list):
    i = 0
    table = []
    while i < len(list):
        par = []
        if(i == len(list) - 1):
            par.append('{0:b}'.format(list[i]).zfill(getVariables(list)))
            par.append('{0:b}'.format(list[0]).zfill(getVariables(list)))
            i = i + 1
        else:
            par.append('{0:b}'.format(list[i]).zfill(getVariables(list)))
            par.append('{0:b}'.format(list[i+1]).zfill(getVariables(list)))
            i = i + 1
        table.append(par)
    return table

def getMiniTerms(table, bit):
    minTerms = []
    for register in table:
        if register[1][bit] == '1':
            minTerms.append(register[0])
    return minTerms

def printMinterms(table,list):
    for i in range(getVariables(list)):
        print("bit ",i)
        minTerms = getMiniTerms(table,i)
        print(minTerms)
        for term in minTerms:
            loop = 0
            for bit in term:
                if bit == '1':
                    print(chr(VARIABLE + loop), end = "")
                else:
                    print(chr(VARIABLE + loop), '\'',end = "")
                loop = loop + 1
            if (term == minTerms[-1]):
                pass
            else:
                print("+", end="")
        print("")



def main():
    list = clearArgs(sys.argv)
    verifyRepeated(list)
    table = generateTable(list)
    print(table)
    printMinterms(table,list)



if __name__ == '__main__':
    main()
