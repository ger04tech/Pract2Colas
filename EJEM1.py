
class Nodo:
    def __init__(self, orden):
        self.orden = orden  
        self.siguiente = None  



class Orden:
    def __init__(self, cliente, cantidad):
        self.cliente = cliente
        self.cantidad = cantidad

    def imprimir(self):
        
        print(f"Cliente: {self.cliente}")
        print(f"Cantidad: {self.cantidad}")
        print("------------")



class Pila:
    def __init__(self):
        self.tope = None  
        self.tamaño = 0  

    def apilar(self, orden):
        
        nuevo_nodo = Nodo(orden)  
        nuevo_nodo.siguiente = self.tope  
        self.tope = nuevo_nodo  
        self.tamaño += 1 

    def desapilar(self):
        
        if self.tope is None:  
            return None
        nodo = self.tope  
        self.tope = self.tope.siguiente  
        self.tamaño -= 1  
        return nodo.orden  

    def imprimir_pila(self):
       
        nodo = self.tope  
        while nodo is not None:  
            nodo.orden.imprimir() 
            nodo = nodo.siguiente  


if __name__ == "__main__":
   
    orden1 = Orden("Cliente 1", 10)
    orden2 = Orden("Cliente 2", 20)
    orden3 = Orden("Cliente 3", 30)

    
    pila = Pila()

    pila.apilar(orden1)
    pila.apilar(orden2)
    pila.apilar(orden3)

   
    pila.imprimir_pila()
