
# ==========================================================
# PRACTICA No. 3
# INVENTARIO INDUSTRIAL Y GESTION DE COMPRAS
# POO - HERENCIA - EVALUACION DE PROVEEDORES
# ==========================================================


# ==========================================================
# CLASE PADRE: EQUIPO
# ==========================================================

class Equipo:

    LIMITE_CONSUMO = 100

    def __init__(self, codigo, marca, potencia_kw, horas_uso):
        self.codigo = codigo
        self.marca = marca
        self.potencia_kw = potencia_kw
        self.horas_uso = horas_uso

    def consumo_diario(self):
        return self.potencia_kw * self.horas_uso

    def verificar_consumo(self):

        if self.consumo_diario() >= self.LIMITE_CONSUMO:
            return "ALERTA: ALTO CONSUMO - EQUIPO CRITICO"

        return "Consumo normal"


# ==========================================================
# CLASE HIJA: MOTOR
# ==========================================================

class Motor(Equipo):

    def __init__(self, codigo, marca, potencia_kw, horas_uso, fases):

        super().__init__(codigo, marca, potencia_kw, horas_uso)

        self.fases = fases

    def describir(self):

        return (
            f"Motor {self.codigo} | "
            f"Marca: {self.marca} | "
            f"Potencia: {self.potencia_kw} kW | "
            f"Horas: {self.horas_uso} | "
            f"Fases: {self.fases} | "
            f"Consumo: {self.consumo_diario():.2f} kWh/dia | "
            f"{self.verificar_consumo()}"
        )


# ==========================================================
# NUEVA CLASE: PROVEEDOR
# ==========================================================

class Proveedor:

    def __init__(self, nombre, calidad, precio, dias_entrega):

        self.nombre = nombre
        self.calidad = calidad
        self.precio = precio
        self.dias_entrega = dias_entrega

    def describir(self):

        return (
            f"Proveedor: {self.nombre} | "
            f"Calidad: {self.calidad}/10 | "
            f"Precio: ${self.precio:,.2f} MXN | "
            f"Entrega: {self.dias_entrega} dias"
        )


# ==========================================================
# FUNCIONES DE VALIDACION
# ==========================================================

def ingresar_codigo():

    while True:

        codigo = input("Codigo del motor: ").strip()

        if codigo and all(
            c.isalnum() or c == "-" for c in codigo
        ):
            return codigo.upper()

        print("Error: utilice letras, numeros o guiones.")


def ingresar_marca():

    while True:

        marca = input("Marca del motor: ").strip()

        if marca and all(
            palabra.isalpha() for palabra in marca.split()
        ):
            return marca.title()

        print("Error: ingrese solamente letras y espacios.")


def ingresar_numero(mensaje):

    while True:

        try:
            valor = float(input(mensaje))

            if valor > 0:
                return valor

            print("El valor debe ser mayor que cero.")

        except ValueError:
            print("Ingrese un valor numerico valido.")


def ingresar_entero(mensaje, minimo=1, maximo=None):

    while True:

        try:
            valor = int(input(mensaje))

            if valor >= minimo and (
                maximo is None or valor <= maximo
            ):
                return valor

            print("Valor fuera del rango permitido.")

        except ValueError:
            print("Ingrese un numero entero valido.")


def preguntar_si(mensaje):

    while True:

        respuesta = input(mensaje + " (S/N): ").strip().upper()

        if respuesta in ("S", "N"):
            return respuesta == "S"

        print("Respuesta no valida. Escriba S o N.")


# ==========================================================
# FUNCION PARA REGISTRAR UN MOTOR
# ==========================================================

def capturar_motor():

    print("\n--- DATOS DEL MOTOR ---")

    codigo = ingresar_codigo()
    marca = ingresar_marca()

    potencia = ingresar_numero("Potencia en kW: ")
    horas = ingresar_numero("Horas de uso diario: ")

    fases = ingresar_entero(
        "Numero de fases (1, 2 o 3): ", 1, 3
    )

    return Motor(codigo, marca, potencia, horas, fases)


# ==========================================================
# NUEVA FUNCION: EVALUACION DE PROVEEDORES
# ==========================================================

def evaluar_proveedores(tipo_compra, proveedores):

    print("\n" + "=" * 65)
    print("EVALUACION DE PROVEEDORES".center(65))
    print("=" * 65)

    if tipo_compra == "1":

        # COMPRA NORMAL: MENOR PRECIO
        seleccionado = min(
            proveedores,
            key=lambda p: p.precio
        )

        criterio = "MENOR PRECIO"

    elif tipo_compra == "2":

        # COMPRA PROGRAMADA: MAYOR CALIDAD
        seleccionado = max(
            proveedores,
            key=lambda p: p.calidad
        )

        criterio = "MAYOR CALIDAD"

    else:

        # COMPRA CRITICA: MENOR TIEMPO DE ENTREGA
        seleccionado = min(
            proveedores,
            key=lambda p: p.dias_entrega
        )

        criterio = "MENOR TIEMPO DE ENTREGA"

    print(f"\nCriterio de seleccion: {criterio}")

    print("\nComparativo de cotizaciones:")

    for proveedor in proveedores:

        print(proveedor.describir())

    print("\n" + "-" * 65)
    print("PROVEEDOR SELECCIONADO".center(65))
    print("-" * 65)

    print(seleccionado.describir())

    print("\nMotivo: mejor resultado segun el criterio establecido.")

    return seleccionado


