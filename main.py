from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *

app = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start") & filters.private)
async def start_msg(client, message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"Hi {message.from_user.mention}!\n\nI am a Super Fast Music Bot. Add me to your group to enjoy high quality music! 🎶",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("➕ Add to Group", url=f"https://t.me/{client.me.username}?startgroup=true"),
            ],
            [
                InlineKeyboardButton("🛠 Support", url="https://t.me/your_support_chat"),
                InlineKeyboardButton("Updates 📢", url="https://t.me/your_channel")
            ]
        ])
    )

print("Bot is Starting...")
app.run()
