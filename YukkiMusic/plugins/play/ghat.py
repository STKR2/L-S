from strings.filters import command
from YukkiMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message

async def add_contact(client, user_id: int, first_name: str, username: str = None):
    try:
        if username:
            await client.add_contact(user_id, first_name=first_name, username=username)
        else:
            await client.add_contact(user_id, first_name=first_name)
    except Exception as e:
        print(f"Error adding contact: {e}")

@app.on_message(command(["اضفني", "ضيفني", "سجلني"]))
async def add_contact_command(message: Message):
    try:
        if message.from_user.username:
            await add_contact(app, message.from_user.id, message.from_user.first_name, username=message.from_user.username)
        else:
            await add_contact(app, message.from_user.id, message.from_user.first_name)
        await message.reply_text("تمت إضافتك إلى جهات الاتصال في حساب المساعد")
    except Exception as e:
        await message.reply_text(f"خطأ : {e}")
