import threading
hit = 0
import vk_api, random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkApi
from vk_api.longpoll import VkEventType
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
import time
global flag
global PVPK
global rand
global trigger
import random
import random
import matplotlib.pyplot as plt
import matplotlib.colors as clrs
import random
second_part = False

import matplotlib.pyplot as plt
import matplotlib.colors as clrs
import random
arr = []
fin_x=0
fin_y=0
settings = dict(one_time=False, inline=True)
keyboard_1 = VkKeyboard(**settings)
keyboard_1.add_callback_button(label='&#128316;', color=VkKeyboardColor.PRIMARY, payload={"type": "pvp", "text": "1@*"})
keyboard_1.add_line()
keyboard_1.add_callback_button(label='&#9664;', color=VkKeyboardColor.PRIMARY, payload={"type": "pvp","text": "2@*"})
keyboard_1.add_callback_button(label='&#9654;', color=VkKeyboardColor.PRIMARY, payload={"type": "pvp","text": "3@*"})
keyboard_1.add_line()
keyboard_1.add_callback_button(label='&#128317;', color=VkKeyboardColor.PRIMARY, payload={"type": "pvp","text": "4@*"})

def move(arr, i, j):
    row = 0
    col = 0
    while i == row or j == col or arr[row][col] != 3:
        row = random.randint(0, len(arr) - 1)
        col = random.randint(0, len(arr) - 1)
    arr[row][col] = arr[i][j]
    arr[i][j] = 3


def is_happy(arr, i, j, counter):
    happiness = 0
    if i > 0:
        if arr[i - 1][j] == arr[i][j]:
            happiness += 0.125
        elif arr[i - 1][j] == 3:
            happiness += 0.0625
        if j > 0:
            if arr[i - 1][j - 1] == arr[i][j]:
                happiness += 0.125
            elif arr[i - 1][j - 1] == 3:
                happiness += 0.0625
        if j < len(arr) - 1:
            if arr[i - 1][j + 1] == arr[i][j]:
                happiness += 0.125
            elif arr[i - 1][j + 1] == 3:
                happiness += 0.0625
    if j > 0:
        if arr[i][j - 1] == arr[i][j]:
            happiness += 0.125
        elif arr[i][j - 1] == 3:
            happiness += 0.0625
    if i < len(arr[0]) - 1:
        if arr[i + 1][j] == arr[i][j]:
            happiness += 0.125
        elif arr[i + 1][j] == 3:
            happiness += 0.0625
        if j > 0:
            if arr[i + 1][j - 1] == arr[i][j]:
                happiness += 0.125
            elif arr[i + 1][j - 1] == 3:
                happiness += 0.0625
        if j < len(arr) - 1:
            if arr[i + 1][j + 1] == arr[i][j]:
                happiness += 0.125
            elif arr[i + 1][j + 1] == 3:
                happiness += 0.0625
    if j < len(arr) - 1:
        if arr[i][j + 1] == arr[i][j]:
            happiness += 0.125
        elif arr[i][j + 1] == 3:
            happiness += 0.0625
    if (i == 0 and j == 0) or (i == len(arr) - 1 and j == 0) or (i == 0 and j == len(arr) - 1) or (
            i == len(arr) - 1 and j == len(arr) - 1):
        happiness += 0.125 * 5
    elif i == 0 or j == 0 or i == len(arr[0]) - 1 or j == len(arr) - 1:
        happiness += 0.125 * 3
    if happiness >= 0.6:
        counter += 1
        return [counter, True]
    return [counter, False]

