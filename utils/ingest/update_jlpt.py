import json

with open('./jlpt_kanjis.json', 'r') as jf:
    jlpt = json.load(jf)
    with open('./data.json', 'r') as dtf:
        data = json.load(dtf)
        new_data = { 'kanjis': {} }
        for k in data['kanjis']:
           new_data['kanjis'][k] = data['kanjis'][k]  
           cur_kanji = new_data['kanjis'][k]['kanji']
           try:
               new_data['kanjis'][k]['jlpt'] = jlpt[cur_kanji]
           except KeyError:
               pass
        dtf.close()
        with open('./data.json', 'w') as drfw:
            drfw.write(json.dumps(new_data, ensure_ascii=False))
            drfw.close()


