
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("ALTER TABLE users ADD COLUMN profile_pic TEXT")
conn.commit()
conn.close()

print("Column added")


class IncomeRecordsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = None
        self.dialog = None

    def set_username(self, username):
        self.username = username
        self.load_income_records()

    def load_income_records(self):
        username = MDApp.get_running_app().current_user
        self.ids.records_box.clear_widgets()
        incomes = fetch_all_incomes(username)

        if not incomes:
            self.ids.records_box.add_widget(MDLabel(
                text="No income records found.",
                halign="center"
            ))
            return

        for income in incomes:
            income_id, amount, username, date = income   # ✅ correct order

            item = OneLineRightIconListItem(
                text=f"₦{amount} on {date} ({username})",
                on_release=lambda x, d=date, a=amount, u=username: self.show_income_details(d, a, u)
            )

            edit_icon = IconRightWidget(
                icon="pencil",
                on_release=lambda x, eid=income_id: self.load_income_for_edit(eid)
            )
            edit_icon.padding = [0, 0, dp(13), 0]

            delete_icon = IconRightWidget(
                icon="delete",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                on_release=lambda x, eid=income_id: self.confirm_delete(eid)
            )
            delete_icon.padding = [0, 0, dp(23), 0]

            item.add_widget(edit_icon)
            item.add_widget(delete_icon)
            self.ids.records_box.add_widget(item)

    def load_income_for_edit(self, income_id):
        app = MDApp.get_running_app()
        add_screen = app.root.get_screen("income")
        add_screen.load_income_for_edit(income_id)
        app.root.current = "income"

    def confirm_delete(self, income_id):
        dialog = MDDialog(
            title="Confirm Deletion",
            text="Are you sure you want to delete this income record?",
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda x: dialog.dismiss()
                ),
                MDFlatButton(
                    text="DELETE",
                    on_release=lambda x, eid=income_id: self.delete_income_by_date(eid, dialog)
                ),
            ],
        )
        dialog.open()

    def delete_income_by_date(self, income_id, dialog):
        print(f"Deleting income with ID: {income_id}")
        delete_income(income_id)
        dialog.dismiss()
        self.load_income_records()
        toast("Income deleted successfully")

    def show_income_details(self, date, amount, username):
        if self.dialog:
            self.dialog.dismiss()

        content = (
            f" Date: {date}\n"
            f" Amount: ₦{amount}\n"
            f" User: {username}"
        )

        self.dialog = MDDialog(
            title="Income details",
            text=content,
            buttons=[
                MDFlatButton(
                    text="Close",
                    on_release=lambda x: self.dialog.dismiss()
                )
            ]
        )
        self.dialog.open()

    def go_back(self):
        self.manager.current = "income"
