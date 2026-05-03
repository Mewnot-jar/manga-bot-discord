import discord
from discord.ext import commands
import aiohttp
from deep_translator import GoogleTranslator

class MangaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.estados_es = {
            "Finished": "Finalizado",
            "Publishing": "En emision",
            "On Hiatus": "En pausa",
            "Discontinued": "Descontinuado",
            "Not yet published": "Aun no publicado",
        }

    @commands.command(name="manga")
    async def buscar_manga(self, ctx, *, nombre_manga):
        url = f"https://api.jikan.moe/v4/manga?q={nombre_manga}&limit=1"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    json_data = await response.json()
                    lista_resultados = json_data.get('data', [])

                    if not lista_resultados:
                        await ctx.send(f"No se ha encontrado el manga {nombre_manga}")
                        return
                        
                    manga = lista_resultados[0]

                    sinopsis_en = manga.get('synopsis', 'Sin descripcion disponible.')
                    if sinopsis_en != 'Sin descripcion disponible.':
                        sinopsis_es = GoogleTranslator(source='en', target='es').translate(sinopsis_en)
                    else:
                        sinopsis_es = sinopsis_en
                        
                    estado_en = manga.get('status', 'Desconocido')
                    estado_es = self.estados_es.get(estado_en, estado_en)

                    embed = discord.Embed(
                        title=manga.get('title', 'Titulo desconocido'),
                        description=f"{sinopsis_es}",
                        color=discord.Color.dark_red(),
                        url=manga.get('url', '')
                    )

                    imagen = manga['images']['jpg']['large_image_url']
                    embed.set_thumbnail(url=imagen)

                    embed.add_field(name="⭐ Puntaje", value=manga.get('score', 'N/A'), inline=True)
                    embed.add_field(name="📚 Volumenes", value=manga.get('volumes', 'N/A'), inline=True)
                    embed.add_field(name="📌 Estado", value=estado_es, inline=True)

                    embed.set_footer(text="Datos de MyAnimeList | Traducido al español")

                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Error al conectar con el servidor")

async def setup(bot):
    print("¡Cargando el módulo de Manga!")
    await bot.add_cog(MangaCog(bot))