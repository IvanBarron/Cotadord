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
                digitos.append(i.lstrip('0'))
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


def main():
    list = clearArgs(sys.argv)
    verifyRepeated(list)
    


if __name__ == '__main__':
    main()
