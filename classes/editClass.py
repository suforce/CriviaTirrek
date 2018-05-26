from kivy.uix.screenmanager import Screen
from classes.loginClass import loginClass as login
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
import calendar
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

class editClass(Screen):
    def confirm(self):
        username=self.ids["username"].text
        email=self.ids["email"].text
        name=self.ids["name"].text
        password=self.ids["password"].text
        birthdate=self.ids["birthdate"].text
        homeland=self.ids["homeland"].text
        with login.baglanti:
            login.cursor.execute("update uyeler set kullaniciAdi='{}', sifre='{}', eMail='{}', adSoyad='{}', memleket='{}', dogumTarihi='{}' where uyeID=1".format(username, password, email, name, homeland, birthdate))
            login.baglanti.commit()
            self.ids["confirm"].text="Your Information Are Successfully Update"