def ordenar_por_porcentaje(resultado):
        return resultado['porcentaje']

def contar_pases_y_efectividad(nombre_archivo):
    estadisticas={"Australia":[],"Argentina":[]}

    jugadoras={}

    with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                partes_linea = linea.strip().split(';')
                pais = partes_linea[0]
                numero_jugador = partes_linea[1]
                nombre_jugadora = partes_linea[2]
                pase_completado = partes_linea[3]
                if nombre_jugadora not in jugadoras:
                    jugadoras[nombre_jugadora]=[pais,numero_jugador,0,0] #pais,numero camiseta,pases bien,pases mal
                jugadora=jugadoras[nombre_jugadora]
                if pase_completado=="0":
                    jugadora[3]+=1
                else:
                    jugadora[2]+=1
    archivo.close()

    for jugadora in jugadoras:
        datos=jugadoras[jugadora]
        pases_totales=datos[2]+datos[3]
        porcentaje_bien=round(((datos[2]*100)/pases_totales),2)
        estadisticas[datos[0]].append({'numero':datos[1],'nombre':jugadora,'cantidad_pases':pases_totales,'pases_bien':datos[2],'pases_mal':datos[3],'porcentaje':porcentaje_bien})

    estadisticas['Australia']=sorted(estadisticas['Australia'],key=ordenar_por_porcentaje,reverse=True)
    estadisticas['Argentina']=sorted(estadisticas['Argentina'],key=ordenar_por_porcentaje,reverse=True)

    return estadisticas

def main():
     estadisticas=contar_pases_y_efectividad('pases.txt')
     print(estadisticas)
if __name__=="__main__":
    main()
