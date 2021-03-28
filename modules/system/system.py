from pyrogram import Client as app, filters
import os
import random
import importlib

class Main:
	des = "Системный модуль, для управления юзерботом"
	ver = "1.0 beta"
	cmd_list = {
		"help": "Список доступных модулей",
		"help [модуль]": "Посмотреть информацию о модуле",
		"lmod [имя] + реплай": "загрузить модуль",
		"demod [имя]": "Удалить модуль",
		"drmod": "Отправить модуль в чат",
		"rename [имя] [новое]": "Переименовать модуль",
	}


def modules_list():
	return [module[:-3] for module in os.listdir("modules") if module.endswith(".py")]
def system_modules_list():
	return [module[:-3] for module in os.listdir("modules/system") if module.endswith(".py")]

@app.on_message(filters.me & filters.command("help", "."))
def help_bot(app, msg):
	me = app.get_me()
	try:
		name_module = msg.text.split(maxsplit=1)[1].replace("/", ".")
		if name_module in modules_list():
			s = importlib.import_module(f"modules.{name_module}")
			try:
				des = s.Main.des
			except:
				des = "Неизвестно"
			try:
				ver = s.Main.ver
			except:
				ver = "Неизвестно"
			try:
				cmd_list = s.Main.cmd_list
				text_cmd = ""
				for i in cmd_list.keys():
					text_cmd += f"• {i} - {cmd_list[i]}\n"
			except:
				text_cmd = "Неизвестно"
			text = f"Информация о модуле **{name_module}:**\n\n**Описание:**\n{des}\n\n**Версия:**\n{ver}\n\n**Команды:**\n{text_cmd}"
			msg.edit(text)
		else:
			msg.edit(f"Модуль **{name_module}** не найден!")
	except IndexError:
		moduls = modules_list()
		text = f"**[KGBot](tg://user?id={me.id})**\n\n**Доступные модули:**\n"
		for i in moduls:
			text += f"• {i}\n"
		text += f"\nВсего модулей: **{len(moduls)}**\n.help [name] - информация о модуле"
		msg.edit(text)
@app.on_message(filters.command("info", "#") & filters.me & filters.reply)
def info(app, msg):
	print(msg.reply_to_message)
@app.on_message(filters.me & filters.command("lmod", ".") & filters.reply)
def load_module(app, msg):
	doc = msg.reply_to_message.document
	chars = "abcdefghijklmnopqrstuvwxyz"
	try: 
		name = msg.text.split(maxsplit=1)[1]
		name = name.replace(" ", "_")
	except:
		name = ""
		for i in range(7):
			name += random.choice(chars)
	if doc:
		if doc.mime_type == "text/x-python":
			file_id = doc.file_id
			if name not in modules_list():
				msg.edit("Скачиваем...")
				app.download_media(file_id, f"modules/{name}.py")
				msg.edit("Перезагрузка бота...")
				app.restart(False)
				msg.edit(f"Модуль **{name}** установлен и готов к использованию")
			else:
				msg.edit("Модуль с таким именем существует!")
		else:
			msg.edit("Файл не имеет нужный формат (`.py`)")
	else:
		msg.edit("Это не файл...")
@app.on_message(filters.me & filters.command("demod", "."))
def delete_module(app, msg):
	try:
		name = msg.text.split(maxsplit=1)[1]
		name = name.replace(" ", "_")
		if name in modules_list():
			os.popen(f"rm modules/{name}.py")
			app.restart(False)
			msg.edit(f"Модуль **{name}** удалён!")
		else:
			msg.edit(f"Модуль **{name}** не найден!")
	except IndexError:
		msg.edit("Не указано имя модуля")
@app.on_message(filters.me & filters.command("drmod", "."))
def drop_module(app, msg):
	chat = msg.chat
	chat_perm = chat.permissions
	chat_tp = chat.type
	stat = False
	try:
		name = msg.text.split(maxsplit=1)[1].replace(" ", "_")
		if name in modules_list():
			if chat_tp == ("private" or "bot"):
				stat = True
			else:
				if chat_perm.can_send_media_messages:
					stat = True
			if stat:
				msg.edit("Загружаю модуль...")
				app.send_document(msg.chat.id, f"modules/{name}.py")
				msg.delete()
			else:
				msg.edit("Загрузка файлов в этот чат запрещена")
		else:
			msg.edit(f"Модуль **{name}** не найден")
	except IndexError:
		msg.edit("Укажите имя модуля!")
@app.on_message(filters.me & filters.command("rename","."))
def module_renamer(app, message):
    stock = message.text.split(' ',2)[1]
    name = message.text.split(' ',2)[2]
    if stock in modules_list():
      os.rename(f"modules/{stock}.py", f"modules/{name}.py")
