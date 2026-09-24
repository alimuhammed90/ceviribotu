# Görev #3
from translate import Translator

import requests
from collections import defaultdict

# Görev #5

class TextAnalysis():   
    
    # Görev #1
    memory = defaultdict(list)


    

    

    def __init__(self, text, owner):

        

        # Görev #2
        TextAnalysis.memory[owner].append(self)



        

        self.text = text
        self.translation = self.__translate(self.text, "tr", "en")

        # Görev #6
        self.response = self.get_answer()

    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "tr")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            # Görev #4
            translator = Translator(from_lang="tr", to_lang="en")
            ceviri = translator.translate(text)
            return ceviri
        except:
            return "Çeviri girişimi başarısız oldu"
