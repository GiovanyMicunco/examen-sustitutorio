class Persona:
    def __init__(self,nombre,edad, ciudad):
        self.__nombre=nombre
        self.edad=edad
        self.ciudad=ciudad
    def Imprimir_datos(self):
        print("Nombre   :",self.__nombre)
        print("Edad :",self.edad)
        print("Ciudad   :",self.ciudad)
        
class Empleado(Persona):
    def __init__(self,nombre,edad,ciudad):
        super().__init__(nombre,edad,ciudad)
        self.sueldo=float(input("Ingresar el sueldo de {} :".format(self._Persona__nombre)))
        
    def impuesto(self):
        impuesto=self.sueldo*0.09
        if self.sueldo>5500:
            print("{} debe pagar {} soles de impuesto".format(self._Persona__nombre,impuesto))
        else:
            print("{} no debe pagar impuestos".format(self._Persona__nombre))
        return impuesto
def manejo_diccionario(empleados):
    diccionario = {}
    for empleado in empleados:
        impuesto = empleado.impuesto()
        diccionario[empleado._Persona__nombre] = {
            'edad': empleado.edad,
            'sueldo': empleado.sueldo,
            'impuesto': impuesto
        }
    return diccionario

def generar_archivo_empleado(empleados):
    with open("empleados.txt","a") as archivo:
        for empleado in empleados:
            archivo.write("{},{},{}".format(empleado._Persona__nombre,empleado.sueldo,empleado.impuesto()))

def mostrar_empleados():
    with open("empleados.txt", "r") as archivo:
        for linea in archivo:
            nombre, sueldo, impuesto = linea.strip().split(',')
            print("El empleado {} tiene una remuneración de {} soles y un impuesto de {} soles.".format(nombre, sueldo, impuesto))

def encontrar_empleado(nombre):
    with open("empleados.txt", "r") as archivo:
        for linea in archivo:
            nombre_empleado, sueldo, impuesto = linea.strip().split(',')
            if nombre_empleado == nombre:
                print("El empleado {} tiene una remuneración de {} soles y un impuesto de {} soles.".format(nombre, sueldo, impuesto))
                return
        print("Empleado no encontrado.")

empleados=[]
while True:
    nombre= input("Ingrese el nombre del empleado (o 'q' para salir): ")
    if nombre == 'q':
        break
    edad=int(input("Ingrese la edad de  {}:".format(nombre)))
    ciudad=input("Ingrese la ciudad de {}: ".format(nombre))
    empleado= Empleado(nombre,edad,ciudad)
    empleados.append(empleado)
generar_archivo_empleado(empleados)
mostrar_empleados()
nombre_buscar = input("Ingrese el nombre del empleado a buscar: ")
encontrar_empleado(nombre_buscar)

diccionario = manejo_diccionario(empleados)
print("Diccionario de empleados:", diccionario)
    

            
        
        
    