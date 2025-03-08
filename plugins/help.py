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
    
    await message.reply_text(
        text="""<b><blockquote>❗️How to Search Movies Here❓
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
1. Just Send Movie Name and Movie Released Year Correctly.
<blockquote>(Check Google for Correct Movie Spelling and Movie Released Year)</blockquote>

Examples: -
Oppam 2016
Baahubali 2015 1080p
<blockquote>(For Getting only 1080p Quality Files)</blockquote>
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Baahubali 2015 Malayalam
Baahubali 2015 Tamil
<blockquote>(For Dubbed Movie Files)</blockquote>
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
❗️On Android, Better Use VLC Media Player For Watch Movie's.
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Cᴏɴᴛᴀᴄᴛ Bᴏᴛ Dᴇᴠᴇʟᴏᴘᴇʀ (Oʀ) Rᴇᴘᴏʀᴛ Bᴜɢꜱ..!! 👉 @aktelegram1</b>""",
        reply_markup=reply_markup
    )
