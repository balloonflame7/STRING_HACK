import os
import logging
import asyncio
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from RAUSHAN.Helpers.data import LOG_TEXT
from pyromod import listen 

#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
START_PIC = Config.START_PIC



if not START_PIC:
    START_PIC = "https://pbs.twimg.com/profile_images/1283191609530691586/jyRaqQhO_400x400.jpg"

#rich
LOG = Console()

#logger
logging.basicConfig(level=logging.INFO)

#client
app = Client(
    "SupremeStark",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    


async def RAUSHAN():
    os.system("clear")
    header = Table(show_header=True, header_style="bold green")
    header.add_column(LOG_TEXT)
    LOG.print(header)
    LOG.print(f"[bold cyan]Nobita Bots")
    LOG.print("[bold yellow]𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭.............")
    await app.start()    
    


loop = asyncio.get_event_loop()
loop.run_until_complete(RAUSHAN())    
