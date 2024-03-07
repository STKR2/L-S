from strings.filters import command
from YukkiMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message

app = Client("BABZUKJZ5WQKwUsAVI6Mnk-d_NX5L9T2CjGmZah9KpnqlZ-huldZUgHoTVS5DnvFvtxb877ecM55JeQle3eZT4UTX37S-_EzacmsCCK-Artj63CrctQcdrcbPoHEm1t0Hz4lZs54fiXPHpxAroQk5pULj0OPEc1YVMOhtGtSj8MEVe0cXDUvEldXH0szN539qU24WTcKll_qYEWEPO1C6WI-bJwoLRj7Rn1-RRvBC1Qf56qdwBHckvtLuE2qX5WmxmVypV0Q9GjBXtdlUJQjU8V7bwR1PgGxNB6TfSaFTxF9tbtfGal3RIOaTGf3lLv_SAULNa4kkkY_r7JuWlXisX8BAAAAAXmnGC0A")

async def add_contact(user_id, first_name, username=None):
    try:
        if username:
            await app.add_contact(user_id, first_name=first_name, username=username)
        else:
            await app.add_contact(user_id, first_name=first_name)
        print(f"تمت إضافة {first_name} إلى جهات الاتصال")
    except Exception as e:
        print(f"Error adding contact: {e}")

@app.on_message(command(["addme", "ضيفني"]))
async def leave_one(client, message: Message):
    try:
        if message.from_user.username:
            await add_contact(message.from_user.id, message.from_user.first_name, username=message.from_user.username)
        else:
            await add_contact(message.from_user.id, message.from_user.first_name)
        await message.reply_text("تمت إضافتك إلى جهات الاتصال في حساب المساعد")
    except Exception as e:
        await message.reply_text(f"خطأ : {e}")
