from disnake.ext import commands
import disnake


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return await ctx.bot.is_owner(ctx.author)

    @commands.message_command(name="Bookmark This!")
    async def bookmark_message(self, inter: disnake.MessageCommandInteraction):
        try:
            await inter.author.send(f"Work in Progress\n{inter.data}")
        except disnake.errors.Forbidden:
            await inter.response.send_message("LOL BOOKMARK FAILURE BECAUSE DMS ARE OFF! Laugh at this user!")


def setup(bot):
    bot.add_cog(Owner(bot))

