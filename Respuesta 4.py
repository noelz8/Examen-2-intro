#Examen 2 introduccion a la programacion
#Respuesta 4
class barras(object):
    def __init__(self):
        pass
    def grafico(self,valores):
        if isinstance(valores,list) and valores !=[]:
            return self.grafico_aux(valores,0,[])
        else: return "Error"

    def grafico_aux(self,valores,fila,resultado):
        if fila==len(valores):
            return resultado
        elif fila ==len(valores[0:]):
            return self.grafico(valores,fila,resultado+fila(print"+"))
        elif len(matriz[fila])==len(matriz[0:]):
            return self.grafico_aux(matriz,fila,resultado)
