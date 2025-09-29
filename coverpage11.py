
kv_0= """
MDScreen:
    name: 'cover'
    MDFloatLayout:
        md_bg_color: 0.1,0.1,0.1,1
        Image:
            source: "convert.png"
            pos_hint: {'center_x':0.5, 'center_y':0.65}
            size_hint: 0.9, 0.9
    
    MDLabel:
        text: 'Track more. Spend wise.'
        font_style: "Subtitle1"
        font_size: "17sp"
        pos_hint: {'center_y':0.57}
        halign: 'center'
        color: rgba(15, 221, 182, 255)    

    MDLabel:
        text: 'WELCOME TO GLADE'
        font_style: "Button"
        font_size: "23sp"
        pos_hint: {'center_y':0.38}
        halign: 'center'
        # color: rgba(127,127,127,255)
        

    MDLabel:
        text: 'The best place to keep track of your expenses!'
        #font_style: "Button"
        font_size: "12sp"
        size_hint_x: 0.85
        pos_hint: {'center_x':0.5,'center_y':0.3}
        halign: 'center'

        
    MDRaisedButton:
        text: "CLICK TO PROCEED"
        #size_hint: 0.66, 0.65
        size_hint: 0.82, 0.07
        pos_hint: {'center_x':0.5,'center_y':0.18}
        background_color: 0,0,0,0
        font_style: "Caption"
        on_release:
            root.manager.transition.direction= "left"
            root.manager.current = "prelogin"
"""