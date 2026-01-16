import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import PyTgCalls
from config import *

# Initialize Bot
app = Client(
    "VinaMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Initialize Call Client
call_py = PyTgCalls(app)

@app.on_message(filters.command("start"))
async def start(client, message):
    bot = await client.get_me()
    
    # English Professional Caption
    caption = (
        f"Hello {message.from_user.mention}, 🥀\n\n"
        f"☉ THIS IS ⌜ {bot.first_name} ⌟ !\n\n"
        f"➻ A FAST & POWERFUL TELEGRAM MUSIC PLAYER BOT WITH SOME AWESOME FEATURES.\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"<u>SUPPORTED PLATFORMS:</u> YOUTUBE, SPOTIFY, APPLE MUSIC, AND MORE.\n\n"
        f"☉ CLICK THE BUTTONS BELOW TO EXPLORE MY COMMANDS."
    )

    # Professional Buttons Layout
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("✚ ADD ME TO YOUR GROUP ✚", url=f"https://t.me/{bot.username}?startgroup=true")],
        [InlineKeyboardButton("HELP & COMMANDS", callback_data="help_menu")],
        [
            InlineKeyboardButton("DEVELOPER", url=f"tg://user?id={OWNER_ID}"),
            InlineKeyboardButton("SUPPORT", url=SUPPORT_CHAT)
        ],
        [InlineKeyboardButton("CHANNEL", url=UPDATE_CHANNEL)]
    ])

    await message.reply_photo(
        photo=START_IMG,
        caption=caption,
        reply_markup=buttons
    )

async def main():
    await app.start()
    await call_py.start()
    print("--------------------------")
    print("Vina Music Bot is now Live!")
    print("--------------------------")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    
