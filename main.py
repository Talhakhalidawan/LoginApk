from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window
import os

class LoginPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [30, 30, 30, 30]  # Top, Left, Bottom, Right padding
        self.spacing = 0  # Remove spacing between elements

        # Add Image above the form
        self.image = Image(source='logo.png', size_hint=(None, None))

        # Calculate the image size based on screen size and limit the maximum width to 70% of the screen width
        self.image_width = Window.width * 0.7
        self.image_height = self.image_width * 0.5  # Maintaining aspect ratio (height = 50% of width)
        
        # Restrict the image size to be within screen bounds
        if self.image_width > Window.width:
            self.image_width = Window.width * 0.7  # Make sure the image width does not exceed screen width
        if self.image_height > Window.height * 0.4:  # Make sure the image height is less than 40% of screen height
            self.image_height = Window.height * 0.4
        
        self.image.size = (self.image_width, self.image_height)

        # Center the image horizontally
        self.image.pos_hint = {"center_x": 0.5}
        self.add_widget(self.image)

        # Title
        self.title = Label(text='Login', font_size=32, bold=True, size_hint=(1, None), height=50)
        self.add_widget(self.title)

        # Form Layout for the inputs
        self.form_layout = GridLayout(cols=1, size_hint_y=None, height=140, padding=[20, 0], spacing=0)

        # Username Input
        self.username_input = TextInput(hint_text='Username', size_hint_y=None, height=40, multiline=False)
        self.username_input.foreground_color = (0, 0, 0, 1)
        self.form_layout.add_widget(self.username_input)

        # Password Input
        self.password_input = TextInput(hint_text='Password', password=True, size_hint_y=None, height=40, multiline=False)
        self.password_input.foreground_color = (0, 0, 0, 1)
        self.form_layout.add_widget(self.password_input)

        self.add_widget(self.form_layout)

        # Login Button directly under the form (no space between)
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
        Window.size = (Window.width, Window.height)
        icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')
        self.icon = icon_path
        return LoginPage()

if __name__ == '__main__':
    MyApp().run()
