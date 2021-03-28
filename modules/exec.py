from pyrogram import Client, filters
import os
import importlib

class Main:
	des = "Выполнение Python кода. Без возврата"
	ver = "1.0"
	cmd_list = {
		"exec + код": "выполнение"
	}

@Client.on_message(filters.command("exec", ".") & filters.me)
def exec_func(app, msg):
	try:
		code = msg.text.split(maxsplit=1)[1]
	except:
		code = msg.reply_to_message.text
	exec(f'{code}')