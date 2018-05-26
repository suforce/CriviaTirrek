from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang.builder import Builder
from kivy.core.window import Window

###             Classes             ###
from classes.loginClass import loginClass
from classes.mainClass import mainClass
from classes.signupClass import signupClass
from classes.newGameClass import newGameClass
from classes.tirrekationClass import tirrekationClass
from classes.waroftirrekClass import waroftirrekClass
from classes.gameClass import gameClass
from classes.factoryClass import factoryClass
from classes.questionAddClass import questionAddClass
from classes.giftClass import giftClass
from classes.aboutusClass import aboutusClass
from classes.profileClass import profileClass
from classes.editClass import editClass

class CriviaTirrek(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm=ScreenManager() 
        Window.size = (450, 550)
    def build(self):
        Builder.load_file("kv/loginClass.kv")
        Builder.load_file("kv/signupClass.kv")
        Builder.load_file("kv/mainClass.kv")
        Builder.load_file("kv/newGameClass.kv")
        Builder.load_file("kv/tirrekationClass.kv")
        Builder.load_file("kv/waroftirrekClass.kv")
        Builder.load_file("kv/gameClass.kv")
        Builder.load_file("kv/factoryClass.kv")
        Builder.load_file("kv/questionAddClass.kv")
        Builder.load_file("kv/giftClass.kv")
        Builder.load_file("kv/aboutusClass.kv")
        Builder.load_file("kv/profileClass.kv")
        Builder.load_file("kv/editClass.kv")

        screens=[
            loginClass(name="login"),
            signupClass(name="signup"), 
            mainClass(name="main"),
            newGameClass(name="newgame"),
            tirrekationClass(name="tirrekation"),
            waroftirrekClass(name="waroftirrek"),
            gameClass(name="game"),
            factoryClass(name="factory"),
            questionAddClass(name="questionAdd"),
            giftClass(name="gift"),
            aboutusClass(name="aboutus"),
            profileClass(name="profile"),
            editClass(name="edit")
        ]
        for i in screens:
            self.sm.add_widget(i)
        self.sm.current="login"
        return self.sm

CriviaTirrek().run()