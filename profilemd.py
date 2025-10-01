
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
import sqlite3
from kivymd.uix.button import MDFlatButton
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.toast import toast



class ProfileScreen(MDScreen):
    username = StringProperty("")
    email = StringProperty("")
    profile_pic = StringProperty("images.jpeg")

    def set_user(self, username, email = None, profile_pic = None):
        self.username = username

        if email is not None and profile_pic is not None:
            self.email = email
            self.profile_pic = profile_pic
        else:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("SELECT email, profile_pic FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()
            conn.close()

            if result:
                email_value = result[0] if result[0] else ""
                profile_pic_value = result[1] if result[1] else "images.jpeg"
            
                self.email = email_value
                self.profile_pic = profile_pic_value

                
            else:
                self.email = ""
                self.profile_pic = "images.jpeg"

        if "profile_image" in self.ids:
            self.ids.profile_image.source = self.profile_pic
            self.ids.profile_image.reload()

        

    def upload_picture(self):
        content = BoxLayout(orientation = "vertical")
        filechooser = FileChooserListView(filters= ["*.png", "*.jpg", "*.jpeg"])
        content.add_widget(filechooser)

        btn_select = Button(text = "Select", size_hint_y = None, height = 40)
        content.add_widget(btn_select) 

        popup = Popup(title = "Select Profile Picture", 
                      content = content, 
                      size_hint = (0.9, 0.9))

        def select_image(instance):
            selection = filechooser.selection
            if selection:
                selected_image = selection[0]
                print("Selected image path:", selected_image)

                self.profile_pic = selected_image

                if "profile_image" in self.ids:
                    self.ids.profile_image.source = selected_image
                    self.ids.profile_image.reload()

                
                conn = sqlite3.connect("users.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET profile_pic = ? WHERE username = ?", (selected_image, self.username))
                conn.commit()
                conn.close()

                try:
                    app = MDApp.get_running_app()
                    dashboard = app.root.get_screen('dashboard')
                    drawer_image = dashboard.ids.drawer_image
                    drawer_image.source = selected_image
                    drawer_image.reload()
                    print("Profile picture updated:", selected_image)

                except Exception as e:
                    print("Drawer image update failed:", e)
            

                popup.dismiss()

        btn_select.bind(on_release = select_image)
        popup.open()



    def delete_account(self):
        self.dialog = MDDialog(
            text = "Are you sure you want to delete your account? This action cannot be undone.",
            buttons = [
                MDFlatButton(
                    text = "CANCEL",
                    on_release = lambda x : self.dialog.dismiss()
                ),
                MDFlatButton(
                    text = "DELETE",
                    on_release = self.confirm_delete
                )
            ],
        )
        self.dialog.open()

    def confirm_delete(self, *args):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE username = ?", (self.username,))
        conn.commit()
        conn.close()

        self.username = ""
        self.email = ""
        self.profile_pic = ""

        self.dialog.dismiss()
        self.manager.current = "login"

    def go_back(self):
        self.manager.current = "dashboard"

    
    def delete_profile_picture(self):
        self.dialog = MDDialog(
            text = "Are you sure you want to reset your profile picture to default",
            buttons = [
                MDFlatButton(
                    text = "CANCEL",
                    on_release = lambda x: self.dialog.dismiss()
                ),
                MDFlatButton(
                    text = "RESET",
                    on_release= self.confirm_delete_profile_picture
                )
            ],
        )
        self.dialog.open()

    def confirm_delete_profile_picture(self, *args):
        self.profile_pic = "images.jpeg"
        
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET profile_pic = ? WHERE username = ?", (self.profile_pic, self.username))
        conn.commit()
        conn.close()

        if "profile_image" in self.ids:
            self.ids.profile_image.source = self.profile_pic
            self.ids.profile_image.reload()

        try:
            app = MDApp.get_running_app()
            dashboard = app.root.get_screen("dashboard")
            drawer_image = dashboard.ids.drawer_image
            drawer_image.source = self.profile_pic
            drawer_image.reload()

            print("Profile picture reset to default")

        except Exception as e:
            print("Drawer image reset failed:", e)

        toast("Profile picture reset to default")
        self.dialog.dismiss()

kv_profile = """
<ProfileScreen>:
    name: "profile"
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        MDTopAppBar:
            title: "Profile"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            right_action_items: [["",lambda x: None]]
            padding: [0,0,0,0]
            left_action_padding: 0
            elevation: 10

        FitImage:
            id: profile_image
            source: app.profile_pic
            size_hint: None, None
            size: dp(150), dp(150)
            pos_hint: {'center_x':0.5}
            radius: [dp(75,)]

        MDRaisedButton:
            text: "Upload Picture"
            pos_hint: {'center_x':0.5}
            on_release: root.upload_picture()

        MDRaisedButton:
            text: "Delete Profile Picture"
            pos_hint: {'center_x':0.5}
            on_release: root.delete_profile_picture()

        MDLabel:
            text: f"Username: {root.username}"
            font_style: "H6"
            halign: "center"

        MDLabel:
            text: f"Email : {root.email}"
            font_style: "Subtitle1"
            halign: "center"
        
        Widget:

        MDRaisedButton:
            text: "Delete Account"
            mg_bg_color: app.theme_cls.error_color
            pos_hint: {"center_x":0.5}
            on_release: root.delete_account()
"""
