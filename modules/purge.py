from pyrogram import Client as app, filters

class Main:
	des = "Очистка истории чата"
	ver = "1.0"
	cmd_list = {
		"pur + реплай": "очищает все смс между этими сообщениями. При количестве сообщений >100 может не все удалять"
	}

@app.on_message(filters.me & filters.command("pur", "#") & filters.reply)
def purge_message(app, msg):
	lists = []
	c_list = []
	my_id = msg.message_id
	chat_id = msg.chat.id
	nm_id = msg.reply_to_message.message_id
	s = app.iter_history(chat_id, reverse=True, offset_id=nm_id)
	for i in s:
		lists.append(i.message_id)
		if i.message_id == my_id:
			break
		if len(lists) > 90:
			app.delete_messages(chat_id, lists)
			lists = c_list
	app.delete_messages(chat_id, lists)
