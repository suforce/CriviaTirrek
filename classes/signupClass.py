from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import sqlite3 as sql
import pyautogui

baglanti = sql.connect("sql/baglanti.db")
cursor = baglanti.cursor()

class signupClass(Screen):
    def signup(self):
        username = self.ids["username"].text
        email = self.ids["email"].text
        password = self.ids["password"].text
        repass = self.ids["repass"].text
        if " " in username or " " in email or " " in password or " " in repass:
            self.ids["hata"].text = "Boş Bırakma !"
        if password !=  repass:
            self.ids["hata"].text = "Şifreler Aynı Olmak Zorundadır !"
        else:
            cursor.execute("select * from uyeler where kullaniciAdi = '" + username + "'")
            if cursor.rowcount > 0:
                self.ids["hata"].text = "Bu Kullanıcı Adı İle Kayıtlı Bir Üyelik Zaten Var"
            else:
                cursor.execute("select * from uyeler where eMail = '" + email + "'")
                if cursor.rowcount > 0:
                    self.ids["hata"].text = "Bu E-Mail İle Kayıtlı Bir Üyelik Zaten Var"
                else:
                    cursor.execute("insert into uyeler(kullaniciAdi, sifre, eMail, health, diamond, money) values('{0}', '{1}', '{2}', 3, 10, 1000)".format(username, password, email))
                    self.ids["hata"].text = "Üye Kaydı Başarıyla Yapıldı, Şimdi Giriş Yapabilirsiniz."
                    self.parent.current="login"