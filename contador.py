import sys
import re
#from utils import Utils
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

def main():
    list = clearArgs(sys.argv)
    verifyRepeated(list)
    table = generateTable(list)
    print(table)






if __name__ == '__main__':
    main()
