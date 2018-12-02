import random
from nameko.web.handlers import http
from dependencies import LocationsProvider, TemplateProvider, CurrentAnswersProvider


class GeoGuessService:
    name = "geo_guess_service"
    locations = LocationsProvider()
    template = TemplateProvider()
    current_answer = CurrentAnswersProvider()

    @http('GET, POST', "/")
    def game(self, request):
        guess_result = None
        answer = request.get_data()
        if answer:
            if answer == self.current_answer.location.id:
                guess_result = "Good guess"
            else:
                guess_result = f"Wrong guess, it was {self.current_answer.location.name}"

        puzzle = self.get_new_puzzle()
        self.current_answer.location = puzzle.location

        return self.template.render(
            all_locations=self.locations,
            puzzle=puzzle,
            guess_result=guess_result
        )  # loc_to_guess, loc_to_start)


    def get_new_puzzle(self):
        loc = random.choice(self.locations)
        return loc
        # loc_to_start = self.find_location_nearby(loc_to_guess)
