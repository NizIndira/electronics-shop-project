from src.item import Item


class MixinLang:

    def __init__(self):
        self.__language = 'EN'

    def change_lang(self):
        self.__language = {self.__language == 'EN': 'RU',
                           self.__language == 'RU': 'EN'}[True]
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLang):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)
