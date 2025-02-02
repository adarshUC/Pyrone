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
    "[AADARSH](t.me/JAADUGARXD) TERA BAAP !!", "CHUD GYA PAPA SEEE", "KISAN KO KHODNA OR", "SALE RAPEKL KRDKA TERA", 
    "HAHAHAAAAA", "KIDSSSS", "BACHHE TERI MAA KI CHUTT", "TERI BHEN KI CHUTT BHOSDIWALE", 
    "TERI MA CHUD GYI AB FRAR MT HONA", "YE LDNGE BAPP SE", "KIDSSS FRAR HAHAHH", "BHEN KE LWDE SHRM KR", 
    "KITNI GLIYA PDWEGA APNI MA KO", "NALLEE", "SUAR KE PILLE TERI MAAKO SADAK PR LITAKE CHOD DUNGA 😂😆🤤", 
    "ABE TERI MAAKA BHOSDA MADERCHOOD KR PILLE PAPA SE LADEGA TU 😼😂🤤", 
    "GALI GALI NE SHOR HE TERI MAA RANDI CHOR HE 💋💋💦", "ABE TERI BEHEN KO CHODU RANDIKE PILLE KUTTE KE CHODE 😂👻🔥", 
    "TERI MAAKO AISE CHODA AISE CHODA TERI MAAA BED PEHI MUTH DIA 💦💦💦💦", 
    "TERI BEHEN KE BHOSDE ME AAAG LAGADIA MERA MOTA LUND DALKE 🔥🔥💦😆😆", "RANDIKE BACHHE TERI MAAKO CHODU CHAL NIKAL", 
    "KITNA CHODU TERI RANDI MAAKI CHUTH ABB APNI BEHEN KO BHEJ 😆👻🤤", 
    "TERI BEHEN KOTO CHOD CHODKE PURA FAAD DIA CHUTH ABB TERI GF KO BHEJ 😆💦🤤", 
    "TERI GF KO ETNA CHODA BEHEN KE LODE TERI GF TO MERI RANDI BANGAYI ABB CHAL TERI MAAKO CHODTA FIRSE ♥️💦😆😆😆😆", 
    "HARI HARI GHAAS ME JHOPDA TERI MAAKA BHOSDA 🤣🤣💋💦", "CHAL TERE BAAP KO BHEJ TERA BASKA NHI HE PAPA SE LADEGA TU", 
    "TERI BEHEN KI CHUTH ME BOMB DALKE UDA DUNGA MAAKE LAWDE", 
    "TERI MAAKO TRAIN ME LEJAKE TOP BED PE LITAKE CHOD DUNGA SUAR KE PILLE 🤣🤣💋💋",  
    "TERI MAAAKE NUDES GOOGLE PE UPLOAD KARDUNGA BEHEN KE LAEWDE 👻🔥",
    "TERI MAAAKE NUDES GOOGLE PE UPLOAD KARDUNGA BEHEN KE LAEWDE 👻🔥", 
    "TERI BEHEN KO CHOD CHODKE VIDEO BANAKE XNXX.COM PE NEELAM KARDUNGA KUTTE KE PILLE 💦💋", 
    "TERI MAAAKI CHUDAI KO PORNHUB.COM PE UPLOAD KARDUNGA SUAR KE CHODE 🤣💋💦", 
    "ABE TERI BEHEN KO CHODU RANDIKE BACHHE TEREKO CHAKKO SE PILWAVUNGA RANDIKE BACHHE 🤣🤣", 
    "TERI MAAKI CHUTH FAADKE RAKDIA MAAKE LODE JAA ABB SILWALE 👄👄", "TERI BEHEN KI CHUTH ME MERA LUND KAALA", 
    "TERI BEHEN LETI MERI LUND BADE MASTI SE TERI BEHEN KO MENE CHOD DALA BOHOT SASTE SE",  
    "BETE TU BAAP SE LEGA PANGA TERI MAAA KO CHOD DUNGA KARKE NANGA 💦💋", 
    "HAHAHAH MERE BETE AGLI BAAR APNI MAAKO LEKE AAYA MATH KAT OR MERE MOTE LUND SE CHUDWAYA MATH KAR", 
    "CHAL BETA TUJHE MAAF KIA 🤣 ABB APNI GF KO BHEJ", 
    "SHARAM KAR TERI BEHEN KA BHOSDA KITNA GAALIA SUNWAYEGA APNI MAAA BEHEN KE UPER", 
    "ABE RANDIKE BACHHE AUKAT NHI HETO APNI RANDI MAAKO LEKE AAYA MATH KAR HAHAHAHA",  
    "KIDZ MADARCHOD TERI MAAKO CHOD CHODKE TERR LIYE BHAI DEDIYA", 
    "JUNGLE ME NACHTA HE MORE TERI MAAKI CHUDAI DEKKE SAB BOLTE ONCE MORE ONCE MORE 🤣🤣💦💋", 
    "GALI GALI ME REHTA HE SAND TERI MAAKO CHOD DALA OR BANA DIA RAND 🤤🤣", 
    "SAB BOLTE MUJHKO PAPA KYOUNKI MENE BANADIA TERI MAAKO PREGNENT 🤣🤣", 
    "SUAR KE PILLE TERI MAAKI CHUTH ME SUAR KA LOUDA OR TERI BEHEN KI CHUTH ME MERA LODA", 
    "CHAL CHAL APNI MAAKI CHUCHIYA DIKA", "HAHAHAHA BACHHE TERI MAAAKO CHOD DIA NANGA KARKE", 
    "TERI GF HE BADI SEXY USKO PILAKE CHOODENGE PEPSI", "2 RUPAY KI PEPSI TERI MUMMY SABSE SEXY 💋💦", 
    "TERI MAAKO CHEEMS SE CHUDWAVUNGA MADERCHOOD KE PILLE 💦🤣", 
    "TERI BEHEN KI CHUTH ME MUTHKE FARAR HOJAVUNGA HUI HUI HUI", "SPEED LAAA TERI BEHEN CHODU RANDIKE PILLE 💋💦🤣", 
    "ARE RE MERE BETE KYOUN SPEED PAKAD NA PAAA RAHA APNE BAAP KA HAHAH🤣🤣", 
    "SUN SUN SUAR KE PILLE JHANTO KE SOUDAGAR APNI MUMMY KI NUDES BHEJ", "ABE SUN LODE TERI BEHEN KA BHOSDA FAAD DUNGA", 
    "TERI MAAKO KHULE BAJAR ME CHOD DALA 🤣🤣💋", "SHRM KR", "MERE LUND KE BAAAAALLLLL", 
    "KITNI GLIYA PDWYGA APNI MA BHEN KO", "RNDI KE LDKEEEEEEEEE", "KIDSSSSSSSSSSSS", "Apni gaand mein muthi daal", 
    "Apni lund choos", "Apni ma ko ja choos", "Bhen ke laude", "Bhen ke takke", "Abla TERA KHAN DAN CHODNE KI BARIII", 
    "BETE TERI MA SBSE BDI RAND", "LUND KE BAAAL JHAT KE PISSSUUUUUUU", "LUND PE LTKIT MAAALLLL KI BOND H TUUU", 
    "KASH OS DIN MUTH MRKE SOJTA M TUN PAIDA NA HOTAA", "GLTI KRDI TUJW PAIDA KRKE", "SPEED PKDDD", 
    "Gaand main LWDA DAL LE APNI MERAAA", "Gaand mein bambu DEDUNGAAAAAA", "GAND FTI KE BALKKK", 
    "Gote kitne bhi bade ho, lund ke niche hi rehte hai", "Hazaar lund teri gaand main", "Jhaant ke pissu-", 
    "TERI MA KI KALI CHUT", "Khotey ki aulad", "Kutte ka awlad", "Kutte ki jat", "Kutte ke tatte", 
    "TETI MA KI.CHUT , tERI MA RNDIIIIIIIIIIIIIIIIIIII", "Lavde ke bal", "muh mei lele", "Lund Ke Pasine", 
    "MERE LWDE KE BAAAAALLL", "HAHAHAAAAAA", "CHUD GYAAAAA", "Randi khanE KI ULADDD", "Sadi hui gaand", 
    "Teri gaand main kute ka lund", "Teri maa ka bhosda", "Teri maa ki chut", "Tere gaand mein keede paday", 
    "Ullu ke pathe", "SUNN MADERCHOD", "TERI MAA KA BHOSDA", "BEHEN K LUND", "TERI MAA KA CHUT KI CHTNIIII", 
    "MERA LAWDA LELE TU AGAR CHAIYE TOH", "GAANDU", "CHUTIYA", "TERI MAA KI CHUT PE JCB CHADHAA DUNGA", "SAMJHAA LAWDE", 
    "YA DU TERE GAAND ME TAPAA TAP��", "TERI BEHEN MERA ROZ LETI HAI", "TERI GF K SAATH MMS BANAA CHUKA HU���不�不", 
    "TU CHUTIYA TERA KHANDAAN CHUTIYA", "AUR KITNA BOLU BEY MANN BHAR GAYA MERA�不", 
    "TERIIIIII MAAAA KI CHUTTT ME ABCD LIKH DUNGA MAA KE LODE", "TERI MAA KO LEKAR MAI FARAR", "RANIDIII", "BACHEE", 
    "CHODU", "RANDI", "RANDI KE PILLE", "TERIIIII MAAA KO BHEJJJ", "TERAA BAAAAP HU",  
    "teri MAA KI CHUT ME HAAT DAALLKE BHAAG JAANUGA", "Teri maa KO SARAK PE LETAA DUNGA", 
    "TERI MAA KO GB ROAD PE LEJAKE BECH DUNGA", "Teri maa KI CHUT MÉ KAALI MITCH", "TERI MAA SASTI RANDI HAI", 
    "TERI MAA KI CHUT ME KABUTAR DAAL KE SOUP BANAUNGA MADARCHOD", "TERI MAAA RANDI HAI", 
    "TERI MAAA KI CHUT ME DETOL DAAL DUNGA MADARCHOD", "TERI MAA KAAA BHOSDAA", "TERI MAA KI CHUT ME LAPTOP", 
    "Teri maa RANDI HAI", "TERI MAA KO BISTAR PE LETAAKE CHODUNGA", "TERI MAA KO AMERICA GHUMAAUNGA MADARCHOD", 
    "TERI MAA KI CHUT ME NAARIYAL PHOR DUNGA", "TERI MAA KE GAND ME DETOL DAAL DUNGA", 
    "TERI MAAA KO HORLICKS PILAUNGA MADARCHOD", "TERI MAA KO SARAK PE LETAAA DUNGAAA", "TERI MAA KAA BHOSDA", 
    "MERAAA LUND PAKAD LE MADARCHOD", "CHUP TERI MAA AKAA BHOSDAA", "TERIII MAA CHUF GEYII KYAAA LAWDEEE", 
    "TERIII MAA KAA BJSODAAA", "MADARXHODDD", "TERIUUI MAAA KAA BHSODAAA", 
    "TERIIIIII BEHENNNN KO CHODDDUUUU MADARXHODDDD", "NIKAL MADARCHOD", "RANDI KE BACHE", "TERA MAA MERI FAN", 
    "TERI SEXY BAHEN KI CHUT OP"]


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
