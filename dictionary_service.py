import json


class Dictionary:

    dictionary = {}

    def __init__(self):
        json_text_file = 'data/ordliste_nytt_format3.csv'
        with open(json_text_file) as json_file:
            self.dictionary = json.load(json_file)

    def find_nor_words(self, search_term):
        if not self.dictionary:
            return None
        result = []
        for word in self.dictionary:
            if self.dictionary[word]['nor'].startswith(search_term):
                result.append(self.dictionary[word])
                #print self.dictionary[word]['nor']
        return result

    def find_eng_words(self, search_term):
        if not self.dictionary:
            return None
        result = []
        for word in self.dictionary:
            if self.dictionary[word]['eng'].startswith(search_term):
                result.append(self.dictionary[word])
                #print self.dictionary[word]['eng']
        return result