def go(m):
    global fin_x
    global fin_y
    if m == 1 and fin_x<19:
        if arr[fin_x+1][fin_y] !=3:
            arr[fin_x][fin_y]=1
            fin_x+=1
            if arr[fin_x][fin_y]==2:
                return True
            arr[fin_x][fin_y] = 4
    if m == 4 and fin_x > 0:
        if arr[fin_x-1][fin_y] !=3:
            arr[fin_x][fin_y]=1
            fin_x-=1
            if arr[fin_x][fin_y]==2:
                return True
            arr[fin_x][fin_y] = 4
    if m == 2 and fin_y > 0:
        if arr[fin_x][fin_y-1] !=3:
            arr[fin_x][fin_y]=1
            fin_y-=1
            if arr[fin_x][fin_y]==2:
                return True
            arr[fin_x][fin_y] = 4
    if m == 3 and fin_y <19:
        if arr[fin_x][fin_y+1] !=3:
            arr[fin_x][fin_y]=1
            fin_y+=1
            if arr[fin_x][fin_y]==2:
                return True
            arr[fin_x][fin_y] = 4
    cmap = clrs.ListedColormap(['red', 'green', 'black', 'yellow'])
    fig = plt.figure()
    p2 = fig.add_subplot()
    p2.pcolormesh(arr, cmap=cmap, edgecolors="k", linewidth=0.5)
    fig.set_size_inches(10, 10)
    margins = {
        "left": 0,
        "bottom": 0,
        "right": 1,
        "top": 1
    }
    fig.subplots_adjust(**margins)
    fig.savefig('figure1.png')
    return False


def shelling(n):

    for i in range(0, n):
        arr.append([])
        for j in range(0, n):
            arr[i].append(random.randint(1, 3))
    for i in range(0, n):
        for j in range(0, n):
            if arr[i][j]==2:
                   if random.randint(1, 2)==2:
                       arr[i][j]=1
    cmap = clrs.ListedColormap(['red','green','black','yellow'])
    fig = plt.figure()
    counter = 0
    while counter < round(n * n / 1.7):
        counter = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] != 3:
                    res = is_happy(arr, i, j, counter)
                    counter = res[0]
                    if not res[1]:
                        move(arr, i, j)
        print(counter)
    hap_max=0
    global fin_x
    global fin_y
    for i in range(n):
        for j in range(n):
            happiness = 0
            counter = 0
            if i > 0:
                if arr[i - 1][j] == 3:
                    happiness += 0.125
                    counter+=1
                elif arr[i - 1][j] == 1:
                    happiness += 0.12
                if j > 0:
                    if arr[i - 1][j - 1] == 3:
                        happiness += 0.06
                    elif arr[i - 1][j - 1] == 1:
                        happiness += 0.13
                if j < len(arr) - 1:
                    if arr[i - 1][j + 1] == 3:
                        happiness += 0.06
                    elif arr[i - 1][j + 1] == 1:
                        happiness += 0.13
            if j > 0:
                if arr[i][j - 1] == 3:
                    happiness += 0.125
                    counter += 1
                elif arr[i][j - 1] == 1:
                    happiness += 0.12
            if i < len(arr[0]) - 1:
                if arr[i + 1][j] == 3:
                    happiness += 0.125
                    counter += 1
                elif arr[i + 1][j] == 1:
                    happiness += 0.12
                if j > 0:
                    if arr[i + 1][j - 1] == 3:
                        happiness += 0.06
                    elif arr[i + 1][j - 1] == 1:
                        happiness += 0.13
                if j < len(arr) - 1:
                    if arr[i + 1][j + 1] == 3:
                        happiness += 0.06
                    elif arr[i + 1][j + 1] == 1:
                        happiness += 0.13
            if j < len(arr) - 1:
                if arr[i][j + 1] == 3:
                    happiness += 0.125
                    counter += 1
                elif arr[i][j + 1] == 1:
                    happiness += 0.12
            if counter >= 2:
                happiness=0
            if (i == 0 and j == 0) or (i == len(arr) - 1 and j == 0) or (i == 0 and j == len(arr) - 1) or (
                    i == len(arr) - 1 and j == len(arr) - 1):
                happiness += 0.122 * 5
            elif i == 0 or j == 0 or i == len(arr[0]) - 1 or j == len(arr) - 1:
                happiness += 0.122 * 3
            if happiness >= hap_max:
                hap_max = happiness
                fin_x=i
                fin_y=j
    arr[fin_x][fin_y]=4
    print(fin_x)
    print(fin_y)
    p2 = fig.add_subplot()
    p2.pcolormesh(arr, cmap=cmap, edgecolors="k",linewidth = 0.5)
    fig.set_size_inches(10, 10)
    margins = {
        "left": 0,
        "bottom": 0,
        "right": 1,
        "top": 1
    }
    fig.subplots_adjust(**margins)
    fig.savefig('figure.png')


