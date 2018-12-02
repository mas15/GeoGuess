import random
from nameko.web.handlers import http
from app.dependencies import LocationsProvider, TemplateProvider, CurrentAnswersProvider


class GeoGuessService:
    name = "geo_guess_service"
    locations = LocationsProvider()
    template = TemplateProvider()
    current_answer = CurrentAnswersProvider()

    @http('GET, POST', "/")
    def game(self, request):
        answer = request.get_data()
        if answer:
            if answer == self.current_answer:
                guess_result = "Good guess"
            else:
                guess_result = f"Wrong guess, it was {self.current_answer}"

        puzzle = self.get_new_puzzle()
        self.current_answer = puzzle.location.id

        return self.template.render(
            all_locations=self.locations,
            puzzle=puzzle,
            guess_result=guess_result
        )  # loc_to_guess, loc_to_start)


    def get_new_puzzle(self):
        loc = random.choice(self.locations)
        return loc
        # loc_to_start = self.find_location_nearby(loc_to_guess)
