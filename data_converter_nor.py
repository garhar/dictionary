from models import WordExplanation
import csv
import codecs
import json
import tempfile


def load_dictionary_explanations():
    dictionary_explanations = {}
    dict_file = 'data/ordliste-forklaringer.csv'
    with open(dict_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        counter = 0
        for row in reader:
            if counter == 100:
                print "100"
            if row:
                word_explanation = WordExplanation(unicode(row[1], "iso-8859-1"), unicode(row[2], "iso-8859-1"))
                dictionary_explanations[unicode(row[0], "iso-8859-1")] = word_explanation
            counter += 1
    return dictionary_explanations


# Orginal fil fra Excel som har blitt stavekontrollert
# Norwegian wordlist
def load_dictionary(dict_expl):
    dictionary = {}
    dict_file = 'data/nor-ordliste2.csv'
    counter = 0
    with open(dict_file) as csvfile:
        reader = csv.reader(csvfile, delimiter='@')
        for row in reader:
            counter += 1
            field1 = unicode(row[0].replace('"', ''), "iso-8859-1")
            field2 = unicode(row[1].replace('"', ''), "iso-8859-1")
            field3 = unicode(row[2].replace('"', ''), "iso-8859-1")
            field4 = unicode(row[3].replace('"', ''), "iso-8859-1")

            # print "Rad1: " + field1
            # print "Rad2: " + field2
            # print "Rad3: " + field3
            # print "Rad4: " + field4

            # Field 1: Norwegian word.

            # Field 2: Fisrt, one or more abbreviations, then explanation of norwegian word.
            # Definition of a abbreviations is that it is present in abbreviations file.

            # Field 3: English word, two spaces, pronunciation in format: UDTL /xxxxx/,
            # two spaces, one or more english abbreviations seperated with ";"

            if field1.startswith('nestkommanderende'):
                print "nestkommanderende"



            # Row 1
            nor_word = ""
            nor_word_expl = ""
            nor_word_abr = []
            if field1:
                field1split = field1.split(" / ")
                if len(field1split) > 0 and field1split[0]:
                    nor_word = field1split[0]
                if len(field1split) > 1 and field1split[1]:
                    temp_nor_word_exp = field1split[1]
                    field1split2 = temp_nor_word_exp.split("  ")
                    nor_word_exp_split_char = ""
                    for word2 in field1split2:
                        if word2 and word_in_dictionary_explanations(dict_expl, word2.strip()):
                            nor_word_abr.append(word2.strip())
                        elif word2:
                            nor_word_expl = nor_word_expl + nor_word_exp_split_char + word2.strip()
                            nor_word_exp_split_char = " "


            # Row 2
            eng_word = ""
            if field2:
                eng_word = field2.strip()

            # Row 3 always empty

            eng_word_abr = {}
            eng_word_pronon = ""
            if field4:
                field4split = field4.split(" ; ")
                for word4 in field4split:

                    # If word4.contains("obso"):
                    #

                    if word4.find("obso") == -1:
                        containsObso = False
                    else:
                        containsObso = True

                    if word4.find("(NO)") != -1:
                        eng_word_abr['NO'] = {"abr": word4.replace("(NO)", "").replace("obso", "").strip(), 'obso': containsObso}
                    elif word4.find("(US)") != -1:
                        eng_word_abr['US'] = {"abr": word4.replace("(US)", "").replace("obso", "").strip(), 'obso': containsObso}
                    elif word4.find("(UK)") != -1:
                        eng_word_abr['UK'] = {"abr": word4.replace("(UK)", "").replace("obso", "").strip(), 'obso': containsObso}
                    else:
                        eng_word_abr['NATO'] = {"abr": word4.replace("(NATO)", "").replace("obso", "").strip(), 'obso': containsObso}

            word = {
                'nor': nor_word,
                'nor_expl': nor_word_expl,
                'nor_abr': nor_word_abr,
                'eng': eng_word,
                'eng_abr': eng_word_abr,
                'eng_pronon': '<not impl.>'
            }

            dictionary['word-'+str(counter)] = word
    return dictionary


def word_in_dictionary_explanations(dict_expl, word):
    for dx in dictionary_explanations:
        if word == dx:
            return True
    return False


def print_dictionary_explanations(dict_expl):
    for expl in dict_expl:
        print expl + ";" + dict_expl[expl].nor + ";" + dict_expl[expl].eng


# def print_dictionary(dictionary):
#     for word in dictionary:
#         print dictionary[word].nor_word + "(" + dictionary[word].nor_word_expl + ") -> " + dictionary[word].eng_word
#         for nor_word_abr in dictionary[word].nor_word_abr:
#             print "- " + nor_word_abr
#         print "-----"
#         # if counter > 100:
#         #     break
#     print "The dictionary contains " + str(len(dictionary)) + " words."


def write_dictionary(dictionary):
    dict_file_name = 'data/ordliste_nytt_format.csv'
    with codecs.open(dict_file_name, 'w', "utf-8") as f:
        f.write('Nor word' + '@' + 'Nor word expl' + '@'
                + 'Nor word abr' + '@' + 'Eng word' + '@'
                + 'Eng word pronun' + '@' + 'Eng word abr' + '\n')
        for word in dictionary:
            f.write(dictionary[word].nor_word + '@' + dictionary[word].nor_word_expl + '@'
                    + dictionary[word].nor_word_abr + '@' + dictionary[word].eng_word + '@'
                    + dictionary[word].eng_word_pronun + '@' + dictionary[word].eng_word_abr + '\n')
        print "Dictionary written to file: " + dict_file_name

if __name__ == '__main__':

    print "Loading dictionary explanations"
    dictionary_explanations = load_dictionary_explanations()
    print "Loaded " + str(len(dictionary_explanations)) + " from dictionary explanations file."

    print "Loading dictionary"
    dictionary = load_dictionary(dictionary_explanations)
    print "Loaded " + str(len(dictionary)) + " from dictionary file."

    # print_dictionary_explanations(dictionary_explanations)
    # print_dictionary(dictionary)

    # json_string = json.dump(dictionary)

    dict_file_name = 'data/ordliste_nytt_format3.csv'
    # f = tempfile.NamedTemporaryFile(mode='w+')

    with codecs.open(dict_file_name, 'w+', "iso-8859-1") as f:
        json.dump(dict(dictionary), f, sort_keys=True, encoding="iso-8859-1")
        f.flush()


    # dict_file_name = 'data/ordliste_nytt_format2.csv'
    # with codecs.open(dict_file_name, 'w', "utf-8") as f:
    #     f.write(json_string)
    # write_dictionary(dictionary)