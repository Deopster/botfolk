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
import cv2
from vk_api.longpoll import VkLongPoll, VkEventType
# из лонг пулла импортируем нужные нам библиотеки.
ch1 = False
ch2 = False
ch3 = False
ch4 = False
ch5 = False
# биба
GROUP_TOKEN = '5bed05069dd3116ea4b816dae17a6101e5c8b07f7a96b44fe007e73e30725e26c1710f0692597feb2d135'
GROUP_ID ="203383087"
# леший
#GROUP_TOKEN = '8ae066879254e846f387710548d59cb48eaf47c5eed7cec622520f5253cf68fe80036f145648bf1805ba4'
#GROUP_ID ="206751328"
# виды callback-кнопок
CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')

# Запускаем бот
vk_session = vk_api.VkApi(token=GROUP_TOKEN)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()
#акт1
acts = ('Хэй ты! Да, ты, кошачьи глазки! Будешь чего заказывать или может провалишь уже отсюда? Таких наемников как ты тут пруд пруди.',
        "Пруд будет в твоих штанах, если пасть не захлопнешь.",
        "Пива мне.",
        "Таких наемников, как я ,столько же, сколько бутылок у этого незадачливого пьяницы ",
        "Трактирщик: Может хоть ты возьмёшься за это дело?",
        "Хорошо, я разузнаю что творится в лесу, но для начала расскажи о нём поподробнее",
        "Хорошо, я разузнаю, что творится в этом лесу, но сначала поговорим о награде.",
        "",
        ""
        )
# Настройки для обоих клавиатур
settings = dict(one_time=False, inline=True)

# №1.акт1
keyboard_1 = VkKeyboard(**settings)
keyboard_1.add_callback_button(label='Нагрубить', color=VkKeyboardColor.PRIMARY, payload={"type": "show_snackbar", "text": "1@*ударил кулаком по столу*"})
keyboard_1.add_line()
keyboard_1.add_callback_button(label='Поросить пива', color=VkKeyboardColor.PRIMARY, payload={"type": "show_snackbar","text": "2@"})
keyboard_1.add_line()
keyboard_1.add_callback_button(label='Ответить сарказмом', color=VkKeyboardColor.PRIMARY, payload={"type": "show_snackbar","text": "3@*показывает на крайний столик с растёкшимся под ним телом*"})

# №2.акт2
keyboard_2 = VkKeyboard(**settings)
keyboard_2.add_callback_button(label='Easy mode', color=VkKeyboardColor.POSITIVE, payload={"type": "show_snackbar", "text": "5@"})
keyboard_2.add_callback_button(label='?', color=VkKeyboardColor.SECONDARY, payload={"type": "show_snackbar", "text": "Упрощённый режим, содержит в себе больше подсказок"})
keyboard_2.add_line()
keyboard_2.add_callback_button(label='Hard mode', color=VkKeyboardColor.NEGATIVE, payload={"type": "show_snackbar","text": "6@*принять квест*"})
keyboard_2.add_callback_button(label='?', color=VkKeyboardColor.SECONDARY, payload={"type": "show_snackbar", "text": "Никаких излишних подсказок, таков путь ведьмака"})
go = VkKeyboard(one_time=True)
go.add_button('Отправиться в лес', color=VkKeyboardColor.SECONDARY)
onplace = VkKeyboard(one_time=True)
onplace.add_button('На месте', color=VkKeyboardColor.SECONDARY)

