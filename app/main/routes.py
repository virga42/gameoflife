from flask import render_template, flash, redirect, url_for, jsonify
from app.main import bp
from app import gol

@bp.route('/')
@bp.route('/index')
def index():
  return render_template('index.html', title='Conway\'s Game of Life')

# @bp.route('/game', methods=['POST'])
# def generation_request():
#     data = request.get_json() or {}
#     # TODO add validation
#     str_universe = data['universe']
#     width = int(data['width'])
    
#     universe = gol.string_to_universe(str_universe, width)

#     u_output = {"universe": gol.universe_to_string(gol.universe_generation(universe, width)), "width": width}

#     response = jsonify(u_output)
#     response.status_code = 200
#     response.headers['Location'] = "api/game"
#     return response

