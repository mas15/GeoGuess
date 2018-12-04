import os
from geo import app
from flask_script import Manager
from geo.crawling import save_locations, load_locations, crawl_locations, NoLocationsCrawled

LOCATIONS_FILE = os.path.join(os.path.dirname(__file__), 'locations.csv')


def get_locations():
    try:
        return load_locations(LOCATIONS_FILE)
    except NoLocationsCrawled:
        locations = crawl_locations()
        save_locations(locations, LOCATIONS_FILE)
        return locations

manager = Manager(app)


@manager.command
def run():
    app.locations = get_locations()
    app.run()


@manager.command
def init():
    get_locations()


if __name__ == '__main__':
    manager.run()