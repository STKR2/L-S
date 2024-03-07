import os
import requests
import yt_dlp
from strings.filters import command
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch
from YukkiMusic import app

def is_valid_youtube_url(url):
    return url.startswith(("https://www.youtube.com", "http://www.youtube.com", "youtube.com"))

@app.on_message(filters.command(["يوت", "تحميل", "تنزيل", "بحث"]))
async def song(_, message: Message):
    m = await message.reply_text("- يتم البحث الان .", quote=True)

    query = message.text.split(" ", 1)[1]  # Get the text after the command
    ydl_opts = {"format": "bestaudio[ext=m4a]"}

    try:
        if is_valid_youtube_url(query):
            link = query
        else:
            results = YoutubeSearch(query, max_results=5).to_dict()
            if not results:
                raise Exception("- لايوجد نتائج البحث .")
            
            link = f"https://youtube.com{results[0]['url_suffix']}"

        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as ex:
        error_message = f"- فشل .\n\n**السبب :** `{ex}`"
        return await m.edit_text(error_message)

    await m.edit_text("- تم الرفع انتضر قليلاً .")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

        rep = f"**- الأسم :** [{title[:23]}]({link})\n**- الوقت :** `{duration}`\n**- بواسطة  :** {message.from_user.first_name}"

        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60

        visit_butt = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="- المطور .", url="https://t.me/Xl444")]
            ]
        )

        # Reply to the user or channel
        if message.chat.type == "private":
            await message.reply_audio(
                audio=audio_file,
                caption=rep,
                thumb=thumb_name,
                title=title,
                duration=dur,
                reply_markup=visit_butt,
            )
        else:
            await app.send_audio(
                chat_id=message.chat.id,
                audio=audio_file,
                caption=rep,
                thumb=thumb_name,
                title=title,
                duration=dur,
                reply_markup=visit_butt,
            )

        await m.delete()

    except Exception as ex:
        error_message = f"- فشل في تحميل الفيديو من YouTube. \n\n**السبب :** `{ex}`"
        await m.edit_text(error_message)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as ex:
        error_message = f"- فشل في حذف الملفات المؤقتة. \n\n**السبب :** `{ex}`"
        await m.edit_text(error_message)
