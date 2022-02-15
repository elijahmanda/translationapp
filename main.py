from unittest import result
from kivymd.app import MDApp
from kivy.lang import Builder
from googletrans import Translator
from lunguages import LANGUAGES
kv = '''
MDBoxLayout :
    id : box
    orientation : 'vertical'
    padding : dp(20)
    spacing : dp(20)
    MDLabel :
        text : 'Result of translation'
        halign : 'center'
        size_hint_y : None
        height : self.texture_size[1]
        font_size: 50
        color : [0,0,0,1]
    MDLabel :
        id : result
        halign : 'center'
        size_hint_y : None
        height : self.texture_size[1]
        font_size : 30
        color : [0,0,0,1]
    MDLabel :
        id : language
        halign : 'center'
        size_hint_y : None
        height : self.texture_size[1]
        font_size : 30
        color : [0,0,0,1]
    MDTextField :
        hint_hext : 'Enter text you want to translate'
        mode: "rectangle"
        id : field
        size_hint_x : None
        width : box.width - 20

        pos_hint : {'center_x': .5}
    MDRoundFlatButton :
        text : 'Translate'
        pos_hint : {'center_x': .5}
        size_hint_x : None
        width : box.width - 20
        on_release : app.translate_text(field.text)
    Widget:


'''

class TranslatorApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def translate_text(self, text):
        translator = Translator()
        result = translator.translate(text).text
        lang = translator.detect(text)
        self.root.ids.result.text = str(result)
        if lang.lang in list(LANGUAGES.keys()):
            lang_res = LANGUAGES[lang.lang]
            self.root.ids.language.text = str(lang_res)
TranslatorApp().run()