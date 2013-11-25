from dictionary import Dictionary

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
