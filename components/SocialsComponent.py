from twitchio.ext import commands


class SocialsComponent(commands.Component):

    @commands.group(invoke_fallback=True)
    async def redes(self, ctx: commands.Context) -> None:
        """Group command for our social links.

        !redes
        """
        await ctx.send("https://discord.gg/pfYbDsZmSh, https://www.youtube.com/@pythonesa, https://blognesa.netlify.app/")

    @redes.command(name="discord", aliases=["dc"])
    async def socials_discord(self, ctx: commands.Context) -> None:
        """Sub command of socials that sends only our discord invite.

        !redes discord
        !redes dc
        """
        await ctx.send("https://discord.gg/pfYbDsZmSh")

    @redes.command(name="youtube", aliases=["yt"])
    async def socials_youtube(self, ctx: commands.Context) -> None:
        """Sub command of socials that sends only our discord invite.

        !redes youtube
        !redes yt
        """
        await ctx.send("https://www.youtube.com/@pythonesa")

    @redes.command(name="blog", aliases=["blognesa"])
    async def socials_blog(self, ctx: commands.Context) -> None:
        """Sub command of socials that sends only our discord invite.

        !redes blog
        !redes blognesa
        """
        await ctx.send("https://blognesa.netlify.app/")
