# Activity 6.2 : Sample Kivy Float

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.lang import Builder


root = Builder.load_string('''

FloatLayout:
    canvas.before:
        Color:
            rgba: 0, 224, 255, 0.5
        Rectangle:
            pos: self.pos
            size: self.size

    Button:
    
        text: 'Click Me!'
        size_hint: .3, .1
        pos_hint: {'center_x':.5, 'center_y': .5}
''')


class FloatApp(App):

    def build(self):
        return root


if __name__ == '__main__':
    app = FloatApp()
    app.run()
