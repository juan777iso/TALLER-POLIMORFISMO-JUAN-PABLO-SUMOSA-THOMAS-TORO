class VehiculoAutonomo():
    def __init__(self, codigo, nivel_bateria):
        self.codigo = codigo
        self.nivel_bateria = nivel_bateria
        self.distancia_recorrida = 0

    def mover(self, distancia):
        pass

    def calcular_consumo(self, distancia):
        pass


class AutomovilElectrico(VehiculoAutonomo):
    def __init__(self, codigo, nivel_bateria, consumo_por_km):
        super().__init__(codigo, nivel_bateria)
        self.consumo_por_km = consumo_por_km

    def calcular_consumo(self, distancia):
        return distancia * self.consumo_por_km

    def mover(self, distancia):
        consumo = self.calcular_consumo(distancia)
        tipo = "Automovil electrico"
        if consumo > self.nivel_bateria:
            return f"[{self.codigo}] {tipo}: no se puede recorrer {distancia} km, se necesitan {consumo} y solo hay {self.nivel_bateria} de bateria disponible"
        self.distancia_recorrida += distancia
        self.nivel_bateria -= consumo
        return f"[{self.codigo}] {tipo}: recorrio {distancia} km, consumio {consumo} de bateria, bateria restante {self.nivel_bateria}"


class Dron(VehiculoAutonomo):
    def __init__(self, codigo, nivel_bateria, altura_vuelo):
        super().__init__(codigo, nivel_bateria)
        self.altura_vuelo = altura_vuelo

    def calcular_consumo(self, distancia):
        return distancia * 0.5 + self.altura_vuelo * 0.5

    def mover(self, distancia):
        consumo = self.calcular_consumo(distancia)
        tipo = "Dron"
        if consumo > self.nivel_bateria:
            return f"[{self.codigo}] {tipo}: no se puede recorrer {distancia} km, se necesitan {consumo} y solo hay {self.nivel_bateria} de bateria disponible"
        self.distancia_recorrida += distancia
        self.nivel_bateria -= consumo
        return f"[{self.codigo}] {tipo}: recorrio {distancia} km, consumio {consumo} de bateria, bateria restante {self.nivel_bateria}"


class RobotTerrestre(VehiculoAutonomo):
    def __init__(self, codigo, nivel_bateria, peso_carga):
        super().__init__(codigo, nivel_bateria)
        self.peso_carga = peso_carga

    def calcular_consumo(self, distancia):
        return distancia * 0.3 + self.peso_carga * 0.2

    def mover(self, distancia):
        consumo = self.calcular_consumo(distancia)
        tipo = "Robot terrestre"
        if consumo > self.nivel_bateria:
            return f"[{self.codigo}] {tipo}: no se puede recorrer {distancia} km, se necesitan {consumo} y solo hay {self.nivel_bateria} de bateria disponible"
        self.distancia_recorrida += distancia
        self.nivel_bateria -= consumo
        return f"[{self.codigo}] {tipo}: recorrio {distancia} km, consumio {consumo} de bateria, bateria restante {self.nivel_bateria}"


lista_vehiculos = [
    AutomovilElectrico("AE-01", 100, 5),
    Dron("DR-01", 50, 20),
    RobotTerrestre("RT-01", 80, 30),
    Dron("DR-02", 5, 50), ]

distancia_a_recorrer = 10

for vehiculo in lista_vehiculos:
    print(vehiculo.mover(distancia_a_recorrer))