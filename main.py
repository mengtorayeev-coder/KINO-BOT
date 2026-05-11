from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8799433110:AAFEiF8J8sxkghnafFTsBZZiLjsmHvWNKYs"
KANAL = "@kinolaruztvv"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    try:
        member = await context.bot.get_chat_member(KANAL, user_id)

        if member.status in ["left", "kicked"]:
            keyboard = [
                [InlineKeyboardButton("📢 Kanalga obuna bo‘lish", url=f"https://t.me/{KANAL.replace('@','')}")],
                [InlineKeyboardButton("✅ Tekshirish", callback_data="check")]
            ]
            await update.message.reply_text(
                "❗ Botdan foydalanish uchun kanalga obuna bo‘ling:",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            await update.message.reply_text("🎬 Xush kelibsiz! Kino botga kirdingiz.")

    except:
        await update.message.reply_text("Xatolik yuz berdi. Kanalni tekshiring.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
