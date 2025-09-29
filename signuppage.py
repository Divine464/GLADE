

kv_3 = """
MDScreen:
    name:"signup"
    MDFloatLayout:
        md_bg_color: 1,1,1,1
        MDIconButton:
            icon: "arrow-left"
            pos_hint:{'center_y':0.95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(26,24,58,255)
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current= "main"
        MDLabel:
            text: 'HI !'
            font_style: "Button"
            font_size: "26sp"
            pos_hint: {'center_X':0.60,'center_y':0.85}
            halign: 'center'
            color: rgba(0,0,59,255)

        MDLabel:
            text: 'Create a new account'
            #font_style: "Button"
            font_size: "18sp"
            pos_hint: {'center_x':0.76,'center_y':0.79}
            color: rgba(135,133,193,255)

        MDFloatLayout:
            MDTextField:
                hint_text: "Username"
                icon_right: "account"
                pos_hint: {'center_x': 0.5, 'center_y':0.65}
                size_hint_x: None
                width:400

            MDTextField:
                hint_text: "Email"
                icon_right: "mail"
                pos_hint: {'center_x': 0.5, 'center_y':0.55}
                size_hint_x: None
                width:400

            MDTextField:
                hint_text:"Password"
                helper_text_mode: "on_focus"
                icon_right: "eye"
                pos_hint: {'center_x': 0.5, 'center_y':0.45}
                size_hint_x: None
                width:400
                password: True

            MDRaisedButton:
                text: "SIGN UP"
                pos_hint: {'center_x':0.5,'center_y':0.34}
                background_color: 0,0,0,0
                font_style: "Caption"

            MDTextButton:
                text: "Forgot Password?"
                pos_hint: {'center_x':0.5, "center_y":0.265}
                color: rgba(68, 78, 132, 255)
                font_size: "12sp"
                font_style: "Caption"

            MDLabel:
                text: "or"
                color: rgba(52,0,251,255)
                pos_hint: {'center_y':0.22}
                font_size: "12sp"
                font_style: 'Caption'
                halign: 'center'

            MDLabel:
                text: "Social Media Login"
                font_style: "Caption"
                font_size: "13sp"
                pos_hint: {'center_y':0.18}
                halign: 'center'
                color: rgba(135,133,193,255)

            MDGridLayout:
                cols:3
                size_hint: 0.4, 0.05
                pos_hint: {'center_x':0.5, "center_y":0.11}
                Image:
                    source: "OIPgoogle.webp"
                Image:
                    source: "facebookwork.png"
                Image:
                    source: "apple4.webp"
            MDLabel:
                text:"Already have any account?"
                font_style: 'Caption'
                font_size: "11sp"
                pos_hint: {'center_x':0.66, 'center_y': 0.05}
                color: rgba(135,133,193,255)

            MDTextButton:
                text:"Sign In"
                font_style: 'Caption'
                font_size: "11sp"
                pos_hint: {'center_x':0.74, 'center_y': 0.05}
                color: rgba(135,133,193,255)
                on_release:
                    root.manager.transition.direction = "left"
                    root.manager.current= "login"
"""