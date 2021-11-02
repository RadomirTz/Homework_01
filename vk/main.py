import vk_api
from tkinter import *
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
import datetime


tk = Tk()
tk.title('vk')
tk.geometry('600x600')


url = StringVar()


entr_1 = Entry(textvariable=url)
lbl_1 = Label(tk, text='')
ava = Label(tk, text='')


def start():
    vk = vk_api.VkApi(token='c59a83546beb703620aac1381e1d327d72ab367af9f1b2f6d69598b5006e70ee0748efa1c9b66d6099468')
    user = vk.method("users.get", { "user_ids": entr_1.get().replace('https://vk.com/', ''), "fields": 'bdate, counters,last_seen, photo_max_orig' } )
    

    name = user[0]['first_name']
    surname = user[0]['last_name']
    birthday = user[0]['bdate']
    count = user[0]['counters']
    last_seen = user[0]['last_seen']
    sta = user[0]['photo_max_orig']


    last_seen_msk_unixtime = last_seen.get('time')+(3600*3)
    utc3 = datetime.datetime.utcfromtimestamp(last_seen_msk_unixtime).strftime('%Y-%m-%d %H:%M:%S')


    lbl_1.config(text='Полное имя: ' + name + ' ' + surname + '\n' + 
      'Дата рождения: ' + birthday + '\n' + 
      'Количество друзей: ' + str(count.get('friends')) + '\n' +
      'Последний раз заходил: ' + utc3)


    response = requests.get(sta, timeout=10)


    pil_image = Image.open(BytesIO(response.content))
    image = ImageTk.PhotoImage(pil_image)
    ava.config(image=image)
    ava.image = image

button_1 = Button(text='Узнать информацию', command=start)


stat = str()


entr_1.pack()
button_1.pack()
lbl_1.pack()
ava.pack()
tk.mainloop()