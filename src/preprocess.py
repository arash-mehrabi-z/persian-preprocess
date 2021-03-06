import re
import normalize
import stopword
import string

class PreProcess():
    def __init__(self,text):
        self.text = text

    def get_text(self):
        return self.text

    def normalize_letter(self):
        normal = normalize.Normal()
        for key, value in normal.normal_dict.items():
            self.text = re.sub(value, key, self.text)

    def remove_punctuation(self):
        self.remove_english_punctuation()
        self.remove_persian_punctuation()
        self.remove_semi_space()
        self.remove_diacritic()
        
    def remove_english_punctuation(self):
        self.text = re.sub(r'[!"#$%&\'\(\)*+,-./:;<=>?@\[\\\]\^_`\{\|\}~]', ' ', self.text)

    def remove_persian_punctuation(self):
        self.text = re.sub(r'[-،؛؟«»]', ' ', self.text)

    def remove_semi_space(self):
        self.text = re.sub(r'[‌]', ' ', self.text)

    # Does not substitude diacritics with a space unlike rest punctuations.
    def remove_diacritic(self):
        self.text = re.sub(r'[^\w\s]', '', self.text)


