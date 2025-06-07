from application.src.views.messages import get_welcome_message


async def start_handler(update, context):
    
    user = update.effective_user
    message =  get_welcome_message(user.first_name)
    await update.message.reply_text(message)