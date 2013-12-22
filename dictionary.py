import settings
import json
import logging

logger = logging.getLogger('dictionary')


class Dictionary():

    CONST_SEARCH_EXACT = "EXACT"
    CONST_SEARCH_STARTS_WITH = "STARTS_WITH"
    CONST_SEARCH_CONTAINS = "CONTAINS"

    dictionary = None

    def __init__(self):
        if settings.is_production():
            json_dictionary_file = 'C:/Dev/projects/dictionaryProd/data/dictionary.json'
        else:
            json_dictionary_file = 'C:/Dev/projects/dictionaryDev/data/dictionary.json'
        logger.info("Dictionary initialized with: " + json_dictionary_file)
        with open(json_dictionary_file) as json_file:
            self.dictionary = json.load(json_file)

    # Find words
    def find_words(self, search_type=CONST_SEARCH_EXACT, search_term='', language='nor'):
        if not self.dictionary:
            logger.error("Dictionary not initialized...")
            return None
        result = []
        # Loop all words in dictionary
        counter = 0
        for dict_word in self.dictionary.keys():
            word = None
            if search_type == self.CONST_SEARCH_EXACT:
                if self.dictionary[dict_word][language].upper() == search_term.upper():
                    word = Word(self.dictionary[dict_word])
            if search_type == self.CONST_SEARCH_STARTS_WITH:
                if self.dictionary[dict_word][language].upper().startswith(search_term.upper()):
                    word = Word(self.dictionary[dict_word])
            if search_type == self.CONST_SEARCH_CONTAINS:
                if self.dictionary[dict_word][language].upper().find(search_term.upper()) != -1:
                    word = Word(self.dictionary[dict_word])
            if word:
                counter += +1
                result.append(word)
            if counter >= 200:
                break
        return self.sort_words(result)

    # Find abbriviations
    def find_abbriviations(self, search_type=CONST_SEARCH_EXACT, search_term=''):
        if not self.dictionary:
            logger.error("Dictionary not initialized...")
            return None
        result = []
        # Loop all words in dictionary
        counter = 0
        for dict_word in self.dictionary.keys():
            word = None
            # Loop all abbr for every dict_word
            for abbr in self.dictionary[dict_word]['abbr']:
                # abbr_ext = self.dictionary[dict_word]['abbr']
                if search_type == self.CONST_SEARCH_EXACT:
                    if abbr['abbr'].upper() == search_term.upper():
                        word = Word(self.dictionary[dict_word])
                if search_type == self.CONST_SEARCH_STARTS_WITH:
                    if abbr['abbr'].upper().startswith(search_term.upper()):
                        word = Word(self.dictionary[dict_word])
                if search_type == self.CONST_SEARCH_CONTAINS:
                    if abbr['abbr'].upper().find(search_term.upper()) != -1:
                        word = Word(self.dictionary[dict_word])
                if word:
                    counter += +1
                    result.append(word)
            if counter >= 200:
                break
        return self.sort_words(result)

    def sort_words(self, words, language='nor'):
        result = sorted(words, key=lambda k: (
            k[language].lower(), k[self.oposite(language)].lower()))
        return result

    # def sort_abbriviations(self, words, language='nor'):
    #     result = sorted(words, key=lambda k: (
    #         k[language].lower(), k[self.oposite(language)].lower()))
    #     return result

    def oposite(self, language):
        if language == 'nor':
            return 'eng'
        else:
            return 'nor'


class Word(dict):

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