

from kivy.properties import StringProperty
from databasemd11 import init_db
from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from coverpage11 import kv_0
from openpage11 import kv_1
from loginpage11 import kv_2, LoginScreen
from signup11 import kv_3, SignupScreen
from dashboardmd import DashboardScreen, kv_5
from forgotmd import ForgotPasswordScreen, kv_6
from expensedatabmd import init_expense_db
from expensedm import AddExpenseScreen, kv_12
from viewexpensesmd import ViewExpensesScreen, kv_0v
from logingfte import PreLoginScreen, kv_lo
from income import IncomeScreen, kv_in, IncomeRecordsScreen, kv_rec, SummaryScreen, kv_summ
from incomedb import create_income_table
from stats import StatsScreen, kv_stat
from profilemd import ProfileScreen, kv_profile


Window.size = (326,580)

class Glade(MDApp):
    current_user = None
    selected_expense_id = None
    profile_pic = StringProperty("images.jpeg")
    def build(self):
        init_db()
        init_expense_db()
        create_income_table()
        screen_manager = ScreenManager()
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        screen_manager.add_widget(Builder.load_string(kv_0))
        screen_manager.add_widget(Builder.load_string(kv_1))
        Builder.load_string(kv_2)
        Builder.load_string(kv_3)
        Builder.load_string(kv_5)
        Builder.load_string(kv_6)
        Builder.load_string(kv_12)
        Builder.load_string(kv_lo)
        Builder.load_string(kv_0v)
        Builder.load_string(kv_in)
        Builder.load_string(kv_rec)
        Builder.load_string(kv_summ)
        Builder.load_string(kv_stat)
        Builder.load_string(kv_profile)


        screen_manager.add_widget(LoginScreen(name="login"))
        screen_manager.add_widget(SignupScreen(name= "signup"))
        screen_manager.add_widget(DashboardScreen(name= "dashboard"))
        screen_manager.add_widget(ForgotPasswordScreen(name= "forgot_password"))
        screen_manager.add_widget(PreLoginScreen(name= "prelogin"))
        screen_manager.add_widget(AddExpenseScreen(name= "add_expense"))
        screen_manager.add_widget(ViewExpensesScreen(name= "view_expenses"))
        screen_manager.add_widget(IncomeScreen(name= "income"))
        screen_manager.add_widget(IncomeRecordsScreen(name= "income_records"))
        screen_manager.add_widget(SummaryScreen(name= "summary"))
        screen_manager.add_widget(StatsScreen(name= "stats"))
        screen_manager.add_widget(ProfileScreen(name= "profile"))

        return screen_manager


if __name__ == "__main__":
    Glade().run()
