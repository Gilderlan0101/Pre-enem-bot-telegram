import asyncio
from application.src.models.user import get_user_data
from application.src.views.messages import comando_cadastrar, get_welcome_message
from application.src.views.plan_premium import  get_support_plans


async def subscribe_premium(update, context):
    
    user = update.effective_user
    username = user.first_name
    user_id = user.id
    check_user = get_user_data(user_id)
    

    if  check_user:
        message = get_support_plans(username)
        await asyncio.sleep(1)
        await update.message.reply_text(message, parse_mode="HTML")

    else:
        message_default = get_welcome_message(username)
        await update.message.reply_text(message_default)
