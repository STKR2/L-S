from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from YukkiMusic import app
import config
    
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
                        "- المطور .", url=OWNER_ID),                        
                 ],[
                InlineKeyboardButton(
                        "- مسح .", callback_data="close"),
               ],
          ]
        ),
    )
