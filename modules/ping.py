from pyrogram import Client, filters
import time

class Main:
	des = "проверяем пинг"
	ver = "1.0"
	cmd_list = {
		"ping": "думаю понятно"
	}

@Client.on_message(filters.command("ping", "#") & filters.me)
def ping(app, msg):
  start = time.time()
  msg.edit("Пингуем...")
  delta_ping = time.time() - start
  msg.edit(f"**Пинг: ** `{delta_ping * 1000:.2f}` мс")