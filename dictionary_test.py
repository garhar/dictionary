#coding=iso-8859-1
# from dictionary_service import DictionaryService


# if __name__ == '__main__':
#     print "dictionary test..."
#
#     dictionary_service = DictionaryService()
#     search_term = u'påta'
#     print "search for: " + search_term
#
#     result = dictionary_service.find_nor_words(search_term)
#     for word in result:
#         print 'result nor: ' + word['nor']
#
#     result = dictionary_service.find_eng_words(search_term)
#     for word in result:
#         print 'result eng: ' + word['eng']

from dictionary import Dictionary
import logging

if __name__ == '__main__':
    print "dictionary test..."

    dictionary = Dictionary()
    # search_term = u'mil'
    search_term = u'forsvar'
    print "search for: " + search_term

    result = dictionary.find_word_startswith(search_term, 'nor')
    i = 0
    for word in result:
        print 'result: ' + result[i].nor + ", " + result[i].eng
        for abr in result[i].nor_abr:
            print("Finding abr for: " + abr['abbr'])

        print "-----"
        # for abr in result[i].eng_abr:
        #     print abr
        # print "-----"
        # for abr in result[i].eng_abr:
        #     print result[i].eng_abr[abr]

        for key, value in result[i].nor_abr_test.items():
            print "key: " + key + ", value: " + value

        i += 1

    # result = dictionary_service.find_eng_words(search_term)
    # for word in result:
    #     print 'result eng: ' + word['eng']