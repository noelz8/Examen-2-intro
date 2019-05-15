#Examen 2 Intro a la programacion
#Pregunta 1 respuesta
class variable(object):
    def __init__(self):
        pass
    def matriz(self,columna):
        if isinstance (columna,int) and columna !=0:
            return self.matriz_aux(columna,1,[],"+")
        else: return "Error"

    def matriz_au(self,columnna,fila,resultado,indice):
        if fila==columna:
            return resultado
        elif self.matriz_aux(self,columnas,fila+1,resultado[fila]+indice]:
            return self.matriz_aux(columna,fila,resultado,indice)
        elif resultado==len(resultado(columna)):
            return self.matriz_aux(columna,fila,resultado,indice)
