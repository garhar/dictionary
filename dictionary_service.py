import json
from dictionary import Dictionary


class DictionaryService:

    filedict = {}
    dictionary = None

    def __init__(self):
        json_text_file = 'data/dictionary.json'
        with open(json_text_file) as json_file:
            # dictionary_dict = json.load(json_file)
            # self.dictionary = Dictionary(dictionary_dict)
            filedict = json.load(json_file)
            dict2 = dict2obj(dict)
            print "Dict: " + dict2[1].nor


    def find_nor_words(self, search_term):
        if not self.dictionary:
            return None
        result = Dictionary()
        for word in self.dictionary:
            if self.dictionary[word]['nor'].startswith(search_term):
                # result.append(self.dictionary[word])
                # print self.dictionary[word]['nor']
                print self.dictionary[word].nor
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


def dict2obj(d):
    if isinstance(d, list):
        d = [dict2obj(x) for x in d]
    if not isinstance(d, dict):
        return d
    class C(object):
        pass
    o = C()
    for k in d:
        o.__dict__[k] = dict2obj(d[k])
    return o