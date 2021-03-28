import os
import time
import urllib
from flask import Flask
from pyrogram import Client
from threading import Thread


app = Client("kgbot")
web = Flask(__name__)


owner = os.getenv("REPL_OWNER")
slug = os.getenv("REPL_SLUG")
url = f"http://{slug}.{owner}.repl.co"

@web.route("/")
def home():
	return "Работает"

	
def site():
	web.run(host="0.0.0.0")
def stay_alive():
	while True:
		start = time.time()
		while True:
			end = time.time()
			if ((end - start) >= (2 * 60)):
				urllib.request.urlopen(url)
				os.system("clear")
				print("Работает")
				break


site_thread = Thread(target=site)
ping_thread = Thread(target=stay_alive)
site_thread.start()
ping_thread.start()

with app:
	print(f"Отлично, бот работает теперь берем \"{url}\", и идем на uptimerobot.com")
app.run()
