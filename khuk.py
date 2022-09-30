tipo = input ('cuando es 500+3001')
def suma (x,y):
    res = x+y
    print (res)
    return res

if tipo == '1':
    primer = int (input ('seleccione un numero'))
    segundo = int (input ('seleccione segundo numero'))

    res = suma (primer, segundo)
    print (f'el resultado {res}')


