from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from datetime import datetime
from YukkiMusic import app
from YukkiMusic import app

    
@app.on_message(command(["الاوامر", "اوامر"]))
async def alive(message: Message):
    chat_id = message.chat.id
    current_time = datetime.utcnow()
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🥇 اوامر البوت", callback_data="user_command"),
            ]
        ]
    )
    text = f"**- تابع الاوامر في الاسفل ↓ **"
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/402c519808f75bd9b1803.jpg",
        caption=text,
        reply_markup=buttons,
    )
