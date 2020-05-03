import json
with open('../data/data.json', 'r') as f:
    dict = json.load(f)
caz = []
rec = []
dth = []
for i in range(len(dict['Romania'])):
    conf = dict['Romania'][i]['confirmed']
    reco = dict['Romania'][i]['recovered']
    deth = dict['Romania'][i]['deaths']
    if(conf > 0):
        caz.append(str(conf) + ' ')
        rec.append(str(reco) + ' ')
        dth.append(str(deth) + ' ')
with open('../data/cases.in', 'w') as f:
    f.write(str(len(caz)) + '\n')
    for i in range(len(caz)):
        f.write(caz[i] + ' ' + rec[i] + ' ' + dth[i])
        f.write('\n')
