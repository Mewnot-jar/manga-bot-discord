# 📖 Manga Discord Bot

![Estado: En Desarrollo](https://img.shields.io/badge/Estado-En%20Desarrollo-orange)

Un bot de Discord desarrollado en Python que permite buscar información de mangas en tiempo real utilizando la API de Jikan (MyAnimeList), además de gestionar una biblioteca personal de favoritos para cada usuario. El bot extrae datos, traduce las sinopsis automáticamente al español y utiliza una base de datos local para almacenar tus lecturas de forma permanente.

## ✨ Características Principales

*   **Búsqueda en tiempo real:** Encuentra mangas y obtén detalles precisos usando la API de Jikan.
*   **Traducción automática:** Las sinopsis en inglés se traducen al español utilizando `deep-translator`.
*   **Persistencia de Datos (SQLite):** Los usuarios pueden guardar y eliminar mangas de su colección personal. La información se almacena de forma segura en una base de datos relacional local.
*   **Estructura Modular (Cogs):** El código está organizado mediante Cogs de `discord.py` (ej. buscador, gestor de favoritos), facilitando la escalabilidad del backend.
*   **Seguridad:** Uso de variables de entorno (`.env`) para proteger las credenciales y exclusión de archivos de base de datos en el control de versiones.

## 🛠️ Tecnologías utilizadas

*   **Python 3**
*   **discord.py** - Framework asíncrono para la API de Discord.
*   **sqlite3** - Motor de base de datos relacional integrado (sin dependencias externas).
*   **aiohttp** - Para peticiones web asíncronas.
*   **deep-translator** - Para la traducción de textos.
*   **Jikan API v4** - API RESTful de MyAnimeList.

## 🚀 Instalación y uso local

Sigue estos pasos para configurar y correr el bot en tu propia máquina.

### 💡 Nota sobre Entornos Virtuales
Se recomienda fuertemente usar un entorno virtual (`venv`) para aislar las dependencias del proyecto.

### 1. Instalar las dependencias
Asegúrate de estar en la raíz del proyecto y ejecuta:
```bash
pip install discord.py aiohttp deep-translator python-dotenv
```
*(Nota: `sqlite3` y `os` vienen preinstalados en la librería estándar de Python, no requieren instalación).*

### 2. Configurar las credenciales
1. Crea un archivo llamado `.env` en la raíz del proyecto.
2. Consigue tu Token en el [Discord Developer Portal](https://discord.com/developers/applications).
3. Pega tu token en el archivo `.env` con el siguiente formato:
```env
DISCORD_TOKEN=tu_token_secreto_aqui
```

### 3. Iniciar el bot
Ejecuta el archivo principal. Al iniciar por primera vez, el código creará automáticamente la carpeta `database` y el archivo `mangas.db` para gestionar los datos de los usuarios.
```bash
python main.py
```

---

## 🎮 Comandos disponibles

*   `!manga <nombre>`: Busca un manga específico y muestra su portada, puntaje, estado y sinopsis en español.
*   `!guardar <nombre>`: Añade un manga a tu base de datos personal. Evita duplicados automáticamente.
*   `!borrar <nombre>`: Elimina un manga específico de tu lista.
*   `!mismangas`: Despliega tu biblioteca personal de mangas guardados.

---

## 🧠 Bitácora de Desarrollo y Troubleshooting

Durante la creación y evolución de este bot, apliqué las siguientes prácticas de arquitectura y seguridad:

1. **Gestión de Secretos y `.gitignore`:** 
   Se implementó la librería `python-dotenv` para aislar el Token de Discord. Se configuró el `.gitignore` para omitir el `.env`, los binarios `__pycache__` y los archivos de base de datos (`*.db`, `*.sqlite3`), evitando filtraciones en GitHub.

2. **Limpieza de Historial en Git:**
   Ante una filtración accidental en un commit inicial, limpié y reinicié el historial de Git local (`Remove-Item -Recurse -Force .git`), inicialicé el repositorio nuevamente y forcé el push a la rama `main` para purgar los secretos del historial remoto.

3. **Arquitectura Limpia (Separación de Capas):**
   El código evolucionó de un script monolítico a una arquitectura por capas. Los comandos de Discord (Cogs) actúan únicamente como la capa de interfaz, mientras que las operaciones CRUD de SQLite fueron aisladas en una clase independiente (`GestorFavoritos` en `db_manager.py`), permitiendo escalar la base de datos sin afectar la lógica del bot.

4. **Prevención de Errores de Entorno en Despliegue:**
   Para evitar problemas de "Directorio no encontrado" en entornos nuevos (ya que Git no rastrea carpetas vacías), implementé `os.makedirs("database", exist_ok=True)` en el inicializador de la base de datos.

## 👨‍💻 Autor
Desarrollado por Mewnot-jar.

## 📝 Licencia
Este proyecto es de código abierto y está disponible para fines educativos y de práctica en desarrollo de backend e integración de APIs.