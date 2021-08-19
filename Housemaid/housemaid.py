import discord
from discord.ext import commands
import dotenv
import logging
import os


dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
prefix = ">>"
bot = commands.Bot(command_prefix=prefix, intents=intents)
logging.basicConfig(level='INFO', filename='maidlog.txt', filemode='w')
startup_cogs = ['jishaku', 'cogs.Owner']

if __name__ == "__main__":
    logging.info("Starting bot...")

    for extension in startup_cogs:
        try:
            bot.load_extension(extension)
        except:
            logging.error(f"Loading {extension} failed.")
        else:
            logging.info(f"Started {extension}...")

    bot.run(TOKEN)

