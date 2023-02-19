import requests
 
class Client:
    history = []
    ip = None
    def __init__(self, name):
        self.name = name
 
    def connect(self, ip):
        try:
            response = requests.get(ip)
        except:
            return False
        if response.text == "Server":
            self.ip = ip
            return True
        else:
            return False
 
    def get_history(self):
        response = requests.get(ip + "/history")
        h = response.json()
        if len(h) > len(self.history):
            for i in range(len(self.history), len(h)):
                print(h[i])
        self.history = h
 
    def send_message(self, message):
        url = ip + "/message?text=" + f"[{self.name}] " + message
        requests.get(url)
 
name = input("Введите Ваше имя: ")
client = Client(name)
ip = input("Введите ip-адрес чата: ")
connected = client.connect(ip)
if connected:
    client.get_history()
    while True:
        text = input("-> ")
        client.send_message(text)
        client.get_history()
else:
    print("Не удалось подключится к чату")