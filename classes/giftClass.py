from kivy.uix.screenmanager import Screen
import numpy, numpy.random
import pyautogui
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import sqlite3 as sql

class giftClass(Screen):
    a=0
    def winGift(self, value):
        self.a+=1
        if value == "money":
            dizi=[25, 50, 100, 250, 500]
        elif value == "health":
            dizi=[1, 2, 3]
        elif value == "diamond":
            dizi=[1, 2, 3, 5]
        rand=numpy.random.randint(1, len(dizi))
        i=dizi[rand]
        if rand == 50:
            yaz="You win 50 penny la tirrek :)"
        else:
            yaz="You win "+str(i)+" "+value
        baglanti=sql.connect('sql/baglanti.db')
        cursor=baglanti.cursor()
        cursor.execute("update uyeler set "+str(value)+"="+value+"+"+str(i)+" where uyeID=1")
        baglanti.commit()
        content = GridLayout(cols=1)
        content_cancel = Button(text='Close', size_hint_y=None, height=40)
        content.add_widget(Label(text=yaz))
        content.add_widget(content_cancel)
        popup = Popup(title="Prize Notification",size_hint=(None, None), size=(200, 200),content=content)
        content_cancel.bind(on_release=popup.dismiss)
        popup.open()
        if self.a==1:
            self.ids["money"].disabled=True
            self.ids["health"].disabled=True
            self.ids["diamond"].disabled=True
            self.ids["message"].text="You've exceeded the daily limit\n  Try again tomorrow."