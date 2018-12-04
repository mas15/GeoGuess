import csv
import requests
from lxml import html
from geo.models import Location

WIKI_DOMAIN = 'https://pl.wikipedia.org'
START_URL = '/wiki/Kategoria:Pomniki_historii'


class NoLocationsCrawled(Exception):
    pass


def crawl_locations():
    locations = [l for l in crawl_locations_page(START_URL)]
    return locations


def crawl_locations_page(locations_list_url):
    print(locations_list_url)
    response = requests.get(WIKI_DOMAIN + locations_list_url)
    tree = html.fromstring(response.content)

    sub_categories_urls = tree.xpath('/html/body/div[3]/div[3]/div[4]/div[2]/div[1]/div/ul/li/div/div[1]/a/@href')
    locations = []
    for sub_url in sub_categories_urls:
        locations.extend(crawl_locations_page(sub_url))

    monuments_titles = tree.xpath('/html/body/div[3]/div[3]/div[4]/div[2]/div/div/div/div/ul/li/a/text()')
    monuments_url = tree.xpath('/html/body/div[3]/div[3]/div[4]/div[2]/div[2]/div/div/div/ul/li/a/@href')

    for monument in zip(monuments_titles, monuments_url):
        loc = crawl_location(monument)
        if loc:
            locations.append(loc)
        # else:
        #     print("bez gpsa..")
        #     print(loc)
    return locations


def crawl_location(monument):
    print("   " + monument[1])

    response = requests.get(WIKI_DOMAIN + monument[1])
    tree = html.fromstring(response.content)
    try:
        latitude = tree.xpath('//span[@class="latitude"]/text()')[1]
        longitude = tree.xpath('//span[@class="longitude"]/text()')[1]
    except IndexError:
        return None
    return Location(monument[0], latitude, longitude)


def load_locations(locations_file):
    try:
        with open(locations_file) as csvfile:
            csv_reader = csv.reader(csvfile)
            locations = [Location(*row) for row in csv_reader]
            return locations
    except FileNotFoundError:
        raise NoLocationsCrawled


def save_locations(locations, locations_file):
    with open(locations_file, 'w') as csvfile:
        csv_out = csv.writer(csvfile)
        for l in locations:
            csv_out.writerow([l.name, l.latitude, l.longitude])


if __name__ == '__main__':
    locations = crawl_locations()
    save_locations(locations, 'locations.csv')
