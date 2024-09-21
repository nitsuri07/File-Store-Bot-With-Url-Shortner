import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "27729248"))
    API_HASH = os.environ.get("API_HASH", "01b3d9c37f023283adb07b5956205f9f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Manjumehra_zx_bot")
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002493533342"))
    SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "shortxlinks.com")
    SHORTLINK_API = os.environ.get('SHORTLINK_API', "fa2a0768fc8d2a51b22e46293634a52670a73c7a")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "6174868004"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Manjumehra:namomehra007_1@cluster0.c1xoy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002349193862")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002466393737"))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
    BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
    OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
    ABOUT_BOT_TEXT = f"""
    ᴛʜɪs ɪs ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀᴘs_ғɪʟᴇsᴛᴏʀᴇ ʙᴏᴛ.
    sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴍᴇᴅɪᴀ ᴏʀ ғɪʟᴇ. ɪ ᴄᴀɴ ᴡᴏʀᴋ ɪɴ ᴄʜᴀɴɴᴇʟ ᴛᴏᴏ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ᴇᴅɪᴛ ᴘᴇʀᴍɪssɪᴏɴ, ɪ ᴡɪʟʟ sᴀᴠᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ғɪʟᴇ ɪɴ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ sʜᴀʀᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ.
    ╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
    │
    ├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
    │
    ├🔸 Language: [Python 3](https://www.python.org)
    │
    ├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
    │
    ╰──────[ 😎 ]───────────⍟
    """
    ABOUT_DEV_TEXT = f"""
    🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [R3](https://telegram.me/Mrx6996)

    I am Super noob Please Support My Hard Work.

    [Donate Me](https://t.me/Mrx6996)
    """
    HOME_TEXT = """
    Hᴇʟʟᴏ, [{}](tg://user?id={})\n\nᴛʜɪs ɪs ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ  **ғɪʟᴇsᴛᴏʀᴇ ʙᴏᴛ**.
    ʜᴏᴡ ᴛᴏ ᴜsᴇ ʙᴏᴛ & ɪᴛ's ʙᴇɴᴇғɪᴛs ??

    📢 sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ & ɪᴛ ᴡɪʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ & ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇ ʟɪɴᴋ.

    ⚠️ ʙᴇɴᴇғɪᴛs: ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴀɴʏ ᴄᴏᴘʏʀɪɢʜᴛ ᴄʜᴀɴɴᴇʟ, ᴛʜᴇɴ ɪᴛs ᴜsᴇғᴜʟ ғᴏʀ ᴅᴀɪʟʏ ᴜsᴀɢᴇ, ʏᴏᴜ ᴄᴀɴ sᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ғɪʟᴇ & ɪ ᴡɪʟʟ sᴇɴᴅ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ʏᴏᴜ & ᴄʜᴀɴɴᴇʟ ᴡɪʟʟ ʙᴇ sᴀғᴇ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪɴғʀɪɢᴍᴇɴᴛ ɪssᴜᴇ. ɪ sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ᴀʟsᴏ ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ᴀʙᴏᴜᴛ ʙᴏᴛ.

    ❌ ᴘᴏʀɴᴏɢʀᴀᴘʜʏ ᴄᴏɴᴛᴇɴᴛs ᴀʀᴇ sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ & ɢᴇᴛ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ.
    """
