import sys
import asyncio

from os import execle, getenv, environ

from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait


# ------------- SESSIONS -------------

SESSION1 = getenv('SESSION1', default=None)
SESSION2 = getenv('SESSION2', default=None)
SESSION3 = getenv('SESSION3', default=None)
SESSION4 = getenv('SESSION4', default=None)
SESSION5 = getenv('SESSION5', default=None)


# ------------- CLIENTS -------------

if SESSION1:
    M1 = Client(SESSION1, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M1 = None

if SESSION2:
    M2 = Client(SESSION2, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M2 = None

if SESSION3:
    M3 = Client(SESSION3, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M3 = None

if SESSION4:
    M4 = Client(SESSION4, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M4 = None

if SESSION5:
    M5 = Client(SESSION5, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M5 = None


ONE_WORDS = ["MADARCHOD", "BHOSDIKE", "LAAAWEEE KE BAAAAAL", "MAAAAR KI JHAAAAT KE BBBBBAAAAALLLLL", "MADRCHOD..",
    "TERI MA KI CHUT..", "LWDE KE BAAALLL.", "MACHAR KI JHAAT KE BAAALLLL", "TERI MA KI CHUT M DU TAPA TAP?",
    "TERI MA KA BHOSDAA", "TERI BHN SBSBE BDI RANDI.", "TERI MA OSSE BADI RANDDDDD", "TERA BAAP CHKAAAA",
    "KITNI CHODU TERI MA AB OR..", "TERI MA CHOD DI HM NE", "MIGHTY !!  BAAP BOLTE",
    "TERI MA KE STH REELS BNEGA ROAD PEE", "TERI MA KI CHUT EK DAM TOP SEXY",
    "MALUM NA PHR KESE LETA HU M TERI MA KI CHUT TAPA TAPPPPP", "LUND KE CHODE TU KEREGA TYPIN", "SPEED PKD LWDEEEE",
    "BAAP KI SPEED MTCH KRRR", "LWDEEE", "PAPA KI SPEED MTCH NHI HO RHI KYA", "ALE ALE MELA BCHAAAA",
    "[ADARSH](t.me/AADARSH_LEGEND) TERA BAAP !!", "CHUD GYA PAPA SEEE", "KISAN KO KHODNA OR", "SALE RAPEKL KRDKA TERA",
    "HAHAHAAAAA", "KIDSSSS", "BACHHE TERI MAA KI CHUTT", "TERI BHEN KI CHUTT BHOSDIWALE",
    "TERI MA CHUD GYI AB FRAR MT HONA", "YE LDNGE BAPP SE", "KIDSSS FRAR HAHAHH", "BHEN KE LWDE SHRM KR""MADARCHOD", "BHOSDIKE", "LAAAWEEE KE BAAAAAL", "MAAAAR KI JHAAAAT KE BBBBBAAAAALLLLL", "MADRCHOD..",
    "TERI MA KI CHUT..", "LWDE KE BAAALLL.", "MACHAR KI JHAAT KE BAAALLLL", "TERI MA KI CHUT M DU TAPA TAP?",
    "TERI MA KA BHOSDAA", "TERI BHN SBSBE BDI RANDI.", "TERI MA OSSE BADI RANDDDDD", "TERA BAAP CHKAAAA",
    "KITNI CHODU TERI MA AB OR..", "TERI MA CHOD DI HM NE", "MIGHTY !!  BAAP BOLTE",
    "TERI MA KE STH REELS BNEGA ROAD PEE", "TERI MA KI CHUT EK DAM TOP SEXY",
    "MALUM NA PHR KESE LETA HU M TERI MA KI CHUT TAPA TAPPPPP", "LUND KE CHODE TU KEREGA TYPIN", "SPEED PKD LWDEEEE",
    "BAAP KI SPEED MTCH KRRR", "LWDEEE", "PAPA KI SPEED MTCH NHI HO RHI KYA", "ALE ALE MELA BCHAAAA",
    "[ADARSH](t.me/AADARSH_LEGEND) TERA BAAP !!", "CHUD GYA PAPA SEEE", "KISAN KO KHODNA OR", "SALE RAPEKL KRDKA TERA",
    "HAHAHAAAAA", "KIDSSSS", "BACHHE TERI MAA KI CHUTT", "TERI BHEN KI CHUTT BHOSDIWALE",
    "TERI MA CHUD GYI AB FRAR MT HONA", "YE LDNGE BAPP SE", "KIDSSS FRAR HAHAHH", "BHEN KE LWDE SHRM KR"]


async def pyrone(client: Client, message: Message):
    chat_id = message.chat.id
    ruser = None

    if message.reply_to_message:
        ruser = message.reply_to_message.message_id
    
    try:
        for word in ONE_WORDS:
            await client.send_chat_action(chat_id, "typing")
            await client.send_message(chat_id, word, reply_to_message_id=ruser)
            await asyncio.sleep(0.3)
    except FloodWait:
        pass


async def restart(_, __):
    args = [sys.executable, "pyrone.py"]
    execle(sys.executable, *args, environ)


# ADDING HANDLERS

if M1:
    M1.add_handler(MessageHandler(pyrone, filters.command(["RANDI KA CHODA", "MC KA AWLAD", "RANDI TERI MAA", "BAAP SE LDEGA", "RANDIKE"], prefixes=None) & filters.me))
    M1.add_handler(MessageHandler(restart, filters.command(["HAHAH", "#farar", "bisi", "#fucked"], prefixes=None) & filters.me))

if M2:
    M2.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M2.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M3:
    M3.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M3.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M4:
    M4.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M4.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M5:
    M5.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M5.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))


# STARTING CLIENTS

if M1:
    M1.start()
    M1.join_chat("TheAltron")

if M2:
    M2.start()
    M2.join_chat("TheAltron")

if M3:
    M3.start()
    M3.join_chat("TheAltron")

if M4:
    M4.start()
    M4.join_chat("TheAltron")

if M5:
    M5.start()
    M5.join_chat("TheAltron")

print("Pyrone Started Successfully")

idle()


# STOPPING CLIENTS

if M1:
    M1.stop()

if M2:
    M2.stop()

if M3:
    M3.stop()

if M4:
    M4.stop()

if M5:
    M5.stop()
