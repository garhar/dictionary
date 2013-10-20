from dictionary_service import Dictionary


if __name__ == '__main__':
    print "dictionary test..."

    dictionary = Dictionary()
    search_term = u'bånn'
    print "search for: " + search_term

    result = dictionary.find_nor_words(search_term)
    for word in result:
        print 'result nor: ' + word['nor']

    result = dictionary.find_eng_words(search_term)
    for word in result:
        print 'result eng: ' + word['eng']
