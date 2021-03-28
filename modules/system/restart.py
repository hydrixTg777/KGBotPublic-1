from pyrogram import Client, filters


class Main:
	des = "Модуль для перезагрузки бота"
	cmd_list = {
		"restart": "Перезагрузить"
	}
	

@Client.on_message(filters.me & filters.command("restart", "."))
def restart_bot(app, msg):
	msg.edit("Перезагрузка...")
	app.restart(False)
	msg.edit("Перезагрузка прошла успешно!")