import vk_api #pip install vk-api
from vk_api.longpoll import VkLongPoll, VkEventType
from course import get_course

token = 'vk1.a.-Te1oQYghQZztxVPB-G4MEiyZ8qZc90iR89DifSiRf2q3jHFr0AWJAmXF4t8EHvmzOlgslwhb8NyWw38dEdsV5d8J-tytYAI304Ra-AjoPtz826ixUp-6PPrfHROg9Z34i8L1nl1wURm59IcY5H-p7EcO1wFUUh0bWy3yRO9C3kmVAi21YGm_dNKBf-MxsiA2ELfXw3Djxw-mB1lzeTQKw'

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

print(VkEventType.MESSAGE_NEW)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text
        user_id = event.user_id
        msg_id = event.message_id
        if msg.lower() == 'привет':
            vk.messages.send(user_id=user_id, random_id=msg_id, message='Ассаламалейкум! Кэфтеме')
        elif msg.lower() == '-к':
            response = f'{get_course("R01235")} рублей за 1 доллар\n' \
                       f'{get_course("R01239")} рублей за 1 евро\n' \
                       f'{get_course("R01375")} рублей за 1 юаней\n'
            vk.messages.send(user_id=user_id, random_id=msg_id, message=response)
        else:
            vk.messages.send(user_id=user_id, random_id=msg_id, message='ээээ ты кто ле')