#-----------------??????????????????????---------------------------------????????
# ??????????
GROUP_TOKEN = '8ae066879254e846f387710548d59cb48eaf47c5eed7cec622520f5253cf68fe80036f145648bf1805ba4'
GROUP_ID ="206751328"

# ?????????????????? ??????
vk_session = vk_api.VkApi(token=GROUP_TOKEN)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()
par=0
#---------------------------------------------------------------------
def sender_k(id, text, key):
    vk_session.method('messages.send',
                      {'chat_id': id, 'message': text, 'random_id': 0, 'keyboard': key, 'dont_parse_links': 1})


def sender_f(id, text, key):
    vk_session.method('messages.send',
                      {'chat_id': id, 'message': text, 'random_id': 0, 'attachment': key, 'dont_parse_links': 1})
"?????? ????????"
PVPc = VkKeyboard(one_time=True)
PVPc.add_button('??????????1', color=VkKeyboardColor.SECONDARY)
PVPc.add_button('??????????2', color=VkKeyboardColor.SECONDARY)
"?????? ???????? ??????????"
"???????????????????? ????????"
Menu = VkKeyboard(one_time=True)
Menu.add_button('??????????1 ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????', color=VkKeyboardColor.NEGATIVE)
#Menu.add_button('??????????2', color=VkKeyboardColor.POSITIVE)
Menu.add_line()
Menu.add_button('??????????3', color=VkKeyboardColor.NEGATIVE)
Menu.add_button('??????????4', color=VkKeyboardColor.POSITIVE)
Menu.add_line()
Menu.add_button('??????????5', color=VkKeyboardColor.NEGATIVE)
Menu.add_button('??????????6', color=VkKeyboardColor.POSITIVE)
Menu.add_line()
Menu.add_callback_button('??????????6', color=VkKeyboardColor.POSITIVE)
CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app','pvp')
"???????????????????? ???????? ??????????"
"???????????????????? ??????"

def check(num,rand):
    if num == rand:
        return 'POSITIVE'
    else:
        return 'NEGATIVE'

def pvpsis(f):
    flag = False
    global trigger
    global hit
    global par
    global rand

    i = 1
    test_list1 =["*?????????? ????????????*","*?????????? ??????????*","*?????????? ????????????*","*?????????? ??????????*","*???????? ?????????? ?? ???????????????? ????????????*","*???????? ???????????? ?? ???????????????? ????????????*","??????????"]
    test_list = ["???????? ????????????","???????? ??????????","???????? ????????????","???????? ??????????","?????????? ????????????","???????????? ????????????","???????????? ????????","??????????","??????????"]
    random.shuffle(test_list)
    PVPK = VkKeyboard(one_time=True)
    while True:
        mp = random.randint(0, 6)
        if mp !=par:
            break
    par = mp
    while i < 9:
        PVPK.add_button(test_list[i-1], color=VkKeyboardColor.POSITIVE)
        if i % 3 == 0:
            PVPK.add_line()
        i += 1
    vk.messages.send(
        chat_id=per,
        random_id=get_random_id(),
        message=test_list1[mp],
        keyboard=PVPK.get_keyboard())
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            msg = event.obj.message['text']
            temp = msg.split(']')
            tp = temp[1].strip()
            num=-1
            test_list_1 = ["???????? ????????????", "???????? ??????????", "???????? ????????????", "???????? ??????????", "???????? ?????????? ????????????",
                         "???????? ???????????? ??????????", "???????????? ????????", "??????????", "??????????"]
            print("-----")
            print(tp)
            print("-1-1-1-1")
            print(test_list1[mp])
            print("-1-1-1-1")
            for i in range (8):
                print(test_list_1[i])
                if tp ==test_list_1[i]:
                    num=i
                    print(num)
            if mp == num:
                hit+=1
                print("??????????")
            print("-----")

            break

