
# from google import genai
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IconRightWidget, OneLineRightIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from incomedb import insert_income, fetch_all_incomes, update_income, delete_income
from summarydb import get_summary_data 
from datetime import datetime
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout            
from kivy.metrics import dp



class IncomeScreen(MDScreen):

    selected_income_id = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        super().__init__(**kwargs)
        self.incomes = {}

    def set_username(self,username):
        self.username = username

    def save_income(self):
        amount = self.ids.income_amount.text
        date = self.ids.income_date.text
        
        try:
            amount = float(amount)
        except ValueError:
            toast("Please enter a valid number")
            return
        
        try:
            datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            toast("Enter a valid date")
            return


        if self.selected_income_id:
            update_income(self.selected_income_id, amount, date)
            toast("Income updated")
            self.selected_income_id = None
        else:
            insert_income(self.username,amount,date)
            toast(f"Income saved successfully")

        self.ids.income_amount.text = ""
        self.ids.income_date.text = ""

    def load_income_for_edit(self, income_id):
        username = MDApp.get_running_app().current_user
        incomes = fetch_all_incomes(username)

        for inc in incomes:
            if inc[0] == income_id:
                self.selected_income_id = income_id
                self.ids.income_amount.text = str(inc[1])
                self.ids.income_date.text = str(inc[3])
                break
    
    def go_to_income_records(self):
        income_screen = self.manager.get_screen("income_records")
        income_screen.set_username(self.username)
        print("Username sent to IncomeRecordsScreen:", self.username)
        self.manager.current = "income_records"


class IncomeRecordsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = None
        self.dialog = None
        # self.confirm_dialog = None

    def set_username(self, username):
        self.username = username
        self.load_income_records()

    def load_income_records(self):
        username = MDApp.get_running_app().current_user
        self.ids.records_box.clear_widgets()
        incomes = fetch_all_incomes(username)

        if not incomes:
            self.ids.records_box.add_widget(MDLabel(
                text = "No income records found.",
                halign = "center"
            ))
            return
        
        for income in incomes:
            income_id, amount, username, date = income
            item = OneLineRightIconListItem(
                text= f"\u20A6{amount}  ({date})",
                on_release = lambda x, d = date, a = amount, u = username:
                self.show_income_details(d,a,u)
            )

            edit_icon = IconRightWidget(
                icon = "pencil",
                on_release = lambda x, eid = income_id: self.load_income_for_edit(eid)
            )
            
            edit_icon.padding = [0,0, dp(13), 0]

            
            delete_icon = IconRightWidget(
                icon = "delete",
                theme_text_color= "Custom",
                text_color=(1,0,0,1),
                on_release = lambda x, eid = income_id: self.confirm_delete(eid)
            )

            delete_icon.padding = [0,0, dp(23), 0]


            item.add_widget(edit_icon)
            item.add_widget(delete_icon)
            self.ids.records_box.add_widget(item)

    def load_income_for_edit(self, income_id):
        app = MDApp.get_running_app()
        add_screen = app.root.get_screen("income")
        add_screen.load_income_for_edit(income_id)
        app.root.current = "income"


    def confirm_delete(self, income_id):
        # if not self.dialog:
        dialog = MDDialog(
            title = "Confirm Deletion",
            text = f"Are you sure you want to delete this income record?",
            buttons = [
                MDFlatButton(text = "CANCEL",
                on_release = lambda x: dialog.dismiss()
                ),
                MDFlatButton(
                    text = "DELETE",
                    on_release = lambda x, eid = income_id: self.delete_income_by_date(eid, dialog)
                ),
            ],
        )
        dialog.open()

    def delete_income_by_date(self,income_id, dialog):
        print(f"Deleting income with ID :{income_id}")
        delete_income(income_id)
        dialog.dismiss()
        self.load_income_records()
        toast("Income deleted successfully")


    def show_income_details(self, date, amount, username):
        if self.dialog:
            self.dialog.dismiss()

        content = (
        f" Date: {username}\n"
        f"\n"
        f" Amount: \u20A6{date}"
        )
        
        self.dialog = MDDialog(
            title = "Income details",
            text = content,
            buttons = [
                MDFlatButton(
                    text = "Close",
                    on_release = lambda x: self.dialog.dismiss()
                )
            ]
        )
        self.dialog.open()

    def go_back(self):
        self.manager.current = "income"


