# preguntar diferentes tipos de datos
# empezamos con un dato de tipo datetime
import datetime


def main():

 # aqui le solicitamos al usuario varios datos, como lo son
 # un string, entero y float 

 strDato = input("Dame un dato string: ")
 _iDato = input("Dame un dato entero: ")
 iDato = int(_iDato)
 _fDato = input("Dame un dato float: ")
 fDato =float(_fDato)

# le preguntamos al usuario para que nos brinde una fecha
# de acuerdo al formato que se pide

 _dtDato = input("Dame una fecha yyyy/mm/dd: ")


 anio=_dtDato[0:4]
 mes=_dtDato[5:7]
 dia=_dtDato[-2:]
 # se muestra en el codigo el año, mes y dia
 print(anio)
 print(mes)
 print(dia)

 dtDato = datetime.datetime(int(anio), int(mes), int(dia))

# se imprimen los tipos de datos que nos dio en un principip

 print(strDato)
 print(type(strDato))
 print(iDato)
 print(type(iDato))
 print(fDato)
 print(type(fDato))
 print(dtDato)
 print(type(dtDato))
 