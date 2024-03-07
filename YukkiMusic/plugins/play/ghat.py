from strings.filters import command
from YukkiMusic import app

@app.on_message(command(["اضفني","ضيفني","سجلني"]))
async def leave_one(client, message):
    try:
        if message.from_user.username:
            await USER.add_contact(message.from_user.username, message.from_user.first_name)
        else:
            await USER.add_contact(message.from_user.id, message.from_user.first_name)
        await message.reply_text("تم اضافتك الي جهات الاتصال في الحساب المساعد")
    except Exception as e:
        await message.reply_text(f"خطأ : {e}")