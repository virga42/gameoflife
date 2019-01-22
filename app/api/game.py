from flask import jsonify, request
from app.api import bp
from app import gol

@bp.route('/game', methods=['POST'])
def generation_request():
    data = request.get_json() or {}
    # TODO add validation
    str_universe = data['universe']
    width = int(data['width'])
    
    universe = gol.string_to_universe(str_universe, width)

    u_output = gol.universe_to_string(gol.universe_generation(universe, width))

    response = jsonify(u_output)
    response.status_code = 201
    response.headers['Location'] = "api/game"
    return response