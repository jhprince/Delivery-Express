helper_string = """
ScreenManager:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    SignupScreen:
    RegHelpScreen:
    ProductInventoryScreen:
    Routescreen:
    PaymentScreen:
    Reportscreen:
    
<WelcomeScreen>:
    name:'welcomescreen'
    MDLabel:
        text:'Welcome'
        font_style:'H5'
        halign:'center'
        pos_hint: {'center_y':0.85}
    MDLabel:
        text:'to'
        font_style:'H4'
        halign:'center'
        pos_hint: {'center_y':0.75}
    MDLabel:
        text:'Delivery express'
        font_style:'H5'
        halign:'center'
        pos_hint: {'center_y':0.65}
    MDRaisedButton:
        text:'Login'
        pos_hint : {'center_x':0.5,'center_y':0.5}
        size_hint: (0.30,0.07)
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Signup'
        pos_hint : {'center_x':0.5,'center_y':0.4}
        size_hint: (0.30,0.07)
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'left'
            
    MDRaisedButton:
        text: 'Help'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        size_hint: (0.13,0.07)
        on_press:
            root.manager.current = 'reghelpscreen'
            root.manager.transition.direction = 'left'
                  
            
<LoginScreen>:
    name:'loginscreen'
    MDLabel:
        text:'Signin'
        theme_text_color: 'Error'
        font_style:'H3'
        halign:'center'
        pos_hint: {'center_y':0.95}
    MDTextField:
        id:login_email
        pos_hint: {'center_y':0.7,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Login'
        size_hint: (0.30,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press:
            app.login()
            app.username_changer()
    MDTextButton:
        text: 'Create an account'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'
    MDRaisedButton:
        text:'Back'
        size_hint: (0.20,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.09}
        on_press:
            root.manager.current = 'welcomescreen'
            root.manager.transition.direction = 'up'
                    
<SignupScreen>:
    name:'signupscreen'
    MDLabel:
        text:'Signup'
        theme_text_color: 'Error'
        font_style:'H4'
        halign:'center'
        pos_hint: {'center_y':0.95}
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.55,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'email'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.65,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.85,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'First Name'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle" 
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Last Name'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"       
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.45,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'eye-off'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.35,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Re-Enter Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'eye-off'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"     
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.20,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()
    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'   
            
<RegHelpScreen>
    name: 'reghelpscreen'
    MDLabel:
        text:'Registration Help'
        pos_hint: {'center_x':0.7, 'center_y':0.95,}
        font_style:'H5'
        theme_text_color: 'Error'
        
    MDLabel:
        text:' Hello everyone, in this lesson, we will see how to keep the user logged in android apps. We have seen in almost every app that the user logs in for the first time and the next time he opens the app, he goes straight inside the app without authentication. Let’s try doing it in a simple way.'
        pos_hint: {'center_x':0.5, 'center_y':0.75,}
        font_style:'Caption'
            
        
    MDRaisedButton:
        text:'Back'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_press:
            root.manager.current = 'welcomescreen'
            root.manager.transition.direction = 'up'                       

<MainScreen>:
    name: 'mainscreen' 
    ScrollView:
        MDList:
            id: ls
            OneLineListItem:
                text: 'Update prize list'
            ThreeLineListItem:
                text: 'Coca-Cola'
                secondary_text: '2 liter x 6 Pieces 606tk'
                tertiary_text: 'Discount price 590tk'   
            ThreeLineListItem:
                text: '7Up'
                secondary_text: '2 Liter x 6 Pieces 600tk'
                tertiary_text: 'Discount price 590tk'
            ThreeLineListItem:
                text: '7Up'
                secondary_text: '2 Liter x 6 Pieces 600tk'
                tertiary_text: 'Discount price 590tk'
            ThreeLineListItem:
                text: 'Mojo'
                secondary_text: '2 Liter x 6 Pieces 360tk'
                tertiary_text: 'Discount price 350tk'
            ThreeLineListItem:
                text: 'Pepsi'
                secondary_text: '2 Liter x 6 Pieces 480tk'
                tertiary_text: 'Discount price 470tk'
            ThreeLineListItem:
                text: 'Mountain Dew'
                secondary_text: '250ml x 24 Pieces 360tk'
                tertiary_text: 'Discount price 350tk'
            ThreeLineListItem:
                text: 'Sprite'
                secondary_text: '2 Liter x 6 Pieces 600tk'
                tertiary_text: 'Discount price 590tk'
            ThreeLineListItem:
                text: 'Fanta'
                secondary_text: '1.25 Liter x 6 Pieces 390tk'
                tertiary_text: 'Discount price 3600tk'
            ThreeLineListItem:
                text: 'Clemon'
                secondary_text: '2 Liter x 6 Pieces 360tk'
                tertiary_text: 'Discount price 350tk'                                
                                                            
    BoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            title: 'Product Type'
            md_bg_color: [1,0,0,1]
            left_action_items: [["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
            right_action_items: [["map",lambda x: nav_drawer.toggle_nav_drawer()]]
            elevation: 10
            
        Widget: 
          
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            spacing: '4dp'
            padding: '4dp'
             
            Image:
                source: 'teeh.jpeg'
             
            MDLabel:
                text: 'SR'
                font_style:'Subtitle1'
                size_hint_y: None
                height: self.texture_size[1] 
                 
            ScrollView:
                MDList:
                    OneLineListItem:
                        text: 'Product Inventory'
                        on_press:
                            root.manager.current = 'productscreen'
                    OneLineListItem:
                        text: 'Route'
                        on_press:
                            root.manager.current = 'routescreen' 
                    OneLineListItem:
                        text: 'Payment' 
                        on_press:
                            root.manager.current = 'paymentscreen'
                    OneLineListItem:
                        text: 'Report' 
                        on_press:
                            root.manager.current = 'reportscreen'
                    OneLineListItem:
                        text: 'Logout'   
                        on_press:
                            root.manager.current = 'welcomescreen'                 
            
             
       
<ProductInventoryScreen>:
    name: 'productscreen'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            title: 'Product Inventory'
            md_bg_color: [1,0,0,1]
            right_action_items: [["printer-search",lambda x: nav_drawer.toggle_nav_drawer()]]
            elevation: 10
            
        Widget: 
        
    MDLabel:
        text: 'Product Sell :'
        font_style: "Subtitle1"
        pos_hint: {'center_x':0.5,'center_y':0.7}
        theme_text_color: 'Error'
    MDLabel:
        text: ' 120 '
        font_style: "H6"
        pos_hint: {'center_x':0.9,'center_y':0.7}
        
    MDLabel:
        text: 'Product Stock :'
        font_style: "Subtitle1"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        theme_text_color: 'Error'
    MDLabel:
        text: ' 540 '
        font_style: "H6"
        pos_hint: {'center_x':0.9,'center_y':0.5}       
        
    MDRaisedButton:
        text:'Back'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_press:
            root.manager.current = 'mainscreen'
            root.manager.transition.direction = 'up'      
<RouteScreen>:
    name: 'routescreen'
    MapView:
        lat:23.735192501978037
        lon:90.6042637753306
        zoom: 10
        on_lat:
            print('lat', self.lat)
        on_lon:
            print:('lon', self.lon) 
                   
    BoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            title: 'Location'
            md_bg_color: app.theme_cls.accent_color
            right_action_items: [["map",lambda x: nav_drawer.toggle_nav_drawer()]]
            elevation: 10
            
        Widget: 
                      
    MDRaisedButton:
        text:'Back'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_press:
            root.manager.current = 'mainscreen'
            root.manager.transition.direction = 'up'     
<PaymentScreen>:
    name: 'paymentscreen'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            title: 'Payment'
            md_bg_color: app.theme_cls.accent_color
            elevation: 10
            
        Widget: 
    Image:
        source: "bkash.jpg"
        pos_hint: {'center_x': 0.5, 'center_y':0.7}
    MDLabel:
        text: "Phone Num : 01xxx-xxxxxx"
        pos_hint: {'center_x': 0.7, 'center_y':0.5}
    MDLabel:
        text: "Or"
        pos_hint: {'center_x': 0.9, 'center_y':0.4}
        font_style: 'H4'
        text_color: 0,0,1,1               
    MDLabel:
        text: 'Cash On Delivery'
        pos_hint: {'center_x': 0.7, 'center_y':0.3}
        font_style: 'H6'    
        
    MDRaisedButton:
        text:'Back'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_press:
            root.manager.current = 'mainscreen'
            root.manager.transition.direction = 'up'    
         
<ReportScreen>:
    name: 'reportscreen'
    MDTextField:
        pos_hint: {'center_y':0.65,'center_x':0.5}
        size_hint : (0.7,0.2)
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle" 
    MDRaisedButton:
        text:'SUBMIT'
        size_hint: (0.20,0.07)
        pos_hint: {'center_x':0.40,'center_y':0.6}     
               
    BoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            title: 'Product Report'
            md_bg_color: [1,0,0,1]
            right_action_items: [["book",lambda x: nav_drawer.toggle_nav_drawer()]]
            elevation: 10
            
        Widget: 
        
    MDRaisedButton:
        text:'Back'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.05}
        on_press:
            root.manager.current = 'mainscreen'
            root.manager.transition.direction = 'up'                                                                      
"""