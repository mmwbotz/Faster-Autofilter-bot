from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters, enums

@Client.on_message(filters.command('help'))
async def ai_generate_private(client, message):
    buttons = [[
            InlineKeyboardButton('⚙️ 𝘽𝙤𝙩 𝙈𝙤𝙫𝙞𝙚 𝙂𝙧𝙤𝙪𝙥 ⚙️', url='https://t.me/mallumovieworldmain'),
            ],[
            InlineKeyboardButton(' ⚓ 𝙊𝙏𝙏 𝙈𝙤𝙫𝙞𝙚 𝙂𝙧𝙤𝙪𝙥 ⚓ ', url='https://t.me/+4JzWwDjdd9xjN2I9'),
            ],[
            InlineKeyboardButton('💻 𝙊𝙏𝙏 𝙐𝙥𝙙𝙖𝙩𝙚 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 💻', url='https://t.me/mallumovieworldmain1')
        ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    # Use triple quotes for multi-line string
    await message.reply_text(
        text="""❗️How to Search Movies Here❓
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
1. Just Send Movie Name and Movie Released Year Correctly.
(Check Google for Correct Movie Spelling and Movie Released Year)

Examples: -
Oppam 2016
Baahubali 2015 1080p
(For Getting only 1080p Quality Files)
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Baahubali 2015 Malayalam
Baahubali 2015 Tamil
(For Dubbed Movie Files)
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
❗️On Android, Better Use VLC Media Player For Watch Movie's.
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Cᴏɴᴛᴀᴄᴛ Bᴏᴛ Dᴇᴠᴇʟᴏᴘᴇʀ (Oʀ) Rᴇᴘᴏʀᴛ Bᴜɢꜱ..!! 👉 @aktelegram1""",
        reply_markup=reply_markup
    )
