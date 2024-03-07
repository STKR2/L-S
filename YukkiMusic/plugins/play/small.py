from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from YukkiMusic import app
from config import OWNER_ID
    
@app.on_message(
    command(["اوامر","الاوامر"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""مرحبآ بك عزيزي » {message.from_user.mention}في قسم مميزات سورس cr ميوزك\n
هنا تكتب الاوامر """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- المطور .", url=config.OWNER_ID),                        
                 ],[
                InlineKeyboardButton(
                        "- مسح .", callback_data="close"),
               ],
          ]
        ),
    )
