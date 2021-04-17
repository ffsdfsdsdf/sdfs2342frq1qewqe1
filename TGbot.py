import telebot
import config
from random import*
from telebot import types

def RunBot():
	try:

		bot = telebot.TeleBot(config.TOKEN)

		#messages.getAllStickers   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		   # item1 = types.KeyboardButton("🎲 Рандомное число")
		   # item2 = types.KeyboardButton("😊 Как дела?")
		 #
		   # markup.add(item1, item2)
		   #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

			#item1 = types.KeyboardButton("Рандомное Число")
			#item2 = types.KeyboardButton("как дела")
			

			#markup.add(item1, item) stickers
			#bot.send_message(message.chat.id, "😕Рад приветствовать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы бить тебе ебало🤯.\n Хочешь узнать что я могу? - введи /команды".format(message.from_user, bot.get_me()),
		       #parse_mode='html', reply_markup=markup)



		@bot.message_handler(commands=['start'])
		def Start(message):
			bot.send_message(message.chat.id, "😕Рад приветствовать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы бить тебе ебало🤯.\nХочешь узнать что я могу? - введи /команды".format(message.from_user, bot.get_me()),
				parse_mode='html')

			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

			item1 = types.KeyboardButton("/команды ⭐️")

			markup.add(item1) 

			stick = open('stickers/sticker.webp', 'rb')
			bot.send_sticker(message.chat.id, stick)

			bot.send_message(message.chat.id, "Чтож, можно приступить..".format(message.from_user, bot.get_me()),
				parse_mode='html', reply_markup=markup)
		    

		@bot.message_handler(commands=['команды'])
		def CMD(message):
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

			item1 = types.KeyboardButton("/анекдот 🤪")
			item2 = types.KeyboardButton("/лох 😡")
			item3 = types.KeyboardButton("/курс 💵")
			item4 = types.KeyboardButton("/да/нет Этот бот крутой? 🍏")
			item5 = types.KeyboardButton("/порно 💦")
			item6 = types.KeyboardButton("/ава 🤩")
			item7 = types.KeyboardButton("/погода ❄️")
			item8 = types.KeyboardButton("/мат 🤬")
			item9 = types.KeyboardButton("Гороскоп🔮")
			
			

			markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9) 

			bot.send_message(message.chat.id, "Ебанушка, держи список всех команд😐".format(message.from_user, bot.get_me()),
				parse_mode='html', reply_markup=markup)

			


		@bot.message_handler(commands=['курс'])
		def Dollar(message):
			import requests
			from bs4 import BeautifulSoup
			import time

			bet = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&source=hp&ei=iWR4YJ_BNOiEwPAPgvS22AY&iflsig=AINFCbYAAAAAYHhymSH12pyG_nMC56JgECoKoUGFal1u&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAELEDEIMBEEYQggIyCAgAELEDEIMBMggIABCxAxCDATICCAAyCAgAELEDEIMBMggIABCxAxCDATIICAAQsQMQgwEyCAgAELEDEIMBMgUIABCxAzIICAAQsQMQgwE6CAguELEDEIMBUIUYWLcnYMEoaAFwAHgAgAF5iAH_BpIBBDExLjGYAQCgAQGqAQdnd3Mtd2l6sAEA&sclient=gws-wiz&ved=0ahUKEwjfqeLg0IDwAhVoAhAIHQK6DWsQ4dUDCAc&uact=5"
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

			
			full_page = requests.get(bet, headers=headers)


			soup = BeautifulSoup(full_page.content, "html.parser")

			Dollar = soup.findAll("span", {"class": "DFlfde SwHCTb"})


			bot.send_message(message.chat.id, "Курс на данный момент: " + str(Dollar[0].text) + " 💵")

		@bot.message_handler(commands=['анекдот']) #http://anekdotov.net/anekdot/index-page-22.html
		def Anekdot(message):
			import requests
			from bs4 import BeautifulSoup
			



			site = "https://www.anekdot.ru/release/anekdot/week/"
			
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

			
			full_page = requests.get(site, headers=headers)


			soup = BeautifulSoup(full_page.content, "html.parser")

			randomintForAnekdot = randint(1,60)

			Anekdot = soup.findAll("div", {"class": "topicbox", "id": randomintForAnekdot})



			bot.send_message(message.chat.id, "Анекдот🤪:")

			try:
				bot.send_message(message.chat.id, Anekdot[0])
			except:
				print("Опять этот анекдот...")
				bot.send_message(message.chat.id, "Упс, на сервере произожла ошибка🌈\nПопробуйте повторить попытку позже🔫")



		#@bot.message_handler(content_types=['text'])
		#def message(message):
			#bot.send_message(message.chat.id, config.Balance + " 🐺")
		@bot.message_handler(commands=['да/нет'])
		def TrueOrFalse(message):
			if(message.text == "/да/нет"):
				bot.send_message(message.chat.id, "Не было указано событие🍺")
			else:
				randomintTrueOrFalse = randint(1,2)
				if(randomintTrueOrFalse == 1):
					bot.send_message(message.chat.id, "Да✅")
				else:
					bot.send_message(message.chat.id, "Нет⛔️")


		@bot.message_handler(commands=['порно'])
		def Porn(message):
			
			stick = open('NackedSticks/'+ str(randint(1,10)) +'.webp', 'rb')
			bot.send_sticker(message.chat.id, stick)
			bot.send_message(message.chat.id, "Уфф💦")


		@bot.message_handler(commands=['ава'])
		def Avatarka(message):
			from PIL import Image
			
			Photo = open('avatars/' + str(randint(1,26)) + '.jpg', 'rb')
			bot.send_message(message.chat.id, "Аватарочка🤜🏻🤛🏻:")
			bot.send_photo(message.chat.id, Photo)


		@bot.message_handler(commands=['лох'])
		def Lox(message):	
			bot.send_message(message.chat.id, "Клоун ебаный🌷")


		@bot.message_handler(commands=['мат'])
		def Mat(message):
			import requests
			from bs4 import BeautifulSoup

			site = "http://www.russki-mat.net/e/mat_slovar.htm"
			
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

			
			full_page = requests.get(site, headers=headers)


			soup = BeautifulSoup(full_page.content, "html.parser")

			randomintMat = randint(1,60)


			Mat = soup.findAll("p", {"class": "art"})

			try:
				bot.send_message(message.chat.id, Mat[int(randomintMat)].text)
			except:
				bot.send_message(message.chat.id, "Упс, на сервере произожла ошибка🌈\nПопробуйте повторить попытку позже🔫")
				print("мат..")
			

		@bot.message_handler(commands=['погода'])
		def Weather(message):
			import requests
			from bs4 import BeautifulSoup

			site = "https://www.gismeteo.ru/weather-velikiye-luki-4144/now/"
			
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

			
			full_page = requests.get(site, headers=headers)


			soup = BeautifulSoup(full_page.content, "html.parser")

			randomintForAnekdot = randint(1,60)


			Weather = soup.findAll("div", {"class": "now__weather"})
			WeatherS = soup.findAll("div", {"class": "now__astro nowastro"})
			Osadki = soup.findAll("div", {"class": "now__desc"})
		#https://time100.ru/Velikie-Luky

			TimeSite = "https://www.google.ru/search?q=%D0%B2%D0%B5%D1%80%D0%BC%D1%8F&newwindow=1&source=hp&ei=Gg97YMDVIvKjgweNlpioAQ&iflsig=AINFCbYAAAAAYHsdKpXqUk_w1NM1OKH2rw-eOpiWLgtj&oq=%D0%B2%D0%B5%D1%80%D0%BC%D1%8F&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAELEDEAoyBAgAEAoyBwgAELEDEAoyDQgAELEDEIMBEMkDEAoyBQgAEJIDMgUIABCSAzIICAAQsQMQgwEyCgguELEDEIMBEAoyBAgAEAoyBwguELEDEAo6DggAELEDEIMBEMcBEKMCOgUIABCxAzoICAAQxwEQrwE6AgguOgIIADoFCC4QkwI6CAgAEMcBEKMCOggILhCxAxCDAToFCC4QsQM6CAguELEDEJMCOggIABCxAxDJA1DBBljVC2CrDWgAcAB4AIABVIgBhgOSAQE1mAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz&ved=0ahUKEwjAytzZ24XwAhXy0eAKHQ0LBhUQ4dUDCAc&uact=5"

			
			full_page = requests.get(TimeSite, headers=headers)


			soup = BeautifulSoup(full_page.content, "html.parser")


			Time = soup.findAll("div", {"class": "gsrt vk_bk dDoNo FzvWSb XcVN5d DjWnwf"})
			Data = soup.findAll("div", {"class": "vk_gy vk_sh"})

			try:
				bot.send_message(message.chat.id, Time[0].text + ", Великие Луки (МСК)\n" + Data[0].text + "\n" +"Температура на улице: " + str(Weather[0].text)+ "☀️" + "\n" + "Осадки: " + Osadki[0].text + "🌨")
			except:
				print("Проблемы с погодой..")
				bot.send_message(message.chat.id, "Упс, на сервере произожла ошибка🌈\nПопробуйте повторить попытку позже🔫")

		@bot.message_handler(content_types=['text'])
		def get_text_messages(message):
			if message.text == "Гороскоп🔮":


				markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

				item1 = types.KeyboardButton("Лев 🦁")
				item2 = types.KeyboardButton("Назад ◀️")


				markup.add(item1, item2) 

				bot.send_message(message.chat.id, "Выберите знак для гороскопа:".format(message.from_user, bot.get_me()),
					parse_mode='html', reply_markup=markup)
			if message.text == "Лев 🦁":
				import requests
				from bs4 import BeautifulSoup
				import time

				Goroskop = "https://horo.mail.ru/prediction/leo/today/"
				headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

				
				full_page = requests.get(Goroskop, headers=headers)


				soup = BeautifulSoup(full_page.content, "html.parser")

				Predskazanie = soup.findAll("div", {"class": "article__item article__item_alignment_left article__item_html"})
				Other = soup.findAll("div", {"class": "p-score-day__item__value"})
				Other2 = soup.findAll("div", {"class": "p-score-day__item__text"})
				


				bot.send_message(message.chat.id, "Предсказание на сегодня🔮\n " + str(Predskazanie[0].text) + " 🦁\n" + Other2[0].text + ": " + Other[0].text + "🧑‍💻\n" +
					Other2[1].text + ": " + Other[1].text + "❤️\n" + Other2[2].text + ": " + Other[2].text + "👾\n" + Other2[3].text + ": " + Other[3].text + "🙌")

			if message.text == "Назад ◀️":
				markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

				item1 = types.KeyboardButton("/анекдот 🤪")
				item2 = types.KeyboardButton("/лох 😡")
				item3 = types.KeyboardButton("/курс 💵")
				item4 = types.KeyboardButton("/да/нет Этот бот крутой? 🍏")
				item5 = types.KeyboardButton("/порно 💦")
				item6 = types.KeyboardButton("/ава 🤩")
				item7 = types.KeyboardButton("/погода ❄️")
				item8 = types.KeyboardButton("/мат 🤬")
				item9 = types.KeyboardButton("Гороскоп🔮")

				
				

				markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9) 

				bot.send_message(message.chat.id, "Ну, назад так назад◀️".format(message.from_user, bot.get_me()),
					parse_mode='html', reply_markup=markup)


		bot.polling(none_stop=True)
	except:
		RunBot()
	RunBot()
RunBot()


