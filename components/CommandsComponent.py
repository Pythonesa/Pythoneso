from twitchio.ext import commands


class CommandsComponent(commands.Component):

    @commands.command(name="comandos")
    async def commands(self, ctx: commands.Context) -> None:
        await ctx.send("Puedes ver mis comandos en: https://comandos.netlify.app/")
