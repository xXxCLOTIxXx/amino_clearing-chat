	global join_users
	author_u = data.message.author.userId
	if author_u in join_users:
		if author_u in baned:
			pass
		else:
			sub_client = amino.SubClient(comId=data.comId, profile=client.profile)
			chatId = data.message.chatId
			author_n = data.message.author.nickname
			try:
				sub_client.kick(userId=author_u, chatId=chatId, allowRejoin=False)
				kick_ = 'OK.'
			except:
				kick_ = 'NO.'
			try:
				sub_client.ban(userId=author_u, reason='Подозрение в рейде типом 109')
				ban_ = 'OK.'
				baned.append(author_u)
			except:
				ban_ = 'NO.'
			try:
				sub_client.edit_chat(chatId=chatId, viewOnly=True)
				edit_ = 'OK.'
			except:
				edit_ = 'NO.'
			try:
				sub_client.send_message(chatId=chatId, message=f'📣{author_n} подозревается в рейдерстве типом join-leave.\n\n🛑Попытка забанить: {ban_}\n\n🛑Попытка кикнуть из чата: {kick_}\n\n🛑Попытка включить режим "Только просмотр": {edit_}')
			except:
				console.print(f"\n[bold red]Не удалось Отправить сообщение о рейде[/]\n")
	else:
		join_users.append(author_u)
#функция для бана рейдеров "join-leave" (Не тестировал, нет возможности, но в тиории работает)
print('Скрипт закончил свою работу!')

