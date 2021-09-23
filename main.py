import vk_api, random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
import time
import requests
import io
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
flag=True
flag1=False
import cv2
import config

GROUP_TOKEN = '9f22a6c9b501d85995fd8993807aecde6af183462cda78613b5615b74ee663f4d7bcc029e33f70815220b'
GROUP_ID ="206800822"
i=0
s=0
ans=0
counter=0
# виды callback-кнопок
CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app','answ')
arr=["","","","","",""]
questions = [["Какой псевдоним носила Эсси Давен?","Агуара","Голубая жемчужина","Куколка","Глазок@1"] ,
             ["Что означает название крепости ведьмаков Каэр Морхен?","Замок Цветущего Поля","Крепость Старого Моря@1","Дни Минувшего Горя","Скалы Зеленого Моря"],
             ["Какой маг был одним из создателей Ведьмаков?","Калькштейн","Саволла","Альзур@1","Гендальф"],
             ["Облик какого дракона могла принимать Саския?","Черного дракона","Златого дракона@1","Зеленого дракона","Красного дракона"],
             ["Кто является правителем вымышленного государства Редании?","Эмгыр вар Эмрейс","Фольтест","Радовид V Свирепый@1","Бран Тиршах"],
             ["Из скольки человек состояла ганза Крыс (без Цири)?","8","3","6@1","4"],
             ["Как называется поселок, в котором Лео Бонарт убил всех Крыс?","Ревность@1","Честность","Верность","Алчность"],
             ["Решающая для второй Северной войны битва под Бренной могла называться...","Битвой под Серым Гусем","Битвой под Майеной","Битвой под Старой Яругой","Битвой под Старыми Жопками@1"],
             ["Какой подарок получает Геральт от Владычицы Озера?","Далия","Арондит@1","Каррабела","Гарваль"],
             ["Именно так звали попугая изначально принадлежавшему Золтану Хиваю","Прекрасный Павлин","Капитан Флинт","Фельдмаршал Дуб@1","Капитан Крюк"],
             ["Какой псевдоним носила Эсси Давен?","Агуара","Голубая жемчужина","Куколка","Глазок@1"],
             ["Как называется государство в устье Яруги?","Нильфгаард@1","Цинтра","Ривия","Редания"],
             ["Откуда у Цири вороная лошадь?","Ей подарил Хотспорн","Она сама забрала@1","Она купила ее на рынке","Случайно нашла"],
             ["Как зовут вороную кобылу Цири?","Кэльпи@1","Плотва","Воронок","Бурава"],
             ["Назовите полное имя Цири","Цирилла Фиона Мюриель Рианнон","Цирилла Фиона Мюриель Рианнон","Цирилла Фиона Мюриель Рианнон","Цирилла Фиона Элен Рианнон@1"],
             ["Что получил Геральт за проявленную доблесть от королевы Мэвы?","Земельный надел в Лирии","Вироледанский меч","Помощь в поисках Цири","Титул рыцаря@1"],
             ["Как называла Йеннифэр Цири в детстве?","Ласточка","Утенок@1","Котенок","Цыпленок"],
             ["Кем была мать Геральта?","Проституткой","Крестьянкой","Колдуньей@1","Дворянином"],
             ["В какой банде была Цири?","Мыши","Крысы@1","Шакалы","Волчары"],
             ["Кто из чародеек мог превращаться в сову?","Йеннифер","Трисс Меригольд","Филиппа Эльхарт@1","Кейра Мец"],
             ["Как зовут владычицу Брокилона?","Нэннеке","Эитне@1","Мильва","Кейра"],
             ["Что больше всего на свете ненавидит Геральт из Ривии?","Монстров","Крестьян","Порталов@1","Магов"],
             ["Кого называют скоя’таэлями?","Краснолюдов-шахтёров","Эльфов партизан@1","вампиров","Ведьмаков"],
             ["Какая раса древнейшая?","Гномы","Краснолюды","Эльфы","Враны@1"]]
CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app','answ')
settings = dict(one_time=False, inline=True)

