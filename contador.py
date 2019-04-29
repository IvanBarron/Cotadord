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
    variable = 1
    while(True):
        if 2**variable >= len(list):
            return variable
        variable = variable + 1

def main():
    list = clearArgs(sys.argv)
    verifyRepeated(list)
    max = getMax(list)
    print(getVariables(list))
    print('{0:b}'.format(max))




if __name__ == '__main__':
    main()
