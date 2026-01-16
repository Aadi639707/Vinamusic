import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
from config import *

# Initialize the Bot Client
app = Client(
    "VinaMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Initialize the Call Client (Userbot Assistant)
call_py = PyTgCalls(app)

@app.on_message(filters.command("start"))
async def start(client, message):
    # Fetching Bot Info dynamically
    bot_info = await client.get_me()
    bot_name = bot_info.first_name
    bot_username = bot_info.username

    # English Caption (Professional Layout)
    caption = (
        f"Hello {message.from_user.mention}, 🥀\n\n"
        f"☉ THIS IS ⌜ {bot_name} ⌟ !\n\n"
        f"➻ A FAST & POWERFUL TELEGRAM MUSIC PLAYER BOT WITH SOME AWESOME FEATURES.\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"<u>SUPPORTED PLATFORMS :</u> YOUTUBE, SPOTIFY, RESSO, APPLE MUSIC AND SOUNDCLOUD.\n\n"
        f"☉ CLICK ON THE HELP BUTTON TO GET INFORMATION ABOUT MY MODULES AND COMMANDS."
    )

    # Buttons Layout (1-1-2-1)
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "✚ ADD ME TO YOUR GROUP ✚", 
                url=f"https://t.me/{bot_username}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton("HELP & COMMANDS", callback_data="help_menu")
        ],
        [
            InlineKeyboardButton("DEVELOPER", url=f"tg://user?id={OWNER_ID}"),
            InlineKeyboardButton("SUPPORT", url=SUPPORT_CHAT)
        ],
        [
            InlineKeyboardButton("CHANNEL", url=UPDATE_CHANNEL)
        ]
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
    print("Vina Music Bot is Online!")
    print("--------------------------")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    
