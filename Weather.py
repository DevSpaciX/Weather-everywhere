from tkinter import *
from tkinter import ttk
import time

import requests
from ttkthemes import ThemedTk
from tkinter import messagebox
root = ThemedTk(theme='arc')
root.title('Моё первое приложение')
root.geometry('600x400+400+250')

API = 'a9ac329033caee40838a079f890fcfa9'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
# https://api.openweathermap.org/data/2.5/weather?appid=key&q=kiev,ua


s = ttk.Style()
s.configure('TLabel', padding=5, font="Arial 12" , fg ='#808080')

def print_weather(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        temp = weather['main']['temp']
        press = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        desc = weather['weather'][0]['description']
        sunrise_ts = weather['sys']['sunrise']
        sunset_ts = weather['sys']['sunset']
        sunrise_struct_time = time.localtime(sunrise_ts)
        sunset_struct_time = time.localtime(sunset_ts)
        sunrise = time.strftime("%H:%M:%S", sunrise_struct_time)
        sunset = time.strftime("%H:%M:%S", sunset_struct_time)
        return f"Местоположение: {city}, {country} \nТемпература: {temp} °C \nАтм. давление: {press} гПа \nВлажность: {humidity}% \nСкорость ветра: {wind} м/с \nПогодные условия: {desc} \nВосход: {sunrise} \nЗакат: {sunset}"
    except:
        return "Ошибка получения данных..."


def get_weather(event=''):
    if not Entry.get():
        messagebox.showwarning('Warning' , 'Введите город')
    else:
        params = {
            'appid': API ,
            'q': Entry.get(),
            'units': 'metric',
            'lang':'ru'

        }
        r = requests.get(API_URL , params = params)
        weather = r.json()
        Label['text'] = print_weather(weather)

head_frame = ttk.Frame(root)
head_frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.9, anchor=N)

Entry = ttk.Entry(head_frame)
Entry.place(relheight=1, relwidth=0.7)

Button = ttk.Button(head_frame, text='Узнать погоду' , command=get_weather)
Button.place(relheight=1, relwidth=0.3, relx=0.7)

lower_frame = ttk.Frame(root)
lower_frame.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.9, anchor='n')

Label = ttk.Label(lower_frame ,font='Arial 10 ',  anchor='nw')
Label.place(relheight=1, relwidth=1)




root.mainloop()