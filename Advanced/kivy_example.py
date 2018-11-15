from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs): # add widgets and define behaviour
        super(LoginScreen, self).__init__(**kwargs) # call super to implement the functionality of the original class being overloaded

        # Organise a 2 grid field in two seperate columns with user and pass labels and fields
        self.cols = 2
        self.add_widget(Label(text='Weight In Kilograms'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)



class MyApp(App):

    def build(self):
        return LoginScreen()




if __name__ == '__main__':
    MyApp().run()