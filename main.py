from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Username'))
        layout.add_widget(TextInput(multiline=False))
        layout.add_widget(Label(text='Password'))
        layout.add_widget(TextInput(password=True, multiline=False))
        layout.add_widget(Button(text='Login', on_press=self.login))
        self.add_widget(layout)

    def login(self, instance):
        self.manager.current = 'upload'

class UploadMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.filechooser = FileChooserIconView(filters=["*.csv", "*.xlsx"])
        layout.add_widget(self.filechooser)
        layout.add_widget(Button(text='Upload', on_press=self.upload))
        self.add_widget(layout)

    def upload(self, instance):
        selected = self.filechooser.selection
        if selected:
            print(f"Selected file: {selected[0]}")
            self.manager.current = 'allergy'

class AllergyFilterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Enter Allergen (e.g. nuts, dairy):'))
        self.allergy_input = TextInput(multiline=False)
        layout.add_widget(self.allergy_input)
        layout.add_widget(Button(text='Show Safe Foods', on_press=self.filter))
        self.result_label = Label(text='')
        layout.add_widget(self.result_label)
        self.add_widget(layout)

    def filter(self, instance):
        allergen = self.allergy_input.text.lower()
        # Replace this with real filtering logic
        self.result_label.text = f"Filtered foods without: {allergen}"

class AllergyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(UploadMenuScreen(name='upload'))
        sm.add_widget(AllergyFilterScreen(name='allergy'))
        return sm

if __name__ == '__main__':
    AllergyApp().run()
