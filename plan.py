<<<<<<< HEAD
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
=======
class Plan:
    def __init__(self, nombre, precio, con_anuncio):
        self.nombre = nombre
        self.precio = precio
        self.con_anuncio = con_anuncio

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def get_con_anuncio(self):
        return self.con_anuncio

    def calcular_total(self, meses):
        total = self.precio * meses
        if meses >= 12:
            total *= 0.9  # Descuento del 10% para planes de más de 12 meses
        return total

    def mostar_info(self):
        if self.con_anuncio:
            anuncio = "Incluye anuncios"
        else:
            anuncio = "No incluye anuncios"
        return "Plan" + self.nombre + " - Precio: $" + str(self.precio) + " - " + anuncio
>>>>>>> 127b57812121761483a07934805821b772de5fd0
