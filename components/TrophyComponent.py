import random
from twitchio.ext import commands


class TrophyComponent(commands.Component):
    def __init__(self, bot):
        self.bot = bot
        self.given_trophies = {}  # user: trophy
        self.trophy_sequence = [
            "Trofeo del Código Antiguo",
            "Cristal del Conocimiento",
            "Fragmento de la Matrix"
        ]

    @commands.command(name="trofeo")
    async def give_trophy(self, ctx: commands.Context) -> None:
        username = ctx.author.name.lower()

        if username in self.given_trophies:
            already_has_messages = [
                f"{username}, ya tenés tu trofeo. Esto no es Hogwarts, no hay puntos extra para tu casa.",
                f"{username}, ¿querés otro? Esto no es Steam. Uno por alma, y ya fue.",
                f"{username}, la avaricia rompe el stream. Ya tenés uno, compartí.",
                f"{username}, el sistema es claro: un trofeo, un mortal. Estás fuera.",
                f"{username}, la vida es injusta. Ganaste algo, dejá que los demás sufran ahora."
            ]
            await ctx.send(random.choice(already_has_messages))
            return

        if len(self.given_trophies) >= 3:
            no_more_messages = [
                f"{username}, llegaste tarde... ya no hay lugar en el podio. Mirá y aprendé.",
                f"{username}, se acabaron los trofeos. Andá a hacer memes de tu fracaso.",
                f"{username}, llegaste con lag. No quedan trofeos. Lo intentaste (más o menos).",
                f"{username}, no hay más lugar en la gloria. Volvé en el próximo stream.",
                f"{username}, el drop ya fue. GG, sin loot para vos."
            ]
            await ctx.send(random.choice(no_more_messages))
            return

        trophy = self.trophy_sequence[len(self.given_trophies)]
        self.given_trophies[username] = trophy

        trophy_messages = {
            "Trofeo del Código Antiguo": [
                f"{username} invocó scripts milenarios y se lleva el Trofeo del Código Antiguo. Nadie lo vio venir. 💻⚡",
                f"{username} fue más rápido que un script roto y se lleva el Trofeo del Código Antiguo.",
                f"{username} activó modo dios en el stream. Trofeo del Código Antiguo asegurado. 🧠✨",
                f"El código fluye por {username}. El Trofeo del Código Antiguo es suyo ahora.",
                f"{username} tocó el teclado primero. Trofeo del Código Antiguo asegurado, con lag y todo."
            ],
            "Cristal del Conocimiento": [
                f"{username} no ganó oro pero brilla como respuesta top de Stack Overflow. Cristal del Conocimiento ganado. 📚💡",
                f"Segundo lugar, primera en sabiduría. {username} se lleva el Cristal del Conocimiento.",
                f"{username} llegó un poco tarde pero con toda la curiosidad. El Cristal del Conocimiento es tuyo. 🔍",
                f"No fue la más rápida, pero sí la más clever. {username}, Cristal del Conocimiento para vos.",
                f"{username} no ganó, pero es más inteligente que la media. Cristal del Conocimiento incoming."
            ],
            "Fragmento de la Matrix": [
                f"{username} se metió al podio como un push sin tests. Fragmento de la Matrix desbloqueado. 🧑‍💻🔮",
                f"{username} se desliza en tercer lugar. Fragmento de la Matrix es tuyo.",
                f"{username} agarró el cable justo a tiempo. Fragmento de la Matrix concedido.",
                f"{username} llegó por milisegundos. Fragmento de la Matrix en tus manos.",
                f"{username}, ¿bronce? No, Fragmento de la Matrix. Estilo ante todo."
            ]
        }

        await ctx.send(random.choice(trophy_messages[trophy]))

    @commands.command(name="podio")
    async def show_podium(self, ctx: commands.Context) -> None:
        if not self.given_trophies:
            await ctx.send("Todavía nadie se llevó un trofeo. ¿Qué pasa, están dormidos?")
            return

        podium_lines = []
        for trophy in self.trophy_sequence:
            owner = next(
                (user for user, t in self.given_trophies.items() if t == trophy), None)
            if owner:
                podium_lines.append(f"{trophy}: {owner}")
            else:
                podium_lines.append(f"{trophy}: ---")

        message = "🏆 Podio actual:\n" + " | ".join(podium_lines)
        await ctx.send(message)
