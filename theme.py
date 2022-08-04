from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

class Demoapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        screen=MDScreen()
        btn_flat=MDRectangleFlatButton(text="Hello World",pos_hint={'center_x':0.5,'center_y':0.5})
        screen.add_widget(btn_flat)
        return screen
Demoapp().run()