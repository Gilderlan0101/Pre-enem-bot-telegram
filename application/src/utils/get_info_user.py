import inspect
from functools import wraps

def with_user_info(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Determina se é método (com self) ou função comum
        sig = inspect.signature(func)
        params = list(sig.parameters.keys())
        if params and params[0] == 'self':
            # Método: args = (self, update, context, ...)
            self_obj = args[0]
            update = args[1]
            context = args[2]
            remaining_args = args[3:]
        else:
            # Função: args = (update, context, ...)
            self_obj = None
            update = args[0]
            context = args[1]
            remaining_args = args[2:]
        # Extrai dados do usuário/chat
        user = getattr(update, 'effective_user', None)
        user_id   = user.id if user else None
        username  = user.username if user else None
        first_name = user.first_name if user else None
        chat = getattr(update, 'effective_chat', None)
        chat_id   = chat.id if chat else None
        # Injeta parâmetros conforme assinatura da função original
        if 'user_id' in params:
            kwargs['user_id'] = user_id
        if 'username' in params:
            kwargs['username'] = username
        if 'first_name' in params:
            kwargs['first_name'] = first_name
        if 'chat_id' in params:
            kwargs['chat_id'] = chat_id
        # Chama a função original com os dados extras
        if self_obj:
            return await func(self_obj, update, context, *remaining_args, **kwargs)
        else:
            return await func(update, context, *remaining_args, **kwargs)
    return wrapper
