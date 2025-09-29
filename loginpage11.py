
from kivy.uix.screenmanager import SlideTransition, FadeTransition, SwapTransition, WipeTransition
from kivymd.app import MDApp
import sqlite3
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast



class LoginScreen(MDScreen):
    def login_user(self):

        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        if not username or not password:
            toast("Please enter both fields")
            return

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT*FROM users WHERE username= ? AND password = ?", (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            toast("Login Successful")
            MDApp.get_running_app().current_user = username

            email = result[2]
            profile_pic = result[4] if result[4] else "images.jpeg"

            dashboard = self.manager.get_screen("dashboard")
            dashboard.set_user(username,email,profile_pic)            

            income_screen = self.manager.get_screen("income")
            income_screen.username = username

            profile_screen = self.manager.get_screen("profile")
            profile_screen.set_user(username, email,profile_pic)
            

            self.manager.transition = WipeTransition()
            self.manager.current = "dashboard"

        else:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username= ?", (username,))
            user_exists = cursor.fetchone()
            conn.close()

            if user_exists:
                toast("Incorrect info")
            else:
                toast("Account does not exist")
        

        self.ids.username.text = ""
        self.ids.password.text = ""
        

    def toggle_password_visibility(self, checkbox, value):
        self.ids.password.password = not value
        self.ids.password_text.text = "Hide Password" if value else "Show Password"


        


kv_2= """
<LoginScreen>:
    name:"login"
    MDFloatLayout:
        md_bg_color: 0.1,0.1,0.1,1
        MDIconButton:
            icon: "arrow-left"
            pos_hint:{'center_y':0.95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            # text_color: rgba(26,24,58,255)
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current= "main"
        MDLabel:
            text: 'WELCOME BACK!'
            font_style: "Button"
            font_size: "26sp"
            pos_hint: {'center_X':0.60,'center_y':0.85}
            halign: 'center'
            color: 0.7,0.75,0.8,1
            


        MDLabel:
            text: 'Sign In To Continue'
            halign: 'center'
            #font_style: "Button"
            font_size: "18sp"
            pos_hint: {'center_x':0.51,'center_y':0.79}
            color: 0.9,0.9,0.9,1


        MDFloatLayout:
            MDTextField:
                id: username
                hint_text: "Username"
                mode: "rectangle"
                #helper_text: "or click on forgot username"
                #helper_text_mode: "on_focus"
                icon_right: "account"
                pos_hint: {'center_x': 0.5, 'center_y':0.65}
                size_hint_x: None
                width:400

            MDTextField:
                id: password
                hint_text:"Password"
                mode: "rectangle"
                helper_text_mode: "on_focus"
                icon_right: "eye"
                pos_hint: {'center_x': 0.5, 'center_y':0.52}
                size_hint_x: None
                width:400
                password: True
            MDCheckbox:
                size_hint: None, None
                font_size: "22sp"
                pos_hint: {'center_x':0.14 , 'center_y':0.4}
                on_active: root.toggle_password_visibility(self,self.active)
            MDLabel:
                id: password_text
                font_size: "15sp"
                text: "Show Password"
                pos_hint: {'center_x':0.7, 'center_y': 0.4}



            MDRaisedButton:
                text: "LOGIN"
                #size_hint: 0.66, 0.65
                pos_hint: {'center_x':0.5,'center_y':0.3}
                background_color: 0,0,0,0
                font_style: "Caption"
                on_release: root.login_user()

            MDTextButton:
                text: "Forgot Password?"
                pos_hint: {'center_x':0.5, "center_y":0.2}
                # color: rgba(68, 78, 132, 255)
                font_size: "18sp"
                font_style: "Caption"
                on_release:
                    root.manager.transition.direction = "left"
                    root.manager.current = "forgot_password"
            # MDLabel:
            #     text: "------------------------- or -------------------------"
            #     #color: rgba(52,0,251,255)
            #     pos_hint: {'center_y':0.22}
            #     font_size: "12sp"
            #     font_style: 'Caption'
            #     halign: 'center'

            

                  

            #MDFloatLayout:
            #    mg_bg_color: rgba(178,178,178,255)
            #    size_hint: 0.033, 0.002
            #    pos_hint: {'center_x': 0.3, 'center_y': 0.218}
            #MDFloatLayout:
            #    text:"----------------"
            #    mg_bg_color: rgba(178,178,178,255)
            #    size_hint: 0.033, 0.002
            #    pos_hint: {'center_x': 0.7, 'center_y': 0.5}

            # MDLabel:
            #     text: "Social Media Login"
            #     font_style: "Caption"
            #     font_size: "13sp"
            #     pos_hint: {'center_y':0.18}
            #     halign: 'center'
            #     color: rgba(135,133,193,255)
            
            
    
                

            MDLabel:
                text:"Don't have any account?"
                font_style: 'Caption'
                font_size: "13sp"
                pos_hint: {'center_x':0.62, 'center_y': 0.07}
                color: rgba(135,133,193,255)

            MDTextButton:
                text:"Sign Up"
                font_style: 'Caption'
                font_size: "13sp"
                pos_hint: {'center_x':0.75, 'center_y': 0.07}
                color: rgba(135,133,193,255)
                on_release:
                    root.manager.transition.direction = "left"
                    root.manager.current= "signup"
"""