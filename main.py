from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon


class Demoapp(MDApp):
    def build(self):
        label = MDLabel(text="Hello world!", halign="center", theme_text_color="Custom",
                        text_color=(236 / 255.0, 98 / 255.0, 81 / 255.0, 1),font_style='Caption')
        iconlabel=MDIcon(icon='language-python',halign='center')
        return iconlabel


Demoapp().run()
