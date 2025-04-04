import flet as ft


quotes = {
    "original": "imagine hurting this guys dawg - john wick.",
    "Abkhazian": "ухаҿы иааг абри аҷкәынцәа ргәаҟра доуг - џьон уик",
    "Icelandic": "ímyndaðu þér að meiða þennan gaur dawg - john wick"
}

languages = "original", "Abkhazian", "french"
translate = languages

def main(page: ft.Page):
    page.title = "Quotes and translator"
    page.width = 300
    page.height = 300
    quote = ft.Text(value=quotes["original"], size=18)
    
    def Translator (e):
     quote.value = (languages.values)

ft.app(target = main)

radio_buttons = ft.Row

ft.Row = ([

ft.Radio(value="original", label="original", on_change=translate),
ft.Radio(value="Abkhazian", label="Abkhazian", on_change=translate),
ft.Radio(value="Icelandic", label="Icelandic", on_change=translate)
])
ft.app(target = main)
