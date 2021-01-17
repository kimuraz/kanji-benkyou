import json


with open('../data.json', 'r') as src:
    kanjis = json.load(src)
    fixtures = []
    id = 1
    for k in kanjis['kanjis']:
        fixture = {}
        fixture['fields'] = kanjis['kanjis'][k]
        fixture['fields']['unicode_code'] = kanjis['kanjis'][k]['unicode']
        del fixture['fields']['unicode']
        fixture['model'] = 'kanjis.Kanji'
        fixture['pk'] = id
        fixtures.append(fixture)
        id += 1
    src.close()
    with open('../../kanji_benkyou_api/kanjis/fixtures/kanjis.json', 'w+') as out:
        json.dump(fixtures, out, ensure_ascii=False)
        out.close()
