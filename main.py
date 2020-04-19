from kivy.app import App
#import kivymd
#from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen
from youtube import video
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from plyer import notification
from kivymd.uix.dialog import MDDialog
import requests
from kivy.clock import Clock
import clipboard

def notificationCheck(dt):
	res = requests.get("https://pastebin.com/raw/NdBzGvhq")
	r = requests.get("https://pastebin.com/raw/fe76KF0B")
	if r.text == "1":
		notification.notify(message=res.text)
		Clock.unschedule(MainApp.check)
	else:
		pass

#Window.size = (400, 640)
class HomeScreen(Screen):
	pass

class SettingsScreen(Screen):
	pass

class MainApp(App):
	theme_cls = ThemeManager()
	theme_cls.theme_style = 'Dark'
	dropdown = ObjectProperty()
	check = Clock.schedule_interval(notificationCheck, 60)

	def on_start(self):
		#Create the dropdown menu
		url = clipboard.paste()
		if "youtube" or "youtu.be" in url: 
			self.getThumbnail(url)
		self.dropdown = MDDropdownMenu(width_mult=1)
		#Add items to the menu
		res = ["720","360"]
		for i in res:
			#print(i)
			self.dropdown.items.append(
				{"viewclass":"MDMenuItem",
				"text": i+"p",
				"callback": self.option_callback})

	def ok(self, text, widget):
		pass

	def option_callback(self, option):
		print(option)
		url = self.root.ids['home_screen'].ids.url
		url = url.text
		if url == "":
			print("First enter an url!")
			err_alert = MDDialog(title="Error", text="Enter a YouTube video url to proceed.", size_hint=[.5, .5], auto_dismiss=False, events_callback=self.ok)
			err_alert.open()
		else:
			video.download(url, option)

	def change_screen(self, screen_name):
		screen_manager = self.root.ids['screen_manager']
		screen_manager.current = screen_name

	def getThumbnail(self, url):
		if url[4] == "s" and "youtube" in url:
			#url = clipboard.paste()
			url_id = url[32:]
			thumbnail = "https://img.youtube.com/vi/"+url_id+"/maxresdefault.jpg"
			#print("HTTPS -",thumbnail)
			self.root.ids['home_screen'].ids.thumbnail.source = thumbnail
		elif "http" and "youtube" in url:
			url_id = url[31:]
			thumbnail = "https://img.youtube.com/vi/"+url_id+"/maxresdefault.jpg"
			#print("HTTP -", thumbnail)
			self.root.ids['home_screen'].ids.thumbnail.source = thumbnail
		elif "youtu.be" and "https" in url:
			url_id = url[17:]
			thumbnail = "https://img.youtube.com/vi/"+url_id+"/maxresdefault.jpg"
			self.root.ids['home_screen'].ids.thumbnail.source = thumbnail
		elif "youtu.be" and "http" in url:
			url_id = url[16:]
			thumbnail = "https://img.youtube.com/vi/"+url_id+"/maxresdefault.jpg"
			self.root.ids['home_screen'].ids.thumbnail.source = thumbnail
		else:
			#print("Hi")
			pass		

	def getURL(self):
		url = self.root.ids['home_screen'].ids.url
		#print(url.text)
		if url.text[0] == " ":
			print("Remove Space from start")	
		else:
			url = url.text
			MainApp.getThumbnail(self, url)
			pass
	

MainApp().run()

	# MDTextFieldRound:
	# 	pos_hint: 0.5, 0.5
	# 	size_hint: 1, .5
	# 	icon_left: "plus"
	# 	hint_text: 'Enter Video URL'
	# 	id: url
	# Widget:
	# 	MDIconButton:
	# 		icon: "send"
	# 		text: "Download"
	# 		on_release: app.getURL()