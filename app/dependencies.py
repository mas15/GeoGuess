import os
import secrets
from jinja2 import Environment, FileSystemLoader
from nameko.extensions import DependencyProvider
from app.crawling import save_locations, crawl_locations, NoLocationsCrawled

TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), 'templates')
LOCATIONS_FILE = os.path.join(os.path.dirname(__file__), 'locations.csv')


class LocationsProvider(DependencyProvider):
    def setup(self):
        try:
            self.locations = self.load_locations(LOCATIONS_FILE)
        except NoLocationsCrawled:
            self.locations = crawl_locations()
            save_locations(self.locations, LOCATIONS_FILE)

    def get_dependency(self, worker_ctx):
        return self.locations


class TemplateProvider(DependencyProvider):

    def setup(self):
        template_loader = FileSystemLoader(searchpath=TEMPLATES_PATH)
        template_env = Environment(loader=template_loader)
        self.template = template_env.get_template("main.html")

    def get_dependency(self, worker_ctx):
        return self.template


class CurrentAnswersProvider(DependencyProvider):

    def __init__(self):
        self.answers = dict()

    def get_dependency(self, worker_ctx):
        try:
            user_id = worker_ctx.data['user_id']
        except KeyError:
            user_id = secrets.token_urlsafe(16)
            worker_ctx.data['user_id'] = user_id
        return self.answers[user_id]

