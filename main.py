from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import os

# Set the window size (optional, adjust based on your screen resolution)
Window.size = (400, 600)

class LoginPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 10

        self.title = Label(text='Login', font_size=32, bold=True, size_hint=(1, 0.1))
        self.add_widget(self.title)

        self.form_layout = GridLayout(cols=1, size_hint_y=None, height=200, padding=[20, 10])

        self.username_input = TextInput(hint_text='Username', size_hint_y=None, height=40)
        self.username_input.foreground_color = (0, 0, 0, 1)
        self.form_layout.add_widget(self.username_input)

        self.password_input = TextInput(hint_text='Password', password=True, size_hint_y=None, height=40)
        self.password_input.foreground_color = (0, 0, 0, 1)
        self.form_layout.add_widget(self.password_input)

        self.add_widget(self.form_layout)

        self.login_button = Button(text='Login', size_hint_y=None, height=50, background_color=(0.1, 0.6, 0.1, 1))
        self.login_button.bind(on_press=self.on_login)
        self.add_widget(self.login_button)

    def on_login(self, instance):
        if self.username_input.text == 'Talha' and self.password_input.text == 'password':
            self.show_popup('Success', 'You have logged in successfully!')
        else:
            self.show_popup('Error', 'Invalid username or password')

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_label = Label(text=message, size_hint=(1, 0.8))
        close_button = Button(text='Close', size_hint=(1, 0.2))
        content.add_widget(popup_label)
        content.add_widget(close_button)

        popup = Popup(title=title, content=content, size_hint=(None, None), size=(400, 200))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

class MyApp(App):
    def build(self):
        icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')
        self.icon = icon_path
        return LoginPage()

if __name__ == '__main__':
    MyApp().run()