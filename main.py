import os

from kivy.app import App
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

from convert import NfoConverter


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    scrollview = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    cancel = ObjectProperty(None)


class RootWidget(BoxLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    scrollview = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0]), encoding='cp437') as stream:
            text = stream.read()
            image = NfoConverter.text_to_image(text)
            sv = ScrollView(
                size=self.ids.boxlayout1.size
            )
            image.save(open('nfo.png', 'wb'), 'png')

            image_width = self.ids.boxlayout1.size[0]
            image_height = (image_width/image.width)*image.height

            print('image_width',image_width,'image_height',image_height)
            image_widget = Image(
                source='nfo.png',
                size=(image_width, image_height),
                size_hint=(None, None),
                keep_ratio=True
            )
            sv.add_widget(image_widget)
            self.ids.boxlayout1.add_widget(sv)

        self.dismiss_popup()

    def save(self):
        self.dismiss_popup()


class NFOEditorApp(App):

    def build(self):
        return RootWidget()



Factory.register('Root', cls=RootWidget)
# Factory.register('LoadDialog', cls=LoadDialog)
# Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    NFOEditorApp().run()
