from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram import Client , filters
from script import *
from config import *





@Client.on_callback_query(filters.regex('about'))
async def about(bot,update):
    text = script.ABOUT_TXT.format(bot.me.mention)
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "home")]
                  ])
    await update.message.edit(text = text,reply_markup = keybord)



@Client.on_message(filters.private & filters.command(["donate"]))
async def donatecm(bot,message):
    text = script.DONATE_TXT
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin",url = "https://t.me/GwitcherG"),
        InlineKeyboardButton("✖️ Close",callback_data = "cancel") ]])
    await message.reply_text(text = text,reply_markup = keybord)    



@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["admin"]))
async def admincm(bot,message):
    text = script.ADMIN_TXT
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("✖️ Close ✖️",callback_data = "cancel") ]])
    await message.reply_text(text = text,reply_markup = keybord)    



@Client.on_callback_query(filters.regex('help'))
async def help(bot,update):
    text = script.HELP_TXT.format(update.from_user.mention)
    keybord = InlineKeyboardMarkup([ 
                    [InlineKeyboardButton('🏞 Thumbnail', callback_data='thumbnail'),
                    InlineKeyboardButton('✏ Caption', callback_data='caption')],
                    [InlineKeyboardButton('🏠 Home', callback_data='home'),
                    InlineKeyboardButton('💵 Donate', callback_data='donate')]
                   ])
    await update.message.edit(text = text,reply_markup = keybord)



@Client.on_callback_query(filters.regex('thumbnail'))
async def thumbnail(bot,update):
    text = script.THUMBNAIL_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('caption'))
async def caption(bot,update):
    text = script.CAPTION_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('donate'))
async def donate(bot,update):
    text = script.DONATE_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)


@Client.on_callback_query(filters.regex('home'))
async def home_callback_handler(bot, query):
    text = f"""{query.from_user.mention} \n<b>I am an Advanced  File Renamer  Converter Bot With  Permanent and Custom  Thumbnail Support.\n\nJust Send Me Any Video or Document !!\n\nOwner - @GwitcherG</b>"""
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("📢 Updates", url="https://t.me/Unlimited_Movie_Zone"),
                    InlineKeyboardButton("💬 Support", url="https://t.me/Unlimited_Movie_Zone")],
                    [InlineKeyboardButton("🛠️ Help", callback_data='help'),
		            InlineKeyboardButton("❤️‍🩹 About", callback_data='about')],
                    [InlineKeyboardButton("🧑‍💻 Developer 🧑‍💻", url="https://t.me/GwitcherG")]
		  ])
    await query.message.edit_text(text=text, reply_markup=keybord)
