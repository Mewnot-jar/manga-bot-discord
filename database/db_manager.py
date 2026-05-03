class GestorFavoritos:
    def __init__(self):
        self.memoria = {}

    def agregar_manga(self, id_usuario, nombre_manga):
        if id_usuario not in self.memoria:
            self.memoria[id_usuario] = []

        manga_minus = nombre_manga.lower()
        guardados_minus = [m.lower() for m in self.memoria[id_usuario]]

        if manga_minus in guardados_minus:
            return False
            
        self.memoria[id_usuario].append(nombre_manga)
        return True
    def obtener_mangas(self, id_usuario):
        return self.memoria.get(id_usuario, [])