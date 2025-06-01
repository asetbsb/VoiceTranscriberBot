import os
from telegram import File
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from transcriber import transcribe_audio

# Replace this with your real token
TELEGRAM_BOT_TOKEN = "7536398117:AAF97OzWXu9DtcesgIQcq2EFCJFIZt-EMiM"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! Send me a voice message and I'll transcribe it for you!")

# /help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Just send a voice or audio message and I'll convert it to text!")

# Voice or audio handler
async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    file_id = message.voice.file_id if message.voice else message.audio.file_id
    new_file: File = await context.bot.get_file(file_id)

    file_name = f"user_audio.ogg" if message.voice else f"user_audio.mp3"
    await new_file.download_to_drive(file_name)

    await update.message.reply_text("📥 Audio received! Running transcription...")

    # Transcription will go here next

    text = transcribe_audio(file_name)
    await update.message.reply_text(f"📝 Transcription:\n{text}")
    
    if os.path.exists(file_name):
        os.remove(file_name)



# Main bot runner
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.VOICE | filters.AUDIO, handle_audio))


    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