print("Бот запущен")
import config
chat = False
touser = 0
mode = 0
check = True
f_toggle: bool = False
per =""
for event in longpoll.listen():
        try:
            if event.type == VkBotEventType.MESSAGE_NEW and event.object.message['action']['type'] == "chat_invite_user":
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=get_random_id(),
                    attachment={'video-206796372_456239018'},
                    message='*тишь леса нарушает шелест веток*')
        except Exception:
            print("не новый участник")
            pass
        try:
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.obj.message['attachments'] != '':
                    msg = event.obj.message['text'].lower()
                    atch = event.obj.message['attachments']
                    for word in atch:
                        try:
                            if word['type'] == 'photo':
                                photo = word['photo']

                                url = photo['sizes'][-1]['url']
                                print(url)
                                import requests
                                filename = 'fff.png'
                                r = requests.get(url, allow_redirects=True)
                                open(filename, 'wb').write(r.content)
                                img = cv2.imread("fff.png")
                                detector = cv2.QRCodeDetector()
                                # обнаружить и декодировать
                                data, bbox, straight_qrcode = detector.detectAndDecode(img)
                                # if there is a QR code
                                if bbox is not None:
                                    print(f"QRCode data:\n{data}")
                                    if data =="3563":
                                        if ch1 is False:
                                            ch1 = True
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                attachment={'video-206796372_456239018'},
                                                message="*След артефакта указывает тебе верный путь*1")
                                            time.sleep(4)
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                keyboard=onplace.get_keyboard(),
                                                message="Используй ведьмачье чутьё, чтобы отследить где спрятана часть артефакта. Как только дойдёшь до того места где он спрятан, то сообщи мне.")
                                        else:
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                attachment={'video-206796372_456239021'},
                                                message="Хм,ты мне это уже показывал")
                                    if data =="3564":
                                        if ch2 is False:
                                            ch2 = True
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                attachment={'video-206796372_456239019'},
                                                message="*След артефакта указывает тебе верный путь*2")
                                            time.sleep(4)
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                keyboard=onplace.get_keyboard(),
                                                message="Используй ведьмачье чутьё, чтобы отследить где спрятана часть артефакта. Как только дойдёшь до того места где он спрятан, то сообщи мне.")
                                        else:
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                attachment={'video-206796372_456239021'},
                                                message="Хм,ты мне это уже показывал")
                                    if data =="3565":
                                        if ch3 is False:
                                            ch3 = True
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                attachment={'video-206796372_456239020'},
                                                message="*След артефакта указывает тебе верный путь*3")
                                            time.sleep(4)
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                keyboard=onplace.get_keyboard(),
                                                message="Используй ведьмачье чутьё, чтобы отследить где спрятана часть артефакта. Как только дойдёшь до того места где он спрятан, то сообщи мне.")
                                        else:
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                attachment={'video-206796372_456239021'},
                                                message="Хм,ты мне это уже показывал")
                                    if data =="3566":
                                        if ch4 is False:
                                            ch4 = True
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                attachment={'video-206796372_456239021'},
                                                message="*След артефакта указывает тебе верный путь*4")
                                            time.sleep(4)
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                keyboard=onplace.get_keyboard(),
                                                message="Используй ведьмачье чутьё, чтобы отследить где спрятана часть артефакта. Как только дойдёшь до того места где он спрятан, то сообщи мне.")
                                        else:
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                attachment={'video-206796372_456239021'},
                                                message="Хм,ты мне это уже показывал")
                                    if data =="3567":
                                        if ch5 is False:
                                            ch5 = True
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                attachment={'video-206796372_456239022'},
                                                message="*След артефакта указывает тебе верный путь*5")
                                            time.sleep(4)
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                keyboard=onplace.get_keyboard(),
                                                message="Используй ведьмачье чутьё, чтобы отследить где спрятана часть артефакта. Как только дойдёшь до того места где он спрятан, то сообщи мне.")
                                        else:
                                            vk.messages.send(
                                                chat_id=event.chat_id,
                                                random_id=get_random_id(),
                                                attachment={'video-206796372_456239021'},
                                                message="Хм,ты мне это уже показывал")
                        except Exception:
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message="Артефакт видно слишком смутно, попробуй отправить его немного иначе.")
                            pass

                print("успех")
                if event.obj.message['text'] != '':
                    msg=event.obj.message['text'].lower()
                    #часть с беседой
                    if event.from_chat and event.chat_id != 1:
                        print(msg)
                        if msg == "поменять":
                            vk_session.method("groups.edit", {"group_id": 203383087, "title": "СТАСЯН"})
                        if msg == "назад":
                            vk_session.method("groups.edit", {"group_id": 203383087, "title": "украiнская бiмба"})
                        if msg == "проверка":
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message="робит")
                        if msg == "74":
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message=event)
                            break
                        if msg == "сброс":
                            mode = 0
                            check = True
                            touser = 0
                            chat = False
                        if msg == "начать":
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message=" *Вечер, полупустой трактир у чёрта на куличиках *")
                            per = event.chat_id
                            per = event.chat_id
                            time.sleep(2)
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                keyboard=keyboard_1.get_keyboard(),
                                message=acts[touser])
                            check = not check
                            chat = True
                        if msg == "[club203383087|@club203383087] отправиться в лес":
                            time.sleep(2)
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message="На выходе из таверны вас окликнул трактирщик, он протянул вам карту")
                            time.sleep(2)
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                message="Эй, ведьмак, постой! На вот, забыл отдать тебе, а то заблудишься в этих ебенях")
                            time.sleep(2)
                            vk.messages.send(
                                chat_id=event.chat_id,
                                random_id=get_random_id(),
                                attachment={'photo-206796372_457239018,photo-206796372_457239017,photo-206796372_457239020,photo-206796372_457239022,photo-206796372_457239023'})
                            time.sleep(2)

                    #часть с лс
                    if event.from_user:
                        if 'callback' not in event.obj.client_info['button_actions']:
                            print(f'Клиент {event.obj.message["from_id"]} не поддерж. callback')
                        if msg == "сброс":
                            mode = 0
                            check = True
                            touser = 0
                            chat = False
                        if check:
                            vk.messages.send(
                                user_id=event.obj.message['from_id'],
                                random_id=get_random_id(),
                                peer_id=event.obj.message['from_id'],
                                message=" *Вечер, полупустой трактир у чёрта на куличиках *")
                            time.sleep(2)
                            vk.messages.send(
                                user_id=event.obj.message['from_id'],
                                random_id=get_random_id(),
                                peer_id=event.obj.message['from_id'],
                                keyboard=keyboard_1.get_keyboard(),
                                message=acts[touser])
                            check = not check
                            print("act1 - passed")
                        else:
                            vk.messages.send(
                                user_id=event.obj.message['from_id'],
                                random_id=get_random_id(),
                                peer_id=event.obj.message['from_id'],
                                message="уж простите,пока пусто")

            # обрабатываем клики
            elif event.type == VkBotEventType.MESSAGE_EVENT:

                #ЛС
                if chat is False:
                    if event.object.payload.get('type') in CALLBACK_TYPES:
                            temp = event.object.payload['text'].split('@')
                            if len(temp) == 2:
                                event.object.payload['text'] =temp[1]
                                tp=int(temp[0])
                            if event.object.payload['text'] != '':
                                r = vk.messages.sendMessageEventAnswer(
                                          event_id=event.object.event_id,
                                          user_id=event.object.user_id,
                                          peer_id=event.object.peer_id,
                                          event_data=json.dumps(event.object.payload))
                    if (tp != '' and len(temp) == 2):
                        last_id = vk.messages.edit(
                                  peer_id=event.obj.peer_id,
                                  message=acts[touser],
                                  conversation_message_id=event.obj.conversation_message_id)
                        touser+=4
                        vk.messages.send(
                            user_id=event.object.user_id,
                            random_id=get_random_id(),
                            peer_id=event.object.peer_id,
                            message='Игрок: '+acts[tp])
                        if touser ==4:
                            time.sleep(3)
                            vk.messages.send(
                                user_id=event.object.user_id,
                                random_id=get_random_id(),
                                peer_id=event.object.peer_id,
                                message="Трактирщик: Ты тут берега не путай. Все вы сначала так. А потом манатки собираете и ищи свищи вас.")

                            time.sleep(4)
                            vk.messages.send(
                                user_id=event.object.user_id,
                                random_id=get_random_id(),
                                peer_id=event.object.peer_id,
                                message="Трактирщик: Завелась тут в лесу то ли нечисть поганая, то ли проклятье тёмное. Каждую ночь начинает пульсировать. Да так мозги ебёт. Не знаем что и делать. И эти наёмнички все как один заночевав у нас в деревне, на следующий день, убегали только пятки сверкали. А старосте всё одно. Сколько ж мы не талдычили этому херу, что в лесу что-то завелось, а он не верит… Житья нам нет.")
                            time.sleep(10)
                            vk.messages.send(
                                user_id=event.object.user_id,
                                random_id=get_random_id(),
                                peer_id=event.object.peer_id,
                                keyboard=keyboard_2.get_keyboard(),
                                message=acts[touser])
                        if touser == 8:
                            print(tp)
                            if tp == 6:
                                mode = 1
                            time.sleep(3)
                            if tp == 5:
                                vk.messages.send(
                                    user_id=event.object.user_id,
                                    random_id=get_random_id(),
                                    peer_id=event.object.peer_id,
                                    message="Трактирщик: Слышал я, что скот передох. Тот, что разрабатывал землю рядом с лесом. Да и ходить по ночам я бы не советовал. Ворон там много и волки по ночам стаями воют. Жутко, вообщем. Но больше всего странностей происходило здесь. Собаки часто лаяли в ту сторону ",
                                    attachment = 'photo-203383087_457239030')
                                time.sleep(5)
                            vk.messages.send(
                                user_id=event.object.user_id,
                                random_id=get_random_id(),
                                peer_id=event.object.peer_id,
                                message="Трактирщик: Насчёт награды, лично мне предложить тебе нечего, но если что найдёшь в лесу - забирай. Оно нам и даром не нужно.")
                            time.sleep(4)
                            vk.messages.send(
                                user_id=event.object.user_id,
                                random_id=get_random_id(),
                                peer_id=event.object.peer_id,
                                message="Игрок: А если ничего не найду?")
                            time.sleep(3)
                            vk.messages.send(
                                user_id=event.object.user_id,
                                random_id=get_random_id(),
                                peer_id=event.object.peer_id,
                                keyboard=go.get_keyboard(),
                                message="Трактирщик: Так и быть, подарю тебе ящик самогона.")
            # ЧАТ
                if chat is True:
                    print("Ответ выбран")
                    print("act1 -> act2")
                    if event.object.payload.get('type') in CALLBACK_TYPES:
                        temp = event.object.payload['text'].split('@')
                        if len(temp) == 2:
                            event.object.payload['text'] = temp[1]
                            tp = int(temp[0])
                        if event.object.payload['text'] != '':
                            print("сюда дошло")
                            r = vk.messages.sendMessageEventAnswer(
                                event_id=event.object.event_id,
                                user_id=event.object.user_id,
                                peer_id=event.object.peer_id,
                                event_data=json.dumps(event.object.payload))

                    if (tp != '' and len(temp) == 2):
                        print("сюда тоже")
                        last_id = vk.messages.edit(
                            peer_id=event.obj.peer_id,
                            message=acts[touser],
                            conversation_message_id=event.obj.conversation_message_id)
                        touser += 4
                        vk.messages.send(
                            chat_id=per,
                            random_id=get_random_id(),
                            message='Игрок: ' + acts[tp])
                        if touser == 4:
                            time.sleep(3)
                            print(tp)
                            print("11111")
                            if tp != 2:
                                vk.messages.send(
                                    chat_id=per,
                                    random_id=get_random_id(),
                                    message="Трактирщик: Ты тут берега не путай. Все вы сначала так. А потом манатки собираете и ищи свищи вас.")
                            else:
                                vk.messages.send(
                                    chat_id=per,
                                    random_id=get_random_id(),
                                    message="Трактирщик: *наливает пиво*")
                            time.sleep(4)
                            vk.messages.send(
                                chat_id=per,
                                random_id=get_random_id(),
                                message="Трактирщик: Завелась тут в лесу то ли нечисть поганая, то ли проклятье тёмное. Каждую ночь начинает пульсировать. Да так мозги ебёт. Не знаем что и делать. И эти наёмнички все как один заночевав у нас в деревне, на следующий день, убегали только пятки сверкали. А старосте всё одно. Сколько ж мы не талдычили этому херу, что в лесу что-то завелось, а он не верит… Житья нам нет.")
                            time.sleep(10)
                            vk.messages.send(
                                chat_id=per,
                                random_id=get_random_id(),
                                keyboard=keyboard_2.get_keyboard(),
                                message=acts[touser])
                        if touser == 8:
                            print(tp)
                            if tp == 6:
                                mode = 1
                            time.sleep(3)
                            if tp == 5:
                                vk.messages.send(
                                    chat_id=per,
                                    random_id=get_random_id(),
                                    message="Трактирщик: Слышал я, что скот передох. Тот, что разрабатывал землю рядом с лесом. Да и ходить по ночам я бы не советовал. Ворон там много и волки по ночам стаями воют. Жутко, вообщем. Но больше всего странностей происходило здесь. Собаки часто лаяли в ту сторону ",
                                    attachment='photo-203383087_457239030')
                                time.sleep(5)
                            vk.messages.send(
                                chat_id=per,
                                random_id=get_random_id(),
                                message="Трактирщик: Насчёт награды, лично мне предложить тебе нечего, но если что найдёшь в лесу - забирай. Оно нам и даром не нужно.")
                            time.sleep(4)
                            vk.messages.send(
                                chat_id=per,
                                random_id=get_random_id(),
                                message="Игрок: А если ничего не найду?")
                            time.sleep(3)
                            vk.messages.send(
                                chat_id=per,
                                random_id=get_random_id(),
                                keyboard=go.get_keyboard(),
                                message="Трактирщик: Так и быть, подарю тебе ящик самогона.")
        except Exception:
            print("ошибка таймаута")
            time.sleep(2)
            vk.messages.send(
                chat_id=per,
                random_id=get_random_id(),
                message="Уж извини, давненько вестей от тебя не было, напомни что ты мне там говорил?")
            pass


