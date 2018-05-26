from kivy.uix.screenmanager import Screen
import pyautogui
import sqlite3 as sql
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from classes.loginClass import loginClass as login

class mainClass(Screen):
    kullaniciID=None
    imageSource="C:/Users/SUForce/Desktop/1.png"
    def __init__(self, **kw):
        super().__init__(**kw)
        from classes.loginClass import loginClass
        login=loginClass()
        with login.baglanti:
            login.cursor.execute("select * from uyeler where uyeID=1")
            veri=login.cursor.fetchone()
            
    def degistir(self, value):
        if value == "5":
            pass
    def logout(self):
        self.parent.current="login"
    
    def news(self):
        content = GridLayout(cols=1)
        content_cancel = Button(text='Cancel', size_hint_y=None, height=40)
        content.add_widget(Label(text='There is no news, \ntry again later (not)'))
        content.add_widget(content_cancel)
        popup = Popup(title="News Notification",size_hint=(None, None), size=(200, 200),content=content)
        content_cancel.bind(on_release=popup.dismiss)
        popup.open()

    def alert(self, value):
        content = GridLayout(cols=1)
        content_cancel = Button(text='Cancel', size_hint_y=None, height=40)
        content.add_widget(Label(text=value+' module is not ready now, \ni think will not ready never.'))
        content.add_widget(content_cancel)
        popup = Popup(title="Module Notification",size_hint=(None, None), size=(250, 250),content=content)
        content_cancel.bind(on_release=popup.dismiss)
        popup.open()