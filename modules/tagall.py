from pyrogram import Client as app, filters
import time

class Main:
	des = "тэгает всех в чате"
	ver = "1.0"
	cmd_list = {
		"tagall": "тэгнуть"
	}

@app.on_message(filters.me & filters.command("tagall", "."))
def tag_all(app, msg):
	chat_id = msg.chat.id
	string = ""
	limit = 1
	for member in app.iter_chat_members(chat_id):
		tag = member.user.username
		if limit <= 5:
			if tag != None:
				string += f"@{tag}\n"
			else:
				string += f"{member.user.mention}\n"
			limit += 1
		else:
			app.send_message(chat_id, text=string)
			limit = 1
			string = ""
			time.sleep(5)