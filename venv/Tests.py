import requests
ai = "24521226-E3D7-0B6E-89E7-2519C582F509"
link = "https://sms.ru/sms/send"
params = {
"api_id" : ai,
"to": "79314027463",
"msg": "qwewqewq"
}
print(requests.get(link, params=params))