class SummaryScreen(MDScreen):
    username = StringProperty()

    def set_username(self,username):
        self.username = username

    def on_enter(self):
        self.load_summary_data()

    def load_summary_data(self):
        data = get_summary_data(self.username)
        
        self.ids.total_income_label.text = f"Total Income : \u20A6{data["total_income"]}"
        self.ids.total_expenses_label.text = f"Total Expenses : \u20A6{data["total_expenses"]}"
        self.ids.balance_label.text = f"Balance : \u20A6{data["balance"]}"
        self.ids.last_income_label.text = f"Last Income : \u20A6{data["last_income"][0]} on {data["last_income"][1]}"
        self.ids.last_expense_label.text = f"Last Expense : \u20A6{data["last_expense"][0]} on {data["last_expense"][1]}"



kv_in = """
<IncomeScreen>:
    name: "income"
    MDFloatLayout:
        md_bg_color: 0.12,0.12,0.12,1

        MDLabel:
            text: "Add Monthly Income"
            halign: "center"
            pos_hint: {'center_x':0.5, 'center_y':0.9}
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: 1,1,1,1

        MDTextField:
            id: income_amount
            hint_text: "Enter income amount"
            mode: 'rectangle'
            size_hint_x: 0.8
            pos_hint: {'center_x':0.5, 'center_y':0.69}

        MDTextField:
            id: income_date
            hint_text: "Enter date (DD-MM-YYYY)"
            mode: 'rectangle'
            size_hint_x: 0.8
            pos_hint: {'center_x':0.5, 'center_y':0.56}
        
        MDRaisedButton:
            text: "Save Income"
            md_bg_color: 0,0.7,0.5,1
            pos_hint:{'center_x':0.26, 'center_y':0.42}
            on_release: 
                root.save_income()

        MDRaisedButton:
            text: "View Records"
            md_bg_color: 0,0.7,0.5,1
            pos_hint:{'center_x':0.73, 'center_y':0.42}
            on_release: 
                root.go_to_income_records()


        MDRaisedButton:
            text: "Back"
            md_bg_color: 0.2,0.6,0.8,1
            pos_hint:{'center_x':0.48, 'center_y':0.22}
            on_release: 
                app.root.current = "dashboard"        

"""

kv_rec = """
<IncomeRecordsScreen>:
    name: "income_records"
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Income Records"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            right_action_items: [["",lambda x: None]]
            padding: [0,0,0,0]
            left_action_padding: 0

        ScrollView:
            MDList:
                id: records_box

"""


kv_summ = """
<SummaryScreen>:
    name: "summary"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(10)

        MDLabel:
            text: "Summary"
            halign: "center"
            font_style:"H4"

        MDLabel:
            id: total_income_label
            text: "Total Income: \u20A60"
            font_style: "H5"

        MDLabel:
            id: total_expenses_label
            text: "Total Expenses: \u20A60"
            font_style: "H5"
        
        MDLabel:
            id: balance_label
            text: "Balance: \u20A60"
            font_style: "H4"
            theme_text_color: "Custom"
            text_color: 0,0.7,0,1

        MDLabel:
            id: last_income_label
            text: "Last Income: None"
            font_style: "Body1"

        MDLabel:
            id: last_expense_label
            text: "Last Expense: None"
            font_style: "Body1"

        MDRaisedButton:
            text: "Back to Dashboard"
            pos_hint: {'center_x':0.5}
            on_release: 
                root.manager.current = "dashboard"      
"""