from pyrogram import Client as app, filters
import pyrogram

class Main:
	des = "Приглашать челика в чат"
	ver = "1.0"
	cmd_list = {
		"invite + юзер|айди": "Приглсить"
	}

@app.on_message(filters.me & filters.command("invite",".") & ~filters.private)
def invite_users(app, msg):
	chat_id = msg.chat.id
	reply = msg.reply_to_message
	if reply != None:
		ids = msg.reply_to_message.from_user.id
		try:
		    app.add_chat_members(chat_id, ids)
		except:
			msg.edit("**Этого челика нельзя добавить**")
	else:
		try: 
			user = msg.text.split(" ", 1)[1]
			try:
				app.add_chat_members(chat_id, user)
			except pyrogram.errors.exceptions.bad_request_400.UserNotMutualContact:
				msg.edit("**Этого пользователя нельзя добавить**")
			except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
				msg.edit("**Нет такого айди**")
			except:
				msg.edit('Не контакт')
		except:
			msg.edit("**Мало информации**")
