


kv_1= """
MDScreen:
    name: 'main'
    MDFloatLayout:
        md_bg_color: 0.1,0.1,0.1,1

        Image:
            source: "piggyfile.png"
            size_hint: 2.5, 2.5
            pos_hint: {'center_x':0.5, 'center_y':0.65}
            

    MDIconButton:
        icon: "arrow-left"
        pos_hint:{'center_y':0.95}
        user_font_size: "30sp"
        theme_text_color: "Custom"
        #text_color: rgba(26,24,58,255)
        on_release:
            root.manager.transition.direction = "right"
            root.manager.current= "prelogin"
    
    
    MDLabel:
        text: 'H E L L O !'
        font_style: "Button"
        font_size: "23sp"
        pos_hint: {'center_y':0.36}
        halign: 'center'
        color: 0.51,0.55,0.59,1

    MDLabel:
        text: 'LOGIN OR SIGNUP'
        font_size: "13sp"
        size_hint_x: 0.85
        pos_hint: {'center_x':0.5,'center_y':0.29}
        halign: 'center'
        color: rgba(127,127,127,255)

    MDRaisedButton:
        text: "LOGIN"
        size_hint: 0.82, 0.07
        pos_hint: {'center_x':0.5,'center_y':0.18}
        background_color: 0,0,0,0
        font_style: "Caption"
        on_release:
            root.manager.transition.direction= "left"
            root.manager.current = "login"

    MDRaisedButton:
        text: "SIGNUP"
        size_hint: 0.82, 0.07
        #size_hint: 0.9, 0.07
        pos_hint: {'center_x':0.5,'center_y':0.09}
        background_color: 0,0,0,0
        font_style: "Caption"
        on_release:
            root.manager.transition.direction= "left"
            root.manager.current = "signup"
    
"""