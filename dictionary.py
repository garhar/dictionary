import json
from operator import itemgetter


class Dictionary():
    dictionary = None

    def __init__(self):

        json_dictionary_file = 'data/dictionary.json'
        with open(json_dictionary_file) as json_file:
            self.dictionary = json.load(json_file)

    def find_word_excact(self, search_term, language='nor'):
        if not self.dictionary:
            return None
        result = []
        i = 0
        for word in self.dictionary.keys():
            if self.dictionary[word][language] == search_term:
                wordClass = Word(self.dictionary[word])
                result.append(wordClass)
            i += 1
        result = sorted(result, key=lambda k: (
        k[language].lower(), k[self.oposite(language)].lower()))
        return result

    def find_word_startswith(self, search_term, language='nor'):
        if not self.dictionary:
            return None
        result = []
        i = 0
        for word in self.dictionary.keys():
            if self.dictionary[word][language].startswith(search_term):
                result.append(Word(self.dictionary[word]))
            i += 1
        result = sorted(result, key=lambda k: (
        k[language].lower(), k[self.oposite(language)].lower()))
        return result

    def find_word_contains(self, search_term, language='nor'):
        if not self.dictionary:
            return None
        result = []
        i = 0
        for word in self.dictionary.keys():
            if self.dictionary[word][language].find(search_term) != -1:
                result.append(Word(self.dictionary[word]))
            i += 1
        result = sorted(result, key=lambda k: (
        k[language].lower(), k[self.oposite(language)].lower()))
        return result

    def oposite(self, language):
        if language == 'nor':
            return 'eng'
        else:
            return 'nor'


class Word(dict):
    nor_abr_expl = []

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            return Word()

    def __setitem__(self, key, value):
        if key and (value or isinstance(value, bool)):
            super(Word, self).__setitem__(key, value)

    def __getitem__(self, key):
        if key in self:
            return super(Word, self).__getitem__(key)
        return None

    def __setattr__(self, name, value):
        if name and (value or isinstance(value, bool)):
            self[name] = value

    def __delattr__(self, name):
        if name:
            del self[name]