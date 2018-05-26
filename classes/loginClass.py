from kivy.uix.screenmanager import Screen
import sqlite3 as sql
import pyautogui

class loginClass(Screen):
    baglanti=sql.connect('sql/baglanti.db')
    cursor=baglanti.cursor()
    with baglanti:
        cursor.execute("create table if not exists `sorular` (`soruID` integer primary key autoincrement, `soru` text not null, `dogruCevap` text not null, `yanlisBir` text not null, `yanlisIki` text not null, `yanlisUc` text not null, `ekleyenID` int(11) not null, soruDurum tinyint(1) not null);")
        cursor.execute("create table if not exists `uyeler` (`uyeID` integer primary key autoincrement, `kullaniciAdi` varchar(15) not null, `sifre` varchar(15) not null, `eMail` varchar(75) not null, adSoyad varchar(75), memleket varchar(20), dogumTarihi datetime, `health` int(3) not null, `diamond` int(4) not null, `money` int(7) not null);")
    def signin(self):
        user=self.ids["username"].text
        password=self.ids["password"].text
        if " " in user:
            self.ids["sonuc"].text="Kullanıcı Adı veya Şifrede Boşluk Olamaz !"
        else:
            if user != "" and password != "":
                self.cursor.execute("select * from uyeler where kullaniciAdi='"+user+"' and sifre='"+password+"'")
                if self.cursor.rowcount == 0:
                    self.ids["sonuc"].text="Kullanıcı Bulunamadı"
                else:
                    from classes.mainClass import mainClass as main
                    self.ids["sonuc"].text="Giriş Başarılı, Yönlendiriliyorsunuz.."
                    satir=self.cursor.fetchone()
                    degisken=satir[0]
                    main.kullaniciID=degisken
                    self.parent.current="main"