from disnake.ext import commands
import disnake


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return await ctx.bot.is_owner(ctx.author)

    @commands.message_command(name="Bookmark This!")
    async def bookmark_message(self, inter: disnake.MessageCommandInteraction) -> None:
        try:
            await inter.author.send(f"Work in Progress\n{inter.author} in {inter.channel_id} in {inter.guild_id} e {inter.target.content} {inter.target.channel}")
            await inter.response.send_message("Bookmarked successfully!", ephemeral=True)
        except disnake.errors.Forbidden:

            await inter.response.send_message(f"LOL {inter.target.author.mention}, SOME CLOWN NAMED {inter.author.mention} TRIED TO BOOKMARK YOUR MESSAGE, BUT HAS DMS OFF! Laugh at this user!")


def setup(bot):
    bot.add_cog(Owner(bot))

