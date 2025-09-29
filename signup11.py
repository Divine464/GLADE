
import sqlite3
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@(gmail|yahoo)\.com$"
    return re.match(pattern, email) 

class SignupScreen(MDScreen):
    def signup_user(self):
        username = self.ids.username.text.strip()
        email = self.ids.email.text.strip()
        password = self.ids.password1.text.strip()
        confirm_password = self.ids.confirm_password1.text.strip()

        if password != confirm_password:
            toast("Passwords do not match")
            return
        

        if not username or not email or not password:
            toast("Please fill in all fields")
            return
        
        if not is_valid_email(email):
            toast("Invalid email")
            return

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        

        cursor.execute("SELECT * FROM users WHERE username= ? AND email= ?",(username, email))
        existing_user = cursor.fetchone()

        if existing_user:
            toast("This account already exists")
            conn.close()
            return

        if cursor.execute(
            "SELECT * FROM users WHERE username= ?",
            (username,)
        ).fetchone():
            toast("Username already exists")
            conn.close()
            return

        if cursor.execute(
            "SELECT * FROM users WHERE email= ?",
            (email,)
        ).fetchone():
            toast("Email already exists")
            conn.close()
            return

        cursor.execute("INSERT INTO users (username, email, password) VALUES(?,?,?)", (username, email, password))
        conn.commit()
        conn.close()
        toast("Signup Successful!")

        self.manager.transition.direction = "left"
        self.manager.current = "login"

        self.ids.username.text = ""
        self.ids.password1.text = ""
        self.ids.email.text = ""
        self.ids.confirm_password1.text = ""



    def toggle_password_visibility(self, checkbox, value):
        
        self.ids.password1.password = not value
        self.ids.confirm_password1.password = not value
        self.ids.password_text1.text = "Hide Password" if value else "Show Password"



kv_3 = """
<SignupScreen>:
    name:"signup"
    MDFloatLayout:
        md_bg_color: 0.1,0.1,0.1,1
        MDIconButton:
            icon: "arrow-left"
            pos_hint:{'center_y':0.95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current= "main"

        MDLabel:
            text: 'HI!'
            font_style: "Button"
            font_size: "28sp"
            pos_hint: {'center_X':0.60,'center_y':0.90}
            halign: 'center'
            color: 0.7,0.75,0.8,1

        MDLabel:
            text: 'Create a new account'
            halign: 'center'
            #font_style: "Button"
            font_size: "19sp"
            pos_hint: {'center_x':0.51,'center_y':0.85}
            color: 0.9,0.9,0.9,1

            
        MDFloatLayout:
            MDTextField:
                id: username
                hint_text: "Username"
                icon_right: "account"
                pos_hint: {'center_x': 0.5, 'center_y':0.72}
                size_hint_x: None
                width:400

            MDTextField:
                id: email
                hint_text: "Email"
                # helper_text: "Must be between 8 - 32 characters"
                helper_text_mode: "on_focus"
                icon_right: "mail"
                pos_hint: {'center_x': 0.5, 'center_y':0.62}
                size_hint_x: None
                width:400


            MDTextField:
                id: password1
                hint_text:"Password"
                icon_right: "eye"
                pos_hint: {'center_x': 0.5, 'center_y':0.52}
                size_hint_x: None
                width:400
                password: True
                
            MDTextField:
                id: confirm_password1
                hint_text:"Confirm Password"
                icon_right: "eye"
                pos_hint: {'center_x': 0.5, 'center_y':0.42}
                size_hint_x: None
                width:400
                password: True    
            
            MDCheckbox:
                size_hint: None, None
                font_size: "22sp"
                pos_hint: {'center_x':0.14 , 'center_y':0.34}
                on_active: root.toggle_password_visibility(*args)
                
            MDLabel:
                id: password_text1
                font_size: "15sp"
                text: "Show Password"
                pos_hint: {'center_x':0.7, 'center_y': 0.34}


            MDRaisedButton:
                text: "SIGN UP"
                #size_hint: 0.66, 0.65
                pos_hint: {'center_x':0.5,'center_y':0.21}
                font_style: "Caption"
                on_release: root.signup_user()
                    
            MDLabel:
                text:"Already have an account?"
                font_style: 'Caption'
                font_size: "13sp"
                pos_hint: {'center_x':0.63, 'center_y': 0.07}
                color: rgba(135,133,193,255)

            MDTextButton:
                text:"Sign In"
                font_style: 'Caption'
                font_size: "13sp"
                pos_hint: {'center_x':0.75, 'center_y': 0.07}
                color: rgba(135,133,193,255)
                on_release:
                    root.manager.transition.direction = "left"
                    root.manager.current= "login"
"""