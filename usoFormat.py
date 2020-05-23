# utilizar la funcion 'format' de un string para incluir 
# valores en una salida 

def main(): 

intbase = 9
intalt = 3
fltAreaTriangulo=(intBase*intAltura)/2
tex = "Area: {2:0.2f} ( {0} por {1} entre dos )"
print(tex.format(intbase, intaltura, fltAreaTriangulo))

# el orden de los parametros es de base cero
# el text Area es un float que no contiene decimales