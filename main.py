import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# Вставьте свой токен группы ВКонтакте
TOKEN = 'YOUR_VK_GROUP_TOKEN'

def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            # Получаем текст сообщения
            message_text = event.text
            user_id = event.user_id
            
            # Пример простого ответа
            if message_text.lower() == "привет":
                response = "Привет! Как я могу помочь?"
            else:
                response = "Я не понимаю, что вы хотите сказать."

            # Отправляем ответ
            vk_session.method('messages.send', {
                'user_id': user_id,
                'message': response,
                'random_id': 0
            })

if __name__ == "__main__":
    main()
