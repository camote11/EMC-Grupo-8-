class Plan:
    """Plan de suscripción: nombre, precio y si muestra anuncios."""

    def __init__(self, nombre, precio, con_anuncios):
        self.__nombre = nombre
        self.__precio = precio
        self.__con_anuncios = con_anuncios

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def tiene_anuncios(self):
        return self.__con_anuncios

    def calcular_total(self, meses):
        """Precio total por varios meses (10% de descuento desde 12 meses)."""
        total = self.__precio * meses
        if meses >= 12:
            total = total * 0.9
        return total

    def mostrar_info(self):
        anuncios = "con anuncios" if self.__con_anuncios else "sin anuncios"
        return f"Plan {self.__nombre} - ${self.__precio}/mes ({anuncios})"