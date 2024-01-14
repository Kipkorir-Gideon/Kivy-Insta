from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder

from libs.screens.home_page import HomePage


class InstaApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        self.load_all_kivy_files()
        return HomePage()
    
    def load_all_kivy_files(self):
        Builder.load_file('libs/screens/home_page.kv')
        Builder.load_file('libs/components/appbar.kv')
        Builder.load_file('libs/components/story_creator.kv')
        Builder.load_file('libs/components/bottom_nav.kv')
        Builder.load_file('libs/components/circular_avatar_image.kv')
        
    def on_start(self):
        self.root.dispatch('on_enter')
    
    
    
if __name__ == '__main__':
    InstaApp().run()