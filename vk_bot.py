import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

def main():
    vk_session = vk_api.VkApi(token='vk1.a.YBiErSQ_8w9mDgy3tvZnoIrhALlf0NL2kbZ_i3uKDPWhoIE54mK_SzDamT8qSG5oLUnkv-_2sjqNm-PcldXLfq0ibX9mvN9NwZtcyx6_wRRXXSWMXmLy5CrRAeBFzKsRMHdQyfKu2jURMumNzU_7R73fQ3SQr4Aqoe0ZG4_Vf_hE_dmJPU7FzUF9Mtz5gvdXgDKIO9nTyixUJPrBx-K__A')
    longpoll = VkLongPoll(vk_session)

    print("Бот запущен и ждет сообщения...")

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            print(f'Получено сообщение: {event.text} от пользователя {event.user_id} (peer_id: {event.peer_id})')
            response = handle_message(event.text)

            # Проверяем, пришло ли сообщение из беседы или личного чата
            if event.peer_id < 2000000000:  # Личное сообщение
                vk_session.method('messages.send', {
                    'user_id': event.user_id,
                    'message': response,
                    'random_id': get_random_id()
                })
            else:  # Сообщение из беседы
                vk_session.method('messages.send', {
                    'chat_id': event.peer_id - 2000000000,  # Переводим peer_id в chat_id
                    'message': response,
                    'random_id': get_random_id()
                })

def handle_message(message):
    if message.lower() == "привет" or message.lower() == "/привет":
        return "Привет! Как дела?"
    elif message.lower() == "как дела?":
        return "У меня все хорошо, спасибо!"
    else:
        return "Извините, я не понимаю вас."

if __name__ == '__main__':
    main()