schet=0
# Запускаем бот
onetime = True
print("отлично работает")
vk_session = vk_api.VkApi(token=GROUP_TOKEN)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()
try:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.message['text'] != '':
                msg = event.obj.message['text'].lower()
                # часть с беседой
                if event.from_chat:
                    if msg == '[club203383087|@club203383087] на месте' or msg == '*тишь леса нарушает шелест веток*':
                        flag = True
                        schet += 1
                        if flag1 is False:
                            flag1 = True
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message="*тишину леса нарушает шелест веток*")
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message="Я страж этого леса")
                        time.sleep(2)
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message="- Ответишь на мои вопросы - получишь то что ищешь")
                        per = event.chat_id
                        for i in range(4):
                            temp = questions[s][i + 1].split('@')
                            arr[i + 1] = temp[0]
                        print(arr)
                        ask = VkKeyboard(**settings)
                        ask.add_callback_button(label=arr[1], color=VkKeyboardColor.PRIMARY,
                                                payload={"type": "answ", "text": questions[s][1]})
                        ask.add_line()
                        ask.add_callback_button(label=arr[2], color=VkKeyboardColor.PRIMARY,
                                                payload={"type": "answ", "text": questions[s][2]})
                        ask.add_line()
                        ask.add_callback_button(label=arr[3], color=VkKeyboardColor.PRIMARY,
                                                payload={"type": "answ", "text": questions[s][3]})
                        ask.add_line()
                        ask.add_callback_button(label=arr[4], color=VkKeyboardColor.PRIMARY,
                                                payload={"type": "answ", "text": questions[s][4]})
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            keyboard=ask.get_keyboard(),
                            message=questions[s][0])
                        s += 1
                        ans = 0
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') in CALLBACK_TYPES:
                temp = event.object.payload['text'].split('@')
                if len(temp) == 2:
                    ans += 1
                if ans >= 2:
                    if schet == 5:
                        last_id = vk.messages.edit(
                            peer_id=event.obj.peer_id,
                            message="Да сколько можно",
                            conversation_message_id=event.obj.conversation_message_id)
                        vk.messages.send(
                            chat_id=per,
                            random_id=get_random_id(),
                            message="Знаешь, ты порядком надоел, думаешь можешь решать мои задачки сколько угодно?")
                        vk.messages.send(
                            chat_id=per,
                            random_id=get_random_id(),
                            message="Леший, я взываю к тебе")
                        ans = 0
                        flag = False
                    else:
                        last_id = vk.messages.edit(
                            peer_id=event.obj.peer_id,
                            message="Эх твоя взяла",
                            conversation_message_id=event.obj.conversation_message_id)
                        vk.messages.send(
                            chat_id=per,
                            random_id=get_random_id(),
                            message="Так и быть, уступаю. Но мы ещё свидимся с тобой, как только ты найдёшь новый артефакт.")
                        ans = 0
                        counter = 0
                        flag = False
            if flag is True:
                for i in range(4):
                    temp = questions[s][i + 1].split('@')
                    arr[i + 1] = temp[0]
                print(arr)
                ask = VkKeyboard(**settings)
                ask.add_callback_button(label=arr[1], color=VkKeyboardColor.PRIMARY,
                                        payload={"type": "answ", "text": questions[s][1]})
                ask.add_line()
                ask.add_callback_button(label=arr[2], color=VkKeyboardColor.PRIMARY,
                                        payload={"type": "answ", "text": questions[s][2]})
                ask.add_line()
                ask.add_callback_button(label=arr[3], color=VkKeyboardColor.PRIMARY,
                                        payload={"type": "answ", "text": questions[s][3]})
                ask.add_line()
                ask.add_callback_button(label=arr[4], color=VkKeyboardColor.PRIMARY,
                                        payload={"type": "answ", "text": questions[s][4]})
                last_id = vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=questions[s][0],
                    keyboard=ask.get_keyboard(),
                    conversation_message_id=event.obj.conversation_message_id)
                s += 1
                print(s)
                print("----")
                print(schet)
                if s >23:
                    s = 0
except Exception:
    time.sleep(2)
    pass