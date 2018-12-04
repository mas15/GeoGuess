import random
from flask import render_template, session, request
from geo import app
from geo.models import Puzzle


@app.route('/', methods=['GET', 'POST'])
def game():
    guess_result = None
    if request.method == 'POST':
        if int(request.form.get('answer')) == session['puzzle_answer']:
            guess_result = "Good guess"
        else:
            guess_result = "Wrong guess"

    puzzle = get_new_puzzle(app.locations)
    session['puzzle_answer'] = puzzle.location_to_guess.id

    return render_template(
        'main.html',
        all_locations=app.locations,
        puzzle=puzzle,
        guess_result=guess_result
    )


def get_new_puzzle(locations):
    loc = random.choice(locations)
    return Puzzle(loc, loc)

    # loc_to_start = self.find_location_nearby(loc_to_guess)
