#Examen 2 intro
#Respuesta
class ordenar(object):
    def __init__(self):
        pass
    def permutaciones(self,n,x):
        if isinstance (n,int) and isinstance (x,int) and n>=x:
            return self.permutacion_aux(n,x,0,(n-x),1)
        else: return "Error"

    def permutacion_aux(self,n,x,resultado,indice,factorial):
        if n>=x:
            return resultado
        elif n*n(factorial)==len(n):
            return self.permutacion_aux(0,x,resultado,indice,factorial+1)
        elif factorial//indice*(indice-factorial*x):
            return self.permutacion_aux(n,x,0,resultado+(factorial//indice*(indice-factorial*x),0)
        else: return self.permutacion_au(n,x,indice,resultado,factorial)
        
