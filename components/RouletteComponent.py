import random
from twitchio.ext import commands


class RouletteComponent(commands.Component):
    def __init__(self, bot):
        self.bot = bot
        self.users_who_used_ruleta = set()  # Los que ya tiraron la suerte

    @commands.command(name="ruleta")
    async def ruleta(self, ctx: commands.Context) -> None:
        username = ctx.author.name.lower()

        if username in self.users_who_used_ruleta:
            await ctx.send(f"{username}, ya usaste la ruleta en este stream. Te toca mirar y llorar. 🛑")
            return

        self.users_who_used_ruleta.add(username)
        roll = random.random()

        vip_messages = [
            f"{username}, la ruleta te coronó VIP. 👑 Disfrutá mientras dure...",
            f"{username}, wow... te ganaste el VIP. Los astros están borrachos hoy. 🌟",
            f"{username}, VIP por obra y gracia del caos. Aprovechá, que no se repite. 🌀",
            f"{username}, el código oscuro decidió: VIP. ✨",
            f"{username}, esto es raro... ¡pero sos VIP ahora! 🎉",
            f"{username}, ascendiste al Olimpo. Bienvenida, criatura VIP. 🏛️",
            f"{username}, ni vos te la creés... pero sí, VIP. 😲",
            f"{username}, el universo glitchó y te dio VIP. Bug con estilo. 🐞💅",
            f"{username}, tu cuenta fue bendecida con el poder del VIP. 🪄",
            f"{username}, lo imposible pasó. Sos VIP. Viví como reina. 👑"
        ]

        good_messages = [
            f"{username}, la ruleta fue amable. 🌸",
            f"{username}, te salvaste... por ahora. 😌",
            f"{username}, el universo conspira a tu favor. 🍀",
            f"{username}, los dados cayeron bien. Te vas con vida. 🎲",
            f"{username}, hoy no morirás... todavía. 🕊️",
            f"{username}, te esquivó la bala digital. 💨",
            f"{username}, la suerte te guiñó el ojo. 😉",
            f"{username}, podés respirar tranquilo/a. Esta vez no. 😮‍💨",
            f"{username}, sobreviviste. Sos el/la elegido/a. 🧬",
            f"{username}, la ruleta se apiadó de vos. Milagro. 🙏"
        ]

        bad_messages = [
            f"{username}, la suerte no estuvo de tu lado. Timeout de {{duration}}s. 💀",
            f"{username}, fuiste elegida por los dioses del ban. {{duration}}s en el rincón. 👋",
            f"{username}, ruleta maldita... te ganaste {{duration}}s de silencio. 😈",
            f"{username}, castigo divino: timeout de {{duration}}s. 🔥",
            f"{username}, fue un gusto tenerte activa. Ahora, a callar. {{duration}}s. 😶",
            f"{username}, los bugs te condenaron. Timeout: {{duration}}s. 🐞🧨",
            f"{username}, caíste en la casilla de la muerte. {{duration}}s. ☠️",
            f"{username}, ni modo, te tocó. Timeout de {{duration}}s. 🎯",
            f"{username}, a reflexionar en silencio. {{duration}}s. 😔",
            f"{username}, el banhammer te rozó. {{duration}}s out. 🔨"
        ]

        if roll <= 0.05:
            await ctx.send(random.choice(vip_messages))

        elif roll <= 0.50:
            await ctx.send(random.choice(good_messages))

        else:
            duration = random.randint(10, 120)
            message = random.choice(bad_messages).replace(
                "{duration}", str(duration))
            await ctx.send(message)
