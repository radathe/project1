#pip install vk-api

import vk_api
import course

token = 'vk1.a.lPoubjhbvPD80vPOVJrG2_BLFri6kPADtOD7BWRn0coXhHEN_iX1HjMVMBJ-C9w62YZabw1O6elP9TfP0VuYO8D_qBjFdyEQe9Ar1bRIlLRTOYxfDbSq9nXnWKfLlP5_ZpmIHEt1lxq90z9f5hXNSauIybSDTzV-42N_rBda3e-IgbLgn9OBJtGaVxv7S6vWDRdfr2AJyOF2751D_7GuQw'

vk = vk_api.VkApi(token=token)


while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] >= 1:
        print(messages)
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        message_text = messages['items'][0]['last_message']['text']
        if 'привет' in message_text.lower():
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Привет! Я умный бот, который скоро будет уметь делать много всего! Скорее подписывайся!'})
        elif 'курс' in message_text.lower():
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': course.get_course('R01235')})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Я тебя не понимаю!'})

# items = [первый диалог, второй диалог, ....]

# {
#     'count': 1,
#     'items': [{
#          'conversation': {
#
#                 'unanswered': True,
#                 'peer': {
#                         'local_id': *айди собеседника или беседы*,
#                         'type': 'user',
#                         'id': *ID собеседника*,
#                         }
#                 'last_message_id': 312,
#                 'in_read': 312,
#                 'out_read': 312,
#                 'can_write': {'allowed': True}
#
#                             },
#         'last_message': {
#                 'is_hidden': False,
#                 'id': 312,
#                 'conversation_message_id': 312,
#                 'from_id': *айди автора последнего сообщения*,
#                 'date': 1531127807,
#                 'important': False,
#                 'attachments': [],
#                 'text': *Текст последнего сообщения*,
#                 'out': 0,
#                 'peer_id': *айди диалога*,
#                 'random_id': 0,
#                 'fwd_messages': []
#                             }
#                 },
#          ]
# }