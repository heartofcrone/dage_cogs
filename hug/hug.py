# Give someone an anime hug!

# Discord
import discord

# Other Libs
import json
import random

# Red
from redbot.core import commands, checks, Config
from redbot.core.data_manager import bundled_data_path

class Hug(commands.Cog):
    """Give someone an anime hug!"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=99978023461, force_registration=True)

        gifs_fp = bundled_data_path(self) / "gifs.json"
        with gifs_fp.open("r", encoding='utf-8') as gifs:
            self.gifs = json.load(gifs)
    
    @commands.guild_only()
    @commands.command()
    async def hug(self, ctx, huggee: discord.Member):
        """Give someone a hug!"""

        gif = random.choice(self.gifs)
        title = f"**{ctx.author.nick}** hugs **{huggee.nick}**..."

        em_perms = ctx.channel.permissions_for(ctx.me).embed_links

        if em_perms is True:
            data = discord.Embed(title=title)
            data.set_image(url=gif)
            msg = await ctx.send(embed=data)
        else:
            msg = await ctx.send(f"{title}\n{gif}")

        return