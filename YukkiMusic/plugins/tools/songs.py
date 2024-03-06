
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
            "format": "mp3/bestaudio/best",
            "verbose": True,
            "geo-bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3"
                }
            ],
            "outtmpl": f"downloads/{song_title}",
        }
        await aux.edit("‹ يتم الرفع  ›")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_link])

        await aux.edit("‹ تم التحميل  ›")
        audio_path = f"downloads/{song_title}.mp3"
        await message.reply_audio(audio_path)

        # Display transparent button below the audio file with the provided link
        await message.reply_to_message.reply_text(
            "تم تنزيل الفيديو بنفس الملف الصوتي الذي تم تنزيله",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("شاهد الفيديو", url=song_link)]]
            )
        )

        try:
            os.remove(audio_path)
        except:
            pass
        
        await aux.delete()
    except Exception as e:
        await aux.edit(f"**Error:** {e}")
