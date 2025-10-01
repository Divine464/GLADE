

from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import TwoLineAvatarIconListItem, IconRightWidget
from expensedatabmd import get_all_expenses, delete_expense
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.metrics import dp



class ViewExpensesScreen(MDScreen):
    dialog = None
    def on_pre_enter(self):
        self.load_view_expenses()

    def load_view_expenses(self):
        username = MDApp.get_running_app().current_user
        self.ids.expense_list.clear_widgets()
        expenses = get_all_expenses(username)

        if not expenses:
            self.ids.expense_list.add_widget(MDLabel(
                text = "No expense record recorded",
                halign = "center"
            ))
            return

        for expense in expenses:
            expense_id, amount, description, category , date, username = expense
            item = TwoLineAvatarIconListItem(
                text = f"{description.capitalize()} - \u20A6{amount}",
                secondary_text = f"{category.capitalize()} on {date}",
                on_release = lambda x, eid = expense: self.show_expense_details(description, amount, date, category)
                                   )
            
            edit_icon = IconRightWidget(
                icon = "pencil",
                on_release = lambda x, eid = expense_id: self.load_expense_for_edit(eid)
            )
            edit_icon.padding = [0,0, dp(13), 0]


            delete_icon = IconRightWidget(
                icon = "delete",
                theme_text_color= "Custom",
                text_color=(1,0,0,1),
                on_release = lambda x, eid = expense_id: self.delete_expense(eid)
            )
            delete_icon.padding = [0,0, dp(23), 0]


            item.add_widget(edit_icon)
            item.add_widget(delete_icon)
            self.ids.expense_list.add_widget(item)

    def show_expense_details(self, description, amount, date, category):
        if self.dialog:
            self.dialog.dismiss()

        content = (
        f" Description: {description}\n"
        f"\n"
        f" Amount: {amount}\n"
        f"\n"
        f" Category: {category}\n"
        f"\n"
        f" Date: {date}\n"
        
        )
        
        self.dialog = MDDialog(
            title = "Expense details",
            text = content,
            buttons = [
                MDFlatButton(
                    text = "Close",
                    on_release = lambda x: self.dialog.dismiss()
                )
            ]
        )
        self.dialog.open()

    def load_expense_for_edit(self, expense_id):
        app = MDApp.get_running_app()
        add_screen = app.root.get_screen("add_expense")
        add_screen.load_expense_for_edit(expense_id)
        app.root.current = "add_expense"

    def delete_expense(self,expense_id):
        def confirm_delete(*args):
            delete_expense(expense_id)
            toast("Expense deleted")
            self.load_view_expenses()    
            self.dialog.dismiss()
        self.dialog = MDDialog(
            title = "Confirm Delete",
            text = "Are you sure you want to delete this expense record?",
            buttons = [
                MDFlatButton(
                    text = "CANCEL",
                    on_release = lambda x: self.dialog.dismiss()
                ),
                MDFlatButton(
                    text = "DELETE",
                    on_release = confirm_delete
                )
            ]
        )
        self.dialog.open()
        
    def go_back(self):
        self.manager.current = "add_expense"


kv_0v = """
<ViewExpensesScreen>:
    name: "view_expenses"
    BoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Expense Records"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            right_action_items: [["",lambda x: None]]
            padding: [0,0,0,0]
            left_action_padding: 0

        ScrollView: 
            MDList:
                id: expense_list

"""
