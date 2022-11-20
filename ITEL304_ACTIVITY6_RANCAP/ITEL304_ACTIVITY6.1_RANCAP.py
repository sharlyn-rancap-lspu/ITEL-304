# Activity 6.1 : Sample login using Kivy

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window


class LoginApp(App):
    def build(self):
        self.title = "Login"
        Window.size = (600, 500)
        Window.clearcolor = (.1, .5, .6, 1)
        layout = GridLayout\
            (cols=2, rows=2, padding=20, spacing=20, row_default_height=40)

        username = TextInput(multiline=False)
        password = TextInput(password=True, multiline=False)
        userlabel = Label(text="Username", size_hint_x=None, width=80)
        passlabel = Label(text="Password", size_hint_x=None, width=80)

        layout.add_widget(userlabel)
        layout.add_widget(username)
        layout.add_widget(passlabel)
        layout.add_widget(password)

        layout1 = BoxLayout(orientation='vertical', padding=50, spacing=20,)
        layout1.add_widget(layout)

        loginbutton = Button(text="Login")
        registerbutton = Button(text="Register")

        layout1.add_widget(loginbutton)
        layout1.add_widget(registerbutton)

        return layout1


if __name__ == '__main__':
    app = LoginApp()
    app.run()
