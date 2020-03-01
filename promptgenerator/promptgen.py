# prompt generator cog for Dage

# Discord
import discord
import json
import random

# Red
from redbot.core import commands, Config
from redbot.core.data_manager import bundled_data_path
from redbot.core.utils.chat_formatting import humanize_list


class Promptgen(commands.Cog):
    """Generate a prompt."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=79797979795642, force_registration=True)
        
        kink_fp = bundled_data_path(self) / "kink.json"
        extremekink_fp = bundled_data_path(self) / "extremekink.json"
        prof_fp = bundled_data_path(self) / "prof.json"
        nsfwprof_fp = bundled_data_path(self) / "nsfwprof.json"
        trope_fp = bundled_data_path(self) / "trope.json"
        nsfwtrope_fp = bundled_data_path(self) / "nsfwtrope.json"
        universe_fp = bundled_data_path(self) / "universe.json"
        
        with kink_fp.open("r") as kinks:
            self.KINKLIST = json.load(kinks)
        with extremekink_fp.open("r") as ekinks:
            self.EXTREMEKINKLIST = json.load(ekinks)
        with prof_fp.open("r") as profs:
            self.PROFLIST = json.load(profs)
        with nsfwprof_fp.open("r") as nsfwprofs:
            self.NSFWPROFLIST = json.load(nsfwprofs)
        with trope_fp.open("r") as tropes:
            self.TROPELIST = json.load(tropes)
        with nsfwtrope_fp.open("r") as nsfwtropes:
            self.NSFWTROPELIST = json.load(nsfwtropes)
        with universe_fp.open("r") as universe:
            self.UNIVERSELIST = json.load(universe)


    @commands.command(aliases=['prompts'])
    async def prompt(self, ctx, numtropes = 1, flag = " ", numkinks = 1):
        """Generate a romance prompt.

        To specify the number of tropes (challenges), just include a number. MAX: 5
        e.g. `[p]prompt 2`

        To include NSFW kinks, add the 'nsfw' flag.
        e.g. `[p]prompt nsfw`

        To include Extreme NSFW prompts, add the 'extreme' flag.
        e.g. `[p]prompt extreme`

        To specify the number of kinks, just include a number AFTER the flag. MAX: 5
        e.g. `[p]prompt 2 extreme 2`
        """

        #data validation
        if numtropes < 0 or numtropes > 5:
            return await ctx.send("Please use a number from 0-5.")
        if numkinks < 0 or numkinks > 5:
            return await ctx.send("Please use a number from 0-5.")

        #code proper
        if flag != " ":
            if flag == "extreme":
                kink = f"Kink: {humanize_list(random.choices(self.EXTREMEKINKLIST, k=numkinks))}\n"
                prof = f"{str(random.choice(self.NSFWPROFLIST))}"
                trope = f"Challenge: {humanize_list(random.choices(self.NSFWTROPELIST, k=numtropes))}"
            elif flag == "nsfw":
                kink = f"Kink: {humanize_list(random.choices(self.KINKLIST, k=numkinks))}\n"
                prof = f"{str(random.choice(self.NSFWPROFLIST))}"
                trope = f"Challenge: {humanize_list(random.choices(self.NSFWTROPELIST, k=numtropes))}"
            else:
                kink = " "
                prof = f"{str(random.choice(self.PROFLIST))}"
                trope = f"Challenge: {humanize_list(random.choices(self.TROPELIST, k=numtropes))}"  
        else:
            kink = " "
            prof = f"{str(random.choice(self.PROFLIST))}"
            trope = f"Challenge: {humanize_list(random.choices(self.TROPELIST, k=numtropes))}"    
        
        universe = f"Universe: **{str(random.choice(self.UNIVERSELIST))} AU**"

        msg = f"{universe}\n{trope}\n{kink}\nBonus: One of the characters is {prof}."

        await ctx.send(msg)

        return



        