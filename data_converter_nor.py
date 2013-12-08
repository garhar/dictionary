import csv
import codecs
import json


def load_dictionary_explanations():
    dictionary_explanations = {}
    dict_file = 'data/nor-ordliste-forklaringer.csv'
    with open(dict_file) as csvfile:
        reader = csv.reader(csvfile, delimiter='@')
        for row in reader:
            if row:
                explanation = {
                    'nor': unicode(row[1], "iso-8859-1"),
                    'eng': unicode(row[2], "iso-8859-1")
                }
                dictionary_explanations[
                    unicode(row[0], "iso-8859-1")] = explanation
    return dictionary_explanations


def print_dictionary_explanations(dict_expl):
    for expl in dict_expl.keys():
        print expl + ";" + dict_expl[expl]['nor'] + ";" + dict_expl[expl][
            'eng']


def export_dict_expl_json(dict_expl):
    export_dict_expl_json = 'data/dict_expl.json'
    with codecs.open(export_dict_expl_json, 'w+',
                     "UTF-8") as dict_expl_json_file:
        json.dump(dict_expl, dict_expl_json_file, ensure_ascii=False,
                  sort_keys=True, encoding="UTF-8")
        dict_expl_json_file.flush()


# Orginal fil fra Excel som har blitt stavekontrollert
# Norwegian wordlist
def load_dictionary(dict_expl):
    dictionary = {}
    dict_file = 'data/nor-ordliste.csv'
    counter = 0
    with open(dict_file) as csvfile:
        reader = csv.reader(csvfile, delimiter='@')
        for row in reader:
            counter += 1
            field1 = unicode(row[0].replace('"', ''), "iso-8859-1")
            field2 = unicode(row[1].replace('"', ''), "iso-8859-1")
            field3 = unicode(row[2].replace('"', ''), "iso-8859-1")
            field4 = unicode(row[3].replace('"', ''), "iso-8859-1")

            # Row 1
            nor = ""
            nor_expl = ""
            nor_usages = []
            nor_usages_dict = {}
            if field1:
                field1split = field1.split(" / ")
                if len(field1split) > 0 and field1split[0]:
                    nor = field1split[0]
                if len(field1split) > 1 and field1split[1]:
                    temp_nor_word_exp = field1split[1]
                    field1split2 = temp_nor_word_exp.split("  ")
                    nor_word_exp_split_char = ""
                    for word2 in field1split2:
                        nor_usages_dict = {}
                        if word2 and is_word_in_dictionary_expl(dict_expl,
                                                                     word2.strip()):
                            nor_usages_dict['abbr'] = word2.strip()
                            nor_usages_dict['abbr_expl'] = get_word_in_dictionary_expl(dict_expl, word2.strip())
                            nor_usages.append(nor_usages_dict)
                        elif word2:
                            nor_expl = nor_expl + nor_word_exp_split_char + word2.strip()
                            nor_word_exp_split_char = " "


            # Row 2
            eng = ""
            if field2:
                eng = field2.strip()

            # Row 3 always empty

            # Row 4
            abbr_dict = {}
            abbr = []
            if field4:
                field4split = field4.split(" ; ")
                for word4 in field4split:

                    if word4.find("obso") == -1:
                        abbr_dict['obso'] = ''
                    else:
                        abbr_dict['obso'] = 'obsolete'

                    if word4.find("(NO)") != -1:
                        # Needed?
                        abbr_dict['language'] = 'NO'
                        abbr_dict['abbr'] = word4.replace("(NO)", "").replace("obso", "").strip()
                    elif word4.find("(US)") != -1:
                        abbr_dict['language'] = 'US'
                        abbr_dict['abbr'] = word4.replace("(US)", "").replace("obso", "").strip()
                    elif word4.find("(UK)") != -1:
                        abbr_dict['language'] = 'UK'
                        abbr_dict['abbr'] = word4.replace("(UK)", "").replace("obso", "").strip()
                    elif word4.find("(NATO)") != -1:
                        abbr_dict['language'] = 'NATO'
                        abbr_dict['abbr'] = word4.replace("(NATO)", "").replace("obso", "").strip()
                    else:
                        abbr_dict['language'] = 'US, UK, NATO'
                        abbr_dict['abbr'] = word4.replace("obso", "").strip()
                    abbr.append(abbr_dict)

            word = {
                'nor': nor,
                'nor_expl': nor_expl,
                'nor_usages': nor_usages,
                'eng': eng,
                'abbr': abbr
            }
            dictionary[counter] = word
    return dictionary


def print_dictionary(dictionary):
    for word in dictionary:
        print dictionary[word]['nor'] + "(" + dictionary[word]['nor_expl'] + ") -> " + dictionary[word]['eng']
        print "-----"
    print "The dictionary contains " + str(len(dictionary)) + " words."


def export_dictionary_json(dictionary):
    export_dictionary_json = 'data/dictionary.json'
    with codecs.open(export_dictionary_json, 'w+',
                     "UTF-8") as export_dictionary_json_file:
        json.dump(dictionary, export_dictionary_json_file, ensure_ascii=False,
                  sort_keys=True, encoding="UTF-8")
        export_dictionary_json_file.flush()


def is_word_in_dictionary_expl(dict_expl, abbr):
    for dx in dictionary_explanations:
        if abbr == dx:
            return True
    return False


def get_word_in_dictionary_expl(dict_expl, abbr):
    if not dict_expl:
        return None
    for abbr_key in dict_expl.keys():
        if abbr_key == abbr:
            return dict_expl[abbr_key]
    return None


if __name__ == '__main__':
    print "Loading dictionary explanations"
    dictionary_explanations = load_dictionary_explanations()
    print "Loaded " + str(
        len(dictionary_explanations)) + " from dictionary explanations file."

    print "Loading dictionary"
    dictionary = load_dictionary(dictionary_explanations)
    print "Loaded " + str(len(dictionary)) + " from dictionary file."

    print "Exporting dictionary..."
    export_dictionary_json(dictionary)
    print "Dictionary exported..."
