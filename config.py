# TEAM BALLOONFLAME7 ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "27079591"
    API_HASH = "c81ae4c3dc026ea4bf49842a8ce4a5f9"
    TOKEN = "8198847203:AAG_HuB34GjqAjN2YFHLiOrpo3btdYz5epE"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://vivek:1234567890@cluster0.c48d8ih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    START_PIC = "https://files.catbox.moe/ppvvg0.jpg"
    SUDOERS = filters.user(["6730956183"])