second_part = False
"????????????"
try:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.message['text'] != '':
                msg = event.obj.message['text'].lower()

                # ?????????? ?? ??????????????
                if event.from_chat:
                    if msg == "????????????????":
                        print("fff")
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message="??????????")
                    if msg == "??????????, ?? ???????????? ?? ????????" or msg == "??????":
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message="????????????")
                        time.sleep(3)
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message="??????, ???? ???????? ????????????????????, ???? ?????? ????, ????????????????.")
                        time.sleep(3)
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            message="???????? ?????????? ???????? ???? ??????????????????, ?? ?? ???????? ???????? 10 ???????????? ???? ????, ?????????? ?????? ????????????.???????? ?? ??????, ?????????? ?????????? ???? ???????? ??????????????????(?????????????? ????????????) ?? ???????????????????? ????????(?????????????? ????????????) ?? ???????????????? ???????????????????? ???? ?????????????????? ?? ??????????(???????????? ????????????). ???? ?????? ????,??????????.")
                        shelling(20)
                        time.sleep(10)
                        upload = vk_api.VkUpload(vk)
                        photo = upload.photo_messages('figure.png')
                        owner_id = photo[0]['owner_id']
                        photo_id = photo[0]['id']
                        access_key = photo[0]['access_key']
                        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                        tic = time.perf_counter()
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=get_random_id(),
                            attachment=attachment,
                            keyboard = keyboard_1.get_keyboard())
                        per = event.chat_id
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') in CALLBACK_TYPES:
                temp = event.object.payload['text'].split('@')
                if len(temp) == 2:
                    event.object.payload['text'] = temp[1]
                    tp = int(temp[0])
                    print(tp)
            toc = time.perf_counter()
            g=(toc - tic)
            if g>10:
                last_id = vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    chat_id=per,
                    random_id=get_random_id(),
                    message="?????????? ??????????",
                    conversation_message_id=event.obj.conversation_message_id)
                arr = []
                fin_x = 0
                fin_y = 0
                second_part = True
            else:
                r = go(tp)
                if r is False:
                    upload = vk_api.VkUpload(vk)
                    photo = upload.photo_messages('figure1.png')
                    owner_id = photo[0]['owner_id']
                    photo_id = photo[0]['id']
                    access_key = photo[0]['access_key']
                    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                    vk.messages.edit(
                        peer_id=event.obj.peer_id,
                        keyboard=keyboard_1.get_keyboard(),
                        attachment=attachment,
                        conversation_message_id=event.obj.conversation_message_id)
                else:
                    vk.messages.edit(
                        peer_id=event.obj.peer_id,
                        chat_id=per,
                        random_id=get_random_id(),
                        message="??????????????, ???? ???????????? ???????????? ?????? ??????????????????",
                        conversation_message_id=event.obj.conversation_message_id)
                    arr = []
                    fin_x = 0
                    fin_y = 0
                    second_part = True
            if second_part is True:
                global trigger
                flag = True
                vk.messages.send(
                    chat_id=per,
                    random_id=get_random_id(),
                    attachment='photo-206751328_457239018',
                    message="???? ????????????????")
                par = event.obj.conversation_message_id
                print(par)
                i = 0
                while i < 5:
                    if flag is False:
                        time.sleep(6)
                    pvpfork = threading.Thread(target=pvpsis, args=(per,), daemon=True)
                    pvpfork.start()
                    flag = False
                    i += 1
                time.sleep(2)
                if hit >= 2:
                    mess = "???????? ??????????, ?????????????? ?? ?????????????? ??????????"
                else:
                    mess = "??????, ???? ???????? ????????, ?????????? ??????????????????"
                vk_session.method('messages.send',
                                  {'chat_id': per,
                                   'message': '?????????? ????????????????, ???????????????? ' + str(hit) + ' ???? 5 ' + mess, 'random_id': 0,
                                   'keyboard': VkKeyboard.get_empty_keyboard(), 'dont_parse_links': 1})

    "??????????"
except Exception:
    print("???????????? ????????????????")
    time.sleep
    pass

if __name__ == '__main__':
    print()