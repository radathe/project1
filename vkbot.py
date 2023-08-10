import vk_api
import course

print(course.get_course('R01235'))

token = 'vk1.a.-Te1oQYghQZztxVPB-G4MEiyZ8qZc90iR89DifSiRf2q3jHFr0AWJAmXF4t8EHvmzOlgslwhb8NyWw38dEdsV5d8J-tytYAI304Ra-AjoPtz826ixUp-6PPrfHROg9Z34i8L1nl1wURm59IcY5H-p7EcO1wFUUh0bWy3yRO9C3kmVAi21YGm_dNKBf-MxsiA2ELfXw3Djxw-mB1lzeTQKw'


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
 
