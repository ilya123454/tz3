from bs4 import BeautifulSoup
import requests
import vk_api
import time
from time import sleep
from datetime import datetime as dt
from datetime import timedelta
import datetime


#Валюта

def val():
    response = requests.get("https://www.mk.ru/news/").text
    soup = BeautifulSoup(response,'html.parser')
    poisk = soup.findAll('div',{'class':'finance-price'})
    a=[]
    for i in poisk:
        a.append(i.text)
    return ("Доллар - "+a[0]+" р"+"\nЕвро - "+a[1]+" р")

#Погода
def wether():
    response = requests.get("https://world-weather.ru/pogoda/russia/arkhangelsk/").text
    soup = BeautifulSoup(response,'html.parser')
    poisk = soup.findAll('span',{'class':'dw-into'})
    a=[]
    for i in poisk:
            a.append(i.text)
    text = a[0]
    parts = text.rsplit('Подробнее')
    res = parts[0]
    return res

def post():
    token = '1bd8fb3e1bd8fb3e1bd8fb3ecc1bb4cb6911bd81bd8fb3e4695147c73229c89abe596ef'
    version = 5.101
    domain = 'life'
    all_post = []
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'domain': domain,
                                'count': 100
                            }
                            )
    data = response.json()['response']['items']
    all_post.extend(data)
    return all_post
def pop():
    a= post()
    tnow=datetime.date.today()
    #tFINISH - конец промежутка
    tFINISH = time.mktime(tnow.timetuple())

    #tSTART - конец промежутка
    tnow -= timedelta(days=1)
    tSTART = time.mktime(tnow.timetuple())
    g1 = (a[0]['likes']['count'])
    first = a[0]
    for i in a:
        if tSTART < i['date']<tFINISH:
            if i['likes']['count']>g1:
                g1 = i['likes']['count']
                first = i
    #g1- количество лайков
    #first - сам пост или словарь
    id_post=first['id']
    link = "https://vk.com/life?w=wall-24199209_"+str(id_post)
    token = '1bd8fb3e1bd8fb3e1bd8fb3ecc1bb4cb6911bd81bd8fb3e4695147c73229c89abe596ef'
    version = 5.101
    domain = 'life'
    response = requests.get('https://api.vk.com/method/utils.getShortLink',
                            params={
                                'access_token': token,
                                'v': version,
                                'url': link
                            }
                            )
    shortlink = (response.json()['response']['short_url'])
    return shortlink

def itog():
    mess = val() + '\n' + wether() + '\n' + pop()
    return mess

while True:
    timestart = {'08:00'}
    d = datetime.datetime.today()
    time = d.strftime('%H:%M')
    if time in timestart:
        print(itog())
        sleep(86400)




# def sms(mess):
#     ai = "24521226-E3D7-0B6E-89E7-2519C582F509"
#     link = "https://sms.ru/sms/send"
#     params = {
#     "api_id" : ai,
#     "to": "79314027463",
#     "msg": mess
#     }
#     print(requests.get(link, params=params))
# sms(mess)












