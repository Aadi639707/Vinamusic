from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import PyTgCalls, filters as fl  # Naya import style
from config import *

app = Client(
    "VinaMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Naye version ke mutabik call_py setup
call_py = PyTgCalls(app)

@app.on_message(filters.command("start"))
async def start(client, message):
    bot = await client.get_me()
    
    caption = (
        f"нᴇʏ {message.from_user.mention}, 🥀\n\n"
        f"☉ тнιѕ ιѕ ⌜ {bot.first_name} ⌟ !\n\n"
        f"➻ ᴀ ғᴀsт & ᴘᴏᴡᴇʀғᴜʟ тᴇʟᴇɢʀᴀм мᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏт ᴡɪтн sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀтᴜʀᴇs.\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"<u>sᴜᴘᴘᴏʀтᴇᴅ ᴘʟᴀтғᴏʀмs :</u> ʏᴏᴜтᴜʙᴇ, sᴘᴏтɪғʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ мᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.\n\n"
        f"☉ ᴄʟɪᴄᴋ ᴏɴ тнᴇ нᴇʟᴘ ʙᴜттᴏɴ тᴏ ɢᴇт ιɴғᴏʀмᴀтɪᴏɴ ᴀʙᴏᴜт мʏ мᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏммᴀɴᴅs."
    )

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("✚ ᴀᴅᴅ мᴇ ιɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚", url=f"https://t.me/{bot.username}?startgroup=true")],
        [InlineKeyboardButton("нᴇʟᴘ & ᴄᴏммᴀɴᴅs", callback_data="help_menu")],
        [
            InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"tg://user?id={OWNER_ID}"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀт", url=SUPPORT_CHAT)
        ],
        [InlineKeyboardButton("ᴄнᴀɴɴᴇʟ", url=UPDATE_CHANNEL)]
    ])

    await message.reply_photo(photo=START_IMG, caption=caption, reply_markup=buttons)

# Bot aur Call client dono ko start karne ke liye
async def main():
    await app.start()
    await call_py.start()
    print("Bot is Live and Call Client Started!")

if __name__ == "__main__":
    app.run(main())
    
