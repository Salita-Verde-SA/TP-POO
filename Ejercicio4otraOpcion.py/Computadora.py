class Computadora:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.componenteCPU=[]
        
    def cargar_componentes(self,componentes):
        self.componenteCPU.append(componentes)
        
    def sumar_precios(self):
        suma=0
        for componente in self.componenteCPU:
            suma+=componente.precio * componente.cantidad
        if suma>50000:
            r=suma*0.40    
            suma+=r
        else:
            r=suma*0.30
            suma+=r
        return suma
    
    def mostrar_informacion(self):
        print("------COMPUTADORA-------")
        print(f"Marca: {self.marca}\nModelo: {self.modelo}")
        print("Componentes: ")
        print(f"{'Componente':<15} {'Marca':<15} {'Cantidad':<15} {'Precio':<15} {'Subtotal':<15}")
        for componente in self.componenteCPU:
            print(f"{componente.componente:<15} {componente.marca:<15} {componente.cantidad:<15} {componente.precio:<15} {componente.cantidad * componente.precio:<15}")
        print(f"\n{'Precio total: ':>62} {self.sumar_precios()}")
            
        
        
   