from modeltranslation.translator import translator, TranslationOptions
from .models import *


class MainPageTranslationOptions(TranslationOptions):
    fields = (
        'text',
    )


translator.register(MainPage, MainPageTranslationOptions)

