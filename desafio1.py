#declaramos para usar metodo choice más adelante
import random
#cambiamos el numero de camisetas a string porque no vamos a usarlas para realizar ninguna operación,tambien quitamos los acentos
argentina=("Argentina", [
 ("Agustina Gorzelany", "11"),
 ("Maria Jose Granatto", "9"),
 ("Sofia Toccalino", "20"),
 ("Agostina Alonso", "10"),
 ("Valentina Raposo", "8"),
 ("Clara Barberi", "5"),
 ("Delfina Thome", "4"),
 ("Sofia Cairo", "7"),
 ("Pilar Campoy", "16")
])

#Agregamos 6 jugadoras mas de jugadoras de australia (para equiparar los equipos)
australia=("Australia", [
("Katrina Powell", "10"),
("Madonna Blyth", "9"),
("Toni Cronk", "17"),
("Bettany Hamilton","12"),
("Lucy Blue", "20"),
("Kaith Lewis", "15"),
("Lin Orwig", "11"),
("Mary Jane", "5"),
("Julia Nicholson", "3"),
])

equipos=[argentina,australia]
#Creamos funciones para modularizar el programa (si después queremos cambiar algo es más fácil desde la función)

#Esta función permite obtener el estado del pase de manera aleatoria (puede ser 0 o 1, por eso pusimos 2)
def obtener_estado_del_pase():
    return str(random.choice(range(2)))
#Esta función permite obtener el tiempo de cada jugadora (elegimos que sea entre 0 y 60,porque un partido dura 60 minutos)
def obtener_tiempo():
    return str(random.choice(range(61)))
#Esta funcion indica si es australia o argentina(Equipos es una lista que creamos arriba)
def obtener_equipo():
    return random.choice(equipos)
def obtener_jugadora(equipo):
    return random.choice(equipo[1])
#Esta función elige de equipo que puede ser australia o argentina, la posición 0 que es de la lista de tuplas el nombre de la jugadora
def obtener_nombre_jugadora(jugadora):
    return jugadora[0]
#Esta función elige de equipo que puede ser australia o argentina, la posición 1 que es de la lista de tuplas el numero de la jugadora
def obtener_numero_jugadora(jugadora):
    return jugadora[1]
def obtener_nombre_equipo(equipo):
    return equipo[0]
#Esta función crea la línea que después será impresa por el programa,se transformó
def crear_registro(equipo,jugadora,pase,tiempo):
    return obtener_nombre_equipo(equipo)+";"+obtener_numero_jugadora(jugadora)+";"+obtener_nombre_jugadora(jugadora)+";"+pase+";"+ tiempo



#imprimir lo que nos piden y en el formato que piden: equipo ; numero de camiseta ; nombre del jugador ; resultado del pase ; minutos de juego (50000 veces)
#Asignamos su valor a la variable archivo  para crear archivo tipo txt y poder escribir sobre el mismo

archivo = open("pases.txt", "a")

#creamos programa para iterar 50 mil veces la línea que genera la función registro de manera aleatoria )usando metodo choice)
def main():
    for i in range (50000):
        #declaramos estas variables dentro del programa para que la linea registro varia en el archivo txt, y así no se imprima siempre el mismo.
        pase = obtener_estado_del_pase()
        tiempo= obtener_tiempo()
        equipo= obtener_equipo()
        jugadora=obtener_jugadora(equipo)
        registro= crear_registro(equipo,jugadora,pase,tiempo)
        
        archivo.write(registro+"\n")

    #Para cerrar el archivo:
    archivo.close()


if __name__=="__main__":
    main()