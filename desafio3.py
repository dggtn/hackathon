import random
def main():
    diferencia=0
    turno_actual = 1
    ronda_actual = 1
    gol_argentina=0
    gol_holanda=0



#VALIDAR DATOS DE ENTRADA
    def obtener_tiro():
        tiro=0
        tiro_invalido=True
        while tiro_invalido:
            try:
                tiro=int(input("Te toca patear de 1 a 9: "))
                if tiro >9 or tiro<1:
                    raise Exception("Tiro invalido")
                else:
                    tiro_invalido=  False
            except:
                tiro_invalido=True
        return tiro

#VALIDAR DATOS DE ENTRADA
    def obtener_ataje():
        ataje=0
        ataje_invalido=True
        while ataje_invalido:
            try:
                ataje=int(input("Te toca atajar de 1 a 9: "))
                if ataje >9 or ataje<1:
                    raise Exception("Ataje invalido")
                else:
                    ataje_invalido=  False
            except:
                ataje_invalido= True
        return ataje

    def convertir_penal():
        ## PEDIR AL USUARIO QUE ELIJA DONDE PATEAR
        tiro_Argentina=obtener_tiro()
        atajes_paisesBajos=random.randint(1, 9)
        ## CONTAR SI ARGENTINA HIZO GOL
        return tiro_Argentina!=atajes_paisesBajos

    def atajar_penal():
        tirosPaisesBajos=random.randint(1, 9)
        ## PEDIR AL USUARIO QUE ELIJA DONDE ATAJAR
        atajesArgentina=obtener_ataje()
        return atajesArgentina==tirosPaisesBajos
    


    while ronda_actual<=5 and (5-ronda_actual+1)>=diferencia:
        print(f"Esta es la ronda nro {ronda_actual}")
        if turno_actual == 1:
            print("Le toca al jugador 1")
            turno_actual = 2
            if convertir_penal():
               print("Gol Argentina")
               gol_argentina+=1
            else:
               print("Argentina no hizo gol")
        else:
            print("Le toca al jugador 2")
            ## HACER QUE LA CPU PATEE CON UN NRO ALEATORIO
            if not atajar_penal():
                gol_holanda+=1
                print("Gol de Holanda")
            else:
                print("Holanda no hizo gol")
            turno_actual = 1
            ronda_actual+=1
        ## MOSTRAR MARCADOR ACTUALIZADO
        diferencia= abs(gol_holanda-gol_argentina)
        print("Holanda= ",gol_holanda,",Argentina=",gol_argentina)
    ## VER SI HAY GANADOR
    ##SI HAY EMPATE, HACER RONDA DE DESEMPATE
    if diferencia==0:
        while diferencia ==0:
            print(f"Esta es la ronda nro {ronda_actual}")
            if convertir_penal():
               print("Gol Argentina")
               gol_argentina+=1
            else:
               print("Argentina no hizo gol")
            if not atajar_penal():
                gol_holanda+=1
                print("Gol de Holanda")
            else:
                print("Holanda no hizo gol")
            ronda_actual+=1
            print("Holanda= ",gol_holanda,",Argentina=",gol_argentina)
            diferencia= abs(gol_holanda-gol_argentina)


    if gol_holanda>gol_argentina:
        print("GANA HOLANDA!!")
    else:
        print("GANA ARGENTINA")


if __name__=="__main__":
    main()