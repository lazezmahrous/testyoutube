from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty, NumericProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.snackbar import BaseSnackbar
import random
from kivy.config import Config
from kivymd.color_definitions import colors
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
import json


class HomeScreen(Screen):
    def click(self):
        app = App.get_running_app()
        app.root.current = "About"
    

class AboutScreen(Screen):
    pass


class ContactScreen(Screen):
    pass


class App(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(ContactScreen(name='contact'))
        kv = Builder.load_file('kivy.kv')
        return kv


if __name__ == '__main__':
    App().run()
