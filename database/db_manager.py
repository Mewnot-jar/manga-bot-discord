import sqlite3
import os

class GestorFavoritos:
    def __init__(self):

        os.mkdirs("database", exist_ok=True)

        self.conexion = sqlite3.connect("database/mangas.db")
        self.cursor = self.conexion.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS favoritos (
                id_usuario INTEGER,
                nombre_manga TEXT,
                UNIQUE(id_usuario, nombre_manga COLLATE NOCASE)
            )
        ''')
        self.conexion.commit()

    def agregar_manga(self, id_usuario, nombre_manga):
        try:
            self.cursor.execute('''
                INSERT OR IGNORE INTO favoritos (id_usuario, nombre_manga)
                VALUES (?, ?)
            ''', (id_usuario, nombre_manga))
            self.conexion.commit()

            if self.cursor.rowcount > 0:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al guardar en BD: {e}")
            return False

    def obtener_mangas(self, id_usuario):
        self.cursor.execute('''
            SELECT nombre_manga FROM favoritos WHERE id_usuario = ?
        ''', (id_usuario,))

        resultados = self.cursor.fetchall()

        lista_mangas = [fila[0] for fila in resultados]
        return lista_mangas
    
    def eliminar_manga(self, id_usuario, nombre_manga):
        try:
            self.cursor.execute('''
                DELETE FROM favoritos WHERE id_usuario = ? AND nombre_manga = ? 
            ''', (id_usuario, nombre_manga,))
            self.conexion.commit()
            if self.cursor.rowcount > 0:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al borrar en BD: {e}")
            return False