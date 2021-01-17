import sys
import json

try:
    lang = sys.argv[1]
    with open('../data.json', 'r') as dt_f:
        dt = json.load(dt_f)
        i18n = {}
        for kanji in dt['kanjis']:
            for meaning in dt['kanjis'][kanji]['meanings']:
                try:
                    i18n[kanji][meaning] = ''
                except KeyError:
                    i18n[kanji] = {}
                    i18n[kanji][meaning] = ''
        dt_f.close()
        with open('./{}.json'.format(lang), 'w+') as lang_f:
            json.dump(i18n, lang_f, ensure_ascii=False, indent=4)
            lang_f.close()

except IndexError:
    print('Err: missing language argument')
    exit(-1) 
