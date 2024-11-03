import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# আপনার bot এর token এখানে দিন
TOKEN = '7471443488:AAEp5y59ryzosfPG9asnyE4qt_1wtBAeJp8'

# লোগিং কনফিগারেশন
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# /start কমান্ডের জন্য ফাংশন
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello, PixelChaser!')

def main() -> None:
    # ApplicationBuilder ব্যবহার করে Application তৈরি
    application = ApplicationBuilder().token(TOKEN).build()

    # Dispatcher এর মাধ্যমে কমান্ড হ্যান্ডলার যুক্ত করা
    application.add_handler(CommandHandler('start', start))

    # Bot চালানো শুরু
    application.run_polling()

if __name__ == '__main__':
    main()
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('This is a simple bot to demonstrate Telegram bot functionality.')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('PixelChaser is designed to help you with tasks!')

# main() ফাংশনের মধ্যে নতুন কমান্ড হ্যান্ডলার যুক্ত করুন
application.add_handler(CommandHandler('help', help_command))
application.add_handler(CommandHandler('about', about_command))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('This is a simple bot to demonstrate Telegram bot functionality.')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('PixelChaser is designed to help you with tasks!')

# main() ফাংশনের মধ্যে নতুন কমান্ড হ্যান্ডলার যুক্ত করুন
application.add_handler(CommandHandler('help', help_command))
application.add_handler(CommandHandler('about', about_command))

