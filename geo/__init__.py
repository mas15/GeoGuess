from flask import Flask


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = b'\xdfP\xdb\xc9\xe4K\x0fc\x10\x06\xca\xaf\x1f\xb3\x00x\xc6\xd2\x96 lg\xf7\xad'

app.locations = []

import geo.views
import geo.models


