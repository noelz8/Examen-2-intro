#Examen 2 intro
#Respuesta 3
class cuadrado(object):
    def __init__(self):
        pass
    def es_magico(self,matriz):
        if isinstance (matriz,list) and matriz !=[]:
            return self.es_magico_aux(matriz,0,0,[],[])
        else: return "Error"

    def es_magico_aux(self,matriz,columna,fila,indicefila,indicecola):
        if len(matriz[fila])==len(matriz[columna]):
            return self.busqueda(matriz,0,0)
        elif fila==len(matriz[columna]):
            return self.es_magico_aux(matriz,0,fila+1,indicefila+fila,[])
        elif columna==len(matriz(fila-1)):
            return self.es_magico_aux(matriz,columna+1,0,[],indicecolumna+columna)
        elif len(indicefila)==len(indicecolumna):
            return self.es_magico_aux(matriz,columna,fila,indicefila,indicecolumna)
    def busqueda(self,matriz,colum,fila):
        if len(matriz[fila])==len(matriz[colum]):
            return self.busqueda_aux(matriz,colum,fila,0):
                else: return False

    def busqueda_aux(self,matriz,colum,fila,result):
        if colum==fila:
            return result
        elif fila==len(matriz[colum]):
            return self.busqueda_aux(matriz,0,fila+1,resultado+[fila])
        elif colum==len(matriz[fila-1]):
            return self.busqueda_aux(matriz,colum+1,0,resultado+len(matriz(colum)))
        elif len(matriz[colum])+len(matriz[fila])==result:
            return True
        
        
