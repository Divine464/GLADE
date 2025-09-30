

import sqlite3
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast



class ForgotPasswordScreen(MDScreen):
    def reset_password(self):
        username = self.ids.username.text.strip()
        email = self.ids.email.text.strip()
        new_password = self.ids.new_password.text.strip()
        confirm_password = self.ids.confirm_password.text.strip()

        if not username or not email or not new_password or not confirm_password:
            toast("All fields are required")
            return
        
        if new_password != confirm_password:
            toast("Passwords don't match")
            return
        
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username= ? AND email= ?",(username, email))
        result = cursor.fetchone()

        if result:
            cursor.execute("UPDATE users SET password= ? WHERE username= ? AND email= ?",(new_password,username,email))
            conn.commit()
            conn.close()
            toast("Password reset successful")
            self.manager.current = "login"
        else:
            toast("Invalid username or email")
            conn.close()


        self.ids.username.text = ""
        self.ids.new_password.text = ""
        self.ids.email.text = ""
        self.ids.confirm_password.text = ""
    
    def toggle_password_visibility(self, checkbox, value):
        
        self.ids.new_password.password = not value
        self.ids.confirm_password.password = not value
        self.ids.password_text.text = "Hide Password" if value else "Show Password"



kv_6 = """
<ForgotPasswordScreen>:
    name: 'forgot_password'
    MDFloatLayout:
        MDLabel: 
            text: "Reset Password"
            halign: "center"
            font_style: "H5"
            pos_hint: {'center_y':0.9}

        MDTextField:
            id: username
            icon_right: "account"
            hint_text: "Username"
            icon_right: "account"
            pos_hint: {'center_x': 0.5, 'center_y':0.72}
            size_hint_x: 0.8
            
        MDTextField:
            id: email
            icon_right: "mail"
            hint_text: "Email"
            pos_hint: {'center_x': 0.5, 'center_y':0.62}
            size_hint_x: 0.8


        MDTextField:
            id: new_password
            icon_right: "eye"
            hint_text:"New Password"
            pos_hint: {'center_x': 0.5, 'center_y':0.52}
            size_hint_x: 0.8
            password: True
            
        MDTextField:
            id: confirm_password
            icon_right: "eye"
            hint_text:"Confirm New Password"
            pos_hint: {'center_x': 0.5, 'center_y':0.42}
            size_hint_x: 0.8
            password: True    

        MDCheckbox:
            size_hint: None, None
            font_size: "22sp"
            pos_hint: {'center_x':0.14 , 'center_y':0.34}
            on_active: root.toggle_password_visibility(*args)
                
        MDLabel:
            id: password_text
            font_size: "15sp"
            text: "Show Password"
            pos_hint: {'center_x':0.7, 'center_y': 0.34}    

        MDRaisedButton:
            text:"Reset Password"
            pos_hint: {'center_x': 0.5, 'center_y':0.24}
            on_release: root.reset_password()

            
        MDRaisedButton:
            text:"Back to login"
            pos_hint: {'center_x': 0.5, 'center_y':0.14}
            on_release: root.manager.current = "login"
        

"""
