
from kivy.uix.screenmanager import SlideTransition, FadeTransition, SwapTransition, WipeTransition
import sqlite3
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.clock import Clock


class DashboardScreen(MDScreen):

    username = StringProperty("User Name")
    email = StringProperty("user@example.com")
    profile_image = StringProperty("default.png")

    

    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

    def set_user(self, username, email, profile_pic):
        self.username = username
        self.email = email
        self.profile_image = profile_pic if profile_pic else "images.jpeg"

        self.ids.welcome_label.text = f"Welcome, {username}"
        self.ids.drawer_image.source = self.profile_image
        self.ids.drawer_image.reload()

        self.load_user_expenses()
    
    def load_user_expenses(self):
        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE username = ?", (self.username,))
        expenses = cursor.fetchall()
        conn.close()
        self.update_expenses_view(expenses)

    def update_expenses_view(self, expenses):
        self.ids.expense_list.clear_widgets()
        for index, item in enumerate(expenses, start=1):
            pass

    def switch_screen(self):
        self.manager.transition = SlideTransition(direction = "right")
        self.manager.current = "main"

    def add_expense(self):
        income_screen = self.manager.get_screen("income")
        income_screen.set_username(self.username)
        self.manager.current = "income"

    def view_report(self):
        print("Navigating to View Report screen")
        report_screen = self.manager.get_screen("report")
        report_screen.set_username(self.username)
        self.manager.current = "report"

    def on_pre_enter(self):
        self.load_user_expenses()
        

    def view_summary(self):
        summary_screen = self.manager.get_screen("summary")
        summary_screen.set_username(self.username)
        self.manager.current = "summary"

    def view_stats(self):
        stats_screen = self.manager.get_screen('stats')
        stats_screen.set_username(self.username)
        self.manager.current = "stats"

    def logout(self):
        self.dialog = MDDialog(
            text = "Are you sure you want to logout?",
            buttons = [
                MDFlatButton(
                    text = "Cancel",
                    on_release = lambda x: self.dialog.dismiss()
                ),
                MDFlatButton(
                    text = "Logout",
                    on_release = self.confirm_logout
                ),
            ]
        )
        self.dialog.open()

    def confirm_logout(self, instance):
        self.dialog.dismiss()
        self.ids.nav_drawer.set_state("close")
        
        Clock.schedule_once(self._complete_logout, 0.1)
    
    def _complete_logout(self, dt):

        self.manager.transition = SlideTransition(direction = "right")
        self.manager.current = "login"



kv_5= """

<DashboardScreen>:
    name: "dashboard"
    ScrollView:
        size_hint: 1, 0.4
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        GridLayout:
            id: expense_list
            cols: 1
            size_hint_y : None
            height: self.minimum_height
            spacing: dp(10)
            padding: dp(10)

    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                BoxLayout:
                    md_bg_color: 0.12,0.12,0.12,1
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: "Dashboard"
                        elevation: 4
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["",lambda x: None]]
                        padding: [0,0,0,0]
                        left_action_padding: 0

                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: '10dp'
                            spacing: '20dp'
                            adaptive_height: True
                            size_hint_y : None
                            height: self.minimum_height

                            MDLabel:
                                id: welcome_label
                                text: 'Welcome'
                                halign: 'center'
                                font_style: "H5"
                                size_hint_y: None
                                height: self.texture_size[1] + dp(20)

                            Widget:

                            MDRaisedButton:
                                text: "Incomes"
                                md_bg_color: 0,0.7,0.5,1
                                size_hint_x:0.6
                                pos_hint:{'center_x':0.5}
                                on_release: 
                                    app.root.current = "income"

                            MDRaisedButton:
                                text: "Expenses"
                                md_bg_color: 0,0.7,0.5,1
                                pos_hint: {'center_x':0.5}
                                size_hint_x:0.6
                                on_release: 
                                    root.manager.transition.direction= "left"
                                    root.manager.current = "add_expense"

                            MDRaisedButton:
                                text: "Chart"
                                md_bg_color: 0,0.7,0.5,1
                                pos_hint: {'center_x':0.5}
                                size_hint_x:0.6
                                on_release: 
                                    # root.manager.transition.direction= "left"
                                    root.view_stats()

                            MDRaisedButton:
                                text: "View Summary"
                                md_bg_color: 0,0.7,0.5,1
                                size_hint_x:0.6
                                pos_hint: {'center_x':0.5}
                                on_release: root.view_summary()

                            Widget:

        MDNavigationDrawer:
            id: nav_drawer
            width: dp(260)

            BoxLayout:
                orientation: 'vertical'
                padding: "16dp"
                spacing: "12dp"

                MDBoxLayout: 
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: "12dp"

                    FitImage:
                        id: drawer_image
                        source: "images.jpeg"
                        size_hint: None, None
                        size: "200dp", "200dp"
                        pos_hint: {'center_x':0.5}
                        ratio: [100]
                        radius: [dp(100,)]
                        allow_stretch: True
                        keep_ratio: True

                    MDLabel:
                        text: root.username
                        font_style: "H5"
                        halign: "center"
                        bold: True
                        theme_text_color: 'Custom'
                        text_color: 1,1,1,1
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: root.email
                        font_style: "Caption"
                        halign: "center"
                        theme_text_color: 'Custom'
                        text_color: 0.8,0.8,0.8,1
                        size_hint_y: None
                        height: self.texture_size[1]

                    

                ScrollView:
                    MDList:
                        MDSeparator:
                            height: "1dp"
                            padding: '16dp'

                        OneLineIconListItem:
                            text: "Profile"
                            on_release: 
                                root.manager.current = "profile"
                                root.manager.get_screen("profile").set_user(root.username)
                            IconLeftWidget:
                                icon: "account-circle"

                        OneLineIconListItem:
                            text: "Logout"
                            on_release: root.logout()
                            IconLeftWidget:
                                icon: "logout"

                        MDSeparator:
                            height: '1dp'
                            padding:'16dp'
        

"""