from dictionary import Dictionary

if __name__ == '__main__':

    dictionary = Dictionary()

    ################################################################
    ##### WORDS
    ################################################################

    # Exact

    # Search for "exact" word nor
    # search_term = u'forsvar'
    # print "search for exact norwegian word: " + search_term
    # result = dictionary.find_words(dictionary.CONST_SEARCH_EXACT, search_term, 'nor')

    # Search for "exact" ord eng
    # search_term = u'winter'
    # print "search for exact english word: " + search_term
    # result = dictionary.find_words(dictionary.CONST_SEARCH_EXACT, search_term, 'eng')

    # Starts with

    # Search for words that "starts with" nor
    # search_term = u'forsv'
    # print "search for norwegian words that starts with: " + search_term
    # result = dictionary.find_words(dictionary.CONST_SEARCH_STARTS_WITH, search_term, 'nor')

    # Search for words that "stats with" eng
    # search_term = u'wint'
    # print "search for norwegian words that starts with: " + search_term
    # result = dictionary.find_words(dictionary.CONST_SEARCH_STARTS_WITH, search_term, 'eng')

    # Contains

    # Search for words that "contains" nor
    # search_term = u'forsk'
    # print "search for norwegian words that starts with: " + search_term
    # result = dictionary.find_words(dictionary.CONST_SEARCH_CONTAINS, search_term, 'nor')

    # Search for words that "contains" eng
    # search_term = u'nter'
    # print "search for norwegian words that starts with: " + search_term
    # result = dictionary.find_words(dictionary.CONST_SEARCH_CONTAINS, search_term, 'eng')

    ################################################################
    ##### ABBREVIATIONS
    ################################################################

    # Exact

    # Search for "exact" abbrievations nor
    # search_term = u'strat'
    # print "search for: " + search_term
    # result = dictionary.find_abbriviations(dictionary.CONST_SEARCH_EXACT, search_term, 'nor_usages')

    # Search for "exact" abbrievations eng
    # search_term = u'etterf'
    # print "search for: " + search_term
    # result = dictionary.find_abbriviations(dictionary.CONST_SEARCH_EXACT, search_term, 'abbr')

    # Starts with

    # Search for "starts with" abbrievations nor
    # search_term = u'strat'
    # print "search for: " + search_term
    # result = dictionary.find_abbriviations(dictionary.CONST_SEARCH_STARTS_WITH, search_term, 'nor_usages')

    # Search for "starts with" abbrievations eng
    # search_term = u'etter'
    # search_term = u'UM'
    # print "search for: " + search_term
    # result = dictionary.find_abbriviations(dictionary.CONST_SEARCH_STARTS_WITH, search_term, 'abbr')

    # Contains

    # Search for "starts with" abbrievations nor
    # search_term = u'trat'
    # print "search for: " + search_term
    # result = dictionary.find_abbriviations(dictionary.CONST_SEARCH_CONTAINS, search_term, 'nor_usages')

    # Search for "starts with" abbrievations eng
    # search_term = u'tterf'
    search_term = u'QMS'
    print "search for: " + search_term
    result = dictionary.find_abbriviations(dictionary.CONST_SEARCH_CONTAINS, search_term)



    ###############################################################

    i = 0
    for word in result:
        print "-----"
        print 'result: ' + result[i].nor + ", " + result[i].eng
        print "nor usage"
        for usage in result[i].nor_usages:
            print("Finding usage for: " + usage['abbr'])

        print "eng abbr"
        for usage in result[i].abbr:
            print("Finding abbr for: " + usage['abbr'])



        # for abbr in result[i].abbr:
        #     print abbr
        # print "-----"
        # for abbr in result[i].abbr:
        #     print result[i].abbr[abbr]

        # for key, value in result[i].nor_usages_test.items():
        #     print "key: " + key + ", value: " + value

        i += 1
    print "-----"
    print "Found " + str(i) + " terms"