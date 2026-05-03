import discord
from discord.ext import commands
from database.db_manager import GestorFavoritos

db = GestorFavoritos()

class FavoritosCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="guardar")
    async def guardar_manga(self, ctx, *, nombre_manga):
        id_usuario = ctx.author.id
        exito = db.agregar_manga(id_usuario, nombre_manga)
        print(exito)
        if exito:
            await ctx.send(f"{ctx.author.name}, has guardado el manga: {nombre_manga} en tu lista de favoritos.")
        else:
            await ctx.send(f"Ya tienes {nombre_manga} en tu lista de favoritos.")
    
    @commands.command(name="mismangas")
    async def ver_mangas(self, ctx):
        id_usuario = ctx.author.id
        mangas_usuario = db.obtener_mangas(id_usuario)

        if not mangas_usuario:
            await ctx.send(f"Todavia no tienes ningun manga guardado.")
        
        embed = discord.Embed(
            title=f"Biblioteca de {ctx.author.name}",
            color=discord.Color.green()
        )

        lista_formateada = ""
        for i, manga in enumerate(mangas_usuario, 1):
            lista_formateada += f"{i}.{manga.capitalize()} "

        embed.description = lista_formateada if lista_formateada else "No has agregado nada aun."
        await ctx.send(embed=embed)

async def setup(bot):
    print("Cargando el modulo de favoritos.")
    await bot.add_cog(FavoritosCog(bot))