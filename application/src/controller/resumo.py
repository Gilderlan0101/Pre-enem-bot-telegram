
from application.src.views.resumo import resum
from application.src.utils.tracker import increment_command_usage

async def resumo_handler(update, context):
    if not context.args:
        await update.message.reply_text("❌ Você precisa digitar um assunto. Ex: /resumo energia solar")
        return

    assunto = " ".join(context.args)
    fake_summary = resum(assunto)

    await update.message.reply_text(fake_summary)
    await increment_command_usage(update)
