from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "8529492576:AAGlx16Nlb1vP8EBx2u-CZtjN5nEO4Du2n8"

CHANNEL_ID = -1003640366694
GROUP_ID = -1004406211338

async def forward_selected_posts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post

    if not message:
        return

    if message.chat.id != CHANNEL_ID:
        return

    text = message.text or message.caption or ""

    if "#community" not in text.lower():
        return

    await context.bot.copy_message(
        chat_id=GROUP_ID,
        from_chat_id=CHANNEL_ID,
        message_id=message.message_id,
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.Chat(CHANNEL_ID) & filters.ALL, forward_selected_posts)
)

print("Bot Started...")
app.run_polling()