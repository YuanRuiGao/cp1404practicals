from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


NEW_COLOUR = (1, 5, 7, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic Labels creation."""
    status_text = StringProperty()

    def __init__(self):
        super().__init__()
        self.names = ["YuanRui_Gao", "Mike", "Gery", "Grace", "John", "jemmy", "Mirko"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """create label from names(list)"""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.color = (1, 0.75, 0.8, 1)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()