# Inicializacion del menu
# Es creado para poder generar tareas hacia el sistema operativo

import os

# El siguiente modulo es para trabajar con una regular expression

import re 

# Esta funcion es para borrar pantalla, en este caso seria 
# una lambda, que es equivalente a un def clear ():
# os.system ('cls') 

limpiarPantalla = lambda : os . system ( 'cls' )

# Se validan las regular expression
# en este caso _txt seria el texto a validar
# _regex es el patron de la regular expression a validar
# Retornar True si _txt cumple con el patron definido 
# en _regex, retornar False si no es asi 

def RegEx (_txt , _regex ):
   coincidencia = re . partido ( _regex , _txt )
   return bool ( coincidencia )

def principal():
   mientras que ( Verdadero ):
   limpiarPantalla ()
   imprimir ( "Lista de contactos" )

# Se comienza con un menu donde se imprimira las diferentes
# opciones que se tienen, dependiendo del numero
# que sea elegido

   print("[1] Agregar un contacto")
   print("[2] Buscar un contacto")
   print("[3] Eliminar un contacto")
   print("[4] Mostrar contactos")
   print("[5] Serializar datos")
   print("[0] Salir")

opcion_escogida = input ( "¿Que deseas hacer?>" )
si RegEx ( opcion_escogida , "^) [123450] {1} $" ):
  si RegEx ( opcion_escogida == "0" :
  imprimir ( "Gracias por hacer uso del programa" )
  rotura 

input ("Pulsa enter para continuar ...")

más :

   print ( "Esa respuesta no es válida" )
   input ("Pulsa enter para continuar ...")

principal()

# Se debe codificar una serie de procedimiento 
# para cada una de las opciones presentadas, para 
# ver si son validas