
from kivymd.app import MDApp
from datetime import datetime
from expensedatabmd import insert_expense, get_all_expenses, update_expense
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast


class AddExpenseScreen(MDScreen):
    selected_expense_id = None


    def save_expense(self):
        amount= self.ids.amount.text.strip()
        description= self.ids.description.text.strip()
        category= self.ids.category.text.strip()
        date= self.ids.date.text.strip()

        username = MDApp.get_running_app().current_user

        if not amount  or not description or not category or not date:
            toast("Please fill in all fields")
            return

        try:
            date_obj = datetime.strptime(date, "%d-%m-%Y")
            date = date_obj.strftime("%d-%m-%Y")
        except ValueError:
            toast("Invalid data format")
            return        

        try:
            float(amount)
        except ValueError:
            toast("Amount must be a number")
            return
        
        if self.selected_expense_id:
            update_expense(self.selected_expense_id, amount, description, category, date)
            toast("Expense updated")
            self.selected_expense_id = None
        else:
            insert_expense(amount, description, category, date, username)
            toast("Expense saved")

        self.clear_inputs()

    def load_expense_for_edit(self, expense_id):
        username = MDApp.get_running_app().current_user
        expenses = get_all_expenses(username)

        for exp in expenses:
            if exp[0] == expense_id:
                self.selected_expense_id = expense_id
                self.ids.amount.text = str(exp[1])
                self.ids.description.text = str(exp[2])
                self.ids.category.text = str(exp[3])
                self.ids.date.text = str(exp[4])
                break

        

    def clear_inputs(self):
        self.ids.description.text = ""
        self.ids.amount.text = ""
        self.ids.category.text = ""
        self.ids.date.text = ""



    def go_to_view(self):
        self.manager.current = "view_expenses"
        
    



        


kv_12 = """

<AddExpenseScreen>:
    name: "add_expense"
    MDFloatLayout:
        MDLabel:
            text: "Add New Expense"
            halign: 'center'
            font_style: "H5"
            pos_hint: {'center_x':0.5, 'center_y':0.9}
        
        MDTextField:
            id: amount
            hint_text: "Amount"
            input_filter: 'float'
            pos_hint: {'center_x':0.5,'center_y':0.65}
            size_hint_x: 0.8

        MDTextField:
            id: description
            hint_text: "Description"
            pos_hint: {'center_x':0.5,'center_y':0.75}
            size_hint_x: 0.8

        MDTextField:
            id: category
            hint_text: "Category (e.g. Food, Transport)"
            pos_hint: {'center_x':0.5,'center_y':0.55}
            size_hint_x: 0.8

        MDTextField:
            id: date
            hint_text: "Date(DD-MM-YYYY)"
            pos_hint: {'center_x':0.5,'center_y':0.45}
            size_hint_x: 0.8
            
        MDRaisedButton:
            text: "Save Expenses" 
            md_bg_color: 0,0.7,0.5,1
            pos_hint: {'center_x':0.26,'center_y':0.35}
            on_release: 
                root.save_expense()

        MDRaisedButton:
            text: "View Expenses"
            md_bg_color: 0,0.7,0.5,1
            pos_hint: {'center_x':0.73, 'center_y':0.35}
            on_release: 
                root.manager.current = "view_expenses"

        MDIconButton:
            icon: "arrow-left"
            pos_hint:{'center_x':0.1,'center_y':0.97}
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current= "dashboard"

        

"""
