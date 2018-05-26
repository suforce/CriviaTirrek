from kivy.uix.screenmanager import Screen
import pyautogui

class factoryClass(Screen):
    click=0
    selected=None

    def select(self, value):
        self.ids["continue"].disabled=False
        self.selected=value
        dizi=["History", "Geography", "Art", "Sport", "Entertainment", "Science"]
        for i in dizi:
            if i == value:
                self.ids[value].text+=" Selected"
                self.ids[value].disabled=True
                dizi.remove(i)
                for k in dizi:
                    self.ids[k].text=k
                    self.ids[k].disabled=False
    def goon(self):
        if self.click == 1:
            self.parent.current="questionAdd"