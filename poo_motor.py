# Primera práctica de clases y objetos.

class Proveedor:
    def __init__(self, nombre, contacto, telefono):
        self.nombre = nombre
        self.contacto = contacto
        self.telefono = telefono

    def enlistar(self):
        return f"Proveedor: {self.nombre}, contacto: {self.contacto}, teléfono: {self.telefono}."

class Motor:
    def __init__(self, tipo, capacidad, ubicacion):
        self.tipo = tipo
        self.capacidad = capacidad
        self.ubicacion = ubicacion
    
    def describir(self):
        return f"Motor {self.tipo}, de {self.capacidad} kW solicitado por {self.ubicacion}"

p1 = Proveedor("Siemens", "Carlos Bañuelos", "656-11-11-11")
p2 = Proveedor("ABB", "Ramón Castro", "656-22-22-22")
p3 = Proveedor("Motorsa", "Verónica López", "656-33-33-33")

m1 = Motor("Monofásico", 20, "Planta # 1")
m2 = Motor("Bifásico", 7.5, "Almacén")
m3 = Motor("Trifásico", 100, "Planta # 4")

print("\n")
print("=" * 65)
print("Motores en Espera de ser Recibidos".center(65))
print("=" * 65)
print(m1.describir())
print(m2.describir())
print(m3.describir())

print("\n")
print("=" * 65)
print("Directorio de Proveedores".center(65))
print("=" * 65)
print(p1.enlistar())
print(p2.enlistar())
print(p3.enlistar())
print("=" * 65)
print("\n")