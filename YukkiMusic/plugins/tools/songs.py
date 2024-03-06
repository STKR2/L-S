import os
import yt_dlp
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from ... import app
from strings.filters import command
from youtubesearchpython import VideosSearch

@app.on_message(command(["بحث", f"يوت"]))
async def song(client: app, message: Message):
    aux = await message.reply_text("‹ جاري البحث  ›")
    
    if len(message.command) < 2:
        return await aux.edit("‹ ارسل يوت واسم الملف الصوتي  ›")
    
    try:
        song_name = message.text.split(None, 1)[1]
        vid = VideosSearch(song_name, limit=1)
        song_title = vid.result()["result"][0]["title"]
        song_link = vid.result()["result"][0]["link"]
        
        ydl_opts = {
            "format": "bestaudio/best",
            "verbose": True,
            "geo-bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3"
                }
            ],
            "outtmpl": f"downloads/{song_title}.%(ext)s",
            "noplaylist": True,  # تجنب تنزيل قوائم التشغيل
        }
        
        await aux.edit("‹ يتم الرفع  ›")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(song_link, download=True)
            audio_path = ydl.prepare_filename(info_dict)
        
        await aux.edit("‹ تم التحميل  ›")
        
        await message.reply_audio(audio_path)

        # Display message below the audio file and provide a transparent button with the specified link
        await message.reply_to_message.reply_text(
            f"هذا الملف الصوتي '{song_title}' تم تنزيله",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("اونلاين", url="https://t.me/Xl444", url_button=True)]]
            )
        )

        try:
            os.remove(audio_path)
        except:
            pass
        
        await aux.delete()
    except Exception as e:
        await aux.edit(f"**Error:** {e}")
