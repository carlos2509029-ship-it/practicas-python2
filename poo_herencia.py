
# ==========================================================
# PRACTICA No. 2 - POO, HERENCIA Y MONITOREO ENERGETICO
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
        else:
            return "Consumo normal"

class Motor(Equipo):

    def __init__(self, codigo, marca, potencia_kw, horas_uso, fases):

        # Heredamos atributos de Equipo
        super().__init__(codigo, marca, potencia_kw, horas_uso)

        # Atributo propio de Motor
        self.fases = fases

    def describir(self):
        return (
            f"Motor {self.codigo}  "
            f"\nMarca: {self.marca}  "
            f"\nPotencia: {self.potencia_kw} kW  "
            f"\nHoras de uso: {self.horas_uso}  "
            f"\n\nFases: {self.fases}  "
            f"\nConsumo diario: {self.consumo_diario():.2f} kWh "
            f"{self.verificar_consumo()}"
        )


# ==========================================================
# FUNCIONES PARA VALIDAR LOS DATOS
# ==========================================================

def ingresar_codigo():
    while True:
        codigo = input("Ingrese código del motor: ").strip()

        if codigo and codigo.isalnum():
            return codigo.upper()

        print("Error: utilice solamente letras y números.")


def ingresar_marca():
    while True:
        marca = input("Ingrese marca del motor: ").strip()

        if marca and all(palabra.isalpha() for palabra in marca.split()):
            return marca.title()

        print("Error: la marca debe contener solamente letras y espacios.")


def ingresar_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))

            if valor > 0:
                return valor

            print("Error: ingrese un número mayor que cero.")

        except ValueError:
            print("Error: ingrese un valor numérico válido.")


def ingresar_fases():
    while True:
        try:
            fases = int(input("Ingrese número de fases: "))

            if fases in (1, 2, 3):
                return fases

            print("Error: las fases permitidas son 1, 2 o 3.")

        except ValueError:
            print("Error: ingrese un número entero.")


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

motores = []

continuar = "S"

while continuar == "S":

    print("\n" + "=" * 60)
    print("REGISTRO DE MOTORES".center(60))
    print("=" * 60)

    codigo = ingresar_codigo()
    marca = ingresar_marca()

    potencia = ingresar_numero("Ingrese potencia en kW: ")
    horas = ingresar_numero("Ingrese horas de uso diario: ")

    fases = ingresar_fases()

    # Crear objeto Motor
    motor = Motor(codigo, marca, potencia, horas, fases)

    # Guardar motor en la lista
    motores.append(motor)

    print("\nMotor registrado correctamente.")

    continuar = input("\n¿Desea agregar otro motor? (S/N): ").strip().upper()

    while continuar not in ("S", "N"):
        continuar = input("Respuesta inválida. Ingrese S o N: ").strip().upper()


# ==========================================================
# REPORTE FINAL
# ==========================================================

print("\n" + "=" * 70)
print("REPORTE GENERAL DE MOTORES".center(70))
print("=" * 70)

for motor in motores:
    print(motor.describir())
    print("-" * 70)

# Resumen energético
consumo_total = sum(m.consumo_diario() for m in motores)

equipos_criticos = sum(
    1 for m in motores
    if m.consumo_diario() >= Equipo.LIMITE_CONSUMO
)

print("\n" + "=" * 70)
print("RESUMEN ENERGETICO".center(70))
print("=" * 70)

print(f"Total de motores registrados: {len(motores)}")
print(f"Consumo energético total: {consumo_total:.2f} kWh/día")
print(f"Equipos críticos: {equipos_criticos}")
print(f"Equipos normales: {len(motores) - equipos_criticos}")

print("=" * 70)
print("FIN DEL PROGRAMA".center(70))
print("=" * 70)
