#!/usr/bin/env python

from kivy import require
require('1.3.0')


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
#from kivy.core.clipboard import Clipboard
from triad.demo import makeGenerator

# top level box
layout = BoxLayout(orientation='vertical')

# field for first keyphrase entry
#layout.add_widget(Label(text='First keyphrase'))
key0 = TextInput(text='<first keyphrase>') # possibly add `password=True`
layout.add_widget(key0)

# field for second keyphrase entry
#layout.add_widget(Label(text='Second keyphrase'))
key1  = TextInput(text='<second keyphrase>')
layout.add_widget(key1)

# field for showing the generated password
#layout.add_widget(Label(text='Generated password'))
gen0 = TextInput(text='<generated password>')
layout.add_widget(gen0)

# define the password generator
generator = makeGenerator('pg2009.json')
def generatePassOnText(instance, value):
   gen0.text = generator(key0.text, key1.text)

# bind the password generator to text entry
key0.bind(text=generatePassOnText)
key1.bind(text=generatePassOnText)

'''
TODO: use the system clipboard
button0 = Button(text='Copy to clipboard')
layout.add_widget(button0)

def copy(self):
   gen0.text = ...

button0.bind(on_release=copy)
'''

class GeneratorApp(App):
    def build(self):
        return layout
    #pass

if __name__ == '__main__':
    GeneratorApp().run()

