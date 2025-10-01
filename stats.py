
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout 
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
import sqlite3



if not hasattr(FigureCanvasKivyAgg, "resize_event"):
    FigureCanvasKivyAgg.resize_event = lambda self, *args, **kwargs : None

if not hasattr(FigureCanvasKivyAgg, "motion_notify_event"):
    FigureCanvasKivyAgg.motion_notify_event = lambda self, *args, **kwargs : None

if not hasattr(FigureCanvasKivyAgg, "button_press_event"):
    FigureCanvasKivyAgg.button_press_event = lambda self, *args, **kwargs : None

if not hasattr(FigureCanvasKivyAgg, "button_release_event"):
    FigureCanvasKivyAgg.button_release_event = lambda self, *args, **kwargs : None

if not hasattr(FigureCanvasKivyAgg, "scroll_event"):
    FigureCanvasKivyAgg.scroll_event = lambda self, *args, **kwargs : None

if not hasattr(FigureCanvasKivyAgg, "key_press_event"):
    FigureCanvasKivyAgg.key_press_event = lambda self, *args, **kwargs : None

if not hasattr(FigureCanvasKivyAgg, "key_release_event"):
    FigureCanvasKivyAgg.key_release_event = lambda self, *args, **kwargs : None

class StatsScreen(MDScreen):
    def set_username(self,username):
        self.username = username
        print("Stats username:", self.username)
        self.load_pie_chart()

    def load_pie_chart(self):
        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()
        cursor.execute("""SELECT LOWER (category), SUM(amount) FROM expenses WHERE username = ?
                    GROUP BY LOWER (category)""",(self.username,))
        data = cursor.fetchall()
        conn.close()
        
        print("Fetched data: ", data)

        if data:
            categories, amounts = zip(*data)
            print("Categories:", categories)
            print("Amounts:", amounts)
            self.display_chart(categories, amounts)
        else:
            self.ids.chart_container.add_widget(MDLabel(
                text = "No chart data found",
                halign = "center"
            ))
            return

    def display_chart(self, categories, amounts):
        self.ids.chart_container.clear_widgets()

        color_mode = "neon"
        neon_colors = ["#00E5FF", "#FF4081", "#69F0AE", "#FFD740", "#FF6E40", "#7C4DFF"]
        pastel_colors = ["#F48FB1", "#81D4FA", "#AED581", "#FFD54F", "#CE93D8","#4DB6AC"]

        if color_mode == "neon":
            palette = neon_colors
        else:
            palette = pastel_colors

        colors = [palette[i % len(palette)] for i in range(len(categories))]

        explode = [0.05] * len(categories)

        fig, ax = plt.subplots(figsize = (8,8))

        fig.patch.set_facecolor("#121212")
        ax.set_facecolor("#121212")
        
        wedges, texts, autotexts = ax.pie(amounts, 
                                          labels = categories, 
                                          autopct= '%1.1f%%', 
                                          startangle= 90, 
                                          shadow= True, 
                                          explode=explode, 
                                          colors=colors, 
                                          textprops={"fontsize": 12, "color":"white"}
                                        )
        for t in texts:
            t.set_text(t.get_text().upper())
            t.set_color("white")
            t.set_fontsize(10)
            t.set_fontweight("bold")
        for at in autotexts:
            at.set_fontsize(9)
            at.set_color("white")
            at.set_fontweight("bold")

        if len(categories) <= 3:
            ncols = len(categories)
        else:
            ncols = 2

        ax.legend(
            wedges,
            [f"{cat.upper()} - {amt}" for cat, amt in zip(categories, amounts)],
            title = "Categories",
            loc = "upper center",
            bbox_to_anchor = (0.5, -0.15),
            ncol = ncols,
            fontsize = 10,
            labelcolor = "white",
            facecolor = "#121212"
        )
        plt.subplots_adjust(bottom=0.3)

        box = BoxLayout()
        chart = FigureCanvasKivyAgg(fig)
        box.add_widget(chart)
        self.ids.chart_container.add_widget(box)

    def on_leave(self):
        container = self.ids.chart_container
        for child in container.children[:]:
            if isinstance(child, FigureCanvasKivyAgg):
                child.figure.clf()

                child.canvas.ask_update()
                child.canvas = None
                container.remove_widget(child)
        container.clear_widgets()
        plt.close('all')

    def go_back(self):
        self.ids.chart_container.clear_widgets()
        self.manager.current = "dashboard"


kv_stat = """
<StatsScreen>:
    name: "stats"
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Expense Chart"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            right_action_items: [["",lambda x: None]]
            padding: [0,0,0,0]
            left_action_padding: 0

        BoxLayout:
            id: chart_container
            orientation: 'vertical'
            size_hint_y: 1

"""
