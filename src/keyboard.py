from src.item import Item


class MixinLang:

    def __init__(self):
        self.language = 'EN'

    def change_lang(self):
        self.language = {self.language == 'EN': 'RU',
                         self.language == 'RU': 'EN'}[True]
        return self



class Keyboard(Item, MixinLang):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)