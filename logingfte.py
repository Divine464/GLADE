

from kivymd.uix.screen import MDScreen
from kivymd.toast import toast


class PreLoginScreen(MDScreen):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
    def show_toast(self,msg):
        toast(msg)



kv_lo= """
<PreLoginScreen>:
    name: 'prelogin'
    MDBoxLayout:
        md_bg_color: 0.1,0.1,0.1,1
        orientation: "vertical"
        spacing: "20dp"
        padding: "24dp"
        # pos_hint: {"center_y":0.5}
        # size_hint_y: None
        # height: self.minimum_height

        MDIconButton:
            icon: "arrow-left"
            pos_hint:{'center_x':0.05,'center_y':0.95}
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current= "cover"

        MDLabel:
            text: "CHOOSE A LOGIN METHOD"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: 1,1,1,1

        MDRectangleFlatIconButton:
            pos_hint: {"center_x":0.5,"center_y":0.8}
            size_hint: 0.82, 0.07
            text: "Continue with Google"
            icon: "google"
            on_release:
                root.show_toast("Not available yet")

        MDRectangleFlatIconButton:
            pos_hint: {"center_x":0.5}
            size_hint: 0.82, 0.07
            text: "Continue with Facebook"
            icon: "facebook"
            on_release:
                root.show_toast("Not available yet")
        MDRectangleFlatIconButton:
            pos_hint: {"center_x":0.5}
            size_hint: 0.82, 0.07

            text: "Continue with Apple"
            icon: "apple"
            on_release:
                root.show_toast("Not available yet")
        MDRectangleFlatIconButton:
            pos_hint: {"center_x":0.5}
            size_hint: 0.82, 0.07

            text: "Continue with Email"
            icon: "email"
            on_release:
                root.manager.transition.direction = "left"
                root.manager.current = "main"
"""