from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build the Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Output text"""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clean_all(self):
        """Clear Text"""
        print("clear")
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()
