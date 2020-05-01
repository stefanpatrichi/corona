import json
with open('data/data.json', 'r') as f:
    dict = json.load(f)
caz = []
for i in range(len(dict['Romania'])):
    conf = dict['Romania'][i]['confirmed']
    if(conf > 0):
        caz.append(str(dict['Romania'][i]['confirmed']) + ' ')
with open('data/cases.in', 'w') as f:
    f.write(str(len(caz)) + '\n')
    for i in caz:
        f.write(str(i))
