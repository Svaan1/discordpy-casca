import random
from discord import Interaction
from discord import app_commands
from discord.ext import commands

COMRADE_FRASES = ["comrade está com a macaca",
                  "vou te mutar",
                  "pajé merda" ,
                  "tudo tem limite",
                  "gente eu não bebo",
                  "que jogo é esse (the sims medieval)",
                  "eca doete",
                  "vou mutar o comrade",
                  "vai ficar conversando ai",
                  "vento do oeste",
                  "comrade acha engraçado ficar parado em um jogo de sniper",
                  "newton temos um problema",
                  "comrade vc n é engraçado",
                  "tá na praia comrade?"
                  ]

class Cavernosos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="comrade")
    async def comrade(self, interaction: Interaction):
        random_message = random.choice(COMRADE_FRASES)

        await interaction.response.send_message(random_message)

async def setup(bot):
    await bot.add_cog(Cavernosos(bot))