from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *

app = Client(
    "VinaMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    # Bot ka username auto-fetch karne ke liye
    bot_username = (await client.get_me()).username
    bot_name = (await client.get_me()).first_name

    # Stylish Caption (Advika Style)
    caption = (
        f"нᴇʏ {message.from_user.mention}, 🥀\n\n"
        f"☉ тнιѕ ιѕ ⌜ {bot_name} ⌟ !\n\n"
        f"➻ ᴀ ғᴀsт & ᴘᴏᴡᴇʀғᴜʟ тᴇʟᴇɢʀᴀᴍ мᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏт ᴡɪтн sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀтᴜʀᴇs.\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"<u>sᴜᴘᴘᴏʀтᴇᴅ ᴘʟᴀтғᴏʀмs :</u> ʏᴏᴜтᴜʙᴇ, sᴘᴏтɪғʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ мᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.\n\n"
        f"☉ ᴄʟɪᴄᴋ ᴏɴ тнᴇ нᴇʟᴘ ʙᴜттᴏɴ тᴏ ɢᴇт ιɴғᴏʀмᴀтɪᴏɴ ᴀʙᴏᴜт мʏ мᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏммᴀɴᴅs."
    )

    # Buttons Layout (1-1-2-1 Pattern)
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("✚ ᴀᴅᴅ мᴇ ιɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚", url=f"https://t.me/{bot_username}?startgroup=true")],
        [InlineKeyboardButton("нᴇʟᴘ & ᴄᴏммᴀɴᴅs", callback_data="help_menu")],
        [
            InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"tg://user?id={OWNER_ID}"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀт", url=SUPPORT_CHAT)
        ],
        [InlineKeyboardButton("ᴄнᴀɴɴᴇʟ", url=UPDATE_CHANNEL)]
    ])

    await message.reply_photo(
        photo=START_IMG,
        caption=caption,
        reply_markup=buttons
    )

print("Vina Music Bot Starting...")
app.run()
