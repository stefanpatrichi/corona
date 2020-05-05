import urllib.request

def get_json():
    print('Getting JSON file...')
    urllib.request.urlretrieve('https://pomber.github.io/covid19/timeseries.json', '../data/data.json')
