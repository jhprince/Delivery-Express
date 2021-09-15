from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.utils import asynckivy
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapView, MapMarker
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem,TwoLineListItem,ThreeLineListItem
from helper import helper_string
from kivy.core.window import Window
import requests

Window.size=(300,500)

class WelcomeScreen( Screen ):
    pass

class MainScreen( Screen ):
    pass

class LoginScreen( Screen ):
    pass


class SignupScreen( Screen ):
    pass

class RegHelpScreen( Screen):
    pass

class ProductInventoryScreen( Screen):
    pass

class Routescreen(Screen):
    pass

class PaymentScreen(Screen):
    pass

class Reportscreen(Screen):
    pass



sm = ScreenManager()
sm.add_widget( WelcomeScreen( name='loginscreen' ) )
sm.add_widget( MainScreen( name='mainscreen' ) )
sm.add_widget( LoginScreen( name='loginscreen' ) )
sm.add_widget( SignupScreen( name='signupscreen' ) )
sm.add_widget( RegHelpScreen( name='reshelpscreen' ) )
sm.add_widget( ProductInventoryScreen(name='productscreen'))
sm.add_widget( Routescreen(name='routescreen'))
sm.add_widget( PaymentScreen(name='payment'))
sm.add_widget( Reportscreen(name='report'))



class DeliveryApp( MDApp ):
    def build(self):
        self.strng = Builder.load_string(helper_string )
        self.url  =  "https://loginsetup-1ddfd-default-rtdb.firebaseio.com/.json"
        return self.strng

    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split())>1:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Username',text = 'Please enter username without space',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail,signupPassword)
            signup_info = str({f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".","-")
            signup_info = signup_info.replace("\'","")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url = self.url,json = to_database)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'
    auth = 'IEoKwhKXqxwsiBINEGPXR9wySMaBpa1deulucnJi'

    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.','-')
        supported_loginPassword = loginPassword.replace('.','-')
        request  = requests.get(self.url+'?auth='+self.auth)
        data = request.json()
        emails= set()
        for key,value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check=True
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        else:
            print("user no longer exists")
    def close_username_dialog(self,obj):
        self.dialog.dismiss()
    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('mainscreen')

    def Help(self):
        print('reghelpscreen')

    def set_heading(self):
        async def set_heading():
             for i in range(5):
                await asynckivy.sleep(1)
                text_heading = self.strng.get_screen('productscreen').id.heading
                text_heading.text = str(i)
             text_heading.text = " 220 "
        asynckivy.start((set_heading()))




    def MapViewExample(FloatLayout):
        super().__init__()
        FloatLayout.MapViewExample()


    def NavigationDrawer(MDBoxLayout, self=None):
        for i in range(20):
            self.root.ids.container.add_widget(
                OneLineListItem(text=f" Item{i}")
            )

    def navigation_draw(self):
        print("Navigation")

DeliveryApp().run()