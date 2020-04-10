import os
from kivy.uix.boxlayout import BoxLayout
 
# from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
 
from kivymd.list import OneLineAvatarListItem, IRightBody
from kivy.uix.screenmanager import Screen
from kivymd.label import MDLabel
from kivymd.navigationdrawer import (
    MDNavigationDrawer,
    NavigationDrawerHeaderBase
)
from kivymd.theming import ThemeManager

class NavigationItem(OneLineAvatarListItem):
    icon = StringProperty()
 
class CommonHead(Screen):
    pass


class Navigatorss(MDNavigationDrawer):
    """Navigator class (image, title and logo)"""
    image_source = StringProperty('images/qidenticon_two.png')
    title = StringProperty('Navigation')
    drawer_logo = StringProperty()


class ContentNavigationDrawer(Navigatorss):
    """Navigate Content Drawer"""
    pass


class Test1(Screen):

    def __init__(self, **kwargs):
        """Set screen of address detail page"""
        print('call first.......................')
        super(Test1, self).__init__(**kwargs)

    def on_enter(self):
        # import pdb;pdb.set_trace()
        if self.ids:
            from kivymd.textfield import MDTextField

            field = MDTextField()
            field.hint_text = "required = True"
            field.required = True
            field.helper_text_mode = "on_error"
            self.ids.box.add_widget(field)
 
class Test2(Screen):
    pass
 
class Test3(Screen):
    pass
 
class TestNavigationDrawer(App):

    theme_cls = ThemeManager()
    def build(self):
        self.nav_drawer = Navigatorss()
        return Builder.load_file(
            os.path.join(os.path.dirname(__file__), 'main.kv'))

    def reset_field_required(self, scr_mngr, box):
        # import pdb;pdb.set_trace()
        if scr_mngr.current != "test1":
            box.clear_widgets()
 
TestNavigationDrawer().run()