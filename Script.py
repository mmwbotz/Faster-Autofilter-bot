class script(object):
    START_TXT = """<b>𝖧𝖾𝗒{}, 𝖨 𝖠𝗆 {}, 𝖧𝖺𝗉𝗉𝗒 🖤 𝖳𝗈 𝖧𝖺𝗏𝖾 𝖸𝗈𝗎

Here You Can Request Movie's, Just Sent Movie Name With Proper Google Spelling..!!

Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟꜱ Cʟɪᴄᴋ /help </b>"""
    
    HELP_TXT = """<b>𝙷𝙴𝚈 {}
<blockquote>𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.</blockquote></b>"""

    # ⚠️ Please don't change our credits 𝚃𝙷𝙰𝙽𝙺𝚂 𝚃𝙾 & 𝙳𝙴𝚅 👇🏻

    ABOUT_TXT = """<b><blockquote>✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}</blockquote>\n
<blockquote>✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/mallumovieworldmain>MMW BOTZ</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: HEROKU
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: [ Sᴛᴀʙʟᴇ 𝙱𝙴𝚃𝙰 ]</blockquote></b>"""

    SOURCE_TXT = """<b><blockquote>This Bot Project Is Private !!!</blockquote></b>"""

    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    
    BUTTON_TXT = """Help: <b>Buttons</b>

- bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/....)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    
    CAPTION = """❀Fɪʟᴇ Nᴀᴍᴇ:-<code>{file_name}</code>

❀Fɪʟᴇ Sɪᴢᴇ:-{file_size}

<b><a href=https://t.me/mallumovieworldmain>Join For Movies</a></b>
<b><a href=https://t.me/mallumovieworldmain1>Join For Updates</a></b>"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}</b> \n‌‌‌‌IMDb Data:
🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10"""

    FLTERS_TXT = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""
    
    GLOBAL_TXT = """ <b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
   
   Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
   
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Tony Stark 

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
"""
    
    ALRT_TXT = """Hᴇʟʟᴏ {},

Tʜɪs ɪs ɴᴏᴛ ʏᴏᴜʀ ʀᴇϙᴜᴇsᴛ.
Rᴇϙᴜᴇsᴛ ʏᴏᴜʀsᴇʟғ...!!"""

    OLD_ALRT_TXT = """Hey {},
You are using one of old message,
Request Again"""

    CUDNT_FND = """<b>I ᴄᴏᴜʟᴅɴ'ᴛ ғɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ. Dɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏғ ᴛʜᴇsᴇ?</b>"""

    I_CUDNT = """<b>I ᴄᴏᴜʟᴅɴ'ᴛ ғɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.</b>"""

    I_CUD_NT = """<b>I ᴄᴏᴜʟᴅɴ'ᴛ ғɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.</b>"""

    MVE_NT_FND = """<b>I ᴄᴏᴜʟᴅɴ'ᴛ ғɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.</b>"""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ ғᴏʀ ϙᴜᴇʀʏ ɪɴ Dᴀᴛᴀʙᴀsᴇ """
    
    NORSLTS = """
#NoResults 

ID <b>: {}</b>

Name <b>: {}</b>

Message <b>: {}</b>"""
    
    STATUS_TXT = """<b><blockquote>📂 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌     - <code>{}</code>

👤Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
♻️Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>

𒆜  𝗗𝗕 1️⃣
📂Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
🗃️Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{} </code>
🆓Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{} </code>

𒆜 𝗗𝗕 2️⃣
📂Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
🗃️Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{} </code>
🆓Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{} </code></blockquote></b>"""
    
    LOG_TEXT_G = """#NewGroup
    test
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !
test
📅 Dᴀᴛᴇ : <code>{}</code>
⏰Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""
    
    LOG_TEXT_P = """#NewUser
    test
ID - <code>{}</code>
Name - {}
"""
    LOGO = """test  !"""
