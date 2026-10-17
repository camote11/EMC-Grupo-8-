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