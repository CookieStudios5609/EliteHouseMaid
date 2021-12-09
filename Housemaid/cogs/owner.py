from disnake.ext import commands
import disnake
import datetime


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx) -> bool:
        return await ctx.bot.is_owner(ctx.author)


def setup(bot):
    bot.add_cog(Owner(bot))

