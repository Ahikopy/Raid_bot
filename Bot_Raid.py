import amino
import pyfiglet
from threading import Thread
print("By ahiko: @ahikopy")
print("Тг канал: https://t.me/domik_ahiki")
print(pyfiglet.figlet_format("Bot_Raid", font='speed'))

client = amino.Client()
email=input("Почту>> ")
password=input("Пароль>> ")
print("Я украл пароль:" + password + ". Ладно, шучу.")

client.login(email = email, password = password)

clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
	print(f"{x}.{name}")	
comId = clients.comId[int(input("Выберите соо>> "))-1]

sub_client = amino.SubClient(comId=comId, profile=client.profile)
chats = sub_client.get_chat_threads(size=7000)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chatId = chats.chatId[int(input("Выберите чат>> "))-1]

message=input('смс>> ')

mest=input("Тип спама>> ")
def sendmes():
	while True:
	   try:
	      messageType=mest
	      sub_client.send_message(chatId=chatId, message=message, messageType=messageType)
	   except Exception as e:
	   	print("Ошибка.")
	   	
for _ in range(int(input("Количество потоков>> " ))):
	Thread(target=sendmes).start()