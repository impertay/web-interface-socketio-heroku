import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

'''def get_level_upper_capacity(html):
    soup = BeautifulSoup(html, 'lxml')
    level_upper_capacity = soup.find('div', id='upper_capacity_level').get('style')
    number_level_upper_capacity = level_upper_capacity.split(' ')[1].split('%')[0]
    return int(number_level_upper_capacity)'''

def get_levels(html, level):
    soup = BeautifulSoup(html, 'lxml')
    level_capacity = soup.find('div', id=level).get('style')
    number_level_capacity = level_capacity.split(' ')[1].split('%')[0]
    return int(number_level_capacity)

def parser_level_capacity():
    url = 'http://70498866.ngrok.io'
#    level_upper_capacity = get_level_upper_capacity(get_html(url))
    level_upper_capacity = get_levels(get_html(url), 'upper_capacity_level')
    level_bottom_capacity = get_levels(get_html(url), 'bottom_capacity_level')
    levels = {
        'upper_capacity': level_upper_capacity,
        'bottom_capacity': level_bottom_capacity,
    }
    return levels
'''    if level_upper_capacity > 40:
        return 'Уровень привышен'
    else:
        return level_upper_capacity'''