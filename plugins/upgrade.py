from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client , filters




@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
    text = """**Free Plan User**
Daily  Upload limit 5GB
Price 0

**🪙 Basic**
Daily  Upload  limit 20GB
Price Rs 150  LKR/🌎 0.5$  per Month

**⚡ Standard**
Daily Upload limit 50GB
Price Rs 300  LKR /🌎 1$  per Month

**💎 Pro**
Daily Upload limit 100GB
Price Rs 600  LKR /🌎 2$  per Month

Payment Details :-
<b>➜ Contact Developer to Get Payment Options @GwitcherG </b>

After Payment Send Screenshots Of Payment To Admin @GwitcherG"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://t.me/GwitcherG"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await update.message.edit(text = text,reply_markup = keybord, disable_web_page_preview=True)
    
    

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
    text = """**Free Plan User**
Daily  Upload limit 5GB
Price 0

**🪙 Basic**
Daily  Upload  limit 20GB
Price Rs 150  LKR /🌎 0.5$  per Month

**⚡ Standard**
Daily Upload limit 50GB
Price Rs 300  LKR /🌎 1$  per Month

**💎 Pro**
Daily Upload limit 100GB
Price Rs 600  LKR /🌎 2$  per Month

Payment Details :-
<b>➜ Contact Developer to Get Payment Options @GwitcherG </b>

After Payment Send Screenshots Of Payment To Admin @GwitcherG"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://t.me/GwitcherG"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await message.reply_text(text=text, reply_markup=keybord, quote=True, disable_web_page_preview=True)
