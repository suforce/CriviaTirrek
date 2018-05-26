from kivy.uix.screenmanager import Screen
import pyautogui

class profileClass(Screen):
    def read(self):
        from loginClass import loginClass as login
        with login.baglanti:
            login.cursor.execute("select * from uyeler where uyeID=1")
            sonuc=login.cursor.fetchone()
            pyautogui.alert(str(sonuc[3]))
            self.ids["username"].text=sonuc[1]
            self.ids["email"].setAttribute("hint_text", sonuc[3])
            self.ids["name"].setAttribute("hint_text", sonuc[4])
            self.ids["homeland"].setAttribute("hint_text", sonuc[5])
            self.ids["birthdate"].setAttribute("hint_text", sonuc[6])
            self.ids["health"].setAttribute("hint_text", sonuc[7])
            self.ids["diamond"].setAttribute("hint_text", sonuc[8])
            self.ids["money"].setAttribute("hint_text", sonuc[9])