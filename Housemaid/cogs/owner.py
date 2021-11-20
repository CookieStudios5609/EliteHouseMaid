from disnake.ext import commands
import disnake
import datetime


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx) -> bool:
        return await ctx.bot.is_owner(ctx.author)

    @commands.message_command(name="Bookmark This!")
    async def bookmark_message(self, inter: disnake.MessageCommandInteraction) -> None:
        try:
            embed_response = disnake.Embed(color=inter.target.author.color, timestamp=datetime.datetime.utcnow())
            embed_response.set_thumbnail(url=inter.target.author.avatar.url)
            embed_response.set_author(name=f"Message in #{inter.target.channel.name} in {inter.guild.name}", icon_url=f"{inter.guild.icon}")
            embed_response.add_field(name=f"Message from {inter.target.author} ({inter.target.author.name}", value=f"[{inter.target.content}]({inter.target.jump_url})")
            embed_response.set_footer(text=f"{self.bot.user}")
            await inter.author.send(embed=embed_response)
            await inter.response.send_message("Check your DMs!", ephemeral=True, delete_after=5.0)
        except disnake.errors.Forbidden:

            await inter.response.send_message(f"LOL {inter.target.author.mention}, SOME CLOWN NAMED {inter.author.mention} TRIED TO BOOKMARK YOUR MESSAGE, BUT HAS DMS OFF! Laugh at this user!")


def setup(bot):
    bot.add_cog(Owner(bot))

