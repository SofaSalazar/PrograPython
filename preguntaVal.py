# usare un modulo para que sean validas las expresiones
# regulares 

import re

# el siguiente modulo permitira la entrada con los datos 
# de tipo datetime

import datetime 

# con la variable a continuacion, permitira preguntar info
# asi como validarla 

capt=""

# esta funcion revisa si un dato es correcto, de lo contrario
# continua el codigo/preguntando, solo se enumeran entre ()

def askandcheck(_patron,_pregunta_"Por favor, ingresa un  dato: "):
  global capt
  while true: 
    _mvalor = input(_pregunta)
    coincide = re.search(_patron, mvalor)
    if (coincide):
      capt= _mvalor
      break
    else:
      print("El dato que ingresaste es incorrecto. Intentalo de nuevo")

# la funcion siguiete permite convertir una expresion
# año/mes/dia a datetime

def strodate (_dtoconv):
  return datetime.datetime(int(_dtoconv[0:4]), int(_dtoconv[5:7]) int(_dtoconv[-2:1]))

  def main():
    
    # aqui solo se acepta un codigo de 4 digitos 
    askandcheck ("^[0-9]{4}$), "ID (4 digitos): )
    numeroID=capt

    # el nombre solo permitira de 1 a 20 letras mayusculas o 
    # espacio

    askandcheck("^([A-Z ]) {1,20}$", "Nombre: ")
    nombre=capt

    askandcheck("^[S|N]$", "Acepta (S/N): ")
    acepta=capt

    # ahora la fecha

    askandcheck("^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|3[01])$","Ingresa una fecha (YYYY-MM-DD): ")
    fecha=capt 

    # se imprime los datos ingresados de numeroID, nombre, acepta y fecha