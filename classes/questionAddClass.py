from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup 
import sqlite3 as sql

class questionAddClass(Screen):
    def cont(self):
        baglanti=sql.connect('sql/baglanti.db')
        cursor=baglanti.cursor()
        question=self.ids["question"]
        true=self.ids["true"]
        wrong1=self.ids["wrong1"]
        wrong2=self.ids["wrong2"]
        wrong3=self.ids["wrong3"]
        if question.text == "Write Your Question":
            content = GridLayout(cols=1)
            content_cancel = Button(text="I'm Sorry", size_hint_y=None, height=40)
            content.add_widget(Label(text='Question can not be empty !'))
            content.add_widget(content_cancel)
            popup = Popup(title="Alert",size_hint=(None, None), size=(275, 275),content=content)
            content_cancel.bind(on_release=popup.dismiss)
            popup.open()
            question.focus=True
        elif true.text == "Right Answer":
            content = GridLayout(cols=1)
            content_cancel = Button(text="I'm Sorry", size_hint_y=None, height=40)
            content.add_widget(Label(text='Right Answer can not be empty !'))
            content.add_widget(content_cancel)
            popup = Popup(title="Alert",size_hint=(None, None), size=(275, 275),content=content)
            content_cancel.bind(on_release=popup.dismiss)
            popup.open()
            true.focus=True
        elif wrong1.text == "Wrong Answer 1":
            content = GridLayout(cols=1)
            content_cancel = Button(text="I'm Sorry", size_hint_y=None, height=40)
            content.add_widget(Label(text='Wrong Answer 1 can not be empty !'))
            content.add_widget(content_cancel)
            popup = Popup(title="Alert",size_hint=(None, None), size=(275, 275),content=content)
            content_cancel.bind(on_release=popup.dismiss)
            popup.open()
            wrong1.focus=True
        elif wrong2.text == "Wrong Answer 2":
            content = GridLayout(cols=1)
            content_cancel = Button(text="I'm Sorry", size_hint_y=None, height=40)
            content.add_widget(Label(text='Wrong Answer 2 can not be empty !'))
            content.add_widget(content_cancel)
            popup = Popup(title="Alert",size_hint=(None, None), size=(275, 275),content=content)
            content_cancel.bind(on_release=popup.dismiss)
            popup.open()
            wrong2.focus=True
        elif wrong3.text == "Wrong Answer 3":
            content = GridLayout(cols=1)
            content_cancel = Button(text="I'm Sorry", size_hint_y=None, height=40)
            content.add_widget(Label(text='Wrong Answer 3 can not be empty !'))
            content.add_widget(content_cancel)
            popup = Popup(title="Alert",size_hint=(None, None), size=(275, 275),content=content)
            content_cancel.bind(on_release=popup.dismiss)
            popup.open()
            wrong3.focus=True
        else:
            with baglanti:
                cursor.execute("insert into sorular(soru, dogruCevap, yanlisBir, yanlisIki, yanlisUc, ekleyenID, soruDurum) values('{}', '{}', '{}', '{}', '{}', 1, 0)".format(question, true, wrong1, wrong2, wrong3))
                baglanti.commit()
                content = GridLayout(cols=1)
                content_cancel = Button(text="Great", size_hint_y=None, height=40)
                content.add_widget(Label(text='Your question  will be add after administrator approval.\n                                       Thank You'))
                content.add_widget(content_cancel)
                popup = Popup(title="Notification",size_hint=(None, None), size=(400, 400),content=content)
                content_cancel.bind(on_release=popup.dismiss)
                popup.open()
                wrong3.focus=True
                self.parent.current="main"