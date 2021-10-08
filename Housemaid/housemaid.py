import disnake
from disnake.ext import commands
import dotenv
import logging
import os


dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = disnake.Intents.default()
prefix = ">>"
bot = commands.Bot(command_prefix=prefix, intents=intents, test_guilds=[])
logging.basicConfig(level='INFO', filename='maidlog.txt', filemode='w')
startup_cogs = ['cogs.owner']

if __name__ == "__main__":
    logging.info("Starting bot...")

    for extension in startup_cogs:
        try:
            bot.load_extension(extension)
        except: # fix bare except
            logging.error(f"Loading {extension} failed.")
        else:
            logging.info(f"Started {extension}...")

    bot.run(TOKEN)

