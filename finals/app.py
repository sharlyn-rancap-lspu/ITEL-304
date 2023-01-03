from kivmob import KivMob, TestIds, RewardedListenerInterface

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.properties import NumericProperty



class Screenmgr(ScreenManager):
    pass


class SimpleUI(Screen):
    pass


class InterstitialAdScreen(Screen):
    pass


class Rewarded(Screen):
    pass


class SimpleApp(MDApp):
    def __init__(self, **kwargs):
        self.theme_cls.theme_style = "Dark"
        super().__init__(**kwargs)

    ads = KivMob(TestIds.APP)  # put your Admob Id in case you want to put your own ads.
    points = NumericProperty(0)

    def build(self):
        self.ads.new_banner(TestIds.BANNER, False)
        self.ads.request_banner()
        self.ads.show_banner()

        return Screenmgr()



if __name__ == "__main__":
    SimpleApp().run()
