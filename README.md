# 📖 Manga Discord Bot

Un bot de Discord desarrollado en Python que permite buscar información de mangas en tiempo real utilizando la API de Jikan (MyAnimeList). El bot extrae los datos, traduce las sinopsis automáticamente al español y las presenta en un formato visual atractivo mediante Embeds.

## ✨ Características

*   **Búsqueda rápida:** Encuentra mangas usando el comando `!manga`.
*   **Traducción automática:** Las sinopsis en inglés son traducidas al español en tiempo real utilizando `deep-translator`.
*   **Diseño visual:** Las respuestas se envían en formato **Embed**, mostrando la portada del manga, puntaje, cantidad de capítulos y estado de publicación.
*   **Estructura Modular (Cogs):** El código está organizado mediante Cogs de `discord.py`, lo que facilita el mantenimiento, la escalabilidad y la lectura del código.
*   **Seguridad:** Uso de variables de entorno (`.env`) para mantener el Token de Discord seguro y fuera del control de versiones.

## 🛠️ Tecnologías utilizadas

*   [Python 3](https://www.python.org/)
*   [discord.py](https://discordpy.readthedocs.io/) - Framework para la API de Discord.
*   [aiohttp](https://docs.aiohttp.org/) - Para peticiones asíncronas.
*   [deep-translator](https://pypi.org/project/deep-translator/) - Para la traducción de textos.
*   [Jikan API v4](https://docs.jikan.moe/) - API no oficial de MyAnimeList.
