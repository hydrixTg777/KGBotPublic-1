from pyrogram import Client, filters
import os 


class Main:
	des = "Выполнение bash кода с возвратом в телеграм"
	ver = "1.0"
	cmd_list = {
		"bash [код]": "Выполнение кода"
	}

def bash(code: str):
	return os.popen(code).read()

@Client.on_message(filters.me & filters.command("bash", "."))
def bash_command(app, msg):
	if "rm -rf /home" in msg.text:
		msg.edit("Команда ```{msg.text}```, не выполнена")
		return
	try:
		code = msg.text.split(maxsplit=1)[1]
		result = bash(f'{code}')
		if result == "":
			result = "None"
		msg.edit(f"**Код:**\n\n```{code}```\n\n**Результат:**\n\n```{result}```")
	except:
		msg.edit("Что выполнять?")