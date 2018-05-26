from kivy.uix.screenmanager import Screen

class newGameClass(Screen):
    def secim(self, value):
        classic=self.ids["classic"]
        challenge=self.ids["challenge"]
        random=self.ids["random"]
        explanation=self.ids["explanation"]
        if value == "1":
            explanation.text="if you win 6 roundes, you will win the match"
            classic.text="Classic Selected"
            challenge.text="Challenge"
            classic.disabled=True
            challenge.disabled=False
        elif value == "2":
            explanation.text="Play multiple opponents at the same time"
            challenge.text="Challenge Selected"
            classic.text="Classic"
            challenge.disabled=True
            classic.disabled=False
        elif value == "3":
            random.background_color=1, 1, 1, 1
            random.disabled=True

    def startGame(self, value):
        if value == "1":
            self.parent.current = "game"