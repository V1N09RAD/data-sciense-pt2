#Социальные индикаторы. Среднедушевой денежный доход населения (руб.)
from datetime import datetime
import csv
from matplotlib import pyplot as plt
filename = 'inddata_73.csv'
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class PerCapitaIncome(App):
	def build(self):
		self.bl = BoxLayout(orientation = "vertical")
		self.lb = Label(text = "Среднедушевой денежный доход населения (руб.) с 2001 - 2006г.", 
			font_size = 25)
		self.ti = TextInput(multiline=False,
			text = "Введите область",
			font_size = 25,
			size_hint = (0.7, 0.1),
			pos_hint = {"center_x": 0.5,
			"center_y": 0.5},
			padding_y = (10, 10))
		self.bt = Button(text = "Визуализировать",
			font_size = 25,
			size_hint = (0.7, 0.1),
			pos_hint = {"center_x": 0.5,
			"center_y": 0.5})
		self.bl.add_widget(self.lb)
		self.bl.add_widget(self.ti)
		self.bl.add_widget(self.bt)
		self.bt.bind(on_press = self.babki)
		return self.bl
	def babki(self, instance):
		self.textt = self.ti.text
		a = self.textt
		def bablo(a):
			vremy, dengi = [], []
			with open(filename, encoding = 'utf8') as f:
				reader = csv.reader(f)
				header_row = next(reader)
				for row in reader:
					d = float(row[7])
					v = datetime.strptime(row[6], "%Y-%m-%dT%H:%M:%S")
					r = str(row[3])
					if r == a:
						vremy.append(v)
						dengi.append(d)
			fig, ax = plt.subplots()
			plt.plot(vremy, dengi)
			plt.title(f"Среднедушевой денежный доход населения (руб.) 2001 - 2006 {a}")
			plt.xlabel("Дата")
			plt.ylabel("Денежный доход")
			plt.show()
		bablo(a)
if __name__ == "__main__":
	PerCapitaIncome().run()
