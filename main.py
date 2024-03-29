from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class DarkPython(App):
    def build(self):

        self.window = GridLayout()
        self.window.cols = 1

        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        
        self.window.add_widget(Image(source="hakclogo_300x180.png"))

        self.greeting = Label(
            text="What is your name?",
            font_size = 20,
            color="#ff0000",
            bold=True
            )
        self.window.add_widget(self.greeting)
        self.user = TextInput(
            multiline=False,
            padding_y = (20, 20),
            size_hint = (1, 0.5),
            font_size = 15,
            halign="center"
            )
        

        self.window.add_widget(self.user)
        self.button = Button(
            text="ENTER",
            size_hint = (1, 0.5),
            bold=True,
            background_color="ff0000"
            )
        

        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window


    def callback(self, instance):
        self.greeting.text = "Hello " + self.user.text + "!"

if __name__ == "__main__":
    DarkPython().run()