# ==========================================================
# NUEVA FUNCION: REGISTRO DE COMPRAS
# ==========================================================

def gestionar_compras():

    compras = []

    print("\n" + "=" * 65)
    print("MODULO DE GESTION DE COMPRAS".center(65))
    print("=" * 65)

    if not preguntar_si("\n¿Existen motores pendientes de compra?"):
        print("No hay necesidades de compra registradas.")
        return compras

    while True:

        print("\n" + "=" * 65)
        print("NUEVA SOLICITUD DE COMPRA".center(65))
        print("=" * 65)

        motor = capturar_motor()

        print("\nTIPO DE COMPRA")
        print("1. Normal")
        print("2. Programada")
        print("3. Critica")

        tipo = input("Seleccione el tipo de compra (1/2/3): ").strip()

        while tipo not in ("1", "2", "3"):
            tipo = input("Opcion incorrecta. Seleccione 1, 2 o 3: ").strip()

        nombres_tipos = {
            "1": "Normal",
            "2": "Programada",
            "3": "Critica"
        }

        print("\nIngrese las cotizaciones de TRES proveedores.")

        proveedores = []

        for i in range(3):

            print(f"\n--- COTIZACION DEL PROVEEDOR {i + 1} ---")

            nombre = input("Nombre del proveedor: ").strip()

            while not nombre:
                nombre = input("El nombre es obligatorio: ").strip()

            calidad = ingresar_numero(
                "Calificacion de calidad (1 a 10): "
            )

            while calidad > 10:
                print("La calidad maxima es 10.")
                calidad = ingresar_numero(
                    "Calificacion de calidad (1 a 10): "
                )

            precio = ingresar_numero(
                "Precio cotizado en MXN: "
            )

            dias = ingresar_entero(
                "Tiempo de entrega en dias: ", 0
            )

            proveedor = Proveedor(
                nombre, calidad, precio, dias
            )

            proveedores.append(proveedor)

        # Evaluar las tres cotizaciones

        seleccionado = evaluar_proveedores(tipo, proveedores)

        # Guardar solicitud y resultado

        compras.append({
            "motor": motor,
            "tipo": nombres_tipos[tipo],
            "proveedores": proveedores,
            "seleccionado": seleccionado
        })

        print("\nSolicitud evaluada correctamente.")

        if not preguntar_si("¿Desea agregar otro motor a compras?"):
            break

    return compras


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():

    motores = []

    print("\n" + "=" * 70)
    print("SISTEMA DE GESTION DE ACTIVOS INDUSTRIALES".center(70))
    print("=" * 70)

    # ------------------------------------------------------
    # MODULO 1: INVENTARIO DE MOTORES
    # ------------------------------------------------------

    print("\nMODULO 1: INVENTARIO DE MOTORES")

    if preguntar_si("¿Desea registrar motores instalados?"):

        while True:

            motor = capturar_motor()

            motores.append(motor)

            print("\nMotor registrado correctamente.")

            if not preguntar_si("¿Desea agregar otro motor?"):
                break

    # Reporte de inventario

    print("\n" + "=" * 70)
    print("REPORTE GENERAL DE MOTORES".center(70))
    print("=" * 70)

    for motor in motores:

        print(motor.describir())
        print("-" * 70)

    consumo_total = sum(
        motor.consumo_diario() for motor in motores
    )

    equipos_criticos = sum(
        1 for motor in motores
        if motor.consumo_diario() >= Equipo.LIMITE_CONSUMO
    )

    print(f"\nMotores registrados: {len(motores)}")
    print(f"Consumo total: {consumo_total:.2f} kWh/dia")
    print(f"Equipos criticos: {equipos_criticos}")

    # ------------------------------------------------------
    # MODULO 2: GESTION DE COMPRAS
    # ------------------------------------------------------

    compras = gestionar_compras()

    # ------------------------------------------------------
    # REPORTE FINAL DE COMPRAS
    # ------------------------------------------------------

    print("\n" + "=" * 70)
    print("RESUMEN FINAL DE COMPRAS".center(70))
    print("=" * 70)

    for compra in compras:

        motor = compra["motor"]
        proveedor = compra["seleccionado"]

        print(
            f"\nMotor solicitado: {motor.codigo} | "
            f"Marca: {motor.marca} | "
            f"Potencia: {motor.potencia_kw} kW"
        )

        print(f"Tipo de compra: {compra['tipo']}")
        print(f"Proveedor elegido: {proveedor.nombre}")
        print(f"Precio: ${proveedor.precio:,.2f} MXN")
        print(f"Entrega: {proveedor.dias_entrega} dias")

    print("\n" + "=" * 70)
    print("FIN DEL PROGRAMA".center(70))
    print("=" * 70)


# ==========================================================
# EJECUCION
# ==========================================================

if __name__ == "__main__":
    main()
