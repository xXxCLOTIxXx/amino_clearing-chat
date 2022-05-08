import os
try:import amino
except:
	os.system('pip install amino.py')
	import amino
	os.system('cls')


client = amino.Client()
os.system('cls')
print("made by CLOTI (Xsarz)  Telegram: t.me/DXsarz    GITHUB: https://github.com/xXxCLOTIxXx\n")
print("На аккаунте должна быть лидерка")

while True:
	try:
		gmail=input("Почта>> ")
		password=input("пароль>> ")
		client.login(email=gmail, password=password)
		print(f"\nБот успешно авторизован под аккаунтом {gmail} !\n")
		break
	except Exception as error:
		print(f"\n[bold red]Не удалось авторизовать бота\n\n {error}\n\n")

while True:
    try:
        chat = client.get_from_code(input("Ссылка чат для чистки>>")).json
        chatId = chat['extensions']['linkInfo']['objectId']
        comId = chat['extensions']['linkInfo']['ndcId']
        sub_client = amino.SubClient(comId=comId,profile=client.profile)
        print("\n\nДанные успешно получены!\n\n")
        break
    except:
        print("\n\nПроизошла ошибка!\n\n")

while True:
	try:
		mess_del = int(input("Коло-во сообщений для удаления (Слишком много не нужно)>> "))
		break
	except:
		print("\nВведите число!\n")

def clear_chat(num, chatId, sub_client):
	try:
		messages = sub_client.get_chat_messages(chatId=chatId, size=num).json
		for i in range(num):
			mess_id = messages[i]['messageId']
			sub_client.delete_message(chatId=chatId, messageId=mess_id, asStaff=True, reason='Чистка чата')
	except:
		print('Произошла ошибка при попытке очистить чат')


clear_chat(mess_del,chatId,sub_client)

print('Скрипт закончил свою работу!')

